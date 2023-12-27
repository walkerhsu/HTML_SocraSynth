import os
import sys
import csv
if __name__ == "__main__":
    os.system("rm -rf links/.DS_Store")
    os.system("rm -rf txt_files/.DS_Store")
    files_links = os.listdir("links")
    print(len(files_links))
    files_txt_files = os.listdir("txt_files")
    print(len(files_txt_files))
    sum1 = 0
    sum2 = 0
    move = True
    if move:
        for txtfile in files_txt_files:
            sum1 += 1
            if txtfile[-4:] != ".txt":
                continue
            if os.path.exists(f"links/{txtfile[:-4]}"):
                os.system(f"cp txt_files/{txtfile} links/{txtfile[:-4]}/{txtfile}")
                print(txtfile)
                sum2 += 1
        os.chdir("links")
        for folder in files_links:
            sum1 += 1
            tmp = os.listdir(folder)
            print(tmp)
        print(sum1, sum2)
        