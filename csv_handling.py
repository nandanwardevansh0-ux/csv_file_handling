import csv
with open("sample.csv", "r") as file:
    data = csv.reader(file)
    print(data)
    # for i in data:
    #     print(i)
    #     print(i[0])  # Accessing the first column of each row

    # for i in data:
    #     if i[0]=="1004":
    #         print(i[0])
 #if we want to ignore the first row of the csv file we can use this
    count=0
    # for i in data:
    #     if count==0:
    #         continue
    #         count=count+1
    #     else:
    #         print(i[0])  # Accessing the first column of each row

    for row in data:
        if row[2] =="python":
            print(row[1])


with open("sample.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    total =0
    for row in reader:
        total =total +int(row[4])
print("Total:", total)



        
            
        