import os
import sys
import csv
if __name__ == "__main__":
    # os.system("rm -rf CSV/.DS_Store")
    files = os.listdir("CSV")
    print(len(files))
    sum1 = 0
    sum2 = 0
    move = False
    if move:
        for file in files:
            if file[-4:] == ".csv":
                sum1 += 1
                if os.path.exists(f"CSV/{file[:-4]}"):
                    # print("yes")
                    os.system(f"mv CSV/{file} CSV/{file[:-4]}/GPT3.5/{file}")
                    print(file)
                    sum2 += 1
                else:
                    print(file)
        print(sum1, sum2)
        