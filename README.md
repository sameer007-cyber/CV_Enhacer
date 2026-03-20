# 🚀 AI Resume Analyzer with ATS Evaluation

An AI-powered Resume Analyzer that evaluates resumes against job descriptions using LLMs and provides actionable insights such as ATS match score, skill gaps, and detailed feedback.

---

## 📌 Problem Statement

Recruiters use Applicant Tracking Systems (ATS) to filter resumes based on keywords and relevance. Many candidates get rejected due to poor alignment with job descriptions.

This project explores how AI can simulate ATS evaluation and provide intelligent feedback to improve resumes.

---

## 🧠 Features

- 📄 Resume Analysis (HR-style feedback)
- 📊 ATS Match Score (percentage + missing keywords)
- 🧩 Skill Gap Identification
- 💡 Improvement Suggestions
- ⚡ Fast and interactive UI using Streamlit

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Google Gemini API (LLM)
- PyMuPDF (PDF text extraction)

---

## ⚙️ How It Works

1. User uploads resume (PDF)
2. System extracts text using PyMuPDF
3. User provides job description
4. Gemini AI analyzes:
   - Resume vs Job Description
   - Keyword matching
   - Skill gaps
5. Outputs structured feedback

---

## 📸 Demo

(Add screenshots here after running app)

---

## 🚀 Installation

```bash
git clone https://github.com/YOUR_USERNAME/ai-resume-analyzer.git
cd ai-resume-analyzer
pip install -r requirements.txt
