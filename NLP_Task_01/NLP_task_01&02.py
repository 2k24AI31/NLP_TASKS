import pandas as ps
import numpy as ny
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Bag of words,, Task no 1 
print("=" * 60)
print("TASK 1: Bag of Words Matrix Construction")
print("=" * 60)

corpus = [
    "The product performance is amazing and fast",
    "The service was fast and performance was great",
    "Terrible customer service and bad performance"
]

# Step1,  removing the stop words 
vectorizer = CountVectorizer(stop_words='english')

# Step2, Fit-transform
bow_matrix = vectorizer.fit_transform(corpus)

# Step3, vocanb extracting 
vocabulary = vectorizer.get_feature_names_out()
print("\nVocabulary:")
print(list(vocabulary))

# Step 4: Convert sparse matrix into a Pandas DataFrame
bow_df = ps.DataFrame(
    bow_matrix.toarray(),
    columns=vocabulary,
    index=[f"Document {i+1}" for i in range(len(corpus))]
)

print("\nBag of Words Matrix:")
print(bow_df)


  # Search engine,,TASK2  

print("\n" + "=" * 60)
print("TASK 2: Document Search Engine & Relevance Ranking")
print("=" * 60)

documents = [
    "Machine learning algorithms analyze structured data effectively",
    "Deep learning and neural networks excel at processing unstructured data",
    "Natural language processing helps computers understand human language",
    "Python is widely used for machine learning and data science"
]

query = ["machine learning algorithms for data"]

# Step1, Fit CountVectorizer on documents
doc_vectorizer = CountVectorizer()
doc_vectors = doc_vectorizer.fit_transform(documents)

# Step2, Transform the query using the SAME fitted vectorizer
query_vector = doc_vectorizer.transform(query)

print("\nDocument Vocabulary:")
print(list(doc_vectorizer.get_feature_names_out()))

# Step3, Compute pairwise cosine similarity (query vs each document)
similarity_scores = cosine_similarity(query_vector, doc_vectors)[0]

# Step4, Rank documents from highest score to lowest
results_df = ps.DataFrame({
    "Document": documents,
    "Similarity Score": similarity_scores
})
results_df = results_df.sort_values(by="Similarity Score", ascending=False).reset_index(drop=True)
results_df.index = results_df.index + 1  # rank starting at 1

print("\nQuery:", query[0])
print("\nRanked Documents (highest to lowest relevance):")
print(results_df.to_string())

print("VIVA & REFLECTION ANSWERS (see README.md for full text)")
print("=" * 60)
