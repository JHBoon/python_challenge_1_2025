# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources/budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis/budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0

# Add more variables to track other necessary financial data
net_change_list = []
previous_net = None
average_change = 0
greatest_increase = 0
greatest_decrease = 0

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)
    csv_list = list(reader)

    # Skip the header row
header = csv_list[0]

    # Extract first row to avoid appending to net_change_list
previous_net = int(csv_list[1][1])
total_months += 1
total_net = previous_net

    # Track the total and net change
for row in csv_list[2:]:
        total_months += 1

    # Track the total net
        current_net = int(row[1])
        total_net += current_net

    # Track the net change
        net_change =current_net - previous_net
        net_change_list.append(net_change)

    # Calculate the greatest increase in profits (month and amount)
        if net_change > greatest_increase:
            greatest_increase = net_change
            greatest_increase_month = row[0] 

    # Calculate the greatest decrease in losses (month and amount)
        if net_change < greatest_decrease:
            greatest_decrease = net_change
            greatest_decrease_month = row[0]

    # Calculate the average net change across the months
        previous_net = current_net 
        if net_change_list:
            average_change = sum(net_change_list) / len(net_change_list)

# Generate the output summary
print("Financial Analysis")
print("----------------------------")
# Print the output
print(f"Total Months: {total_months}")
print(f"Total Net:  ${total_net}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest increase in Profits:{greatest_increase_month} ${greatest_increase}")
print(f"Greatest decrease in Profits: {greatest_decrease_month} ${greatest_decrease}")


# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write("Financial Analysis\n")
    txt_file.write("----------------------------\n")
    txt_file.write(f"Total Months: {total_months}\n")
    txt_file.write(f"Total Net:  ${total_net}\n")
    txt_file.write(f"Average Change: ${average_change:.2f}\n")
    txt_file.write(f"Increase in Profits:{greatest_increase_month} ${greatest_increase}\n")
    txt_file.write(f"Increase in Profits: {greatest_decrease_month} ${greatest_decrease}\n")