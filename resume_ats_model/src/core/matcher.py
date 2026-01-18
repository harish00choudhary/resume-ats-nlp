import os
from sentence_transformers import SentenceTransformer, util

# Absolute path to model folder
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "model", "resume_ats_model")

model = SentenceTransformer(MODEL_PATH)

def get_similarity_score(resume_text, jd_text):
    embeddings = model.encode(
        [resume_text, jd_text],
        convert_to_tensor=True
    )
    score = util.cos_sim(embeddings[0], embeddings[1])
    return float(score)
