import csv

# with open("report.csv", "w", newline="") as file:
#     writer = csv.writer(file)
#     for i in range(50):

#         writer.writerow(["Name", "Age", "City"])
#         writer.writerow(["Alice", "25"])
#         writer.writerow(["Bob", "30", ])
#         writer.writerow(["Charlie", "error", "Chicago"])
#         writer.writerow(["David", "40", "Houston"])
#         writer.writerow(["Eve", "45", "Phoenix"])
#         writer.writerow(["Frank", "Error", "Philadelphia"])

with open("report_error.csv", "w", newline="") as file:
    writer = csv.writer(file)
    with open("report.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if (len(row)==3) and (row[1].lower()=="error"):
                writer.writerow(row)
        