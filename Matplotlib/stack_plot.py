import matplotlib.pyplot as plt

# Today, we will learn about stack plots in matplotlib. It's used to compare different pie charts of a same "whole value" over a period of time. It is used to show how the different elements of the "whole value" change over a period of time.

# student's time spent on different activities in a week:
days = [1, 2, 3, 4, 5, 6, 7] 
studying = [3, 4, 3, 5, 4, 3, 4]
playing = [2, 2, 1, 1, 2, 3, 2]
watching_tv = [2, 1, 2, 2, 1, 1, 1]
sleeping = [5, 5, 6, 5, 6, 5, 5]

plt.figure(figsize=(10, 5)) # set window size
plt.title('Time spent on different activities for a week')
plt.stackplot(days, studying, playing, watching_tv, sleeping, labels=["Studying", "Playing", "Watching TV", "Sleeping"], colors=['r', 'g', 'b', 'y'])
plt.legend(loc = "upper left") # set postion of legend
plt.xlabel('Activities')
plt.ylabel('Hours')
plt.show()