products = ['Product A', 'Product B', 'Product C', 'Product D']
sales = [350, 520, 280, 410]

import matplotlib.pyplot as plt

products = ['Product A', 'Product B', 'Product C', 'Product D']
sales = [350, 520, 280, 410]

fig, ax = plt.subplots(figsize=(12, 6))
ax.bar(products, sales, color='#4A90E2')
ax.set_ylim(0, 600)

ax.set_title(
    'Quarterly Sales Performance',
    fontsize=20,
    fontweight='bold',
    fontfamily='serif',
    pad=20
)

ax.set_ylabel(
    'Units Sold',
    fontsize=14,
    fontstyle='italic'
)

ax.set_xlabel(
    'Product Category',
    fontsize=14
)

ax.tick_params(axis='x', labelsize=12)
ax.tick_params(axis='y', labelsize=12)

ax.text(
    x=1,
    y=530,
    s='Top Performer!',
    fontsize=12,
    fontweight='bold',
    color='green',
    fontfamily='sans-serif',
    ha='center'
)

plt.show()

