#!/usr/bin/env python
# coding: utf-8

# In[57]:


import numpy as np
import pandas as pd
from sklearn import preprocessing
from datascience import *
import matplotlib
import sys


# In[2]:


# table= Table.read_table('data1.csv')
# table


# # In[3]:


# dataset_1 = pd.read_csv('data1.csv')
# data_1 = pd.DataFrame(dataset_1,columns=['Commodity','Cost $','Supplier Performance Rating','Component Performance Rating']) 
# data_1


# # In[4]:


# y_train = dataset_1['Supplier']
# le2  = preprocessing.LabelEncoder()
# y_train = le2.fit_transform(y_train)
# y_train


# # In[5]:


# le  = preprocessing.LabelEncoder()
# data_1['Commodity'] = le.fit_transform(data_1['Commodity'])
# data_1


# # In[26]:


# from sklearn.neighbors import KNeighborsClassifier
# classifier = KNeighborsClassifier(n_neighbors=1, metric='minkowski', p=2)
# classifier.fit(data_1, y_train)


# # In[27]:


# def enter(a):
#         b= le.transform(a)
#         return b.item(0)
    
# temp = input()
# temp = enter([temp])
# company = classifier.predict([[temp,15,10,10]]).item(0)
# le2.inverse_transform([company])


# # In[20]:


# # def conversion (arr[],n):
# #     b= enter(n)
# #     arr[]= arr[]

# #type(b)


# # In[24]:


# company = classifier.predict([[1,10,10,10]])
# le2.inverse_transform([company])


# # In[22]:


# # #a = ['HDD 500GB']
# # a = [company]
# # b = le2.inverse_transform(a)
# # b


# # In[23]:


# dataset_1.plot.scatter('Cost $', 'Supplier Performance Rating')


# # In[24]:


# # Timeliness of delivery, Financial condition of company, Quality of service
# Time= make_array(10,8,10,6,4,2)
# Finance= make_array(10,6,4,10,8,6)
# Quality= make_array(10,4,6,8,10,6)
# Supplier= make_array("Samsung", "Intel", "Nvidea", "Samsung", "Intel", "Samsung")
# Commodity= make_array("HDD", "HDD", "Screen", "CPU", "Screen", "HDD")


# # In[256]:


Graphics_table= Table.read_table("Graphics_100.csv")
Graphics_table


# In[282]:


Screen_table= Table.read_table("Screen_100.csv")
Screen_table


# In[293]:


RAM_table= Table.read_table("Screen_100.csv")
RAM_table


# In[312]:


SSD_table= Table.read_table("SSD.csv")
SSD_table


# In[324]:


Proc_table= Table.read_table("Processor_100.csv")
Proc_table


# In[213]:


Supplier_rating= Table.read_table("HDD_100.csv")
Supplier_rating


# In[155]:


def price_val(typ,size,cost):
    sup= Supplier_rating.where("type",are.equal_to(typ))
    
    


# In[214]:


Supplier_rating.column('Time')                                    


# In[268]:


#converting into standard units
def standard_units(xyz):
    return(xyz-np.mean(xyz))/np.std(xyz)


# In[257]:


Graphic_rating= Graphics_table.with_columns('Normalization Time', standard_units(Graphics_table.column('Time')), 'Normalization Finance', standard_units(Graphics_table.column('Finance')), 'Normalization Quality', standard_units(Graphics_table.column('Quality')))


# In[283]:


Screen_rating= Screen_table.with_columns('Normalization Time', standard_units(Screen_table.column('Time')), 'Normalization Finance', standard_units(Screen_table.column('Finance')), 'Normalization Quality', standard_units(Screen_table.column('Quality')))


# In[294]:


RAM_rating= RAM_table.with_columns('Normalization Time', standard_units(RAM_table.column('Time')), 'Normalization Finance', standard_units(RAM_table.column('Finance')), 'Normalization Quality', standard_units(RAM_table.column('Quality')))


# In[325]:


Proc_rating= Proc_table.with_columns('Normalization Time', standard_units(RAM_table.column('Time')), 'Normalization Finance', standard_units(RAM_table.column('Finance')), 'Normalization Quality', standard_units(RAM_table.column('Quality')))


# In[313]:


SSD_rating= SSD_table.with_columns('Normalization Time', standard_units(SSD_table.column('Time')), 'Normalization Finance', standard_units(SSD_table.column('Finance')), 'Normalization Quality', standard_units(SSD_table.column('Quality')))


# In[216]:


Supplier_rating= Supplier_rating.with_columns('Normalization Time', standard_units(Supplier_rating.column('Time')), 'Normalization Finance', standard_units(Supplier_rating.column('Finance')), 'Normalization Quality', standard_units(Supplier_rating.column('Quality')))


# In[295]:


Graphic_rating


# In[296]:


RAM_rating


# In[314]:


SSD_rating


# In[326]:


Proc_rating


# In[284]:


Screen_rating


# In[217]:


Supplier_rating


# In[259]:


