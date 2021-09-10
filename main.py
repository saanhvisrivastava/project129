import csv

dataset_1 = []
dataset_2 = []

with open("read.csv", "r") as f:
    csvreader = csv.reader(f)
    print(csvreader)
    for row in csvreader: 
        dataset_1.append(row)



headers_1 = dataset_1[0]
star_data_1 = dataset_1[1:]

#headers_2 = dataset_2[0]
#star_data_2 = dataset_2[1:]

#headers = headers_1 + headers_2
star_data = []
for index, data_row in enumerate(star_data_1):
    star_data.append(star_data_1[index])

with open("sorted.csv", "a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers_1)
    csvwriter.writerows(star_data)
