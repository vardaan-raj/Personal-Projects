# Questions

A Simple Question Answering System which retrieves the most relevant documents related to a query and presents the most relevant passage in an interactive manner using Artificial Intelligence.
## Introduction
Question Answering (QA) is a field within natural language processing focused on designing systems that can answer questions. Among the more famous question answering systems is Watson, the IBM computer that competed (and won) on Jeopardy!. A question answering system of Watson’s accuracy requires enormous complexity and vast amounts of data, but here we’ll design a very simple question answering system based on inverse document frequency.

## Requirements
- **Streamlit**
- **Python**
- **Nltk(Natural Language Toolkit)**

## Usage

```python
streamlit run Questions.py corpus
```
![image](https://user-images.githubusercontent.com/37051428/132874828-eec7a64f-6806-4184-a0bc-e90895127fd2.png)


https://user-images.githubusercontent.com/37051428/132878368-3fd32c40-fda3-40ec-a6b4-8700a85a73da.mp4



## Description
Our question answering system will perform two tasks: document retrieval and passage retrieval. Our system will have access to a corpus of text documents. When presented with a query (a question in English asked by the user), document retrieval will first identify which document(s) are most relevant to the query. Once the top documents are found, the top document(s) will be subdivided into passages (in this case, sentences) so that the most relevant passage to the question can be determined.



