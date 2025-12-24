📄 Resume ATS Analyzer (NLP-Based)

An Applicant Tracking System (ATS) Resume Analyzer built using NLP and Sentence Transformers.
This project compares a candidate’s resume with a job description and calculates a matching score, helping users understand how well their resume aligns with a specific role.

🚀 Features

📑 Extracts text from PDF resumes

🧠 Uses Sentence Transformers for semantic similarity

📊 Calculates resume–job description match percentage

🖥️ Interactive Streamlit web interface

🔍 Highlights ATS-style relevance instead of keyword matching

🛠️ Tech Stack

Python

Sentence Transformers (all-MiniLM-L6-v2)

PyTorch

Hugging Face Transformers

Streamlit

pdfplumber

scikit-learn

Pandas

🧠 Project Architecture
project_resumeATS/
│
├── app.py                  # Streamlit UI
├── resume_parser.py        # Extracts text from resume PDF
├── jd_parser.py            # Processes job description
├── matcher.py              # Loads model & computes similarity
├── train_model.py          # Fine-tuning Sentence Transformer
├── resume_ats_integration.py
├── training_data.csv       # Custom training dataset
├── .gitignore
└── README.md

📊 How It Works

1.Resume Upload
  - User uploads a resume in PDF format.
  - pdfplumber extracts raw text.

2. Job Description Input
  - User pastes the job description.

3. Text Embedding
  - Resume and JD are converted into vector embeddings using a Sentence Transformer.

4. Similarity Calculation
  - Cosine similarity is computed between embeddings.
  - Output is shown as a percentage match score.

🧪 Model Training (Important for Interviews)
Dataset

Custom dataset with columns:

company_name

job_description

position_title

description_length

model_response

Training Approach

Base Model: all-MiniLM-L6-v2

Fine-tuned using SentenceTransformer .fit()

Loss Function: CosineSimilarityLoss

Framework: PyTorch + Hugging Face Accelerate

Why Sentence Transformers?

Better semantic understanding than keyword matching

Captures meaning, synonyms, and context

Lightweight and fast for real-time apps

🖥️ Running the Project Locally
1️⃣ Clone the Repository
git clone https://github.com/harish00choudhary/resume-ats-nlp.git
cd resume-ats-nlp

2️⃣ Create Virtual Environment
python -m venv .venv
source .venv/Scripts/activate   # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt


(If requirements.txt is missing, install manually)

pip install streamlit sentence-transformers pdfplumber torch accelerate datasets

4️⃣ Train the Model (Optional)
python train_model.py

5️⃣ Run the App
streamlit run app.py

📈 Output Explanation

Match score is shown as 0–1 range
  - Example: 0.88 = 88% match

This is cosine similarity, not a probability

Higher score → better alignment with job description

🎯 Use Cases

Job seekers optimizing resumes

Understanding ATS screening behavior

NLP similarity learning project

ML + Streamlit portfolio project

🔮 Future Improvements

Highlight missing skills

Resume section-wise scoring

Multiple JD comparison

Cloud deployment (Streamlit Cloud / Hugging Face Spaces)

UI enhancement with HTML/CSS

👨‍💻 Author

Harish Choudhary
B.Tech CSE (AI)
Aspiring ML / NLP Engineer
