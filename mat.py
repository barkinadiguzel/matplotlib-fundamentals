import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import random

# ---------------------------
# 1. Line Plot & Bar Plot
# ---------------------------
years = [2016 + x for x in range(16)]
weights = [80,76,69,90,87,78,98,57,
           80,76,69,90,87,78,98,57]

# Line plot
plt.plot(years, weights, c="r", lw=4, linestyle="dashed")
plt.title("Line Plot Example")
plt.xlabel("Years")
plt.ylabel("Weight")
plt.show()

# Bar plot
plt.bar(years, weights, align="center", edgecolor="g")
plt.title("Bar Plot Example")
plt.show()

# Scatter plot
xdata = np.random.random(50) * 100
ydata = np.random.random(50) * 100
plt.scatter(xdata, ydata, c="red", marker="*", alpha=0.6, s=150)
plt.title("Scatter Plot Example")
plt.show()

# ---------------------------
# 2. 2D Histogram
# ---------------------------
ages = np.random.normal(20, 1.5, 1000)
scores = np.random.normal(50, 10, 1000)

plt.hist2d(ages, scores, bins=30, cmap="Reds")
plt.xlabel("Age")
plt.ylabel("Score")
plt.colorbar(label="Frequency")
plt.title("2D Histogram")
plt.show()

# ---------------------------
# 3. Pie Chart
# ---------------------------
langs = ["Python", "C++", "Assembly", "Java", "C#"]
votes = [100, 60, 40, 2, 8]
explodes = [0, 0, 0, 0.2, 0]

plt.pie(votes, labels=langs, explode=explodes,
        autopct="%.2f%%", startangle=90)
plt.title("Pie Chart Example")
plt.show()

# ---------------------------
# 4. Box Plot
# ---------------------------
heights = np.random.normal(172, 8, 200)
heights = np.clip(heights, 164, 180)  # Limit between 164 and 180

plt.boxplot(heights)
plt.title("Box Plot Example")
plt.show()

# ---------------------------
# 5. Styled Line Plot
# ---------------------------
style.use("ggplot")
years = [2014 + x for x in range(8)]
income = [55, 56, 62, 61, 56, 69, 64, 65]

income_ticks = list(range(50, 81, 2))
plt.plot(years, income, label="Company1")
plt.yticks(income_ticks, [f"{x}$USD" for x in income_ticks])
plt.title("Income of Office")
plt.xlabel("Years")
plt.ylabel("Income")
plt.legend(loc="lower right")
plt.show()

# ---------------------------
# 6. Subplots (2x2 Grid)
# ---------------------------
x = np.arange(1, 100)

fig, axs = plt.subplots(2, 2, figsize=(10, 6))
axs[0, 0].plot(x, np.sin(x)); axs[0, 0].set_title("Sine Wave")
axs[0, 1].plot(x, np.cos(x)); axs[0, 1].set_title("Cosine Wave")
axs[1, 0].plot(x, np.random.random(99)); axs[1, 0].set_title("Random Function")
axs[1, 1].plot(x, np.log(x)); axs[1, 1].set_title("Log Function")

fig.suptitle("Four Plots")
plt.tight_layout()
plt.savefig("fourplots.png", dpi=300, transparent=False, bbox_inches="tight")
plt.show()

# ---------------------------
# 7. 3D Surface Plot
# ---------------------------
ax = plt.axes(projection="3d")

x = np.arange(-5, 5, 0.5)
y = np.arange(-5, 5, 0.5)
X, Y = np.meshgrid(x, y)
Z = np.sin(X) * np.cos(Y)

ax.plot_surface(X, Y, Z, cmap="inferno")
ax.set_title("3D Surface Plot")
plt.show()

# ---------------------------
# 8. Live Updating Bar Chart
# ---------------------------
heads_tails = [0, 0]

for _ in range(50):
    heads_tails[random.randint(0, 1)] += 1
    plt.bar(["Heads", "Tails"], heads_tails, color=["red", "blue"])
    plt.pause(0.001)

if heads_tails[0] > heads_tails[1]:
    print("Heads won!!")
elif heads_tails[0] == heads_tails[1]:
    print("Achievement unlocked: 50-50 is real!")
else:
    print("Tails won!!")

plt.show()
