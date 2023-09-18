########################################################################################################################

#  Step 1 - inventory_snapshot_import_and_clean.py
#  Path - "C:/Users/cfontaine/Desktop/colins_buyer_folder/cognos_project/forecasting_project/daily_order_calculator_final/inventory_snapshot_import_and_clean.py"

########################################################################################################################

# importing libraries
import pandas as pd

# open and create a dataframe from the PPRO reports
file1 = "C:/Users/wlemma/PycharmProjects/pythonProject/Top_10_Movers/inventory_snapshot_today.csv"

# Read file 1
df = pd.read_csv(file1)

# removes last row of the data (grand total row)
df.drop(df.tail(1).index, inplace=True)
# change datatype of PROD# column to int so it will match during merge
df = df.astype({'PROD#': int})

# Cleaning up the data from PPRO to not have duplicate rows, we use false as index so we keep product description as
df_new = df.groupby(df['PROD#'], as_index=False).aggregate(
    {'ON HAND (ACTL)': 'sum', 'PRODUCT DESCRIPTION': 'first', 'BUY': 'first'})

# recreating dataframe in order to save to file
df_new = df_new[['BUY',
                 'PROD#',
                 'PRODUCT DESCRIPTION',
                 'ON HAND (ACTL)']]

# save to new file
s = df_new.to_csv('C:/Users/wlemma/PycharmProjects/pythonProject/Top_10_Movers/PPRO_report_inventory_cleaned.csv')
########################################################################################################################

#  Step 2 - 2_wk_movement_import_and_clean.py
#  Path - "C:/Users/cfontaine/Desktop/colins_buyer_folder/cognos_project/forecasting_project/daily_order_calculator_final/2_wk_movement_import_and_clean.py"

########################################################################################################################

# importing libraries
import pandas as pd

# open and create a dataframe from the PPRO report.
file1 = "C:/Users/wlemma/PycharmProjects/pythonProject/Top_10_Movers/last_2wk_movement_today_customers.csv"

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
     'PRODUCT DESCRIPTION': 'first',
     'CUSTOMER': 'count'})

# pivot the data for the order pivot table
df2 = pd.pivot_table(df, values='QUAN', index=['PROD#'], columns='SHIP DATE').reset_index()
# fill empty, na or NaN values with 0 to reflect 0 orders
df2 = df2.fillna(0)
# Save the dataframe to a new file that is cleaned.
s = df2.to_csv('C:/Users/wlemma/PycharmProjects/pythonProject/Top_10_Movers/PPRO_2wk_movement_cleaned.csv')

# pivot the data
df3 = pd.pivot_table(df, values='CUSTOMER', index=['PROD#'], columns='SHIP DATE').reset_index()
# fill empty, na or NaN values with 0 to refelct 0 orders
df3 = df3.fillna(0)
# Save the dataframe to a new file that is cleaned.
s = df3.to_csv('C:/Users/wlemma/PycharmProjects/pythonProject/Top_10_Movers/PPRO_2wk_movement_cleaned_customers.csv')


########################################################################################################################

#  Step 3 - merge_inventory_movement.py
#  Path - "C:/Users/cfontaine/Desktop/colins_buyer_folder/cognos_project/forecasting_project/daily_order_calculator_final/merge_inventory_movement.py"

########################################################################################################################

# importing libraries
import pandas as pd

file1 = "C:/Users/wlemma/PycharmProjects/pythonProject/Top_10_Movers/PPRO_report_inventory_cleaned.csv"
file2 = "C:/Users/wlemma/PycharmProjects/pythonProject/Top_10_Movers/PPRO_2wk_movement_cleaned.csv"

# Pass the files into a dataframe variables.
df_1 = pd.read_csv(file1)
df_2 = pd.read_csv(file2)

#Merge the two files and get rid of the extra columns
merged_df = df_1.merge(df_2, on='PROD#', how='left')
#
# Fill empty values with '0' as we do not want missing data but a 0 order
merged_df = merged_df.fillna(0)
# Create a new dataframe with 'unnamed' columns dropped
new_df = merged_df.drop(merged_df.columns[merged_df.columns.str.contains('unnamed', case=False)], axis=1, inplace=True)
# Generate new dataframe in order to pass into a save file
new_df = merged_df

# Save file
s = new_df.to_csv('C:/Users/wlemma/PycharmProjects/pythonProject/Top_10_Movers/merged_inventory_movement.csv')


########################################################################################################################

