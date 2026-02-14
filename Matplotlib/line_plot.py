import matplotlib.pyplot as plt

# Today we will learn matplotlib. It is used to visualize data.

years = [1990, 1992, 1994, 1996, 1998, 2000, 2003, 2005, 2007, 2010]
runs = [500, 700, 1100, 1500, 1800, 1200, 1700, 1300, 900, 1500]

# plotting our first plot:
# syntax:
# plt.plot(x-axis data, y-axis data)

# line plot:
plt.plot(years, runs)

# adding labels for x,y axis
plt.title("Sachin Tendulkar's Yearly Runs")
plt.xlabel("Years")
plt.ylabel("Runs")

# legend:
plt.legend(['Sachin'])
plt.show()


# Multiple line plots:
kohli = [0, 0, 500, 800, 1100, 1300, 1500, 1800, 1900, 2100]
sehwag = [0, 300, 800, 1200, 1500, 1700, 1600, 1400, 1000, 0]

plt.plot(years, kohli, label = 'Kohli')
plt.plot(years, sehwag, label = 'Sehwag')
plt.legend()
plt.show()

# Here, it is better to use label instead of legend. Legends can be a bit confusing.


# You can also customise your plot using format strings: '[colour][marker_style][line_style]'
# red colour dotted line with circle marker:
plt.plot(years, kohli, 'ro:', label = 'Kohli')

# green colour triangle marker with dashed line
plt.plot(years, sehwag, 'g^--', label = 'Sehwag')
plt.legend()
plt.show()

# You can also do it like this:
plt.plot(years, kohli, color = 'red', marker = 'o', linestyle = ':',label = 'Kohli')
plt.plot(years, sehwag, color = 'green', marker = '^', linestyle = '--', label = 'Sehwag')
plt.legend()
plt.show()

# You can increase linewidth too.
plt.plot(years, kohli, linewidth=3, label='Kohli')
plt.plot(years, sehwag, label='Sehwag')
plt.grid() # shows a grid in the background.
plt.legend()
plt.show()


# plt.tight_layout(): used when using sub plots to prevent overlapping of titles and labels.


# Changing style of plots: We can change theme and style of matplotlib using plt.style.use():
print(plt.style.available)

plt.style.use('fast')
plt.plot(years, kohli, color='red', linewidth=3, label='Kohli')
plt.plot(years, sehwag, color='green', label='Sehwag')
plt.grid()
plt.legend()
plt.show()


# xkcd style: It is cartoonish
with plt.xkcd():
    plt.plot(years, kohli, color='red', linewidth=3, label='Kohli')
    plt.plot(years, sehwag, color='green', label='Sehwag')
    plt.grid()
    plt.legend()
    plt.show()


# Note: Avoid plotting too many plots at a time. It will look like a ambiguous modern art.
