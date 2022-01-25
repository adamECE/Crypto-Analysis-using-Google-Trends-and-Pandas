'''
File name: calc.py
Author: Adam Hoffmeister  
//add more info later
''' 
# import crypto_initialization as c_init #idk if i need this
import statistics as s 
import numpy as np 

# _____VOLUME FUNCTIONS____
def total_vol_over_period(vals, days): 
    '''
    Computes the total volume over the series of data points.
    Follows (theres some math term I can't remember but CALC I my guy) 
    '''
    if len(vals) != len(days):
        print("ERROR: LEN VALS DAYS ARE NOT THE SAME")

    total = 0 
    for i in range(1,len(vals)):
        low_val = min(vals[i],vals[i-1])    
        high_val = max(vals[i], vals[i-1])
        day_pd = days[i]- days[i-1]
        total += (low_val * day_pd) + ((high_val-low_val)*(day_pd/2))
    return total 

def compare_last_2month_vol(node1,node2,year,month):
    vals1, days1, vals2, days2  = compare_last_2month(node1,node2,year,month)
    total_1 = total_vol_over_period(vals1, days1)
    total_2 = total_vol_over_period(vals2, days2)
    return total_1, total_2 

# _____GROWTH RATE FUNCTIONS_____ 
def compare_growth(vals):
    '''
    Computes the average growth rate between
    each consecutive pair of values 
    in the given data set.  

    growth rate = (final val / inital val ) - 1 

    Arguments: Vals - An array of vals from the CryptoNode 
    class 

    Returns: Average growth rate (float)
    '''
    growth_total = 0 
    for i in range(1,len(vals)):
        growth_total += (vals[i] / vals[i-1]) - 1
    
    return (growth_total / i) * 100 

def compare_last_2month_growth(node1,node2,year,month):
    vals1, days1, vals2, days2  = compare_last_2month(node1,node2,year,month)
    growth_rate_1 = compare_growth(vals1) # removed days was that intentional? 
    growth_rate_2 = compare_growth(vals2)

    return growth_rate_1, growth_rate_2

def compare_last_2month_price_gr(node, pnode, year, month):
    vals, pvals  = compare_2_months(node,pnode,year,month)
    growth_rate = compare_growth(vals)
    price_growth_rate = compare_growth(pvals)

    return growth_rate, price_growth_rate

#___FUNCTIONS TO FIND CORRELATION COEFICIENT____

def determine_correlation_coef(node, nodep, year, month):
    vals, pvals = compare_2_months_day_specific(node, nodep, year, month)
    correlation_coef = np.corrcoef(vals, pvals)
    return correlation_coef

# USING THIS FUNCTION 
def compare_2_months_day_specific(node1, node2, year, month):
    if month == 1:
        m = 12 
        y = year - 1 
    else:
        m = month - 1 
        y = year 
    vals1 = vals_over_year_month(node1, y, m)
    days1 = days_over_year_month(node1, y, m)
    temp = vals_over_year_month(node1, year, month)
    days2 = days_over_year_month(node1, year, month)
    vals1.extend(temp)   

    vals2 = [] 
    for day in days1:
        vals2.extend(val_over_year_month_day(node2, y, m, day))
    for day in days2:
        vals2.extend(val_over_year_month_day(node2, year, month, day)) 

    return vals1, vals2

def val_over_year_month_day(root, year, month, day):
    vals = []
    type = root.get_type()
    if type == 'Root':
        for node in root.get_sub_cats():
            vals.extend(vals_over_year_month(node, year, month))
    else:
        if type == 'Year': 
            if root.get_val() == year:
                for node in root.get_sub_cats():
                    vals.extend(vals_over_year_month(node, year, month))
        elif type == 'Month': 
            if root.get_val() == month:
                for node in root.get_sub_cats():
                    vals.extend(vals_over_year_month(node, year, month))
        elif type == 'Day':
            if root.get_val() == day:
                for node in root.get_sub_cats():
                    vals.extend(vals_over_year_month(node, year, month))
        elif type == 'Val':
            vals.extend([root.get_val()])
    return vals

# ____FUNCTIONS TO FIND SPECIFIC DATAPOINTS____
def compare_last_2month(node1, node2, year, month):
    if month == 1:
        m = 12 
        y = year - 1 
    else:
        m = month - 1 
        y = year 
    vals1 = vals_over_year_month(node1, y, m)
    vals1.extend(vals_over_year_month(node1, year, month)) 
    days1 = days_over_year_month(node1, y, m)
    temp1 = days_over_year_month(node1, year, month)
    temp1 = days_extension_from_month(days1, month)
    days1.extend(temp1)

    vals2 = vals_over_year_month(node2, y, m)
    vals2.extend(vals_over_year_month(node2, year, month)) 
    days2 = days_over_year_month(node2, y, m)
    temp2 = days_over_year_month(node2, year, month)
    temp2 = days_extension_from_month(days2, month)
    days2.extend(temp2)

    return vals1, days1, vals2, days2 
    
def compare_2_months(node1,node2,year,month):
    if month == 1:
        m = 12 
        y = year - 1 
    else:
        m = month - 1 
        y = year 
    vals1 = vals_over_year_month(node1, y, m)
    vals1.extend(vals_over_year_month(node1, year, month)) 

    vals2 = vals_over_year_month(node2, y, m)
    vals2.extend(vals_over_year_month(node2, year, month)) 

    return vals1, vals2

def vals_over_year_month(root, year, month):
    vals = []
    type = root.get_type()
    if type == 'Root':
        for node in root.get_sub_cats():
            vals.extend(vals_over_year_month(node, year, month))
    else:
        if type == 'Year': 
            if root.get_val() == year:
                for node in root.get_sub_cats():
                    vals.extend(vals_over_year_month(node, year, month))
        elif type == 'Month': 
            if root.get_val() == month:
                for node in root.get_sub_cats():
                    vals.extend(vals_over_year_month(node, year, month))
        elif type == 'Day':
            for node in root.get_sub_cats():
                vals.extend(vals_over_year_month(node, year, month))
        elif type == 'Val':
            vals.extend([root.get_val()])
    return vals 

def vals_over_year(root, year):
    vals = []
    type = root.get_type()
    if type == 'Root':
        for node in root.get_sub_cats():
            vals.extend(vals_over_year_month(node, year))
    else:
        if type == 'Year': 
            if root.get_val() == year:
                for node in root.get_sub_cats():
                    vals.extend(vals_over_year_month(node, year))
        elif type == 'Month': 
            for node in root.get_sub_cats():
                vals.extend(vals_over_year_month(node, year))
        elif type == 'Day':
            for node in root.get_sub_cats():
                vals.extend(vals_over_year_month(node, year))
        elif type == 'Val':
            vals.extend([root.get_val()])
    return vals 
    
def days_over_year_month(root, year, month):
    vals = []
    type = root.get_type()
    if type == 'Root':
        for node in root.get_sub_cats():
            vals.extend(vals_over_year_month(node, year, month))
    else:
        if type == 'Year': 
            if root.get_val() == year:
                for node in root.get_sub_cats():
                    vals.extend(vals_over_year_month(node, year, month))
        elif type == 'Month': 
            if root.get_val() == month:
                for node in root.get_sub_cats():
                    vals.extend(vals_over_year_month(node, year, month))
        elif type == 'Day':
            vals.extend([root.get_val()])

    return vals

def days_extension_from_month(days, month):
    '''
    When calculating over a two month period, 
    account for the difference in months between 
    '''
    # Set of months with 31 days 
    month_31 = [1,3,5,7,8,10,12]

    # Adjust if month is Jan 
    if month == 1:
        month = 12 
    else:
        m = month - 1 

    # Add difference in days to month 
    if m == 2: # If Feb
        for i in range(len(days)):
            days[i] = days[i] + 28
    if m in month_31: 
        for i in range(len(days)):
            days[i] = days[i] + 31
    else:
        for i in range(len(days)):
            days[i] = days[i] + 30

    return days


# ____WRITING FUNCTIONS____
def intro_statement(name1, name2):
    ret_str = "This is a report of the data collected from the input files. The"
    return 