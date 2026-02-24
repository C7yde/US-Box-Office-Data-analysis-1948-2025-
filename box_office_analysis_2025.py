"""
Box Office Industry Analysis (1995 -2025)
Correlation and trend analysis

Author : DesmondGraham Utalor
"""

import pandas as pd

"""Loading the data"""
#domestic_box_office_51_df = pd.read_csv("Domestic_box_office 51.csv",encoding="ANSI",index_col="Year")
#pd.set_option("display.max_columns",6)
#print(domestic_box_office_51_df.sort_values("Year",ascending=True))
annual_ticket_prices_df = pd.read_csv("US_Ticket_Prices.csv")
#print(annual_ticket_prices_df)

"""updating the year column to int"""
annual_ticket_prices_df.Year = annual_ticket_prices_df["Year"].astype(int)
full_year = pd.DataFrame({"Year": range(annual_ticket_prices_df["Year"].min(), 2025 + 1)})
#print(full_year)
annual_ticket_prices_df2017 = pd.merge(full_year,annual_ticket_prices_df,on="Year",how="left")
#print(annual_ticket_prices_df2017)
"""create table annual_ticket_prices"""
#annual_ticket_prices_df2017.to_csv("annual_ticket_prices.csv",index= False)
annual_ticket_prices = pd.read_csv("annual_ticket_prices.csv")
pd.set_option("display.max_columns",8)
pd.set_option("display.max_rows",100)
#print(annual_ticket_prices)
"""load ticket sales data"""
tickets_sold_df = pd.read_excel("BF.xlsx")
#pd.set_option("display.max_columns",5)
#print(tickets_sold_df)
"""load studio film release data"""
film_releases_df = pd.read_excel("BF1.xlsx")
#pd.set_option("display.max_columns",8)
#print(film_releases_df)
"""TICKET SALES AND BOX OFFICE"""
tickets_sold_df["Year"] = tickets_sold_df["Year"].astype(int)
annual_ticket_prices_df2017.rename(columns={"Average Ticket Price (USD)":"Average Ticket Price"},inplace=True)
#print(annual_ticket_prices_df2017.columns)
tickets_sold_df1 = pd.merge(annual_ticket_prices_df2017,tickets_sold_df,on= "Year",how="left",suffixes=("","_from_annual_ticket_prices_df2017"))
#replace nans in tickets sold df with values from annual_ticket_prices_df2017
tickets_sold_df1.columns = tickets_sold_df1.columns.str.strip()
tickets_sold_df1["Average Ticket Price (USD)"] = tickets_sold_df1["Average Ticket Price (USD)"].fillna(tickets_sold_df1["Average Ticket Price"])
pd.set_option("display.max_columns",8)
pd.set_option("display.max_rows",100)
tickets_sold_df1.drop(columns=["Average Ticket Price"],inplace=True)
#print(tickets_sold_df1)
"""FILM STUDIO RELEASES"""
film_releases_df["Year"] = film_releases_df["Year"].astype(int)
film_releases_df1 = pd.merge(full_year,film_releases_df,on= "Year",how="left")
film_releases_df1["Total releases"] = film_releases_df1["Total Major 6"] + film_releases_df1["Total Other Studios"]
#film_releases_df1["Year"] = pd.to_datetime(film_releases_df1["Year"])
pd.set_option("display.max_columns",8)
pd.set_option("display.max_rows",100)
#print(film_releases_df1)
"""CPI INFLATION RATE table load and cleaning"""
cpi_df = pd.read_csv("CPIAUCSL.csv")

cpi_df["observation_date"] = pd.to_datetime(cpi_df["observation_date"])

cpi_df["Year"] = pd.DatetimeIndex(cpi_df["observation_date"]).year
cpi_df["Month"] = pd.DatetimeIndex(cpi_df["observation_date"]).month
cpi_df["day"] = pd.DatetimeIndex(cpi_df["observation_date"]).day
pd.set_option("display.max_columns",8)
pd.set_option("display.max_rows",1000)
yearly_cpi = cpi_df.groupby("Year")["CPIAUCSL"].mean().reset_index()
yearly_cpi.columns = ["Year","CPI"]

"""calculating Inflation_rate"""
yearly_cpi["Inflation_rate %"] = (yearly_cpi["CPI"].pct_change() * 100).round(2)
#print(yearly_cpi)
#print(cpi_df)

"""Merge ticket sales,box office and cpi data as box_office_df"""
box_office_df = pd.merge(tickets_sold_df1, yearly_cpi, on="Year", how="left")
box_office_df["Inflation_rate %"] = box_office_df["Inflation_rate %"].astype(float)
#box_office_df.to_csv("box_office_df.csv")
#print(box_office_df)
data = pd.read_csv("box_office_df.csv")
#print(data)
data.columns = data.columns.str.strip()
film_releases_df1.columns = film_releases_df1.columns.str.strip()


"""CORRELATION AND RELATIONSHIPS"""
#Correlation between average ticket price and sales
avg_price_v_sales = data[["Average Ticket Price (USD)","Tickets Sold"]].corr()
#print(avg_price_v_sales)

#Correlation between box office gross and consumer price index
box_office_v_cpi = data[["Total Box Office","CPI"]].corr()
#print(box_office_v_cpi)

#Total box office per year
box_office = data.groupby("Year")["Total Box Office"].sum()
#print(box_office)

#Total film releases per year
releases = film_releases_df1.groupby("Year").sum().sum(axis=1)
#print(releases)

#Correlation between total box office and film releases per year
combined_df = pd.DataFrame({"Total revenue":box_office,"Total releases":releases}).dropna()
#print(combined_df.corr())

#Correlation between % ticket price change and % CPI change per year
data["Ticket Price % change"] = data["Average Ticket Price (USD)"].pct_change() * 100
data["CPI % change"] = data["CPI"].pct_change() * 100
#print(data[["Ticket Price % change","CPI % change"]].corr())


