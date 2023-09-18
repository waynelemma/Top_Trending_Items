<h2> Weekly Trends - Top 10 Movers </h2>

<h3>Overview</h3>

This Python project consists of a series of scripts designed to automate and streamline the process of identifying the top 10 product movers for a given week. These movers are identified based on specific criteria, 
and the project involves data import, cleaning, calculation, and reporting.

After importing and cleaning the required data, the script generates an Excel spreadsheet detailing key metrics such as a weekly (%) change in cases sold, customer count, and average order size. These stats are then averaged together to find the 'mover_rate' (expressed as %), providing a more comprehensive overview of each item's sales performance:

| PROD# | PRODUCT DESCRIPTION          | last_wk_total | this_wk_total | rate_of_change | cust_count_last_wk | cust_count_this_wk | cust_count_rate_of_change | avg_cs_per_cust_last_wk | avg_cs_per_cust_this_wk | avg_cust_rate_of_change | mover_rate |
|-------|------------------------------|---------------|----------------|----------------|--------------------|---------------------|---------------------------|-------------------------|--------------------------|------------------------|------------|
| 9118  | TOFU XTRA FIRM CS 12/12OZ    | 20            | 86             | 3.3            | 13                 | 39                  | 2                         | 1.54                    | 2.21                     | 0.43                   | 1.91       |
| 2994  | APPLE RED SLICED SK/ON CS 4/5# | 32            | 108            | 2.38           | 12                 | 26                  | 1.17                      | 2.67                    | 4.15                     | 0.56                   | 1.37       |
| 2110  | CARROT WHOLE PEELED KK CS 2/10# | 13            | 36             | 1.77           | 9                  | 21                  | 1.33                      | 1.44                    | 1.71                     | 0.19                   | 1.1        |
| 19460 | PEAS SUGAR SNAP LB 1#         | 9             | 22             | 1.44           | 6                  | 11                  | 0.83                      | 1.5                     | 2                        | 0.33                   | 0.87       |
| 891   | ONION WHITE JULIEN 1/4" KK CS 2/5# | 42            | 103            | 1.45           | 18                 | 25                  | 0.39                      | 2.33                    | 4.12                     | 0.77                   | 0.87       |
| 2142  | ONION YLW 1/4" RING KK CS 2/5# | 38            | 91             | 1.39           | 13                 | 18                  | 0.38                      | 2.92                    | 5.06                     | 0.73                   | 0.84       |
| 2396  | BLEND FAJITA 1/4" KK CS 2/5#   | 139           | 310            | 1.23           | 19                 | 23                  | 0.21                      | 7.32                    | 13.48                    | 0.84                   | 0.76       |
| 63326 | PEAR PK 6PK                    | 17            | 35             | 1.06           | 11                 | 19                  | 0.73                      | 1.55                    | 1.84                     | 0.19                   | 0.66       |
| 1016  | ASPARAGUS JUMBO CS 11#         | 69            | 140            | 1.03           | 51                 | 59                  | 0.16                      | 1.35                    | 2.37                     | 0.75                   | 0.65       |
| 8750  | APPLE GALA LOCAL 125-138CT CS 40# | 39            | 79             | 1.03           | 16                 | 28                  | 0.75                      | 2.44                    | 2.82                     | 0.16                   | 0.64       |
| 1411  | POT C WHITE CS 50#             | 9             | 18             | 1              | 7                  | 8                   | 0.14                      | 1.29                    | 2.25                     | 0.75                   | 0.63       |

<h3>How It Works</h3>

The project performs the following tasks:

- Inventory Snapshot Import and Cleaning: This script imports an inventory snapshot, removes the last row (presumably a total row), and cleans the data.

- 2-Week Movement Import and Cleaning: This script imports 2-week movement data, cleans it, and pivots it to prepare for analysis.

- Merge Inventory Movement: This script merges inventory and movement data and creates a cleaned dataset for further analysis.

- Shorts Calculator Today: This script calculates the top 10 movers based on specified criteria, including rate of change in orders and customer counts.

<h3>Benefits</h3>

This project offers the following benefits:

- <strong>Automation</strong>: Automates the process of identifying the top 10 product movers, saving time and reducing manual effort.

- <strong>Data Integrity</strong>: Ensures data integrity by cleaning and processing the data.

- <strong>Insightful Reporting</strong>: Allows Purchasing, Marketing, Sales, and Customer Service to more accurately gauge product movement. This data is helpful to evaluate if current marketing strategies are effective in promoting specific products, or if
adjustments need to be made.

<h3>Prerequisites</h3>

Before using this project, ensure that you have the following prerequisites installed:

- Python (3.x recommended)
- Pandas library
- NumPy library

<h3>Installation</h3>

Clone this repository to your local machine

Install the required libraries:

> pip install pandas numpy

<strong>Note</strong>: Ensure you are placing your data files in the appropriate directories and updating the file paths in the scripts to point to your data.

Execute each script sequentially as described in the comments within each script:

> Run inventory_snapshot_import_and_clean.py
> Run 2_wk_movement_import_and_clean.py
> Run merge_inventory_movement.py
> Run shorts_calculator_today.py

<strong>The final report will be generated as 'top_10_movers_this_week.csv.'</strong>



