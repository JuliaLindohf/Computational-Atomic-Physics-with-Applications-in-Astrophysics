import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

inputdata = pd.read_fwf("Be_2s2p3P.dat")

inputdata.rename(columns = {'sqrt(r)':'sqrt_r', 'P(nl;r)':'wavefunctions'}, inplace = True)

# to divide the dataframe into three chunks 
# to convert each column to a list 
list1 = inputdata['sqrt_r'].tolist() 
list2 = inputdata['wavefunctions'].tolist()  
