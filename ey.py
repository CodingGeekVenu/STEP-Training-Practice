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

def analyze_super_wheels_sales():
    month_data = {'April': 30, 'May': 31, 'June': 30, 'July': 31, 'August': 31, 'September': 30}

    retail_sales = 0
    corporate_sales = 0
    
    for month, days in month_data.items():
        daily_sales = 1
        inc = 2
        monthly_total = 0
        
        for day in range(1, days + 1):
            if day % 5 == 0:
                corporate_sales += daily_sales
            else:
                retail_sales += daily_sales
            
            monthly_total += daily_sales
            
            daily_sales += inc
            inc += 2
            
        print(f"Month: {month}, Total Sales: {monthly_total}")

    total_sales = retail_sales + corporate_sales

    print(f"Total Corporate Sales: {corporate_sales}")
    print(f"Total Retail Sales: {retail_sales}")
    print(f"Total Overall Sales: {total_sales}")

analyze_super_wheels_sales()