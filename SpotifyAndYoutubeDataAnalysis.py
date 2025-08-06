        #!/usr/bin/env python
        # coding: utf-8

        # In[1]:


        import pandas as pd
        import numpy as np
        import seaborn as sns
        import matplotlib.pyplot as plt
        get_ipython().run_line_magic('matplotlib', 'inline')


        # In[2]:


        data = pd.read_csv("Spotify Youtube Dataset.csv")


        # In[3]:


        data


        # In[4]:


        data.columns


        # In[5]:


        data.info()                   # to get some basic information about the datset


        # In[6]:


        # removing the columns from the dataframe

        data.drop(columns = ['Unnamed: 0', 'Url_spotify', 'Uri', 'Url_youtube'], inplace = True)


        # In[7]:


        data



        # In[8]:


        # checking missing values counts in each column of the dataframe

        data.isna().sum()


        # In[9]:


        # filling the missing values with 0 in Likes & Commnets column

        data['Likes'] =  data['Likes'].fillna(0)
        data['Comments'] = data['Comments'].fillna(0)


        # In[10]:


        data.isnull().sum()     # to check the count of missing values in each column


        # In[11]:


        data.dropna(inplace = True)               # It drops the rows that contains all or any missing values


        # In[12]:


        data.isnull().sum()     # to check the count of missing values in each column


        # In[13]:


        data.info()


        # # Q.1) Top 10 Artists - with the Highest Views on YouTube?

        # In[14]:


        data.head(2)


        # In[15]:


        Artist_grouped =  data.groupby('Artist')['Views'].sum()


        # In[16]:


        Artist_grouped


        # In[17]:


        Artist_sorted =  Artist_grouped.sort_values(ascending = False)


        # In[18]:


        Artist_sorted.head(10)


        # ## Q.2) Top 10 Tracks - with the Highest Streams on Spotify?

        # In[19]:


        data.head(1)


        # In[20]:


        x = data[['Track', 'Stream']]          # creating a new dataframe with 2 columns - Track & Stream

        x


        # In[21]:


        most_stream_track =  x.sort_values(by = ['Stream'], ascending=False).head(10) # sorting the dataframe wrt Stream column


        # In[22]:


        most_stream_track


        # ## Q.3) What are the most common Album Types on Spotify? How many tracks belong to each album type?

        # In[23]:


        data.head(1)


        # In[24]:


        data.Album_type.unique()              # to check the unique values in a column


        # In[25]:


        a_type =  data['Album_type'].value_counts()     # It shows all unique values with their counts in the column

        a_type


        # In[26]:


        # draw a Pie chart

        plt.pie( a_type, labels =  a_type.index, autopct = "‘%1.1f%%’", startangle= 60 , 
                colors= 'myr', shadow='True', explode = (0.05,0.05,0.05),  pctdistance = 0.75)

        plt.show()


        # ## Q.4) How do the Average Views, Likes, and Comments are compared between different Album Types?¶

        # In[27]:


        data.head(1)


        # In[28]:


        # group the Album Type column, and show the mean of three columns

        df = data.groupby('Album_type')[['Likes', 'Views', 'Comments']].mean()

        df


        # In[29]:


        type(df)


        # In[30]:


        df = df.reset_index()                # rest_index - To convert the index of a Series into a column to form a DataFrame

        df


        # In[31]:


        # melt - unpivot a dataframe

        df_melted  = pd.melt( df, id_vars = 'Album_type', var_name = "Attribute", value_name = 'Total' )

        df_melted


        # In[32]:


        # Draw the Bar Plot

        plt.figure(figsize = (9,4))

        sns.barplot( x = 'Album_type', y = 'Total', hue = 'Attribute', data = df_melted );


        # ### Q.5) Top 5 YouTube Channels - based on the Views?¶

        # In[33]:


        c_views = data.groupby('Channel')['Views'].sum().sort_values(ascending=False).head()

        c_views


        # In[34]:


        c_views = c_views.reset_index()

        c_views.head(10)


        # In[35]:


        type(c_views)


        # In[36]:


        # sns.set_style("whitegrid")

        sns.barplot( x = "Views", y = "Channel", data = c_views, color='black')
        plt.title('Top 5 Channels by Views')
        plt.xlabel('Views')
        plt.ylabel('Channel')
        plt.show()


        # ## Q.6) The Top Most Track - based on Views?

        # In[37]:


        data.sort_values( by = 'Views', ascending = False).head(1)


        # ## Q.7) Which Top 7 Tracks have the highest Like-to-View ratio on YouTube?

        # In[38]:


        track_lv = data[['Track', 'Likes', 'Views']]

        track_lv


        # In[39]:


        track_lv.insert(3, 'LV_Ratio', data['Likes']/data['Views'] )


        # In[40]:


        track_lv


        # In[41]:


        track_lv.sort_values( by = 'LV_Ratio', ascending = False).head(7)


        # Q.8) Top Albums having the Tracks with Maximum Danceability ?

        # In[42]:


        # creating groups for each Album

        T_danceability =  data.groupby('Album')['Danceability'].sum().sort_values(ascending=False)

        T_danceability


        # In[43]:


        data[data.Album == 'Greatest Hits']          # filtering the dataframe with 'Greatest Hits'


        # ## Q.9) What is the Correlation between Views, Likes, Comments, and Stream?

        # In[44]:


        # creating a new dataframe with 4 columns

        df_vlcs = data[['Views', 'Likes', 'Comments', 'Stream']] 

        df_vlcs


        # In[45]:


        df_vlcs.corr()                      # correlation matrix for the required columns


        # In[46]:


        sns.heatmap(df_vlcs.corr())            # drawing a heatmap for the correlation matrix


        # In[ ]:




