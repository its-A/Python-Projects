'''---- Example 1: Executive Summary: this answers big picture questions very quickly ----'''
sales_data = [
    {'product_id': 'P001', 'category': 'Electronics', 'region': 'North', 'quantity': 2, 'price': 1200},
    {'product_id': 'P002', 'category': 'Apparel', 'region': 'North', 'quantity': 5, 'price': 50},
    {'product_id': 'P003', 'category': 'Home Goods', 'region': 'South', 'quantity': 10, 'price': 25},
    {'product_id': 'P004', 'category': 'Electronics', 'region': 'South', 'quantity': 1, 'price': 1500},
    {'product_id': 'P001', 'category': 'Electronics', 'region': 'West', 'quantity': 3, 'price': 1200},
    {'product_id': 'P005', 'category': 'Apparel', 'region': 'West', 'quantity': 8, 'price': 45},
    {'product_id': 'P006', 'category': 'Home Goods', 'region': 'North', 'quantity': 12, 'price': 20},
    {'product_id': 'P002', 'category': 'Apparel', 'region': 'South', 'quantity': 6, 'price': 50}
]

total_revenue = 0
sales_by_category = {}

for sale in sales_data:
    revenue = sale['quantity'] * sale['price']
    total_revenue += revenue
    category = sale['category']
    sales_by_category[category] = sales_by_category.get(category, 0) + revenue

gross_profit = total_revenue * 0.40
top_category = max(sales_by_category, key=sales_by_category.get)

print("--- Sales Report | For: EXECUTIVE ---")
print(f"Total Revenue this period: ${total_revenue:,.2f}")
print(f"Estimated Gross Profit: ${gross_profit:,.2f}")
print(f"Insight: Overall financial performance is strong, driven mainly by {top_category}.")





'''---- Example 2: Manager Summary ----This report is more detailed than the executive version because a manager needs to compare performance across regions and act on it'''
sales_data = [
    {'product_id': 'P001', 'category': 'Electronics', 'region': 'North', 'quantity': 2, 'price': 1200},
    {'product_id': 'P002', 'category': 'Apparel', 'region': 'North', 'quantity': 5, 'price': 50},
    {'product_id': 'P003', 'category': 'Home Goods', 'region': 'South', 'quantity': 10, 'price': 25},
    {'product_id': 'P004', 'category': 'Electronics', 'region': 'South', 'quantity': 1, 'price': 1500},
    {'product_id': 'P001', 'category': 'Electronics', 'region': 'West', 'quantity': 3, 'price': 1200},
    {'product_id': 'P005', 'category': 'Apparel', 'region': 'West', 'quantity': 8, 'price': 45},
    {'product_id': 'P006', 'category': 'Home Goods', 'region': 'North', 'quantity': 12, 'price': 20},
    {'product_id': 'P002', 'category': 'Apparel', 'region': 'South', 'quantity': 6, 'price': 50}
]

sales_by_region = {}

for sale in sales_data:
    revenue = sale['quantity'] * sale['price']
    region = sale['region']
    sales_by_region[region] = sales_by_region.get(region, 0) + revenue

lowest_region = min(sales_by_region, key=sales_by_region.get)

print("--- Sales Report | For: MANAGER ---")
print("Revenue by Region:")
for region, total in sales_by_region.items():
    print(f"- {region}: ${total:,.2f}")
print(f"Insight: {lowest_region} has the lowest revenue and may need additional attention.")


'''---- Example 3: Technical Summary ----This report focuses on structure, validation, and data quality.'''
sales_data = [
    {'product_id': 'P001', 'category': 'Electronics', 'region': 'North', 'quantity': 2, 'price': 1200},
    {'product_id': 'P002', 'category': 'Apparel', 'region': 'North', 'quantity': 5, 'price': 50},
    {'product_id': 'P003', 'category': 'Home Goods', 'region': 'South', 'quantity': 10, 'price': 25},
    {'product_id': 'P004', 'category': 'Electronics', 'region': 'South', 'quantity': 1, 'price': 1500},
    {'product_id': 'P001', 'category': 'Electronics', 'region': 'West', 'quantity': 3, 'price': 1200},
    {'product_id': 'P005', 'category': 'Apparel', 'region': 'West', 'quantity': 8, 'price': 45},
    {'product_id': 'P006', 'category': 'Home Goods', 'region': 'North', 'quantity': 12, 'price': 20},
    {'product_id': 'P002', 'category': 'Apparel', 'region': 'South', 'quantity': 6, 'price': 50}
]

num_transactions = len(sales_data)
unique_products = set(sale['product_id'] for sale in sales_data)

print("--- Sales Report | For: TECHNICAL ---")
print(f"Dataset contains {num_transactions} transaction records.")
print(f"Number of unique product IDs: {len(unique_products)}")
print(f"Data Schema Fields: {', '.join(sales_data[0].keys())}")
print("Recommendation: Validate price consistency for repeated product IDs.")