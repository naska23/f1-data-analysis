import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import statistics

from fontTools.ttLib.tables.otTraverse import bfs_base_table

def pit_stop_outliers(df):

    Q1 = df['pit_stop_milliseconds'].quantile(0.25)
    Q3 = df['pit_stop_milliseconds'].quantile(0.75)

    IQR = Q3 - Q1

    outliers = df[
        (df['pit_stop_milliseconds'] < Q1 - 1.5 * IQR) |
        (df['pit_stop_milliseconds'] > Q3 + 1.5 * IQR)
    ]
    df_remove_outs = df[
        (df['pit_stop_milliseconds'] > Q1 - 1.5 * IQR) &
        (df['pit_stop_milliseconds'] < Q3 + 1.5 * IQR)
    ]
    print(df_remove_outs)

    df_remove_outs.to_csv('/Users/oblj-nkvarantan/PycharmProjects/F1 DATA/pit_stop_data_clean.csv', index=False)

    # scatterplot
    plt.figure(figsize=(12, 6))
    sns.scatterplot(data=df, x='race_id', y='pit_stop_milliseconds', label='All')
    sns.scatterplot(data=outliers, x='race_id', y='pit_stop_milliseconds', color='red', label='Outliers')
    plt.title("Pit Stop Outliers by Race")
    plt.legend()
    plt.savefig('/Users/oblj-nkvarantan/PycharmProjects/F1 DATA/pit_stop_scatter.png', dpi=300, bbox_inches='tight')
    print("Plot Saved Successfully")
    plt.show()
    print(f"Outlier Detection Finished. Encountered & Eliminated {len(outliers)} outliers.")  # Using fstring (f pred prvo navednico) povemo pythonu, da ko naleti na { } med oklepaji pričakuje vrednost spremenljivke in jo sprintne
    return df_remove_outs

#median = get_median(df['stolpec'])
#median = get_median(df,'stolpec')


#df = pd.read_csv('/Users/oblj-nkvarantan/PycharmProjects/F1 DATA/pit_stops_driver_race.csv') #reading data from file
def get_median(column):
    return statistics.median(column)

# check for missing values
def null_values_check(df):
    print("Checking for null values:")
    print(df.isnull().sum())

# check for duplicates
def check_duplicates(df):
    duplicates = df.duplicated()
    print(f"Duplicates rows: {duplicates.sum()}")

# create new scatter plot with cleaned data
def scatterplot_cleaned_pit_stops(df):
    plt.figure(figsize=(12, 6))
    sns.scatterplot(data=df, x='race_id', y='pit_stop_milliseconds', color='green', label='Cleaned Data')
    plt.title("Pit Stop Times")
    plt.xlabel("Race ID")
    plt.ylabel("Pit Stop Duration (ms)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('/Users/oblj-nkvarantan/PycharmProjects/F1 DATA/pit_stop_scatter_clean.png', dpi=300, bbox_inches='tight')
    print("Plot Saved Successfully")
    plt.show()


def main():
    df = pd.read_csv('/Users/oblj-nkvarantan/PycharmProjects/F1 DATA/pit_stops_driver_race.csv')
    df_remove_outs = pit_stop_outliers(df)
    #null_values_check(df_remove_outs)
    #remove_duplicates(df_remove_outs)
    #print(df_remove_outs.dtypes)
    scatterplot_cleaned_pit_stops(df_remove_outs)


if __name__ == "__main__":
    main()