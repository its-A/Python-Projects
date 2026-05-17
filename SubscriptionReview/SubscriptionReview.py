'''SCENERIO:The Subscription Growth Review
Junior Data Analyst at SkillSprint, an online learning platform that offers short subscription-based courses.

The company recently launched a new weekend promotion to increase subscriptions. At the end of the quarter, the business team wants a clear review of how the campaign performed.

You have been given a CSV file containing weekly performance data. Before you can analyze it, you need to inspect the file, clean several issues, organize the data into a usable structure, and then produce findings for two audiences:

a technical audience (the product analytics team),
a non-technical audience (the executive leadership team).
Your task is to complete the full beginner-level analytics workflow: data collection, preprocessing, storage, analysis, EDA, and data storytelling.'''



import pandas as pd
import csv
import statistics

#Task1: Load & Inspect the Data
raw_rows = []

with open ('/Users/eugeniaportillo/Desktop/GitHub/Subscription Growth Review/weekly_growth.csv') as file:
    reader = csv.DictReader(file)
    field_names = reader.fieldnames
    for row in reader:
        raw_rows.append(row)
        

print("Fields:", field_names)
print("Record count:", len(raw_rows))

for row in raw_rows:
    print(row)

#Task2: Clean & Store the Data    

ticket_values = []
for row in raw_rows:
    if row["support_tickets"] != "":
        ticket_values.append(int(row["support_tickets"]))

ticket_median = int(statistics.median(ticket_values))

seen = set()
cleaned_data = []

for row in raw_rows:
    row_key = tuple(row.items())
    if row_key in seen:
        continue
    seen.add(row_key)

    region = row["region"].strip().title()

    signups = int(row["signups"])
    active_users = int(row["active_users"])
    paid_subscriptions = int(row["paid_subscriptions"])
    revenue = int(row["revenue"])

    if row["support_tickets"] == "":
        support_tickets = ticket_median
    else:
        support_tickets = int(row["support_tickets"])

    conversion_rate = round((paid_subscriptions / signups) * 100, 2)

    cleaned_data.append({
        "week": row["week"],
        "region": region,
        "signups": signups,
        "active_users": active_users,
        "paid_subscriptions": paid_subscriptions,
        "revenue": revenue,
        "support_tickets": support_tickets,
        "conversion_rate": conversion_rate
    })

   
for row in cleaned_data:
    print(row)

#Task3: Perform Analysis 
total_revenue = sum(row["revenue"] for row in cleaned_data)

revenue_by_region = {}
for row in cleaned_data:
    region = row["region"]
    revenue_by_region[region] = revenue_by_region.get(region, 0) + row["revenue"]

top_region = max(revenue_by_region, key=revenue_by_region.get)
top_revenue_week = max(cleaned_data, key=lambda row: row["revenue"])

average_conversion = round(
    sum(row["conversion_rate"] for row in cleaned_data) / len(cleaned_data), 2
)

print("Total revenue:", total_revenue)
print("Revenue by region:", revenue_by_region)
print("Top region:", top_region)
print("Highest revenue week:", top_revenue_week["week"], top_revenue_week["revenue"])
print("Average conversion rate:", average_conversion)

#Task4: EDA Review
revenue_by_week = {}
for row in cleaned_data:
    week = row["week"]
    revenue_by_week[week] = revenue_by_week.get(week, 0) + row["revenue"]

highest_ticket_row = max(cleaned_data, key=lambda row: row["support_tickets"])

print("Revenue by week:")
for week, revenue in revenue_by_week.items():
    print(week, revenue)

print("Highest support ticket record:", highest_ticket_row)

#Task5: Technical Report
#Objective, Data Preparation, Key Metrics, EDA Notes, Recommendation
print("Technical Report: Subscription Growth Review")
print("\nObjective:")
print("Review weekly subscription performance after the weekend promotion.")
print("\nData Preparation:")
print("The dataset contained inconsistent region capitalization, one missing support ticket value, and one exact duplicate row.")
print("The region values were standardized, the missing ticket value was filled with the median of the available ticket values, and the duplicate row was removed.")
print("\nKey Metrics:")
print(f"- Total revenue: ${total_revenue}")
print(f"- Top revenue region: {top_region}")
print(f"- Highest revenue week: {top_revenue_week['week']} (${top_revenue_week['revenue']})")
print(f"- Average conversion rate: {average_conversion}%")
print("\nEDA Notes:")
print("Revenue appears stronger in the later weeks.")
print("One West-region record has the highest support ticket value and should be reviewed as a possible outlier or friction point.")
print("\nRecommendation:")
print("Continue tracking revenue and conversion rate, but also segment support tickets by issue type to determine whether higher performance is creating new user problems.")


#Task6: Non-Technical Report
#what was analyzed, most important result, why it matters, what should haveppen next, which two visuals would recommend for the presentation

print("\nNon-Technical Report:")
print("We reviewed weekly performance after the weekend promotion to understand how subscription growth changed over the quarter. The strongest result is that revenue and conversions improved over time, with one region performing especially well. This matters because it suggests the campaign is helping turn new signups into paid subscribers. However, one part of the data also shows unusually high support demand, so growth should be reviewed together with user experience. As a next step, the company should continue the campaign while investigating support ticket causes. For the presentation, I would recommend a line chart showing revenue by week and a bar chart comparing total revenue by region.")


