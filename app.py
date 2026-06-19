from flask import Flask, render_template, request
from google import genai
import markdown

app = Flask(__name__)

client = genai.Client(api_key="AQ.Ab8RN6JAWQYQK1CPJwS3PwDzatBM5JHazRsF2DLDtymweyV--A")

@app.route("/", methods=["GET", "POST"])
def index():
    feedback = None
    error = None
    resume_text = ""
    job_description = ""

    if request.method == "POST":
        resume_text = request.form["resume"]
        job_description = request.form.get("job_description", "")

        prompt = f"""
You are an expert resume reviewer. Analyze the following resume and provide detailed feedback.

Resume:
{resume_text}

{"Job Description: " + job_description if job_description else ""}

Please provide:
1. Overall Score (out of 10)
2. Strengths (what's good)
3. Weaknesses (what's missing or weak)
4. Specific Improvements (actionable suggestions)
5. Keywords Missing (important keywords not in the resume)

Format your response clearly with these exact headings.
"""
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )
            feedback = markdown.markdown(response.text)
        except Exception as e:
            error = f"Something went wrong: {str(e)}"

    return render_template("index.html",
                         feedback=feedback,
                         error=error,
                         resume_text=resume_text,
                         job_description=job_description)

if __name__ == "__main__":
    app.run(debug=True, port=5003)