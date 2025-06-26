import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import statistics as st

# get the number of times a race has been hosted at each circuit
def circuit_count(df):
    circuit_year_counts = df.groupby('circuit_name')['year'].nunique().reset_index()
    circuit_year_counts = circuit_year_counts.sort_values(by='year', ascending=False)
    return circuit_year_counts

def select_data(df, circuit_year_counts):
    top_circuits = circuit_year_counts.head(10)['circuit_name'].tolist()
    df_top = df[df['circuit_name'].isin(top_circuits)]
    return df_top

def analyze_pit_stop_trend(df):
    # group by circuit name and year and get the mean
    trend = df.groupby(['circuit_name', 'year']) ['pit_stop_milliseconds'].mean().reset_index()

    # create plot
    plt.figure(figsize=(20,12))
    g = sns.FacetGrid(trend, col='circuit_name', col_wrap=3, height=2, sharex=False,sharey=True)
    g.map_dataframe(sns.lineplot, x='year', y='pit_stop_milliseconds', marker="o")
    g.set_axis_labels("Year", "Avg Pit Stop (ms)")

    g.set_titles(col_template="{col_name}")
    g.fig.suptitle("Average Pit Stop Time Lost By Circuit Over Time", fontsize=16)
    g.tight_layout()
    g.fig.subplots_adjust(top=0.92)

    g.savefig('/Users/oblj-nkvarantan/PycharmProjects/F1 DATA/pit_stop_trend_by_circuit.png', dpi=300)
    print("Trend plot saved.")
    plt.show()


def main():
    df = pd.read_csv('/Users/oblj-nkvarantan/PycharmProjects/F1 DATA/pit_stop_data_clean_circuits.csv')

    # Get the most raced circuits
    circuit_year_counts = circuit_count(df)

    # Filter data to include only top 10 circuits by number of races
    df_top = select_data(df, circuit_year_counts)

    # Plot the trend
    analyze_pit_stop_trend(df_top)



if __name__ == "__main__":
        main()
