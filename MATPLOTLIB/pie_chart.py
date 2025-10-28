import matplotlib.pyplot as plt

product = ["A", "B", "C", "D"]
sales = [700, 800, 300, 1000]
plt.pie(sales, labels=product, colors=["gold", "coral", "skyblue", "green"], autopct='%1.1f%%')
plt.show()