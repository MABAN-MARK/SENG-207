#!/usr/bin/env python
# coding: utf-8

# ### MABAN KWAME MARK
# ### 10990509
# ### Biomedical Engineering
# ### Project 1
# 

# In[99]:


import pandas  as pd
import seaborn as sns
import matplotlib.pyplot as plt


import numpy as np
from sklearn.linear_model import LinearRegression


# In[100]:


df = pd.read_csv('data.csv')
df





# ### Getting some information on the various parameters within the data
# 

# In[101]:


df.info()


# ### frow the info data , there are some missing  data values that must be fixed 

# In[102]:


df.tail()


# In[103]:


df.describe()


# In[104]:


df.shape


# In[105]:


z=df.duplicated()



# In[106]:


z


# ### From  the above information , some of the columns have missing  values and hence must be filled
# ### To fix the dataset first we must use either the mean , mode or median to  fill in the empty slot(s) with the specific columns. 

# In[107]:


df.info()


# ### columns with missing data  quality , pH , total sulfur dioxide , free sulfur dioxide,chlorides, density ,citric acid  and fixed acidity          
# 

# ### Using the mean approach 

# ##### Mean of  fixed acidity as mean_fa
# 

# In[108]:


mean_fa = df["fixed acidity"].mean()
mean_fa


# ##### mean of citric acid as mean_ca

# In[109]:


mean_ca= df["citric acid"].mean()


# In[110]:


mean_ca


# ##### mean of  Chlorides as mean_c

# In[111]:


mean_c=df['chlorides'].mean()


# In[112]:


mean_c


# ###### mean of  free sulfur dioxide as mean_fds

# In[113]:


mean_fds=df["free sulfur dioxide"].mean()


# In[114]:


mean_fds


# ##### mean of total sulfur dioxide as  mean_tsd

# In[115]:


mean_tsd=df["total sulfur dioxide"].mean()


# In[116]:


mean_tsd


# ##### mean of density as mean_d

# In[117]:


mean_d=df['density'].mean()


# In[118]:


mean_d


# ##### Mean of pH as mean_pH

# In[119]:


mean_pH=df['pH'].mean()


# In[120]:


mean_pH


# ##### Mean of quality as mean_Q

# In[121]:


mean_Q= df['quality'].mean()


# In[122]:


mean_Q


# In[123]:


df["pH"]



# In[124]:


df["total sulfur dioxide"]=df["total sulfur dioxide"].fillna(mean_tsd)
df["pH"]=df["pH"].fillna(mean_pH)
df["quality"]=df["quality"].fillna(mean_Q)
df["fixed acidity"]=df["fixed acidity"].fillna(mean_fa)
df["free sulfur dioxide"]=df["free sulfur dioxide"].fillna(mean_fds)
df["chlorides"]=df["chlorides"].fillna(mean_c)
df["citric acid"]=df["citric acid"].fillna(mean_ca)
df["density"]=df["density"].fillna(mean_d)



# In[125]:


df


# In[126]:


df.info()


# In[127]:


df.describe()


# In[128]:


sns.histplot(df.pH)


# In[129]:


mean_pH


# In[130]:


x= df.pH>mean_pH
x.value_counts()


# In[131]:


plt.pie(x.value_counts(), labels=x.value_counts())
plt.legend()


# In[132]:


q= df.quality>mean_Q
q.value_counts()

plt.pie(x.value_counts(), labels=q.value_counts())
plt.legend()


# In[133]:


mean_Q


# In[134]:


df['acidity'] = df['pH'] < 7
df['basic'] = df['pH'] > 7

pivot_table = df.pivot_table(index='pH', columns=['acidity', 'basic'], values='alcohol')


sns.heatmap(pivot_table, cmap='coolwarm')


# In[135]:


corr = df.corr()


sns.heatmap(corr, cmap='coolwarm', annot=True)
plt.title('Correlation Matrix')
plt.show()


# In[136]:


sns.scatterplot(x='quality', y='pH', data=df)
plt.show()


# In[137]:


X = df[['quality']]
y = df['pH']
model = LinearRegression()
model.fit(X, y)
print("Intercept:", model.intercept_)
print("Coefficient:", model.coef_)
plt.show()


# In[138]:


print("mean_Q:", np.mean(df['quality']))
print("Standard Deviation of pH:", np.std(df['pH']))
print("Correlation between quality and pH:", df['quality'].corr(df['pH']))


# ### Statistical inferences of individual columns in  the  dataset.

# #### For Wine Quality

# In[139]:


df['quality'].describe()



# #### For pH

# In[140]:


df['pH'].describe()


#   #### For alcoholic content of the wine  manufactured

# In[141]:


df['alcohol'].describe()


# #### for the fixed acidity of the  wine produced

# In[142]:


df['fixed acidity'].describe()


# #### for the volatile acidity of the wines

# In[143]:


df['volatile acidity'].describe()


#  #### For citric acid 

# In[144]:


df['citric acid'].describe()


# #### For Residual sugar

# In[145]:


df['residual sugar'].describe()


#  #### For Chlorides

# In[146]:


df['chlorides'].describe()


# ####  For Free Sulphur dioxide

# In[147]:


df['free sulfur dioxide'].describe()


# #### For Total Sulphur dioxide

# In[148]:


df['total sulfur dioxide'].describe()


# #### For Density

# In[149]:


df['density'].describe()


# #### For Sulphates

# In[150]:


df['sulphates'].describe()


# ##### the graph below show alcoholic content of the various wines  manufactured
# 

# In[151]:


sns.histplot(df.alcohol)


# ### CONSIDERING THE RESIDUAL SUGAR CONTENT OF THE WINES MANUFACTUREED

# In[152]:


mean_RS=df["residual sugar"].mean()
mean_RS
print("The mean residual sugar of the wines is {:.6f}.".format(mean_RS))


# In[153]:


R= df.alcohol>mean_RS
R.value_counts()



# In[154]:


mean_RS = df['residual sugar'].mean()
R = df['residual sugar'] > mean_RS
counts = R.value_counts()

plt.pie(counts, labels=['Above Mean', 'Below Mean'])

plt.title('Residual sugar Content Above/Below Mean')
plt.legend()
plt.show()


# In[155]:


df.isnull().any()


# In[ ]:




