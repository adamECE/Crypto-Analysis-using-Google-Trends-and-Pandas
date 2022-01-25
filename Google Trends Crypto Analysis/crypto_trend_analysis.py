'''
File Name: crypto_trend_analysis.py
Author: Adam Hoffmeister 
//add more info later 

In this current version, the excel file must be 
manually created. An example excel file is provided 
[give a link or something]


'''
# MIGHT NEED TO CHANGE NAME TO MAIN CUZ BRUH 
import pandas as pd
import crypto_initialization as c_init
import trend_analysis_functions as f  
            

def main():
    # excel_file_name = input("Enter the file name of your Excel file: ")
    '''
    This example uses the USDT_SOL_oct.csv flie as an example
    importing the desired file and uncommenting the line listed above 
    will allow the program to analyze different files. 
    '''
    
    excel_file_name = "USDT_SOL_oct.csv"
    df = pd.read_csv(excel_file_name)

    #initalizing data 
    df_crypto = df.tail(52) # check if every spreadsheet has significant rows 
    dates = df_crypto['Category: All categories']
    vals_1 = df_crypto['Unnamed: 1']
    vals_2 = df_crypto['Unnamed: 2']

    # crypto_1 = create_crypto(dates, vals_1)
    # crypto_2 = create_crypto(dates, vals_2)

    # create_date_array(dates)

   
if __name__ =="__main__":
    main() 