#  Step 4 - shorts_calculator_today.py
#  Path - "C:/Users/cfontaine/Desktop/colins_buyer_folder/cognos_project/forecasting_project/daily_order_calculator_final/shorts_calculator_today.py"

########################################################################################################################

# importing libraries
import pandas as pd
import numpy as np

file1 = "C:/Users/wlemma/PycharmProjects/pythonProject/Top_10_Movers/merged_inventory_movement.csv"
file2 = "C:/Users/wlemma/PycharmProjects/pythonProject/Top_10_Movers/prop_master_list.csv"
file3 = "C:/Users/wlemma/PycharmProjects/pythonProject/Top_10_Movers/PPRO_2wk_movement_cleaned_customers.csv"

# create dataframe from the file
df = pd.read_csv(file1)
df2 = pd.read_csv(file2)
df3 = pd.read_csv(file3)

# Calculates the sum of last week cases ordered
df['last_wk_total'] = df[df.columns[5]] + df[df.columns[6]] + df[df.columns[7]] + df[df.columns[8]] + df[df.columns[9]] + df[df.columns[10]] + df[df.columns[11]]
# Calculates the sum of this week cases ordered
df['this_wk_total'] = df[df.columns[12]] + df[df.columns[13]] + df[df.columns[14]] + df[df.columns[15]] + df[df.columns[16]] + df[df.columns[17]] + df[df.columns[18]]
# Calculating the growth rate between the two columns
df['rate_of_change'] = ((df['this_wk_total'] - df['last_wk_total']) / df['last_wk_total'])


# Calculates the sum of last week customers who ordered
df3['cust_count_last_wk'] = df3[df3.columns[2]] + df3[df3.columns[3]] + df3[df3.columns[4]] + df3[df3.columns[5]] + df3[df3.columns[6]] + df3[df3.columns[7]] + df3[df3.columns[8]]
# Calculates the sum of this week customers who ordered
df3['cust_count_this_wk'] = df3[df3.columns[9]] + df3[df3.columns[10]] + df3[df3.columns[11]] + df3[df3.columns[12]] + df3[df3.columns[13]] + df3[df3.columns[14]] + df3[df3.columns[15]]
df3_new = df3[['PROD#',
               'cust_count_last_wk',
               'cust_count_this_wk'
             ]]
# Calculates the rate of change of customers between the last two weeks
df3['cust_count_rate_of_change'] = ((df3['cust_count_this_wk'] - df3['cust_count_last_wk']) / df3['cust_count_last_wk'])

#Merge the two files and get rid of the extra columns
merged_df = df3.merge(df, on='PROD#', how='left')

df = merged_df
df['avg_cs_per_cust_last_wk'] = df['last_wk_total'] / df['cust_count_last_wk']
df['avg_cs_per_cust_this_wk'] = df['this_wk_total'] / df['cust_count_this_wk']
df['avg_cust_rate_of_change'] = ((df['avg_cs_per_cust_this_wk'] - df['avg_cs_per_cust_last_wk']) / df['avg_cs_per_cust_last_wk'])
df['mover_rate'] = ((df['rate_of_change'] + df['cust_count_rate_of_change'] + df['avg_cust_rate_of_change']) / 3)


# list of item codes that are not useful to keep in this report
drop_codes = df2['PROD#']

# dropping codes from final report.
df = df[~df['PROD#'].isin(drop_codes)]

df = df.round(decimals=2)
df = df.sort_values(['mover_rate'], ascending=[False])


# filter values from different columns
df = df[(df.rate_of_change > 0) &
        (df.cust_count_rate_of_change > 0) &
        (df.cust_count_last_wk > 5) &
        (df.cust_count_this_wk > 5) &
        (df.last_wk_total > 5) &
        (df.this_wk_total > 5) &
        (df.avg_cs_per_cust_last_wk > 1.25) &
        (df.avg_cust_rate_of_change > 0.1)
        ]


# remove other columns and show this dataframe on save
df_new = df[['BUY',
             'PROD#',
             'PRODUCT DESCRIPTION',
             'last_wk_total',
             'this_wk_total',
             'rate_of_change',
             'cust_count_last_wk',
             'cust_count_this_wk',
             'cust_count_rate_of_change',
             'avg_cs_per_cust_last_wk',
             'avg_cs_per_cust_this_wk',
             'avg_cust_rate_of_change',
             'mover_rate'
             ]]

# save to new file
s = df_new.to_csv('C:/Users/wlemma/PycharmProjects/pythonProject/Top_10_Movers/top_10_movers_this_week.csv')