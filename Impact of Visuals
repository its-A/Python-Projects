'''--- Example 1: Unplanned Data Dump ---'''
sales_data = [
    ("Product A", "Q1", 50), ("Product A", "Q2", 55), ("Product A", "Q3", 70), ("Product A", "Q4", 65),
    ("Product B", "Q1", 120), ("Product B", "Q2", 130), ("Product B", "Q3", 110), ("Product B", "Q4", 115),
    ("Product C", "Q1", 25), ("Product C", "Q2", 40), ("Product C", "Q3", 60), ("Product C", "Q4", 85)
]

print("Unplanned Data Dump:")
for entry in sales_data:
    print(f"Product: {entry[0]}, Quarter: {entry[1]}, Sales: ${entry[2]}k")


'''--- Example 2: Planned Data Presentation ---'''
'''Question: Which product grew the most from Q1 to Q4?'''
sales_data = [
    ("Product A", "Q1", 50), ("Product A", "Q2", 55), ("Product A", "Q3", 70), ("Product A", "Q4", 65),
    ("Product B", "Q1", 120), ("Product B", "Q2", 130), ("Product B", "Q3", 110), ("Product B", "Q4", 115),
    ("Product C", "Q1", 25), ("Product C", "Q2", 40), ("Product C", "Q3", 60), ("Product C", "Q4", 85)
]

product_sales = {}
for product, quarter, sale in sales_data:
    if product not in product_sales:
        product_sales[product] = {}
    product_sales[product][quarter] = sale

product_growth = {}
for product, quarterly_data in product_sales.items():
    growth = quarterly_data["Q4"] - quarterly_data["Q1"]
    product_growth[product] = growth

print("Planned Presentation: Product Growth from Q1 to Q4")
print("-------------------------------------------------")
for product, growth in product_growth.items():
    print(f"{product}: Growth of ${growth}k")

'''--- Example 3: Quick Look at matplotlib ---'''    
import matplotlib.pyplot as plt

# 1. Provide the data
days = [1, 2, 3, 4, 5]
sales = [10, 15, 12, 20, 25]

# 2. Create the plot
plt.plot(days, sales, marker='o')

# 3. Add a title and labels
plt.title("Simple Sales Trend")
plt.xlabel("Day")
plt.ylabel("Sales")

# 4. Display the visual
plt.show()