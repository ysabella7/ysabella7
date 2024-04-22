import csv
csvfile = open("myfile.csv", "x")
print("File Created")

csvwriter = csv.writer(csvfile)
csvwriter.writerow(['Name', 'Age', 'City'])
print("Columns Created")

csvwriter.writerow(['Alice', 25, 'New York'])
print("Data Created")

csvfile.close()
print("Closed")