#!/usr/bin/env python
# coding: utf-8

# Attributes:
# 
# 1. BMI - (UW, NW, OW, OB)
#     Underweight: BMI less than 18.5
#     Normal weight: BMI between 18.5 and 24.9
#     Overweight: BMI between 25 and 29.9
#     Obese: BMI 30 or greater
# 2. Avg_hours_of_sleep - (1-10)
# 
# 3. No._of_Friends - (0-6) --> 6 friends indicates he/She can have more than 6 friends also
# 
# 4. Character_type - (0,1)
#     0-Introvert
#     1-Extrovert
# 5. Academic_score - (0-100)
# 
# 6. Stressed -(0,1)
#     0-Student_not_stressed
#     1-Student_stressed

# In[1]:


import random as rd
sleep = rd.choices(list(range(2,12)),k=100)
frnds = rd.choices(list(range(0,7)),k=100)


# In[ ]:





# In[2]:


data = {"sleep_hours":sleep,
       "friends":frnds}


# In[3]:


df = pd.DataFrame(data)


# In[4]:


df.sleep_hours.value_counts()


# In[5]:


df.friends.value_counts()


# In[6]:


character = []
for i in df.friends:
    if i>3:
        character.append(0)
    else:
        character.append(1)


# In[7]:


df['Nature'] = character


# In[8]:


df.Nature.value_counts()


# In[9]:


df


# In[10]:


bmi = rd.choices([12+ rd.random()*5,19 + rd.random()*5,25 + rd.random()*5,30 + rd.random()*5],k = 100)


# In[11]:


df['BMI'] = bmi


# In[12]:


score = rd.choices(range(35,100),k=100)


# In[13]:


df['Academic_score'] = score


# In[14]:


stress = []
for i in range(0,100):
    if df.friends.iloc[i]<3 and df.Academic_score.iloc[i]<75 and df.BMI.iloc[i]>30:
        stress.append(1)
    elif df.Nature.iloc[i] == 1 and df.Academic_score.iloc[i]>60 and 18 < df.BMI.iloc[i] <24:
        stress.append(0)
    elif df.sleep_hours.iloc[i]<5:
        stress.append(1)
    else: stress.append(0)


# In[15]:


df['stress'] = stress


# In[16]:


df


# In[17]:


df.to_csv("Student_stress.csv")


# In[ ]:





# In[18]:


#loading Data set
df1 = pd.read_csv("Student_stress.csv",index_col = 0) 


# In[19]:


df1


# In[28]:


df1.info()


# In[29]:


df1.describe()


# In[31]:


x = df1.drop('stress',axis = 1)
y = df1.stress


# In[33]:





# In[21]:


import seaborn as sns


# In[26]:


import matplotlib.pyplot as plt


# In[27]:


plt.figure(figsize = (14,8))
sns.heatmap(df1.corr(),annot = True)


# In[34]:


from sklearn.model_selection import train_test_split
trainx,testx,trainy,testy = train_test_split(x,y)


# In[35]:


from sklearn.svm import SVC
svc = SVC()


# In[36]:


svc.fit(trainx,trainy)


# In[37]:


y_pred = svc.predict(testx)


# In[41]:


from sklearn.metrics import classification_report,accuracy_score,confusion_matrix
sns.heatmap(confusion_matrix(testy,y_pred),annot = True)


# In[43]:


print(classification_report(testy,y_pred))


# In[44]:


accuracy_score(testy,y_pred)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




