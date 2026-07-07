from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf(job_role, score, ats, found_skills, missing_skills, ai_suggestion):

    doc = SimpleDocTemplate("resume_report.pdf")
    styles = getSampleStyleSheet()

    elements = []

    elements.append(Paragraph("Smart Resume Analyzer Report", styles["Title"]))
    elements.append(Spacer(1, 12))

    elements.append(Paragraph(f"<b>Job Role:</b> {job_role}", styles["Normal"]))
    elements.append(Paragraph(f"<b>Resume Score:</b> {score}%", styles["Normal"]))
    elements.append(Paragraph(f"<b>ATS Score:</b> {ats}%", styles["Normal"]))

    elements.append(Spacer(1, 12))

    elements.append(Paragraph("<b>Skills Found</b>", styles["Heading2"]))

    for skill in found_skills:
        elements.append(Paragraph(f"- {skill}", styles["Normal"]))

    elements.append(Spacer(1, 12))

    elements.append(Paragraph("<b>Missing Skills</b>", styles["Heading2"]))

    for skill in missing_skills:
        elements.append(Paragraph(f"- {skill}", styles["Normal"]))

    elements.append(Spacer(1, 12))

    elements.append(Paragraph("<b>AI Suggestions</b>", styles["Heading2"]))

    ai_text = ai_suggestion.replace("\n", "<br/>")
    elements.append(Paragraph(ai_text, styles["Normal"]))

    doc.build(elements)

    print("✅ PDF Created Successfully")