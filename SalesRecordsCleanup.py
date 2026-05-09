
import csv

with open("raw_sales.csv", mode="r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    header = next(reader)

    print("Header:", header)
    print("\nRaw rows:\n")
    for row in reader:
        print(row)
        

cleaned_rows = []

with open("raw_sales.csv", mode="r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        sale_id, customer, amount, date_text = [value.strip() for value in row]

        if customer == "":
            customer = "Unknown"

        if amount == "":
            amount = "0.0"

        cleaned_rows.append([sale_id, customer, amount, date_text])

from datetime import datetime

valid_rows = []

for row in cleaned_rows:
    sale_id, customer, amount, date_text = row

    amount = float(amount)
    sale_date = datetime.strptime(date_text, "%d/%b/%Y")

    if amount >= 0:
        valid_rows.append({
            "sale_id": sale_id,
            "customer": customer,
            "amount": amount,
            "sale_date": sale_date
        })

unique_records = []
seen = set()

for record in valid_rows:
    record_tuple = (
        record["sale_id"],
        record["customer"],
        record["amount"],
        record["sale_date"]
    )

    if record_tuple not in seen:
        seen.add(record_tuple)
        unique_records.append(record)

with open("cleaned_sales.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow(["sale_id", "customer", "amount", "sale_date"])

    for record in unique_records:
        writer.writerow([
            record["sale_id"],
            record["customer"],
            f"{record['amount']:.2f}",
            record["sale_date"].strftime("%Y-%m-%d")
        ])

with open("cleaned_sales.csv", mode="r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)

    print("\nContents of cleaned_sales.csv:\n")
    for row in reader:
        print(row)


'''OUTPUT:

Header: ['sale_id', 'customer', 'amount', 'date']

Raw rows:

['1001', ' Alice ', ' 120.50 ', '14/Jul/2026']
['1002', 'Bob', '', '15/Jul/2026']
['1003', ' Charlie ', '200.00', '16/Jul/2026']
['1001', ' Alice ', '120.50', '14/Jul/2026']
['1004', ' ', '150.75', '17/Jul/2026']
['1005', 'Eva', '-50.00', '18/Jul/2026']
['1006', ' Daniel ', ' 89.99 ', '19/Jul/2026']
['1007', 'Emma', '310.25', '20/Jul/2026']
['1008', ' Frank ', ' ', '21/Jul/2026']
['1009', 'Gina', '45.00', '22/Jul/2026']
['1010', ' Henry ', '500.00', '23/Jul/2026']
['1011', 'Isla', ' 75.50 ', '24/Jul/2026']
['1012', ' Jack ', '120.00', '25/Jul/2026']
['1013', ' ', '60.00', '26/Jul/2026']
['1014', 'Karen', '-15.00', '27/Jul/2026']
['1015', 'Leo', '220.40', '28/Jul/2026']
['1016', 'Mia', '220.40', '28/Jul/2026']
['1016', 'Mia', '220.40', '28/Jul/2026']
['1017', ' Noah ', ' 0.00 ', '29/Jul/2026']
['1018', 'Olivia', '185.90', '30/Jul/2026']

Contents of cleaned_sales.csv:

['sale_id', 'customer', 'amount', 'sale_date']
['1001', 'Alice', '120.50', '2026-07-14']
['1002', 'Bob', '0.00', '2026-07-15']
['1003', 'Charlie', '200.00', '2026-07-16']
['1004', 'Unknown', '150.75', '2026-07-17']
['1006', 'Daniel', '89.99', '2026-07-19']
['1007', 'Emma', '310.25', '2026-07-20']
['1008', 'Frank', '0.00', '2026-07-21']
['1009', 'Gina', '45.00', '2026-07-22']
['1010', 'Henry', '500.00', '2026-07-23']
['1011', 'Isla', '75.50', '2026-07-24']
['1012', 'Jack', '120.00', '2026-07-25']
['1013', 'Unknown', '60.00', '2026-07-26']
['1015', 'Leo', '220.40', '2026-07-28']
['1016', 'Mia', '220.40', '2026-07-28']
['1017', 'Noah', '0.00', '2026-07-29']
['1018', 'Olivia', '185.90', '2026-07-30']
