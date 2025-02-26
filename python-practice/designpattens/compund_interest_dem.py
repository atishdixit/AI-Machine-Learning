amount = float(input("Enter Amount"))
interest = float(input("Enter interest Rate"))
years = int(input("Enter nuber of years"))
interest = interest * 0.01
for value in range(years):
    amount = amount+amount*interest;
print("Investment After {} years: {:.2f}".format(years, amount))





