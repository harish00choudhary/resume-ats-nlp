import streamlit as st
from resume_parser import extract_resume_text
from jd_parser import extract_keywords_from_jd
from matcher import get_similarity_score

st.set_page_config(page_title="AI Resume ATS", page_icon="📝")

st.title("📝 AI-Powered Company-Specific Resume ATS")

st.write("Upload your resume and paste the job description to get an ATS match score.")

# ---- Resume Upload ----
resume_file = st.file_uploader("Upload Resume (PDF format)", type=["pdf"])

# ---- Job Description Text ----
jd_text = st.text_area("Paste Job Description Here")

if st.button("Analyze"):
    if resume_file is None:
        st.warning("⚠ Please upload a resume!")
    elif jd_text.strip() == "":
        st.warning("⚠ Please paste a job description!")
    else:
        # Extract resume text
        resume_text = extract_resume_text(resume_file)

        # Extract JD skills
        jd_skills = extract_keywords_from_jd(jd_text)

        # ATS score
        ats_score = get_similarity_score(resume_text, jd_text)

        # Display results
        st.subheader("📊 ATS Match Score")
        st.metric(label="Match Percentage", value=f"{ats_score*100}%")

        st.subheader("🛠 Skills Required from JD")
        st.write(", ".join(jd_skills) if jd_skills else "No skills detected.")

        st.subheader("📄 Extracted Resume Text (Preview)")
        st.write(resume_text[:1000] + "..." if len(resume_text) > 1000 else resume_text)
