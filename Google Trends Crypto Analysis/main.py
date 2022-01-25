'''
File Name: main.py
Author: Adam Hoffmeister 
//add more info later 

In this current version, the excel file must be 
manually created. An example excel file is provided 
[give a link or something]


'''
import pandas as pd
import crypto_initialization as c_init
import trend_analysis_functions as f  
import numpy as np 
            

def main():
    # excel_file_name = input("Enter the file name of your Excel file: ")
    '''
    This example uses the USDT_SOL_oct.csv flie as an example
    importing the desired file and uncommenting the line listed above 
    will allow the program to analyze different files. 
    '''
    
    # using random volume values as an example. 
    # ideally need to estimate daily searches by idk monthly/30. CHECK THIS QUICKLY 
    crypto_1_volume = 12300/30.5
    crypto_2_volume = 16100/30.5 

    excel_file_name = "USDT_SOL_oct.csv"
    df = pd.read_csv(excel_file_name)

    excel_file_name2 = "Solana Historical Data Oct 2020-21 - Investing.com.csv"
    dfp = pd.read_csv(excel_file_name2)


    # initalizing data 
    df_crypto = df.tail(52) # check if every spreadsheet has significant rows 
    df_dates = df_crypto['Category: All categories']
    df_vals_1 = df_crypto['Unnamed: 1']
    df_vals_2 = df_crypto['Unnamed: 2']
    
    dates = c_init.convert_to_array(df_dates)
    vals_1 = c_init.convert_to_array(df_vals_1)
    vals_2 = c_init.convert_to_array(df_vals_2)
    
    crypto_1 = c_init.create_crypto(dates, vals_1, crypto_1_volume)
    crypto_2 = c_init.create_crypto(dates, vals_2, crypto_2_volume)

    # initializing price tree 
    dfp_dates_2 = dfp['Date']
    dfp_price_2 = dfp['Price']

    price_2 = c_init.convert_to_array(dfp_price_2)
    p_dates = c_init.convert_to_array(dfp_dates_2)

    crypto_price_2 = c_init.create_crypto_price(p_dates, price_2)

    # calculating data 
    vol1, vol2 = f.compare_last_2month_vol(crypto_1,crypto_2,2021,10)
    growth_rate_1, growth_rate_2 = f.compare_last_2month_growth(crypto_1,crypto_2,2021,10)

    c1_growth_rate, p1_growth_rate = f.compare_last_2month_price_gr(crypto_2,crypto_price_2,2021,10)

    # x = f.determine_correlation_coef(crypto_2, crypto_price_2,2021, 10)

    # reporting calculated data in text file 
    name1 = "Tether"
    name1 = "Solana"

    print(vol1, vol2, growth_rate_1, growth_rate_2, c1_growth_rate, p1_growth_rate)
    
    # pf = open('report_overview.txt','w')
    # pr.close() 
    




if __name__ =="__main__":
    main() 