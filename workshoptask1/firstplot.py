import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

inputdata = pd.read_fwf("Be_2s2p3P.dat")

# to give each column a new name, making life a bit easier for me later
inputdata.rename(columns = {'sqrt(r)':'sqrt_r', 'P(nl;r)':'wavefunctions'}, inplace = True)

# to divide the dataframe into three chunks 
# to convert each column to a list 
list1 = inputdata['sqrt_r'].tolist() 
list2 = inputdata['wavefunctions'].tolist()  

# three spectral are included 
str_elem = ['1s', '2s', '2p'] 

class wavefunctionplot:
  def __init__(self, sqrtlist, wavefunction, str_elem): 
    # to store the instance variable
    self.sqrtlist = sqrtlist
    self.wavefkt = wavefunction
    self.listnames = str_elem

  def breakframe(self): 
    # the number of elements 
    L = len(self.sqrtlist) 
    # to store all usable indice
    indexlist = []
    newlist = [ ]
    for i in range(L):
      try:
        elem = self.sqrtlist[i]
        newelem = float(elem)
        newlist.append(newelem)
      except: 
        newelem = 0
        indexlist.append(i)
        newlist.append(newelem)
    indexlist.append(L) 
    # the products are two new instance lists 
    self.indexlist = indexlist

  def newdataframe(self): 
    # to store the data in a new dictionary 
    self.newdict = {}

    def newfram(list1, list2): 
      # the first list contains the sqrt r 
      # to transform the sqrt r to regular r 
      regular_r = [np.sqrt(float(r)) for r in list1] 
      wave = [float(elem)**2 for elem in list2] 
      data = { 'Regular_r': regular_r, 'wavedensity': wave}
      # the output is a new dataframe 
      #print( data )
      return pd.DataFrame(data)

    nr_entrance = len(self.listnames) 
    L = nr_entrance
    # to create new entrance to the dictionary 
    for i in range(L): 
      first_index = self.indexlist[i]+1
      if i != L:
        last_index =self.indexlist[i+1]-1
      else:
        last_index = self.indexlist[i+1] 

      list1 = self.sqrtlist[first_index:last_index] 
      list2 = self.wavefkt[first_index:last_index]  
      # print( len(list1), len(list2))
      self.newdict[self.listnames[i]] = newfram(list1, list2)

  def plot_lineplots(self): 
    plt.figure(figsize=(15, 10))
    for ent in self.listnames: 
      newdataframe = self.newdict[ent] 
      plt.plot(newdataframe['Regular_r'].tolist(), newdataframe['wavedensity'].tolist(), label=ent,  linewidth=5)
    plt.legend()
    plt.grid(True)
    plt.xlabel('Regular r')
    plt.ylabel('Density')
    plt.show()

    
model1 =  wavefunctionplot(list1, list2, ['1s', '2s', '2p'])
model1.breakframe()

model1.newdataframe()
model1.plot_lineplots()
