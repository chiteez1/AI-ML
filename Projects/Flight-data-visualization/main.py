import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# load datset:
data = sns.load_dataset('flights')

while True:
    # Print options:
    print("1. No. of passengers, month-wise.")
    print("2. No. of passengers, year-wise.")
    print("3. Overall growth of passengers.")
    print("4. Exit.")
    ch = int(input("Enter an option:"))

    # Check for exit option:
    if ch == 4:
        break

    elif ch == 1:
        try:
            # Plot a bar to show no. of month-wise passengers of an year
            year = int(input("Enter year:"))
            df = data.query(f'year == {year}')  # only select the specific year
            plt.figure(figsize=(10, 5)) # adjust the figure size accordingly
            sns.barplot(x='month', y='passengers', data=df)
            plt.title("Month-wise passengers")
            plt.grid()
            plt.show()
        except:
            print("An error occured. Please try again later")

    elif ch == 2:
        try:
            # Plot a bar plot to show year-wise passenger growth.
            groups = data.groupby('year') # create groups according to years.
            s = groups['passengers'].mean() # get average passenger count per year.
            df = pd.DataFrame({"Year": s.index, "Passengers": s.values})
            plt.figure(figsize=(10, 5))
            sns.barplot(x="Year", y="Passengers", data=df)
            plt.title("Year-wise passengers")
            plt.grid()
            plt.show()
        except:
            print("An error occured. Please try again later")

    elif ch == 3:
        try:
            groups = data.groupby('year')
            s = groups['passengers'].mean()
            df = pd.DataFrame({"Year": s.index, "Passengers": s.values})
            plt.figure(figsize=(10, 5))
            sns.lineplot(x="Year", y="Passengers", data=df)
            plt.title("Year-wise growth in passengers")
            plt.grid()
            plt.show()
        except:
            print("An error occured. Please try again later")

    else:
        print("Invalid option! Please try again.")
