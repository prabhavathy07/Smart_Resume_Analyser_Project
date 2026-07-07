def generate_report(found_skills,score,missing_skills):

    file = open("output/report.txt","w")

    file.write("=== Smart Resume Analyser ===\n\n")

    file.write("Skills Found:\n")

    for skill in found_skills:file.write("-" + skill + "\n")

    file.write ("\nResume Score: "+ str(score) + "/100\n\n")

    file.write("Missing Skills:\n")

    for skill in missing_skills:file.write("-" + skill + "\n")

    file.close()

    print("\nReport Generated Successfully!")