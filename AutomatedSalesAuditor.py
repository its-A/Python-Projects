'''Your tasks are:

1.Create a list of sales values: [25.50, "error", 40.00, 15.75, "missing", 100.00].
2. Write a function called clean_and_sum that takes a list as an input.
3. Inside the function, use a loop to iterate through the list.
4. Use try-except to skip any value that cannot be converted to a float.
5. Calculate the total sales and the average sale price.
6. Return a dictionary containing the total and the average.'''

# 1. Create your raw_sales list
raw_sales = [25.50,"error",40.00, 15.75, "missing",100.00]

# 2-4. Define your clean_and_sum function here
def clean_and_sum(sales_list):
    clean_data = []
    for item in sales_list:
        try:
            #attempting conversion
            val = float(item)
            clean_data.append(val)
        except ValueError:
            #Skipping strings or missing values
            continue
        total_val = sum(clean_data)
#logic to avoid ZeroDivisionError if the lsit was all junk
    if len(clean_data) > 0:
        avg_val = total_val / len(clean_data)
    else:
        avg_val = 0
    return {"total": total_val, "average": avg_val}

# Final: Call your function with raw_sales and print the result

print(clean_and_sum(raw_sales))