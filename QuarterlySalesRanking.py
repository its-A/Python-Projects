'''--- Example: Ranking Results into Performance Tiers Quarterly Sales'''

quarterly_sales_by_product = {
    "Stellar Smartwatch": 1850,
    "Quantum Laptop": 2200,
    "Nova Tablet": 1700,
    "Eclipse E-Reader": 950,
    "Gravity Bluetooth Speaker": 1200,
    "Orbit Wireless Mouse": 650,
    "Cosmic Coffee Maker": 450,
    "Meteor Mechanical Keyboard": 890,
    "Galaxy Gaming Chair": 1350,
    "Pulsar Power Bank": 510,
    "Supernova VR Headset": 250,
    "Comet Cable Organizer": 150
}
#Sorting products from highest to lowest sales
ranked_sales = sorted(
    quarterly_sales_by_product.items(),
    key=lambda item: item[1],
    reverse=True
)

for product, sales in ranked_sales:
    print(product, sales)

#This sorting step matters because it creates a logical order. The strongest products appear first, and the weakest ones appear last.
#Next, we can define tiers and create a text-based report:

TOP_TIER_COUNT = 3
BOTTOM_TIER_COUNT = 3

print("=" * 50)
print("Quarterly Product Performance Report")
print("=" * 50)
print("This report groups products into performance tiers to guide focus.\n")

for rank, (product, value) in enumerate(ranked_sales, start=1):
    if rank <= TOP_TIER_COUNT:
        print(f"{rank}. {product.upper()}: {value} units   (Top Performer)")
    elif rank > len(ranked_sales) - BOTTOM_TIER_COUNT:
        print(f"{rank}. {product.lower()}: {value} units   (Watchlist)")
    else:
        print(f"{rank}. {product}: {value} units")

print("\n--- Key Insight ---")
print("The top 3 products are driving a significant portion of our sales.")
print("The bottom 3 products may require review or support.")