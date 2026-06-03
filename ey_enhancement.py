'''
Problem - 1:  Ernst & Young

Sales trend -> Next Day = Previous Day + 2 * (n-1)
               where n is the day number

Corportate Customers - every 5th day (5, 10, 15, 20 etc)
Retail Customers - every day except 5th day

Output: Total vehicles sold per month
        (April, May, June, July, August, September)
        Sales by customer type
        - Retail Sales
        - Corporate Sales
'''

months = {'April': 30, 'May': 31, 'June': 30, 'July': 31, 'August': 31, 'September': 30}

def count_sales_per_month(month):
    total_sales = 0
    for day in range(1, months[month] + 1):
        total_sales += (day**2 - day + 1)  
    return total_sales

def count_corportate_sales_per_month(month):
    total_sales = 0
    for day in range(5, months[month] + 1, 5):
        total_sales += (day**2 - day + 1)  
    return total_sales

def count_retail_sales_per_month(month):
    total_sales = 0
    for day in range(1, months[month] + 1):
        if day % 5 != 0:
            total_sales += (day**2 - day + 1)
    return total_sales

def main():
    total_retail_sales = 0 
    total_corportate_sales = 0
    for month in months:
        total_sales = count_sales_per_month(month)
        print(f"Month: {month}, Total Sales: {total_sales}")
        total_retail_sales += count_retail_sales_per_month(month)
        total_corportate_sales += count_corportate_sales_per_month(month)

    print(f"Total Retail Sales: {total_retail_sales}")
    print(f"Total Corportate Sales: {total_corportate_sales}")

main()