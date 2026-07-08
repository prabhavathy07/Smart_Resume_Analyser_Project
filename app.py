from flask import Flask, render_template, request, send_file
import google.generativeai as genai

from src.resume_reader import read_resume
from src.skill_analyser import (
    find_skills,
    calculate_score,
    find_missing_skills,
    get_suggestion,
    ats_score
)
from src.chart_generator import generate_chart
from src.database import create_database, save_history, get_history
from src.pdf_generator import generate_pdf
from src.email_sender import send_email
from src.job_roles import roles

# ---------------- Gemini ----------------

import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")
# ---------------- Flask ----------------

app = Flask(__name__)

create_database()

# ---------------- Home ----------------

@app.route("/")
def home():
    return render_template("index.html")


# ---------------- Analyze ----------------

@app.route("/analyze", methods=["POST"])
def analyze():

    job_role = request.form["job_role"]
    email = request.form.get("email")

    file = request.files["resume"]

    required_skills = roles[job_role]

    resume = read_resume(file)

    found_skills = find_skills(resume)

    matched_skills = []

    for skill in required_skills:
        if skill in found_skills:
            matched_skills.append(skill)

    match_percentage = round(
        len(matched_skills) / len(required_skills) * 100
    )

    score = calculate_score(found_skills, required_skills)

    missing_skills = find_missing_skills(found_skills)

    suggestion = get_suggestion(score)

    ats = ats_score(resume)

    prompt = f"""
You are an expert Resume Reviewer.

Job Role:
{job_role}

Resume:
{resume}

Give only 5 short resume improvement suggestions.
"""

    try:
        response = model.generate_content(prompt)
        ai_suggestion = response.text

    except Exception as e:
        import traceback

        print("=" * 50)
        print("Gemini Error:")
        print(e)
        traceback.print_exc()
        print("=" * 50)

        ai_suggestion = f"""
        AI Error:
        {e}
        """  
    # Chart
    generate_chart(score, ats)
    
    # PDF
    generate_pdf(
        job_role,
        score,
        ats,
        found_skills,
        missing_skills,
        ai_suggestion
    )

    # Email
    if email:
        try:
            send_email(email)
        except Exception as e:
            print("Email Error:", e)

    # Save History
    save_history(job_role, score, ats)

    # Score Color
    if score >= 80:
        score_color = "#28a745"
    elif score >= 50:
        score_color = "#ff9800"
    else:
        score_color = "#dc3545"

    return render_template(
        "result.html",
        score=score,
        ats=ats,
        score_color=score_color,
        job_role=job_role,
        required_skills=required_skills,
        matched_skills=matched_skills,
        match_percentage=match_percentage,
        found_skills=found_skills,
        missing_skills=missing_skills,
        suggestion=suggestion,
        ai_suggestion=ai_suggestion
    )



# ---------------- Download PDF ----------------

@app.route("/download")
def download():
    return send_file(
        "resume_report.pdf",
        as_attachment=True
    )


# ---------------- History ----------------

@app.route("/interview", methods=["POST"])
def interview():

    job_role = request.form["job_role"]

    prompt = f"""
Generate 10 interview questions for a fresher applying for the role of {job_role}.

Only questions.
No answers.
Number them.
"""

    try:
        response = model.generate_content(prompt)
        questions = response.text
    except Exception:
        questions = "Interview Questions are temporarily unavailable."

    return render_template(
        "interview.html",
        job_role=job_role,
        questions=questions
    )
@app.route("/rewrite", methods=["POST"])
def rewrite():

    file = request.files["resume"]

    resume = read_resume(file)

    prompt = f"""
You are an expert Resume Writer.

Rewrite this resume professionally.

Improve:
- Grammar
- ATS Optimization
- Professional wording

Resume:

{resume}
"""

    try:
        response = model.generate_content(prompt)
        rewritten_resume = response.text

    except Exception as e:
        print("Gemini Error:", e)
        rewritten_resume = "AI Resume Rewrite is temporarily unavailable."

    return render_template(
        "rewrite.html",
        rewritten_resume=rewritten_resume
    ) 

@app.route("/history")
def history():

    history_data = get_history()

    return render_template(
        "history.html",
        history=history_data
    )


# ---------------- Run ----------------

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)