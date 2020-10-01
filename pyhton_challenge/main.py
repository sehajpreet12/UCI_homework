VERSION 1.0 CLASS
BEGIN
  MultiUse = -1  'True
END
Attribute VB_Name = "Sheet1"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = True
#import library
Import os
Import csv

#joining path
budget_data = os.Path.Join("Resources", "budget_data.csv")

# open and read csv
with open(budget_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvfile)
    # skip header row
    print(f"Header: {csv_header}")

    # find net amount of profit and loss
    P = []
    months = []

    #read through each row of data after header
    for rows in csvreader:
        P.append(int(rows[1]))
        months.append(rows[0])

    # find revenue change
    revenue_change = []

    for x in range(1, len(P)):
        revenue_change.append((int(P[x]) - int(P[x-1])))
    
    # calculate average revenue change
    revenue_average = Sum(revenue_change) / Len(revenue_change)
    
    # calculate total length of months
    total_months = Len(months)

    # greatest increase in revenue
    greatest_increase = Max(revenue_change)
    # greatest decrease in revenue
    greatest_decrease = Min(revenue_change)


    # print the Results
    Print ("Financial Analysis")

    Print ("....................................................................................")

    Print ("total months: " + Str(total_months))

    Print ("Total: " + "$" + Str(Sum(P)))

    Print ("Average change: " + "$" + Str(revenue_average))

    print("Greatest Increase in Profits: " + str(months[revenue_change.index(max(revenue_change))+1]) + " " + "$" + str(greatest_increase))

    print("Greatest Decrease in Profits: " + str(months[revenue_change.index(min(revenue_change))+1]) + " " + "$" + str(greatest_decrease))


    # output to a text file

    file = open("output.txt","w")

    file.write ("Financial Analysis" + "\n")

    file.write ("...................................................................................." + "\n")

    file.write ("total months: " + Str(total_months) + "\n")

    file.write ("Total: " + "$" + Str(Sum(P)) + "\n")

    file.write ("Average change: " + "$" + Str(revenue_average) + "\n")

    file.write("Greatest Increase in Profits: " + str(months[revenue_change.index(max(revenue_change))+1]) + " " + "$" + str(greatest_increase) + "\n")

    file.write("Greatest Decrease in Profits: " + str(months[revenue_change.index(min(revenue_change))+1]) + " " + "$" + str(greatest_decrease) + "\n")

    file.close()
