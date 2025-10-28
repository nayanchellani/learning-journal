import matplotlib.pyplot as plt

sales = [20, 30, 56, 65, 45, 56, 70, 71, 32, 57, 56, 97, 21, 25, 78, 95, 39, 74, 57, 85, 49, 89]
plt.hist(sales, bins=8, color="red", edgecolor="black")
plt.show()