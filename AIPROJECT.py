from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

job_description = """
Looking for a Python developer with experience in machine learning, data analysis,
TensorFlow, and problem-solving skills.
"""

resumes = [
    "Experienced Python developer with strong background in machine learning and TensorFlow.",
    "Frontend developer skilled in HTML CSS JavaScript.",
    "Data analyst with Python experience and knowledge of machine learning.",
    "Software engineer with Java and system design experience."
]

documents = [job_description] + resumes

vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(documents)

similarity_scores = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()

ranked_resumes = sorted(
    list(enumerate(similarity_scores)),
    key=lambda x: x[1],
    reverse=True
)

for idx, score in ranked_resumes:
    print(f"Resume {idx+1} Score: {score:.4f}")
    print(resumes[idx])
    print()
