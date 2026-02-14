import matplotlib.pyplot as plt

# Today we will learn about subplots. It is a method to show multiple plots in a single window:
# using plt.subplot():
years = [1990, 1992, 1994, 1996, 1998, 2000, 2003, 2005, 2007, 2010]
sachin = [500, 700, 1100, 1500, 1800, 1200, 1700, 1300, 900, 1500]

plt.subplot(1, 2, 1)
plt.title("Runs and years")
plt.bar(years, sachin)
plt.xlabel("Years")
plt.ylabel("Runs")
plt.show()

plt.subplot(1, 2, 2)
plt.title("Runs and years")
plt.plot(years, sachin)
plt.xlabel("Years")
plt.ylabel("Runs")
plt.tight_layout()
plt.show()


# using for loop:
kohli = [0, 0, 500, 800, 1100, 1300, 1500, 1800, 1900, 2100]
sehwag = [0, 300, 800, 1200, 1500, 1700, 1600, 1400, 1000, 0]
titles = ["Sachin's runs", "Kohli's runs", "Sehwag's runs", "Sachin's runs"]
y_data = [sachin, kohli, sehwag, sachin]

fig, axs = plt.subplots(2, 2, figsize=(10, 5))
fig.suptitle("Cricket plot") # Heading at the top
for i in range(2):
    for j in range(2):
        idx = i * 2 + j
        axs[i][j].set_title(titles[idx])
        axs[i][j].plot(years, y_data[idx])
plt.tight_layout()
plt.show()
