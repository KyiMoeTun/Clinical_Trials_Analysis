#Column Definition 
#dbp -> diastolic blood pressure in mmHg
#The diastolic blood pressure in mmHg over the course of 1 month, 2 months, etc. is 
#represented by dbp1, dbp2, etc.
#A -> (new drug)
#B -> (placebo)

import csv

# Open the raw text file for reading
with open('raw.txt', 'r') as raw:
    # Read the lines from the file and store in a list
    content = raw.readlines()

    # Create the header row for the CSV file
    headers = "Subject,TRT,DBP1,DBP2,DBP3,DBP4,DBP5,Age,Sex"
    row = []
    row.append(headers)

    # Loop through the lines in the content list
    for line in content[1:]:
        # Remove whitespaces and join the line
        line = "".join(line.split())

        # Extract the subject
        sub = line[:2] if line[1].isdigit() else line[0]

        # Extract the treatment value
        trt = line[1] if line[2].isdigit() else line[2]

        # Extract the sex value
        sex = line[-1]

        # Extract the age value
        age = line[-3:-1]

        # Extract the DBP values
        new_line = line[3:-3] if line[1].isdigit() else line[2:-3]
        DBP1 = new_line[:3]
        DBP2 = new_line[3:6]
        DBP3 = new_line[6:9]
        DBP4 = new_line[9:12]
        DBP5 = new_line[12:] 

        # Join the extracted values and create a row string
        row_value = ",".join([sub, trt, DBP1, DBP2, DBP3, DBP4, DBP5, age, sex])
        row.append(row_value)

# Open the CSV file for writing
with open('dbp.csv', 'w', newline='') as f:
    # Create a CSV writer object
    writer = csv.writer(f)

    # Loop through the values in the row list
    for value in row:
        # Write each row to the CSV file
        writer.writerow(value.split(','))
