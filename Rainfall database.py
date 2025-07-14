# Rainfall database 

rain_data = [] 

years = int(input("Enter number of years: "))
total_rainfall = 0
total_months = 0

for year in range(1, years + 1):
    monthly_data = [] 
    for month in range(1, 13):
        rainfall = float(input(f"Enter rainfall for year {year}, month {month}: "))
        total_rainfall += rainfall
        total_months += 1
        monthly_data.append(rainfall)  # Add rainfall to current year's list
    rain_data.append(monthly_data)

average = total_rainfall / total_months

print(f"\nTotal months: {total_months}")
print(f"Total rainfall: {total_rainfall:.2f} inches")
print(f"Average rainfall per month: {average:.2f} inches")

month_names = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

print("\nRain database (inches per month):")
for year_index, year_data in enumerate(rain_data, start=1):
    print(f"\nYear {year_index}:")
    for month_index, rainfall in enumerate(year_data):
        print(f"  {month_names[month_index]}: {rainfall:.2f} inches")