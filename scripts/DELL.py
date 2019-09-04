#!/usr/bin/env python
# coding: utf-8

# In[250]:


import numpy as np
import pandas as pd
from sklearn import preprocessing
from datascience import *
import matplotlib


# In[251]:


dataset_1 = pd.read_csv('data1.csv')
data_1 = pd.DataFrame(dataset_1,columns=['Commodity','Cost $','Supplier Performance Rating','Component Performance Rating']) 
#data_1


# In[ ]:





# In[252]:


y_train = dataset_1['Supplier']
le2  = preprocessing.LabelEncoder()
y_train = le2.fit_transform(y_train)
y_train


# In[253]:


le  = preprocessing.LabelEncoder()
data_1['Commodity'] = le.fit_transform(data_1['Commodity'])
#data_1


# In[254]:


from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors=1, metric='minkowski', p=2)
classifier.fit(data_1, y_train)


# In[264]:



# a = ['HDD 500GB']
# enter([input()])


# In[265]:


# def conversion (arr[],n):
#     b= enter(n)
#     arr[]= arr[]

#type(b)


# In[268]:


def enter(a):
        b= le.transform(a)
        return b.item(0)
    
temp = input()
temp = enter([temp])
company = classifier.predict([[temp,15,10,10]]).item(0)
le2.inverse_transform([company])


# In[258]:


# #a = ['HDD 500GB']
# a = [company]
# b = le2.inverse_transform(a)
# b


# In[119]:


dataset_1.plot.scatter('Cost $', 'Supplier Performance Rating')


# In[133]:


# Timeliness of delivery, Financial condition of company, Quality of service
Time= make_array(10,8,10,6,4,2)
Finance= make_array(10,6,4,10,8,6)
Quality= make_array(10,4,6,8,10,6)


# In[134]:


Supplier_rating= Table().with_columns('Time', Time, 'Finance', Finance, 'Quality', Quality)
Supplier_rating


# In[135]:


def standard_units(xyz):
    return(xyz-np.mean(xyz))/np.std(xyz)


# In[136]:


Supplier_rating= Supplier_rating.with_columns('Normalization Time', standard_units(Supplier_rating.column('Time')),'Normalization Finance', standard_units(Supplier_rating.column('Finance')),'Normalization Quality', standard_units(Supplier_rating.column('Quality')))


# In[137]:


Supplier_rating


# In[138]:


Rating = make_array(10,6,6,8,7,5)
Supplier_rating = Supplier_rating.with_column('Rating', Rating)
Supplier_rating
    


# In[139]:


x= Supplier_rating.column('Normalization Time')+Supplier_rating.column('Normalization Finance')+Supplier_rating.column('Normalization Quality')


# In[140]:


Supplier_rating= Supplier_rating.with_column('x_val', x)


# In[141]:


Supplier_rating


# In[147]:


def predict_y(x_val):
    nearby_points = Supplier_rating.where('x_val', are.between(x_val-1, x_val+1))
    return np.mean(nearby_points.column('Rating'))


# In[148]:


Supplier_rating= Supplier_rating.with_column('Predicted Rating', Supplier_rating.apply(predict_y, 'x_val'))


# In[149]:


Supplier_rating


# In[151]:


Supplier_rating.scatter('x_val', 'Predicted Rating')


# In[152]:


def correlation(t,x,y):
    x_standard= standard_units(t.column(x))
    y_standard= standard_units(t.column(y))
    return np.mean(x_standard*y_standard)


# In[153]:


def slope (t,x,y):
    r= correlation(t,x,y)
    y_sd= np.std(t.column(y))
    x_sd= np.std(t.column(x))
    return r*y_sd/x_sd


# In[154]:


def intercept(t,x,y):
    x_mean= np.mean(t.column(x))
    y_mean= np.mean(t.column(y))
    return y_mean- slope(t,x,y)*x_mean


# In[156]:


data_correlation= correlation(Supplier_rating, 'x_val', 'Predicted Rating' )
data_slope= slope(Supplier_rating, 'x_val', 'Predicted Rating')
data_intercept= intercept(Supplier_rating, 'x_val', 'Predicted Rating')


# In[157]:


Supplier_rating1= Supplier_rating.select('Rating', 'x_val', 'Predicted Rating')


# In[163]:


Supplier_rating1= Supplier_rating1.with_column('Regression', data_slope*Supplier_rating1.column('x_val')+ data_intercept)
Supplier_rating1


# In[165]:


Supplier_rating1.plot('x_val')


# In[167]:


predict_y(2)


# In[178]:


def find_x_val(t):
    normalization_time= standard_units(t.column('Time'))
    normalization_finance= standard_units(t.column('Finance'))
    normalization_quantity= standard_units(t.column('Quality'))
    return normalization_time+ normalization_finance+ normalization_quantity


# In[181]:


find_x_val(Supplier_rating)


# In[ ]:




