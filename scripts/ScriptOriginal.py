#!/usr/bin/env python
# coding: utf-8

# In[335]:


import numpy as np
import pandas as pd
from sklearn import preprocessing
from datascience import *
import matplotlib


# In[343]:


Graphics_table= Table.read_table("Graphics_100.csv")
Graphics_table


# In[344]:


Screen_table= Table.read_table("Screen_100.csv")
Screen_table


# In[345]:


RAM_table= Table.read_table("Screen_100.csv")
RAM_table


# In[346]:


SSD_table= Table.read_table("SSD.csv")
SSD_table


# In[347]:


Proc_table= Table.read_table("Processor_100.csv")
Proc_table


# In[348]:


Supplier_rating= Table.read_table("HDD_100.csv")
Supplier_rating


# In[350]:


#converting into standard units
def standard_units(xyz):
    return(xyz-np.mean(xyz))/np.std(xyz)


# In[351]:


Graphic_rating= Graphics_table.with_columns('Normalization Time', standard_units(Graphics_table.column('Time')), 'Normalization Finance', standard_units(Graphics_table.column('Finance')), 'Normalization Quality', standard_units(Graphics_table.column('Quality')))


# In[352]:


Screen_rating= Screen_table.with_columns('Normalization Time', standard_units(Screen_table.column('Time')), 'Normalization Finance', standard_units(Screen_table.column('Finance')), 'Normalization Quality', standard_units(Screen_table.column('Quality')))


# In[353]:


RAM_rating= RAM_table.with_columns('Normalization Time', standard_units(RAM_table.column('Time')), 'Normalization Finance', standard_units(RAM_table.column('Finance')), 'Normalization Quality', standard_units(RAM_table.column('Quality')))


# In[354]:


Proc_rating= Proc_table.with_columns('Normalization Time', standard_units(RAM_table.column('Time')), 'Normalization Finance', standard_units(RAM_table.column('Finance')), 'Normalization Quality', standard_units(RAM_table.column('Quality')))


# In[355]:


SSD_rating= SSD_table.with_columns('Normalization Time', standard_units(SSD_table.column('Time')), 'Normalization Finance', standard_units(SSD_table.column('Finance')), 'Normalization Quality', standard_units(SSD_table.column('Quality')))


# In[356]:


Supplier_rating= Supplier_rating.with_columns('Normalization Time', standard_units(Supplier_rating.column('Time')), 'Normalization Finance', standard_units(Supplier_rating.column('Finance')), 'Normalization Quality', standard_units(Supplier_rating.column('Quality')))


# In[357]:


Graphic_rating


# In[358]:


RAM_rating


# In[359]:


SSD_rating


# In[360]:


Proc_rating


# In[361]:


Screen_rating


# In[362]:


Supplier_rating


# In[363]:


Graphic_x= Graphic_rating.column('Normalization Time')+Graphic_rating.column('Normalization Finance')+Graphic_rating.column('Normalization Quality')


# In[364]:


Screen_x= Screen_rating.column('Normalization Time')+Screen_rating.column('Normalization Finance')+Screen_rating.column('Normalization Quality')


# In[365]:


Proc_x= Proc_rating.column('Normalization Time')+Proc_rating.column('Normalization Finance')+Proc_rating.column('Normalization Quality')


# In[366]:


SSD_x= SSD_rating.column('Normalization Time')+SSD_rating.column('Normalization Finance')+SSD_rating.column('Normalization Quality')


# In[367]:


RAM_x= RAM_rating.column('Normalization Time')+RAM_rating.column('Normalization Finance')+RAM_rating.column('Normalization Quality')


# In[368]:


HDD_x= Supplier_rating.column('Normalization Time')+Supplier_rating.column('Normalization Finance')+Supplier_rating.column('Normalization Quality')


# In[369]:


Graphic_rating= Graphic_rating.with_column('x_val', Graphic_x)


# In[370]:


RAM_rating= RAM_rating.with_column('x_val', RAM_x)


# In[371]:


Proc_rating= Proc_rating.with_column('x_val', RAM_x)


# In[372]:


