import csv

with open("data.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["Trans_ID", "Prod_Id", "price"])
    writer.writerow([1000, 1, 250])
    writer.writerow([1001, 2, 255])

with open("data.csv", "r") as file:
    reader = csv.reader(file)
    # print(list(reader))

    for row in reader:
        print("row", row)
