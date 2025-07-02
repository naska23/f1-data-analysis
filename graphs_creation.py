import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator


def create_race_count_graph(df):
    # extract columns
    years = df['year']
    num_races = df['num_races']

    # create line chart
    plt.figure(figsize=(18, 7), facecolor='black')
    ax = plt.gca()
    ax.set_facecolor('black')  # plot bg
    plt.plot(years, num_races, marker='o', linestyle='-', color='#FF0000')

    # add labels and title
    plt.xlabel('Year', fontsize=14, fontweight='bold', color='white')
    plt.ylabel('Number of Races', fontsize=14, fontweight='bold', color='white')
    plt.title('Evolution Of F1 Race Counts Per Season', fontsize=20, fontweight='bold', color='white')
    plt.grid(False)

    # Set tick params to white
    ax.tick_params(colors='white', which='both')  # tick labels and ticks

    # force y-axis to use full integers
    plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))

    # Manually set y ticks for better control
    ymin, ymax = 6, max(num_races.max(), 25)
    plt.yticks(range(ymin, ymax + 1, 2))  # ticks every 2 units: 6, 8, 10...

    # set x-axis ticks and labels
    start, end = 1950, 2024
    ticks = list(range(start, end + 1, 2))
    if ticks[-1] != end:
        ticks.append(end)

    plt.xticks(ticks=ticks, rotation=45, color='white')

    # make x and y axis lines white
    ax.spines['bottom'].set_color('white')
    ax.spines['left'].set_color('white')

    # show plot
    plt.tight_layout()
    plt.savefig('/Users/oblj-nkvarantan/PycharmProjects/F1 DATA/race_counts_year_graph.png', dpi=300)
    print("Trend plot saved.")
    #plt.savefig('images/race_counts_year_graph.png')
    #print("Saved to images folder")
    plt.show()


def main():
    # load the race_counts_by_year.csv file
    df = pd.read_csv('/Users/oblj-nkvarantan/PycharmProjects/F1 DATA/race_counts_by_year.csv')

    # create plot
    create_race_count_graph(df)


if __name__ == "__main__":
        main()