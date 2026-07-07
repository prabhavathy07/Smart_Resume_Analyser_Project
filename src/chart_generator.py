import os
import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt

def generate_chart(score, ats):

    os.makedirs("static/images", exist_ok=True)

    labels = ["Resume Score", "ATS Score"]
    values = [score, ats]

    plt.figure(figsize=(5, 4))
    plt.bar(labels, values)

    plt.ylim(0, 100)
    plt.ylabel("Percentage")
    plt.title("Resume Analysis")

    plt.savefig(os.path.join("static", "images", "chart.png"))

    plt.close()