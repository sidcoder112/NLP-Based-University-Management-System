from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def rank_texts(texts, query):
    # Initialize TF-IDF vectorizer
    vectorizer = TfidfVectorizer()

    # Fit the vectorizer on texts
    tfidf_matrix = vectorizer.fit_transform(texts + [query])

    # Calculate cosine similarity between query and texts
    similarity = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])

    # Get indices sorted by similarity score (descending order)
    ranked_indices = similarity.argsort()[0][::-1]

    # Rank texts based on sorted indices
    ranked_texts = [(similarity[0, idx], texts[idx]) for idx in ranked_indices]

    return ranked_texts

# Example texts
# texts = [
#     "Python is a widely used high-level programming language.",
#     "Machine learning is a subset of artificial intelligence.",
#     "Data science involves extracting insights from data.",
#     "Python has libraries like NumPy and pandas for data analysis.",
#     "Natural Language Processing (NLP) deals with human language data."
# ]
#
# # Example query
# query = "Python programming language"
#
# # Rank texts based on the query
# ranked_texts = rank_texts(texts, query)
#
# # Print ranked texts
# for rank, text in ranked_texts:
#     print(f"Rank: {rank}, Text: {text}")
