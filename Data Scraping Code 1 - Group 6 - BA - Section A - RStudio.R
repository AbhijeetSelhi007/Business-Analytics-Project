options(max.print = 10000)

install.packages("rtweet")
library (rtweet)

install.packages("twitteR")
library("twitteR")

consumerKey <- 'xxxxxxxxxxxxxxxxxx'
consumerSecret <- 'xxxxxxxxxxxxxxxxxx'
accessToken <- 'xxxxxxxxxxxxxxxxxx'
accessTokenSecret <- 'xxxxxxxxxxxxxxxxxx'

setup_twitter_oauth(consumerKey,consumerSecret,accessToken,accessTokenSecret)
1

searchTwitter("Valentine's Day", n=1000, lang="en")

install.packages("ROAuth")
library("ROAuth")

setup_twitter_oauth(consumerKey,consumerSecret,accessToken,accessTokenSecret)

options(max.print=999999)

Tweets2 <-searchTwitter("Valentine's Day", n=10000, lang="en")
Tweets2

Valentine.df <- twListToDF(Tweets2)
Valentine.df


install.packages("writexl")
library("writexl")
write_xlsx(Valentine.df, "f:/Tweets2.xlsx")
  