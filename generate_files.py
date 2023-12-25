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
            if os.path.exists(f"links/{row[0]}"):
                continue
            os.mkdir(f"links/{row[0]}")
            os.chdir(f"links/{row[0]}")
            os.system("touch links.txt")
            with open("links.txt", "w") as f:
                f.write("Agent A: \nAgent B: \n")
            os.chdir("../../")