SSD_rating= SSD_rating.with_column('x_val', SSD_x)


# In[373]:


Screen_rating= Screen_rating.with_column('x_val', Screen_x)


# In[374]:


Supplier_rating= Supplier_rating.with_column('x_val', HDD_x)


# In[375]:


Graphic_rating


# In[376]:


RAM_rating


# In[377]:


Proc_rating


# In[378]:


Screen_rating


# In[379]:


SSD_rating


# In[380]:


Supplier_rating


# In[381]:


def predict_gy(x_val):
    nearby= Graphic_rating.where('x_val', are.between(x_val-1, x_val+1))
    return np.mean((nearby.column('Time')+nearby.column('Finance')+nearby.column('Quality'))/3)
    


# In[382]:


def predict_ry(x_val):
    nearby= RAM_rating.where('x_val', are.between(x_val-1, x_val+1))
    return np.mean((nearby.column('Time')+nearby.column('Finance')+nearby.column('Quality'))/3)
    


# In[383]:


def predict_py(x_val):
    nearby= Proc_rating.where('x_val', are.between(x_val-1, x_val+1))
    return np.mean((nearby.column('Time')+nearby.column('Finance')+nearby.column('Quality'))/3)


# In[384]:


def predict_sdy(x_val):
    nearby= SSD_rating.where('x_val', are.between(x_val-1, x_val+1))
    return np.mean((nearby.column('Time')+nearby.column('Finance')+nearby.column('Quality'))/3)


# In[385]:


def predict_sy(x_val):
    nearby= Screen_rating.where('x_val', are.between(x_val-1, x_val+1))
    return np.mean((nearby.column('Time')+nearby.column('Finance')+nearby.column('Quality'))/3)


# In[386]:


#predicting value of Rating given a particular x_value
def predict_y(x_val):
    nearby_points = Supplier_rating.where('x_val', are.between(x_val-1, x_val+1))
    return np.mean((nearby_points.column('Time')+nearby_points.column('Finance')+nearby_points.column('Quality'))/3)


# In[387]:


Graphic_rating= Graphic_rating.with_column('Predicted Rating', Graphic_rating.apply(predict_gy, 'x_val'))


# In[388]:


RAM_rating= RAM_rating.with_column('Predicted Rating', RAM_rating.apply(predict_ry, 'x_val'))


# In[389]:


SSD_rating= SSD_rating.with_column('Predicted Rating', SSD_rating.apply(predict_sdy, 'x_val'))


# In[390]:


Proc_rating= Proc_rating.with_column('Predicted Rating', SSD_rating.apply(predict_sdy, 'x_val'))


# In[391]:


Screen_rating= Screen_rating.with_column('Predicted Rating', Screen_rating.apply(predict_sy, 'x_val'))


# In[392]:


Supplier_rating= Supplier_rating.with_column('Predicted Rating', Supplier_rating.apply(predict_y, 'x_val'))


# In[393]:


Graphic_rating.sort("Predicted Rating", descending="True")


# In[394]:


RAM_rating.sort("Predicted Rating", descending="True")


# In[395]:


Proc_rating.sort("Predicted Rating", descending="True")


# In[396]:


SSD_rating.sort("Predicted Rating", descending="True")


# In[397]:


Screen_rating.sort("Predicted Rating", descending="True")


# In[398]:


Supplier_rating.sort("Predicted Rating", descending="True")


# In[399]:


def value_Graphic(n,x):
    tab1= Graphic_rating.where("size", are.equal_to(n)).where("type", are.equal_to(x))
    tab2= tab1.sort("Predicted Rating", descending="True")
    anu = tab2.drop('size','quality','Time','Quality','Finance','Normalization Time','Normalization Finance','Normalization Quality','x_val')
    anu = anu.sort('Predicted Rating',descending=True)
    if(len(anu.column("Predicted Rating"))>5):
        anu=anu.take(np.arange(0,5))
    elif(len(anu.column("Predicted Rating"))<=5):
        anu= anu.take(np.arange(0, len(anu.column("Predicted Rating"))))
    else:
        print("No Value Found")
    a= anu.to_csv("dell1.csv")
    return anu