Graphic_x= Graphic_rating.column('Normalization Time')+Graphic_rating.column('Normalization Finance')+Graphic_rating.column('Normalization Quality')


# In[285]:


Screen_x= Screen_rating.column('Normalization Time')+Screen_rating.column('Normalization Finance')+Screen_rating.column('Normalization Quality')


# In[327]:


Proc_x= Proc_rating.column('Normalization Time')+Proc_rating.column('Normalization Finance')+Proc_rating.column('Normalization Quality')


# In[315]:


SSD_x= SSD_rating.column('Normalization Time')+SSD_rating.column('Normalization Finance')+SSD_rating.column('Normalization Quality')


# In[297]:


RAM_x= RAM_rating.column('Normalization Time')+RAM_rating.column('Normalization Finance')+RAM_rating.column('Normalization Quality')


# In[231]:


HDD_x= Supplier_rating.column('Normalization Time')+Supplier_rating.column('Normalization Finance')+Supplier_rating.column('Normalization Quality')


# In[273]:


Graphic_rating= Graphic_rating.with_column('x_val', Graphic_x)


# In[298]:


RAM_rating= RAM_rating.with_column('x_val', RAM_x)


# In[328]:


Proc_rating= Proc_rating.with_column('x_val', RAM_x)


# In[316]:


SSD_rating= SSD_rating.with_column('x_val', SSD_x)


# In[286]:


Screen_rating= Screen_rating.with_column('x_val', Screen_x)


# In[232]:


Supplier_rating= Supplier_rating.with_column('x_val', HDD_x)


# In[261]:


Graphic_rating


# In[299]:


RAM_rating


# In[329]:


Proc_rating


# In[287]:


Screen_rating


# In[318]:


SSD_rating


# In[233]:


Supplier_rating


# In[276]:


def predict_gy(x_val):
    nearby= Graphic_rating.where('x_val', are.between(x_val-1, x_val+1))
    return np.mean((nearby.column('Time')+nearby.column('Finance')+nearby.column('Quality'))/3)
    


# In[302]:


def predict_ry(x_val):
    nearby= RAM_rating.where('x_val', are.between(x_val-1, x_val+1))
    return np.mean((nearby.column('Time')+nearby.column('Finance')+nearby.column('Quality'))/3)
    


# In[330]:


def predict_py(x_val):
    nearby= Proc_rating.where('x_val', are.between(x_val-1, x_val+1))
    return np.mean((nearby.column('Time')+nearby.column('Finance')+nearby.column('Quality'))/3)


# In[319]:


def predict_sdy(x_val):
    nearby= SSD_rating.where('x_val', are.between(x_val-1, x_val+1))
    return np.mean((nearby.column('Time')+nearby.column('Finance')+nearby.column('Quality'))/3)


# In[288]:


def predict_sy(x_val):
    nearby= Screen_rating.where('x_val', are.between(x_val-1, x_val+1))
    return np.mean((nearby.column('Time')+nearby.column('Finance')+nearby.column('Quality'))/3)


# In[244]:


#predicting value of Rating given a particular x_value
def predict_y(x_val):
    nearby_points = Supplier_rating.where('x_val', are.between(x_val-1, x_val+1))
    return np.mean((nearby_points.column('Time')+nearby_points.column('Finance')+nearby_points.column('Quality'))/3)


# In[246]:


predict_y(3)


# In[278]:


Graphic_rating= Graphic_rating.with_column('Predicted Rating', Graphic_rating.apply(predict_gy, 'x_val'))


# In[303]:


RAM_rating= RAM_rating.with_column('Predicted Rating', RAM_rating.apply(predict_ry, 'x_val'))


# In[320]:


SSD_rating= SSD_rating.with_column('Predicted Rating', SSD_rating.apply(predict_sdy, 'x_val'))


# In[331]:


Proc_rating= Proc_rating.with_column('Predicted Rating', SSD_rating.apply(predict_sdy, 'x_val'))


# In[289]:


Screen_rating= Screen_rating.with_column('Predicted Rating', Screen_rating.apply(predict_sy, 'x_val'))


# In[247]:


Supplier_rating= Supplier_rating.with_column('Predicted Rating', Supplier_rating.apply(predict_y, 'x_val'))


# In[280]:


Graphic_rating.sort("Predicted Rating", descending="True")


# In[304]:


RAM_rating.sort("Predicted Rating", descending="True")


# In[332]:


Proc_rating.sort("Predicted Rating", descending="True")


# In[321]:


SSD_rating.sort("Predicted Rating", descending="True")


# In[290]:


Screen_rating.sort("Predicted Rating", descending="True")


# In[291]:


Supplier_rating.sort("Predicted Rating", descending="True")


# In[266]:

# print(sys.argv[1],sys.argv[2])
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
    a= anu.to_csv("anu1.csv")
    return anu

value_Graphic(sys.argv[1],sys.argv[2])


# In[333]:


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
    a= anu.to_csv("anu2.csv")
    return anu

value_Proc(sys.argv[3],sys.argv[4])


