import nltk
import sys
import os
import string
FILE_MATCHES = 1
SENTENCE_MATCHES = 1
import math


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python questions.py corpus")

    # Calculate IDF values across files
    files = load_files(sys.argv[1])
    file_words = {
        filename: tokenize(files[filename])
        for filename in files
    }
    file_idfs = compute_idfs(file_words)

    # Prompt user for query
    query = set(tokenize(input("Query: ")))

    # Determine top file matches according to TF-IDF
    filenames = top_files(query, file_words, file_idfs, n=FILE_MATCHES)

    # Extract sentences from top files
    sentences = dict()
    for filename in filenames:
        for passage in files[filename].split("\n"):
            for sentence in nltk.sent_tokenize(passage):
                tokens = tokenize(sentence)
                if tokens:
                    sentences[sentence] = tokens

    # Compute IDF values across sentences
    idfs = compute_idfs(sentences)

    # Determine top sentence matches
    matches = top_sentences(query, sentences, idfs, n=SENTENCE_MATCHES)
    for match in matches:
        print(match)


def load_files(directory):

    print("loading data......")

    files={}
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            file_path=os.path.join(directory, filename)
            with open(file_path, 'r', encoding="utf8") as file:
                content=file.read()
            files[filename]=content

    return files

    """
    Given a directory name, return a dictionary mapping the filename of each
    `.txt` file inside that directory to the file's contents as a string.
    """
    #raise NotImplementedError


def tokenize(document):

    words_tokens=nltk.word_tokenize(document)

    refined_words_tokens=[word.lower() for word in words_tokens if word not in string.punctuation and word not in nltk.corpus.stopwords.words("english")]

    return refined_words_tokens
    """
    Given a document (represented as a string), return a list of all of the
    words in that document, in order.
    Process document by coverting all words to lowercase, and removing any
    punctuation or English stopwords.
    """
    #raise NotImplementedError


def compute_idfs(documents):

    idf={}
    total_documents=len(documents)
    for titles in documents:

        for word in documents[titles]:
            if word in idf:
                continue
            word_frequency=1
            for other_titles in documents:
                if titles==other_titles:
                    continue
                else:
                    if word in documents[other_titles]:
                        word_frequency+=1
            idf[word]=math.log(total_documents/word_frequency)

    return idf


    """
    Given a dictionary of `documents` that maps names of documents to a list
    of words, return a dictionary that maps words to their IDF values.
    Any word that appears in at least one of the documents should be in the
    resulting dictionary.
    """
    #raise NotImplementedError


def top_files(query, files, idfs, n):

    tf_idf_scores={file_names:0 for file_names in files}
    for file_name in files:
        for word in query:
            if word in files[file_name]:
                tf=files[file_name].count(word)
                idf=idfs[word]
                tf_idf_scores[file_name] += tf*idf

    return sorted([file for file in files], key=lambda x:tf_idf_scores[x], reverse=True)


    """
    Given a `query` (a set of words), `files` (a dictionary mapping names of
    files to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the filenames of the the `n` top
    files that match the query, ranked according to tf-idf.
    """
    #raise NotImplementedError


def top_sentences(query, sentences, idfs, n):
    top_sentence_score={sentence:[0,0] for sentence in sentences}
    for sentence in sentences:

        for words in query:
            if words in sentences[sentence]:
                top_sentence_score[sentence][0]+=idfs[words]
        query_term_density=0
        for word in sentences[sentence]:
            if word in query:
                query_term_density+=1
        top_sentence_score[sentence][1]=query_term_density/len(sentences[sentence])

    sorted_top_sentence_score = {sentence: values for sentence, values in sorted(top_sentence_score.items(), key=lambda x: (x[1][0], x[1][1]), reverse=True)}

    return list(sorted_top_sentence_score.keys())[:n]



    """
    Given a `query` (a set of words), `sentences` (a dictionary mapping
    sentences to a list of their words), and `idfs` (a dictionary mapping words
    to their IDF values), return a list of the `n` top sentences that match
    the query, ranked according to idf. If there are ties, preference should
    be given to sentences that have a higher query term density.
    """
    #raise NotImplementedError


if __name__ == "__main__":
    main()