value_Graphic(0,1)


# In[400]:


def value_Proc(n,x):
    tab1= Proc_rating.where("size", are.equal_to(n)).where("type", are.equal_to(x))
    tab2= tab1.sort("Predicted Rating", descending="True")
    anu = tab2.drop('size','quality','Time','Quality','Finance','Normalization Time','Normalization Finance','Normalization Quality','x_val')
    anu = anu.sort('Predicted Rating',descending=True)
    if(len(anu.column("Predicted Rating"))>5):
        anu=anu.take(np.arange(0,5))
    elif(len(anu.column("Predicted Rating"))<=5):
        anu= anu.take(np.arange(0, len(anu.column("Predicted Rating"))))
    else:
        print("No Value Found")
    a= anu.to_csv("dell2.csv")
    return anu

value_Proc(0,1)


# In[401]:


def value_SSD(n,x):
    tab1= SSD_rating.where("size", are.equal_to(n)).where("type", are.equal_to(x))
    tab2= tab1.sort("Predicted Rating", descending="True")
    anu = tab2.drop('size','quality','Time','Quality','Finance','Normalization Time','Normalization Finance','Normalization Quality','x_val')
    anu = anu.sort('Predicted Rating',descending=True)
    if(len(anu.column("Predicted Rating"))>5):
        anu=anu.take(np.arange(0,5))
    elif(len(anu.column("Predicted Rating"))<=5):
        anu= anu.take(np.arange(0, len(anu.column("Predicted Rating"))))
    else:
        print("No Value Found")
    a= anu.to_csv("dell3.csv")
    return anu

value_SSD(0,1)


# In[402]:


def value_RAM(n,x):
    tab1= RAM_rating.where("size", are.equal_to(n)).where("type", are.equal_to(x))
    tab2= tab1.sort("Predicted Rating", descending="True")
    anu = tab2.drop('size','quality','Time','Quality','Finance','Normalization Time','Normalization Finance','Normalization Quality','x_val')
    anu = anu.sort('Predicted Rating',descending=True)
    if(len(anu.column("Predicted Rating"))>5):
        anu=anu.take(np.arange(0,5))
    elif(len(anu.column("Predicted Rating"))<=5):
        anu= anu.take(np.arange(0, len(anu.column("Predicted Rating"))))
    else:
        print("No Value Found")
    a= anu.to_csv("dell4.csv")
    return anu

value_RAM(0,1)


# In[403]:


def value_Screen(n,x):
    tab1= Screen_rating.where("size", are.equal_to(n)).where("type", are.equal_to(x))
    tab2= tab1.sort("Predicted Rating", descending="True")
    anu = tab2.drop('size','quality','Time','Quality','Finance','Normalization Time','Normalization Finance','Normalization Quality','x_val')
    anu = anu.sort('Predicted Rating',descending=True)
    if(len(anu.column("Predicted Rating"))>5):
        anu=anu.take(np.arange(0,5))
    elif(len(anu.column("Predicted Rating"))<=5):
        anu= anu.take(np.arange(0, len(anu.column("Predicted Rating"))))
    else:
        print("No Value Found")
    a= anu.to_csv("dell5.csv")
    return anu

value_Screen(0,1)


# In[404]:


def value_HDD(n,x):
    tab1= Supplier_rating.where("size", are.equal_to(n)).where("type", are.equal_to(x))
    tab2= tab1.sort("Predicted Rating", descending="True")
    anu = tab2.drop('size','quality','Time','Quality','Finance','Normalization Time','Normalization Finance','Normalization Quality','x_val')
    anu = anu.sort('Predicted Rating',descending=True)
    if(len(anu.column("Predicted Rating"))>5):
        anu=anu.take(np.arange(0,5))
    elif(len(anu.column("Predicted Rating"))<=5):
        anu= anu.take(np.arange(0, len(anu.column("Predicted Rating"))))
    else:
        print("No Value Found")
    a= anu.to_csv("dell6.csv")
    return anu


value_HDD(0,1)

