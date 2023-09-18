# importing libraries
import pandas as pd

# open and create a dataframe from the PPRO report.
file1 = "C:/Users/cfontaine/Desktop/colins_buyer_folder/cognos_project/forecasting_project/top_10_movers_report/2_wk_movement_today.csv"

# read file into a dataframe
df = pd.read_csv(file1)
# Change name of column so it stays consistent with naming convention of 'PROD#'.
df2 = df.rename({'PROD': 'PROD#'}, axis=1)
# Convert PROD# column to int so it matches during merging
df2['PROD#'] = df2['PROD#'].astype(int)

# rename columns
df2 = df2.rename(columns={'DATE': 'SHIP DATE'})
# use new variable for dataframe
df = df2

# change column to datetime
df['SHIP DATE'] = pd.to_datetime(df['SHIP DATE'])
df['SHIP DATE'] = df['SHIP DATE'].dt.date

# group the data by both the prod and the ship date in order to
# not lose any data across these two critical categories
df = df.groupby(['PROD#', 'SHIP DATE']).aggregate(
    {'QUAN': 'sum',
     'PRODUCT DESCRIPTION': 'first'})

# pivot the data
df = pd.pivot_table(df, values='QUAN', index=['PROD#'], columns='SHIP DATE').reset_index()

# fill empty, na or NaN values with 0 to reflect 0 orders
df = df.fillna(0)

# Save the dataframe to a new file that is cleaned.
s = df.to_csv('C:/Users/cfontaine/Desktop/colins_buyer_folder/cognos_project/forecasting_project/top_10_movers_report/PPRO_2wk_movement_cleaned.csv')
