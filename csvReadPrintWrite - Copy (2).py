import csv
# import pandas
import statistics

# create and open the file 
csvfile = open('myfile3.csv', 'w', newline= '') 
print("File Created")

# create column headers
csvwriter = csv.writer(csvfile)
csvwriter.writerow(['Temp', 'Noise'])
print("Columns Created")

csvwriter.writerow([25, 27])
csvwriter.writerow([23, 24])

print("Data Created")
csvfile.close()
print("Files closed after created rows")

csvfile = open("myfile3.csv","r")
line = csvfile.readline()
print(line, "readline1")
line = csvfile.readline()
print(line, "readline2")
line = csvfile.readline()
print(line, "readline3")
line = csvfile.readline()
print(line, "readline4")
line = csvfile.readline()
print(line, "readline5")
csvfile.close()
print("Filed closed after printing rows")

# open the file to append to it
csvfile = open('myfile3.csv', "a", newline= '') 
csvwriter = csv.writer(csvfile)
csvwriter.writerow([20, 28])
csvwriter.writerow([19, 10])
csvfile.close()
print("closed append")