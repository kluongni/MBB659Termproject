#!/usr/bin/env python

import csv



wantedlist = []
counter = 0
header = ""
with open('snpEff_genes.txt', newline='') as reader:
    for row in reader:
        temp = row.split()
        if counter == 1:
            header = temp
        if (len(temp) > 20) and counter >1:
            if (int(temp[4])>9) or (int(temp[5])>9) or (int(temp[6])>9) or (int(temp[7])>9) or (int(temp[8])>9) or (int(temp[9])>9) or (int(temp[10])>9) or (int(temp[11])>9) or (int(temp[12])>9) or (int(temp[13])>9) or (int(temp[14])>9) or (int(temp[15])>9) or (int(temp[16])>9) or (int(temp[17])>9) or (int(temp[18])>9) or (int(temp[19])>9) or (int(temp[20])>9):
                print(temp)
                wantedlist.append(temp)
        counter += 1

    wantedlist.insert(0,header)
    print(wantedlist)

    with open('output.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(wantedlist)
        
