import matplotlib.pyplot as plt

product = ["A", "B", "C", "D"]
sales = [700, 800, 300, 1300]
plt.barh(product, sales, color="orange", height=0.5, label="Weekly analysis")
plt.xlabel("Products")
plt.ylabel("Sales")
plt.title("Sales comparison")
plt.legend()
plt.show()