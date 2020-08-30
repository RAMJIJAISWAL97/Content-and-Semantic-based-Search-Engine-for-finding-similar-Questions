# Content-and-Semantic-based-Search-Engine-for-finding-similar-Questions
This is a Search Engine developed using Elastic Search and
TensorFlow pre-trained Model which gives top most 15
similar questions to the Query within a second from pool of Question Dataset.


This project helps to search similar questions to the given question.

----> Model is trained in two ways: 1. Simple search based on similar words. 2. Semantic Search based on cosine distance between two sentence vectors.

For the purpose of cosine distance and vectorization, Elastic search is used.

To run This project files you need to connect with Elastic Search Engine running and connection with that.
You can use Docker if you feel problem to resolve incomparibility Problem.
It also required RAM space more that 4GB and internet connection because it require to download pre trained tensor flow model to perform sementic search Query.\n\n\n


Data set is taken from kaggle compatetion.

https://www.kaggle.com/stackoverflow/stacksample

Descreption of Data Set:
Dataset with the text of 10% of questions and answers from the Stack Overflow programming Q&A website.

This is organized as three tables:

Questions contains the title, body, creation date, closed date (if applicable), score, and owner ID for all non-deleted Stack Overflow questions whose Id is a multiple of 10.
Answers contains the body, creation date, score, and owner ID for each of the answers to these questions. The ParentId column links back to the Questions table.
Tags contains the tags on each of these questions
Datasets of all R questions and all Python questions are also available on Kaggle, but this dataset is especially useful for analyses that span many languages.

Example projects include:

Identifying tags from question text
Predicting whether questions will be upvoted, downvoted, or closed based on their text
Predicting how long questions will take to answer


But here in this project I am using only Questions DataSet.
