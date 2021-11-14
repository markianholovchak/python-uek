import csv
with open('students.csv', newline='') as f:
    for line in f:
        reader = csv.DictReader(f)
        for row in reader:
            if(int(row['age']) < 30):
                print(f"{row['first_name']} {row['last_name']} {row['email']}")
