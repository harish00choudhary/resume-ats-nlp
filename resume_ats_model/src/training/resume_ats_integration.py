# Step 0: Install required libraries if not installed
# pip install sentence-transformers pandas torch

import pandas as pd
from sentence_transformers import SentenceTransformer, util
import torch

# Step 1: Load trained model (from Colab)
model = SentenceTransformer('sentence_transformer_resume_ats')  # path to saved model

# Optional: define skill list (same as used in training)
SKILLS = [
    "python", "java", "c++", "javascript", "react", "node",
    "django", "flask", "sql", "mysql", "mongodb", "aws",
    "docker", "kubernetes", "git", "machine learning", "deep learning",
    "nlp", "data structures", "algorithms", "rest api", "linux"
]

# Step 2: Clean text function
import re
def clean_text(text):
    text = text.lower()
    text = re.sub(r'\n', ' ', text)
    text = re.sub(r'\r', ' ', text)
    text = re.sub(r'[^a-z0-9\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# Step 3: Skill extraction function
def extract_skills(text):
    return [skill for skill in SKILLS if skill in text]

# Step 4: Compute similarity & missing skills
def evaluate_resume(resume_text, jd_text):
    resume_clean = clean_text(resume_text)
    jd_clean = clean_text(jd_text)
    
    resume_skills = extract_skills(resume_clean)
    jd_skills = extract_skills(jd_clean)
    
    # Missing skills
    missing_skills = list(set(jd_skills) - set(resume_skills))
    
    # Generate embeddings
    resume_emb = model.encode(resume_clean, convert_to_tensor=True)
    jd_emb = model.encode(jd_clean, convert_to_tensor=True)
    
    # Cosine similarity
    similarity = util.cos_sim(resume_emb, jd_emb).item() * 100  # scale 0-100
    
    result = {
        "match_score": round(similarity, 2),
        "resume_skills": resume_skills,
        "jd_skills": jd_skills,
        "missing_skills": missing_skills
    }
    return result

# Step 5: Example usage
if __name__ == "__main__":
    # Example resume and JD
    resume_text = """
    I have 3 years experience in Python, Django, REST API, and SQL.
    """
    jd_text = """
    We are looking for a Python developer with Django, REST API, SQL, AWS, and Docker experience.
    """
    
    result = evaluate_resume(resume_text, jd_text)
    print("Match Score:", result["match_score"])
    print("Resume Skills:", result["resume_skills"])
    print("Job Description Skills:", result["jd_skills"])
    print("Missing Skills:", result["missing_skills"])