# In[322]:


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
    a= anu.to_csv("anu3.csv")
    return anu

value_SSD(sys.argv[5],sys.argv[6])


# In[306]:


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
    a= anu.to_csv("anu4.csv")
    return anu

value_RAM(sys.argv[7],sys.argv[8])


# In[307]:


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
    a= anu.to_csv("anu5.csv")
    return anu

value_Screen(sys.argv[9],sys.argv[10])


# In[308]:


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
    #a= anu.to_csv("anu.csv")
    return anu


value_HDD(sys.argv[11],sys.argv[12])


# In[ ]:





# In[211]:


#ayush = pd.DataFrame(tab1,columns=['Company','Predicted rating'])
# anu = tab1.drop('size','quality','Time','Quality','Finance','Normalization Time','Normalization Finance','Normalization Quality','x_val')
# anu = ayush.sort('Predicted Rating',descending=True)
# anu= ayush.take(np.arange(0, 5))
# anu


# # In[73]:


# k=pd.unique((tab1.sort("Predicted Rating", descending='TRUE').column("Predicted Rating")))
# k


# # In[75]:


# k=pd.unique((tab1.sort("Predicted Rating", descending='TRUE').column("Predicted Rating")))

# s= make_array()
# s1= make_array()
# for i in np.arange(5):
#     Table1= Supplier_rating.where("Predicted Rating", are.equal_to(k.item(i))).take(1)
#     t= Table1.where("Quality", are.equal_to(4)).column("Company")
#     Table2= Supplier_rating.where("Predicted Rating", are.equal_to(k.item(i))).take(1)
#     t2= Table2.where("Quality", are.equal_to(4)).column("Predicted Rating")
#     s= np.append(t, s)
#     s1= np.append(t2, s1)
    
# anu= Table().with_columns("Name", s, "Predicted Rating", s1)
# anu
# #print(s)


# # In[76]:


# k=pd.unique((Supplier_rating.sort("Predicted Rating", descending='TRUE').column("Predicted Rating")))

# s= make_array()
# s1= make_array()
# for i in np.arange(5):
#     Table1= Supplier_rating.where("Predicted Rating", are.equal_to(k.item(i))).take(1).column("Company")
#     Table2= Supplier_rating.where("Predicted Rating", are.equal_to(k.item(i))).take(1).column("Predicted Rating")
#     s= np.append(Table1, s)
#     s1= np.append(Table2, s1)
    
# anu= Table().with_columns("Name", s, "Predicted Rating", s1)
# anu
# #print(s)


# # In[29]:


# anu.to_csv("a.csv")


# # In[17]:


# Supplier_rating.scatter('x_val', 'Predicted Rating')


# # In[130]:


# def correlation(t,x,y):
#     x_standard= standard_units(t.column(x))
#     y_standard= standard_units(t.column(y))
#     return np.mean(x_standard*y_standard)


# # In[131]:


# def slope (t,x,y):
#     r= correlation(t,x,y)
#     y_sd= np.std(t.column(y))
#     x_sd= np.std(t.column(x))
#     return r*y_sd/x_sd


# # In[132]:


# def intercept(t,x,y):
#     x_mean= np.mean(t.column(x))
#     y_mean= np.mean(t.column(y))
#     return y_mean- slope(t,x,y)*x_mean


# # In[133]:


# data_correlation= correlation(Supplier_rating, 'x_val', 'Predicted Rating' )
# data_slope= slope(Supplier_rating, 'x_val', 'Predicted Rating')
# data_intercept= intercept(Supplier_rating, 'x_val', 'Predicted Rating')


# # In[135]:


# Supplier_rating1= Supplier_rating.select('x_val', 'Predicted Rating')


# # In[136]:


# Supplier_rating1= Supplier_rating1.with_column('Regression', data_slope*Supplier_rating1.column('x_val')+ data_intercept)
# Supplier_rating1


# # In[138]:


# Supplier_rating1.plot('x_val')


# # In[139]:


# predict_y(2)


# # In[ ]:





# # In[140]:


# # To find nearest ratings
# def rate(x,y,z):
#     a= Supplier_rating.where("Time",are.between(x-1,x+1)).where("Quality",are.between(y-1,y+1)).where("Finance",are.between(z-1,z+1))
#     normalization_time= np.std((a.column('Time')))
#     #normalization_finance= standard_units(a.column('Finance'))
#     #normalization_quantity= standard_units(a.column('Quality'))
#     return normalization_time



# #def find_x_val(t):
#     #table_new= t.where("x_val", are.between(n-1,n+1))
#  #   normalization_time= standard_units(t.column('Time'))
#   #  normalization_finance= standard_units(t.column('Finance'))
#    # normalization_quantity= standard_units(t.column('Quality'))
#     #return np.mean(normalization_time+ normalization_finance+ normalization_quantity)


# # In[141]:


# rate(8,6,4)


# # In[142]:


# standard_units(Supplier_rating.column('Time'))


# # In[ ]:




