
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 15:46:48 2020 EET
@author: Naveena 


For Invoice Reconcilliation

SQL query :
 


Excluded Manual fee and Holding fee in thi sverification script
 Ignore the case if there is minor difference in the calculated fee amount value that is  due to rounding the decimal
    
"""

import pandas as pd
#import numpy as np

from rules1 import recon_diff
import math

def cal_fee_amt(datum):
    
    BillID = datum['BillID']
    pack_id = datum['PCKG']
    fee_basis = datum['FEEUNIT']
    fee_basis1 =int(fee_basis)
    
    feeamount = recon_diff (BillID, pack_id, fee_basis1)
    #print ('feebasis',fee_basis)
    #print ('BillID',BillID)
   # feeamount1=int(feeamount)
   # print(type(feeamount))  
   #Round the feeamount into 2
    return round(feeamount, 2)


def isclose(datum):
    diff =  math.isclose(datum['CALC_FEE_AMT'], datum['FEEAMOUNT'])
    return diff


#Start of code


print('Enter the output file name')
outputfilename = input()

#print('Enter the combilned file name')
#com = input()




#This holds the data that is already invoiced by Infinity
Billing = pd.read_excel('input/INV.xlsx')
Billing['FEEAMOUNT'] = pd.to_numeric(Billing['FEEAMOUNT'], errors='coerce')
#print ('Billing',Billing)
#round the amount to 2 and basis to 6
Billing['FEEAMOUNT'] = Billing.apply(lambda datum: round(datum['FEEAMOUNT'], 2), axis=1)
#print(Billing)
# GRoup the data from the Inputfile
data_bp = Billing.filter(['BillID', 'customerID', 'PCKG', 'FEEAMOUNT','FEEUNIT'])
#print ('Billing',data_bp)


combined_data = pd.concat([ data_bp], axis=0, sort=True)
#Calculate the fee at this level.
combined_data['CALC_FEE_AMT'] = combined_data.apply(lambda datum: cal_fee_amt(datum), axis=1)
#Reorder the column order
combined_data = combined_data[['BillID', 'customerID', 'PCKG', 'CALC_FEE_AMT','FEEUNIT']]
#Ignore the cases where fee is calculated as 0.
combined_data = combined_data[combined_data['CALC_FEE_AMT'] > 0]
combined_data['CALC_FEE_AMT'] = combined_data.apply(lambda datum: round(datum['CALC_FEE_AMT'], 2), axis=1)
#print (combined_data)


merged = pd.merge(left=combined_data, right=Billing, how='inner', left_on=['BillID', 'customerID','PCKG','FEEUNIT'], right_on=['BillID', 'customerID','PCKG','FEEUNIT'])
#merged = pd.merge(left=combined_data, right=Billing)
#print ('merged',merged)
merged['FEEAMT_DIFF'] = merged.apply(lambda datum: isclose(datum), axis=1)
merged.reset_index(drop=True, inplace=True)
#print (merged)
#merged.reset_index(drop=False, inplace=False)


merged.to_excel('output/' + outputfilename + '.xlsx')
###combined_data.to_excel('output/' + com + '.xlsx')
