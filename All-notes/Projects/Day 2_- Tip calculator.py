print("Welcome to the tip calculator")

bill = input("What was the total bill? $")
flt_bill = float(bill)

percent = input("What persentage tip you would like to give? 10, 12, or 15? ")
int_percent = int(percent)

people = input("How  many people to split the bill? ")
int_people = int(people)

total_bill = flt_bill * (int_percent/100) + flt_bill


tip = total_bill/int_people

round_tip = round(tip, 2)

print(f"Each person should pay: ${round_tip}")
