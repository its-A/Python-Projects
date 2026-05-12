'''---Example 1: Filtering Numerical Data---'''
# Dataset: final exam scores
exam_scores = [88, 92, 65, 71, 59, 70, 85, 43, 99, 78]

# Empty list to store results
passing_scores = []

# Passing threshold
PASSING_GRADE = 70

# Filter the list
for score in exam_scores:
    if score >= PASSING_GRADE:
        passing_scores.append(score)

print(f"Original Scores: {exam_scores}")
print(f"Passing Scores (>= {PASSING_GRADE}): {passing_scores}")


'''---Example 2: Filtering Text Data in a Complex Structure--'''
support_tickets = [
    {'ticket_id': 'T101', 'priority': 'Low', 'status': 'Closed'},
    {'ticket_id': 'T102', 'priority': 'High', 'status': 'Open'},
    {'ticket_id': 'T103', 'priority': 'Medium', 'status': 'Open'},
    {'ticket_id': 'T104', 'priority': 'High', 'status': 'In Progress'},
    {'ticket_id': 'T105', 'priority': 'Low', 'status': 'Open'}
]

high_priority_tickets = []

for ticket in support_tickets:
    if ticket['priority'] == 'High':
        high_priority_tickets.append(ticket)

print("High-Priority Tickets:")
for ticket in high_priority_tickets:
    print(ticket)


'''---Example 3: Using if, elif, and else to Classify Data--'''
exam_scores = [88, 92, 65, 71, 59]

for score in exam_scores:
    if score >= 90:
        label = "Excellent"
    elif score >= 70:
        label = "Pass"
    else:
        label = "Needs Improvement"

    print(f"Score: {score} -> {label}”)
          

'''---Example 4: Filtering with Compound Conditions
find only support tickets that are high priority and open--'''
support_tickets = [
    {'ticket_id': 'T101', 'priority': 'Low', 'status': 'Closed'},
    {'ticket_id': 'T102', 'priority': 'High', 'status': 'Open'},
    {'ticket_id': 'T103', 'priority': 'Medium', 'status': 'Open'},
    {'ticket_id': 'T104', 'priority': 'High', 'status': 'In Progress'},
    {'ticket_id': 'T105', 'priority': 'Low', 'status': 'Open'}
]

urgent_open_tickets = []

for ticket in support_tickets:
    if ticket['priority'] == 'High' and ticket['status'] == 'Open':
        urgent_open_tickets.append(ticket)

print("Urgent and Open Tickets:")
print(urgent_open_tickets)

'''---Example 5: Filtering with Compound Conditions
find tickets that are either high priority or open--'''
support_tickets = [
    {'ticket_id': 'T101', 'priority': 'Low', 'status': 'Closed'},
    {'ticket_id': 'T102', 'priority': 'High', 'status': 'Open'},
    {'ticket_id': 'T103', 'priority': 'Medium', 'status': 'Open'},
    {'ticket_id': 'T104', 'priority': 'High', 'status': 'In Progress'},
    {'ticket_id': 'T105', 'priority': 'Low', 'status': 'Open'}
]

selected_tickets = []

for ticket in support_tickets:
    if ticket['priority'] == 'High' or ticket['status'] == 'Open':
        selected_tickets.append(ticket['ticket_id'])

print("Selected Tickets:", selected_tickets)


'''---Example 6: Filtering with Compound Conditions
find tickets that are not closed--'''
support_tickets = [
    {'ticket_id': 'T101', 'priority': 'Low', 'status': 'Closed'},
    {'ticket_id': 'T102', 'priority': 'High', 'status': 'Open'},
    {'ticket_id': 'T103', 'priority': 'Medium', 'status': 'Open'},
    {'ticket_id': 'T104', 'priority': 'High', 'status': 'In Progress'},
    {'ticket_id': 'T105', 'priority': 'Low', 'status': 'Open'}
]

active_tickets = []

for ticket in support_tickets:
    if not ticket['status'] == 'Closed':
        active_tickets.append(ticket['ticket_id'])

print("Active Tickets:", active_tickets)



'''---Example 7: Combining and, or, and Parentheses --'''
products = [
    {'sku': 'E101', 'category': 'Electronics', 'type': 'Smartphone', 'stock': 50},
    {'sku': 'E102', 'category': 'Electronics', 'type': 'Laptop', 'stock': 15},
    {'sku': 'H103', 'category': 'Home Goods', 'type': 'Blender', 'stock': 10},
    {'sku': 'E104', 'category': 'Electronics', 'type': 'Headphones', 'stock': 100}
]

flash_sale_items = []

for product in products:
    if product['category'] == 'Electronics' and (product['type'] == 'Smartphone' or product['stock'] < 20):
        flash_sale_items.append(product['sku'])

print(f"SKUs for Flash Sale: {flash_sale_items}")


'''---Example 8: Calculating Metrics per Category: Total Sales per Category --'''
sales_data = [
    ('T001', 'Electronics', 1200),
    ('T002', 'Home Goods', 150),
    ('T003', 'Electronics', 850),
    ('T004', 'Apparel', 55),
    ('T005', 'Home Goods', 220),
    ('T006', 'Electronics', 1500)
]

category_totals = {}

for transaction_id, category, amount in sales_data:
    if category not in category_totals:
        category_totals[category] = 0

    category_totals[category] += amount

print("Total Sales Revenue per Category:")
for category, total in category_totals.items():
    print(f"- {category}: ${total}")


'''---Example 9: Calculating Metrics per Category: Average Score per Group --'''
student_data = [
    ('Ava', 'Group 1', 80),
    ('Ben', 'Group 2', 72),
    ('Cara', 'Group 1', 90),
    ('Dan', 'Group 2', 68),
    ('Ella', 'Group 1', 85)
]

group_totals = {}
group_counts = {}

for name, group, score in student_data:
    if group not in group_totals:
        group_totals[group] = 0
        group_counts[group] = 0

    group_totals[group] += score
    group_counts[group] += 1

print("Average Score per Group:")
for group in group_totals:
    average = group_totals[group] / group_counts[group]
    print(f"- {group}: {average:.2f}")