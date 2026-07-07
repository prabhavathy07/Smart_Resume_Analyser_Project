def find_skills(resume):

    skills = [
        "Python",
        "SQL",
        "Excel",
        "Java",
        "HTML",
        "CSS",
        "JavaScript",
        "Flask",
        "Git",
        "Machine Learning",
        "Data Science"
    ]

    found_skills = []

    for skill in skills:
        if skill.lower() in resume.lower():
            found_skills.append(skill)

    return found_skills

def calculate_score(found_skills, required_skills):

    matched = 0

    for skill in required_skills:
        if skill in found_skills:
            matched += 1

    score = (matched / len(required_skills)) * 100

    return round(score)

def find_missing_skills(found_skills):

    skills = [
        "Python",
        "SQL",
        "Excel",
        "Java",
        "HTML",
        "CSS",
        "JavaScript",
        "Flask",
        "Git",
        "Machine Learning",
        "Data Science"
    ]

    missing_skills= []

    for skill in skills:

        if skill not in found_skills:

            missing_skills.append(skill)

    return missing_skills

def get_suggestion(score):

    if score >= 80:

        return "Excellent Resume! You are ready to apply for IT jobs."
    
    elif score >= 50: 

        return "Good Resume Improve Your missing skills."
    
    else:

        return "Your resume needs improvement.Learn the missing skills."
    
def ats_score(resume):

    score = 0

    if "Skills" in resume:
        score += 20

    if "Education" in resume:
        score += 20

    if "Projects" in resume:
        score += 20

    if "Experience" in resume:
        score += 20

    if "Contact" in resume or "Email" in resume:
        score += 20

    return score