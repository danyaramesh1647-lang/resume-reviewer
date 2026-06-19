# AI Resume Reviewer 🤖
An AI-powered resume reviewer built with Flask and Google Gemini API that analyzes resumes and provides detailed feedback.

## Features
- Paste your resume and get instant AI feedback
- Overall score out of 10
- Strengths and weaknesses analysis
- Specific improvement suggestions
- Missing keywords detection
- Optional job description matching for tailored feedback

## Tech Stack
- **Backend:** Python, Flask
- **API:** Google Gemini API
- **Frontend:** HTML, CSS, Jinja2

## How to Run
1. Clone the repository
2. Install dependencies: `pip install flask google-genai markdown`
3. Add your Gemini API key in app.py
4. Run: `python app.py`
5. Open `http://127.0.0.1:5003`