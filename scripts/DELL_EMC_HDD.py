
import numpy as np
import pandas as pd
from sklearn import preprocessing
from datascience import *
import matplotlib
import sys

# In[2]:


table= Table.read_table('data1.csv')
table


# In[3]:


dataset_1 = pd.read_csv('data1.csv')
data_1 = pd.DataFrame(dataset_1,columns=['Commodity','Cost $','Supplier Performance Rating','Component Performance Rating']) 
data_1


# In[4]:


y_train = dataset_1['Supplier']
le2  = preprocessing.LabelEncoder()
y_train = le2.fit_transform(y_train)
y_train


# In[5]:


le  = preprocessing.LabelEncoder()
data_1['Commodity'] = le.fit_transform(data_1['Commodity'])
data_1



from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors=1, metric='minkowski', p=2)
classifier.fit(data_1, y_train)




def enter(a):
        b= le.transform(a)
        return b.item(0)
    
temp = sys.argv[1]
temp = enter([temp])
company = classifier.predict([[temp,15,10,10]]).item(0)
a=(le2.inverse_transform([company])).item(0)
print(a)


# In[20]:


# def conversion (arr[],n):
#     b= enter(n)
#     arr[]= arr[]

#type(b)


# In[7]:


# company = classifier.predict([[1,10,10,10]]).item(0)
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


# # In[8]:


# Supplier_rating= Table.read_table("HDD1.csv")
# Supplier_rating


# # In[9]:


# Supplier_rating.column('Time')


# # In[10]:


# #converting into standard units
# def standard_units(xyz):
#     return(xyz-np.mean(xyz))/np.std(xyz)


# # In[11]:


# Supplier_rating= Supplier_rating.with_columns('Normalization Time', standard_units(Supplier_rating.column('Time')), 'Normalization Finance', standard_units(Supplier_rating.column('Finance')), 'Normalization Quality', standard_units(Supplier_rating.column('Quality')))


# # In[12]:


# Supplier_rating


# # In[13]:


# Rating = make_array(10,6,6,8,7,5)
# Supplier_rating = Supplier_rating.with_column('Rating', Rating)
# Supplier_rating
    


# # In[14]:


# x= Supplier_rating.column('Normalization Time')+Supplier_rating.column('Normalization Finance')+Supplier_rating.column('Normalization Quality')


# # In[15]:


# Supplier_rating= Supplier_rating.with_column('x_val', x)


# # In[16]:


# Supplier_rating


# # In[17]:


# #predicting value of Rating given a particular x_value
# def predict_y(x_val):
#     nearby_points = Supplier_rating.where('x_val', are.between(x_val-1, x_val+1))
#     return np.mean((nearby_points.column('Time')+nearby_points.column('Finance')+nearby_points.column('Quality'))/3)


# # In[45]:


# y_train = Supplier_rating['Supplier']
# le2  = preprocessing.LabelEncoder()
# y_train = le2.fit_transform(y_train)
# y_train

# le  = preprocessing.LabelEncoder()
# Supplier_rating['Commodity'] = le.fit_transform(Supplier_rating['Commodity'])
# Supplier_rating


# # In[18]:


# predict_y(3)


# # In[19]:


# Supplier_rating= Supplier_rating.with_column('Predicted Rating', Supplier_rating.apply(predict_y, 'x_val'))


# # In[33]:


# Supplier_rating.sort("Predicted Rating", descending="True")


# # In[29]:


# j= make_array(1,1,2,3,4)
# pd.unique(j)


# # In[45]:


# k=pd.unique((Supplier_rating.sort("Predicted Rating", descending='TRUE').column("Predicted Rating")))

# s= make_array()
# s1= make_array()
# for i in np.arange(5):
#     Table1= Supplier_rating.where("Predicted Rating", are.equal_to(k.item(i))).take(1).column("Company")
#     Table2= Supplier_rating.where("Predicted Rating", are.equal_to(k.item(i))).take(1).column("Predicted Rating")
#     s= np.append(Table1, s)
#     s1= np.append(Table2, s1)
    
# Final_table= Table().with_columns("Name", s, "Predicted Rating", s1)
# Final_table


# # In[27]:


# Supplier_rating.scatter('x_val', 'Predicted Rating')


# # In[28]:


# def correlation(t,x,y):
#     x_standard= standard_units(t.column(x))
#     y_standard= standard_units(t.column(y))
#     return np.mean(x_standard*y_standard)


# # In[29]:


# def slope (t,x,y):
#     r= correlation(t,x,y)
#     y_sd= np.std(t.column(y))
#     x_sd= np.std(t.column(x))
#     return r*y_sd/x_sd


# # In[30]:


# def intercept(t,x,y):
#     x_mean= np.mean(t.column(x))
#     y_mean= np.mean(t.column(y))
#     return y_mean- slope(t,x,y)*x_mean


# # In[31]:


# data_correlation= correlation(Supplier_rating, 'x_val', 'Predicted Rating' )
# data_slope= slope(Supplier_rating, 'x_val', 'Predicted Rating')
# data_intercept= intercept(Supplier_rating, 'x_val', 'Predicted Rating')


# # In[32]:


# Supplier_rating1= Supplier_rating.select('Rating', 'x_val', 'Predicted Rating')


# # In[33]:


# Supplier_rating1= Supplier_rating1.with_column('Regression', data_slope*Supplier_rating1.column('x_val')+ data_intercept)
# Supplier_rating1


# # In[34]:


# Supplier_rating1.plot('x_val')


# # In[35]:


# predict_y(2)


# # In[ ]:





# # In[1]:


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


# # In[118]:


# rate(8,6,4)


# # In[116]:


# standard_units(Supplier_rating.column('Time'))


# # In[ ]:




