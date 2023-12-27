import os
import sys
import csv
if __name__ == "__main__":
    csv_file = sys.argv[1]
    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        for idx, row in enumerate(reader):
            if idx == 0:
                continue
            if os.path.exists(f"CSV/{row[0]}"):
                continue
            os.mkdir(f"CSV/{row[0]}")
            os.chdir(f"CSV/{row[0]}")
            os.mkdir(f"GPT3.5")
            os.chdir("../../")