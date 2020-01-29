# Import CSV file

import os
import csv

PyBankcsv = "budget_data.csv"

# Create and open file

with open(PyBankcsv, "r") as csvfile:
	budget_data = csv.reader(csvfile, delimiter = ",")
	header = next(budget_data)

	# Financial Analysis begins here

	Total_Months = 0
	Total_ProfitLoss = 0
	Total_ProfitLoss_Change = 0
	Previous_month_ProfitLoss = 0
	Current_month_ProfitLoss = 0
	Greatest_Increase = 0
	Greatest_Decrease = 0
	ProfitLoss_Change_List = 0

	for row in budget_data:

		# Calculate Total Profit Loss and Count Months
		Total_ProfitLoss = Total_ProfitLoss + int(row[1])
		Total_Months = Total_Months + 1

		# Calculate Increase and Decrease in Profit Loss

		Increase = int(row[1]) - Previous_month_ProfitLoss
		Total_ProfitLoss_Change = Total_ProfitLoss_Change + Increase
		Previous_month_ProfitLoss = int(row[1])
		ProfitLoss_Change_List = ProfitLoss_Change_List + Increase

		if(Increase > Greatest_Increase):
			Greatest_Increase = Increase

		if(Increase < Greatest_Decrease):
			Greatest_Decrease = Increase

def Average_ProfitLoss(ProfitLoss):
	ProfitLoss_Change_List = ProfitLoss.split()
	ProfitLoss_Sum=0
	for i in len(ProfitLoss_Change_List):
		ProfitLoss_Sum += len(ProfitLoss_Change_List[i])
	return ProfitLoss_Change_List/i

	

# Print Output

print()
print(f"Financial Analysis")
print(f"--------------------")
print(f"Total Months: {Total_Months}")
print(f"Total ProfitLoss: ${Total_ProfitLoss:.0f}")
print(f"Average Change: ${ProfitLoss_Change_List:.2f}")
print(f"Greatest Increase: ${Greatest_Increase:.0f}")
print(f"Greatest Decrease: ${Greatest_Decrease:.0f}")



