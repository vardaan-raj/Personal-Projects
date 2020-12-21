import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    prob_dist={}
    linked_pages=corpus[page]
    if len(linked_pages)==0:
        for pages in corpus.keys():
            prob_dist[pages]=(1-damping_factor)/len(corpus.keys())
        return prob_dist
    for pages in linked_pages:
        prob_dist[pages]=damping_factor/(len(linked_pages))
    for pages in prob_dist.keys():
        prob_dist[pages]+=(1-damping_factor)/len(corpus.keys())
    prob_dist[page]=(1-damping_factor)/len(corpus.keys())
    return prob_dist

    """
    Return a probability distribution over which page to visit next,
    given a current page.
    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    #raise NotImplementedError


def sample_pagerank(corpus, damping_factor, n):
    page_rank={}
    for pages in corpus.keys():
        page_rank[pages]=0
    page=random.choice(list(corpus.keys()))
    page_rank[page]+=1/n
    for i in range(1, n):
        prob_model=transition_model(corpus, page, damping_factor)
        page_links=[]
        page_prob=[]
        for j, k in prob_model.items():
            page_links.append(j)
            page_prob.append(k)
        page=random.choices(page_links, weights=page_prob)[0]
        page_rank[page]+=1/n
    return page_rank

    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.
    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    #raise NotImplementedError


def iterate_pagerank(corpus, damping_factor):
    page_rank={}
    for pages in corpus.keys():
        page_rank[pages]=1/(len(corpus.keys()))
    page_rank_change=1
    while page_rank_change>=0.001:
        page_rank_change=0
        page_rank_copy=page_rank.copy()
        for pages in page_rank.keys():
            links=[link for link in corpus if pages in corpus[link]]
            part1=(1-damping_factor)/len(corpus.keys())
            part2=[]
            if len(links)!=0:
                for link in links:
                    num_links=len(corpus[link])
                    part2.append(page_rank_copy[link]/num_links)
            page_rank[pages]=part1+ damping_factor*(sum(part2))
            if page_rank_change<(abs(page_rank[pages]-page_rank_copy[pages])):
                page_rank_change=abs(page_rank[pages]-page_rank_copy[pages])
    return page_rank


    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.
    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    #raise NotImplementedError


if __name__ == "__main__":
    main()
