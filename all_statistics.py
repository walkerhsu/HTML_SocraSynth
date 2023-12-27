import os
import csv
from matplotlib import pyplot as plt

if __name__ == "__main__":
    read = True
    rewrite = False
    if rewrite:
        with open("all_subjects.csv", "w") as f_w:
            with open("subjects-public.csv", 'r') as f_r:
                reader = csv.reader(f_r)
                for idx, row in enumerate(reader):
                    f_w.write(f"{row[0]}\n")
            with open("subjects-private.csv", 'r') as f_r:
                reader = csv.reader(f_r)
                for idx, row in enumerate(reader):
                    if idx == 0:
                        continue
                    f_w.write(f"{row[0]}\n")
    if read:
        score = []
        with open("all_subjects.csv", 'r') as f:
            reader = csv.reader(f)
            for idx, row in enumerate(reader):
                if idx == 0:
                    continue
                score.append(int(row[1]))

        print(f"average score : {sum(score)/len(score)}")
        plt.hist(score, bins=100)
        plt.xlabel("Score")
        plt.ylabel("Frequency")
        plt.title("Distribution of Scores")
        plt.savefig("score_distribution.png")
        plt.legend([f"Mean: {sum(score)/len(score)}"])
                
                