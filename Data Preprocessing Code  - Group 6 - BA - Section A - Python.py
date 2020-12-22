#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# -*- coding: utf-8 -*-

import pandas as pd
import string
string.punctuation
import re
import nltk
# nltk.download('wordnet')
# nltk.download('punkt')
from nltk.tokenize import TweetTokenizer
from nltk.stem import WordNetLemmatizer
# from nltk.stem import SnowballStemmer
# from nltk.corpus import stopwords




def dataImport ():
    global df
    global data1
    data1 = pd.read_excel (r'I:\MBA_Second Year\Term 5\BA\Project\Tweets2.xlsx')# This path and text file varies with the system
    df= pd.DataFrame(data1, columns= ['text'])
    # print(df.head(10))
    
def remove_num_spchar(text):
    text_nonum = re.sub(r'\d+', '', text)
    text_nonum_nospchar = re.sub("([^\x00-\x7F])+"," ",text_nonum)
    text_nonum_nospchar_other=re.sub("http\S+"," ",text_nonum_nospchar)
    return text_nonum_nospchar_other

def remove_punctuation(text):
    global no_punct
    global words_wo_punct
    no_punct=[words for words in text if words not in string.punctuation]
    words_wo_punct=''.join(no_punct)
    return words_wo_punct


def tokenizer(text):
    tt= TweetTokenizer()
    text= tt.tokenize(text)
    return text

#Used the wordnet method
def lemmetizer(text):
    wordnet_lemmatizer = WordNetLemmatizer()
    text = [wordnet_lemmatizer.lemmatize(word) for word in text]
    return text

#Used only lemmetizer for now, either one should be used
#If stemmer is required, uncomment def stemmer(text) and import SnowballStemmer package
# comment lemmetizer(text) function
#Then change the functions accordingly below, after dataImport()

# def stemmer(text):
#     snowball_stemmer = SnowballStemmer('english')
#     text = [snowball_stemmer.stem(word) for word in text]
#     return text


def remove_stopwords(text):
    stopword = nltk.corpus.stopwords.words('english')
    text = [word for word in text if word not in stopword]
    return text
# # def final_remove(text):
#     outchar= 
    
    

dataImport()
df['text_nonum']=df['text'].apply(lambda x: remove_num_spchar(x) )
df['text_nonum_wopunct']=df['text_nonum'].apply(lambda x: remove_punctuation(x))
df['text_nonum_wopunct_tokenized']=df['text_nonum_wopunct'].apply(lambda x: tokenizer(x))
df['text_nonum_wopunct_tokenized_lemmetized']=df['text_nonum_wopunct_tokenized'].apply(lambda x: lemmetizer(x))
df['text_nonum_wopunct_tokenized_lemmetized_nostopwords']=df['text_nonum_wopunct_tokenized_lemmetized'].apply(lambda x: remove_stopwords(x))
print(df.head(10))
df.to_excel (r'I:\MBA_Second Year\Term 5\BA\Project\export_dataframe.xlsx', index = False, header=True)  
# Use the above function only to generate the file
#change the path 'I:\MBA_Second Year\Term 5\BA\Project\export_dataframe.xlsx' based on the requirements

# df['text_nonum_wopunct_tokenized_nostopwords_nospecialchar']=df['text_nonum_wopunct_tokenized_nostopwords'].apply(lambda x: remove_special_char(x))
# df['text_wo_punct']=df['text'].apply(lambda x: remove_punctuation(x))
# df['text_wo_punct_split']=df['text_wo_punct'].apply(lambda x: tokenize(x.lower()))
# df['text_wo_punct_split_wo_stopwords'] = df['text_wo_punct_split'].apply(lambda x: remove_stopwords(x))
# df['text_wo_punct_split_wo_stopwords_numbers'] = df['text_wo_punct_split_wo_stopwords'].apply(lambda x: remove_numbers(x))
# df.to_excel (r'I:\MBA_Second Year\Term 5\BA\Project\export_dataframe.xlsx', index = False, header=True)  
  

