import re

SKILLS = [
    "python", "java", "c++", "javascript", "react", "node",
    "django", "flask", "sql", "mysql", "mongodb", "aws",
    "docker", "kubernetes", "git", "machine learning",
    "deep learning", "nlp", "data structures", "algorithms",
    "rest api", "linux"
]

def extract_keywords_from_jd(text):
    """Extract skills and keywords from JD."""
    text = text.lower()
    found = [skill for skill in SKILLS if skill in text]
    return found
