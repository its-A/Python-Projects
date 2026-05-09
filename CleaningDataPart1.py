sales_data = [
    {'Product ID': 'abc123',  'Units Sold': 10,     'Revenue USD': 1250.0, 'Date': '2023-01-01'},
    {'Product ID': 'abc123',  'Units Sold': 10,     'Revenue USD': 1250.0, 'Date': '2023-01-01'},
    {'Product ID': 'abc123 ', 'Units Sold': 10,     'Revenue USD': 1250.0, 'Date': '2023-01-01'},
    {'Product ID': 'XYZ789',  'Units Sold': -5,     'Revenue USD': -300.0, 'Date': '2023-02-15'},
    {'Product ID': None,      'Units Sold': 8,      'Revenue USD': 800.0,  'Date': '2023-03-10'},
    {'Product ID': 'test123', 'Units Sold': 1000,   'Revenue USD': 50000.0,'Date': '2023-03-15'},
    {'Product ID': 'test123', 'Units Sold': 1000,   'Revenue USD': 50000.0,'Date': '2023-03-15'},
    {'Product ID': 'DEF456',  'Units Sold': None,   'Revenue USD': 150.0,  'Date': '2023-03-20'}
]

print("Original Data:\n")
for i, record in enumerate(sales_data):
    print(f"{i+1}. {record}")

sales_cleaned = [
    record for record in sales_data
    if record['Product ID'] is not None and record['Units Sold'] is not None
]

print("\nAfter Removing Missing Values:\n")
for i, record in enumerate(sales_cleaned):
    print(f"{i+1}. {record}")

for record in sales_cleaned:
    record['Product ID'] = record['Product ID'].strip()

print("\nAfter Stripping Whitespace from 'Product ID':\n")
for i, record in enumerate(sales_cleaned):
    print(f"{i+1}. {record}")

sales_cleaned = [
    record for record in sales_cleaned
    if record['Units Sold'] >= 0 and record['Revenue USD'] >= 0
]

print("\nAfter Removing Negative Values:\n")
for i, record in enumerate(sales_cleaned):
    print(f"{i+1}. {record}")

unique_records = []
seen = set()

for record in sales_cleaned:
    record_tuple = tuple(record.items())
    if record_tuple not in seen:
        seen.add(record_tuple)
        unique_records.append(record)

sales_cleaned = unique_records

print("\nAfter Removing Duplicates:\n")
for i, record in enumerate(sales_cleaned):
    print(f"{i+1}. {record}")
