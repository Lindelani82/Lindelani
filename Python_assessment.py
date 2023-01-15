#!/usr/bin/env python
# coding: utf-8

# # python assessment by lindelani mathenjwa
# 

# In[ ]:


#question1
#Let us import an excel file from videos folder in computer so that we will convert it to csv file the start to work


# In[8]:





# In[2]:


import pandas as pd


# In[4]:


inputExcelFile=(r"C:\Users\Student\Videos\transaction11.xlsx")


# In[5]:


excelFile=pd.read_excel(inputExcelFile)


# In[7]:


excelFile.to_csv(r'C:\Users\Student\Videos\transaction.csv',index= None, header=True)


# In[6]:


dataframeObject=pd.DataFrame(pd.read_csv(r'C:\Users\Student\Videos\transaction.csv'))


# In[20]:


#dataframeObject


# In[164]:


#Still question1
#Here we are printing a summary for the whole Data


# In[22]:


summary=dataframeObject.describe()


# In[23]:


print(summary)


# In[24]:


#Question2
# we now creating a new column called CostPerTransaction


# In[25]:


dataframeObject["CostPerTransaction"]=dataframeObject["NumberOfItemsPurchased"]*dataframeObject["CostPerItem"]


# In[27]:





# In[28]:


#Question3
#we now creating a new column called SalesPerTransaction


# In[29]:


dataframeObject["SalesPerTransaction"]=dataframeObject["NumberOfItemsPurchased"]*dataframeObject["SellingPricePerItem"]


# In[ ]:





# In[31]:


#Question4
#We now Creating a new column called ProfitPerTransaction


# In[32]:


dataframeObject["ProfitPerTransaction"]=dataframeObject["SalesPerTransaction"]-dataframeObject["CostPerTransaction"]


# In[ ]:





# In[34]:


#Question5
#We now rounding ProfitPerTransaction to the nearest whole number


# In[35]:


new_ProfitPerTransaction=dataframeObject["ProfitPerTransaction"].round()


# In[36]:


dataframeObject["ProfitPerTransaction"]=new_ProfitPerTransaction


# In[ ]:





# In[38]:


#Question6
#we combining 3 columns Day,Month and Year to form one column called new_date


# In[39]:


dataframeObject["new_date"]=dataframeObject["Day"].astype(str)+ '-'+dataframeObject["Month"]+'-'+dataframeObject["Year"].astype(str)


# In[ ]:





# In[41]:


#Question7
#in the column of ItemDesctription we lowering letters to be lowecases


# In[43]:


dataframeObject["ItemDescription"]=dataframeObject["ItemDescription"].str.lower()


# In[ ]:





# In[45]:


#Question8
#we now spliting and expand the column ClientKeywords


# In[46]:


dataframeObject["ClientKeywords"].str.split(",",expand=True)


# In[48]:


#Still question 8
#Here i was appending the splited columns to the DataFrame


# In[58]:


dataframeObject[["0","1","2"]]=dataframeObject["ClientKeywords"].str.split(",",expand=True)


# In[59]:


dataframeObject


# In[57]:


#Still Question 8
#Then i decide to rename those columns with my own way


# In[64]:


dataframeObject["ClientAge"]=dataframeObject["0"]
dataframeObject["ClientType"]=dataframeObject["1"]
dataframeObject["LengthofContract"]=dataframeObject["2"]


# In[ ]:





# In[ ]:





# In[66]:


#Still Question8
#I then droped those columns that were created after spliting up becuase i already named new columns 


# In[67]:


dataframeObject.drop("0",axis=1,inplace=True)


# In[68]:


dataframeObject.drop("1",axis=1,inplace=True)


# In[69]:


dataframeObject.drop("2",axis=1,inplace=True)


# In[ ]:





# In[71]:


#Qustion9
#Then columnn ClientKeyword was droped


# In[72]:


dataframeObject.drop("ClientKeywords",axis=1,inplace=True)


# In[ ]:





# In[ ]:


#Still question 9 


# In[74]:


#we now cleaning after spliting up


# In[75]:


dataframeObject["ClientAge"]=dataframeObject["ClientAge"].str.replace("[","")
dataframeObject["ClientAge"]=dataframeObject["ClientAge"].str.replace("'","")


# In[76]:


dataframeObject["ClientType"]=dataframeObject["ClientAge"].str.replace("'","")


# In[77]:


dataframeObject["LengthofContract"]=dataframeObject["LengthofContract"].str.replace("]","")
dataframeObject["LengthofContract"]=dataframeObject["LengthofContract"].str.replace("'","")


# In[82]:


print(dataframeObject)
dataframeObject


# In[83]:


dataframeObject.to_csv((r"C:\Users\Student\Downloads\transaction.csv"),header=False,index=False)


# 

# In[ ]:





# In[ ]:





# In[ ]:





# In[15]:





# In[ ]:




