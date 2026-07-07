from resume_reader import read_resume

print("===== Smart Resume Analyzer =====")

resume = read_resume()

print(resume)

from skill_analyser import find_skills




from resume_reader import read_resume

from skill_analyser import find_skills,calculate_score,find_missing_skills,get_suggestion

from report_generator import generate_report 

print("===== Smart Resume Analyzer =====")

resume = read_resume()

print(resume)

skills = find_skills(resume)

print("\nSkills Found:")

for skill in skills:
    
    print("-", skill)

score = calculate_score(skills)

print("\nResume Score:", score, "/100")

missing = find_missing_skills(skills)

print("\nMissing skills:")

for skill in missing:

    print("-",skill)

suggestion = get_suggestion(score)

print("\nSuggestion:",suggestion)

generate_report(skills, score, missing)