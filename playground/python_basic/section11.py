import csv
w = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]]

with open('./resource/sample3.csv','w', newline='') as f:
    wt = csv.writer(f)
    wt.writerows()