#Install {rtweet} CRAN.
install.packages("rtweet")

#Load {rtweet}
library(rtweet)

## view rtweet's authorization vignette
vignette("auth", package = "rtweet")

## name of twitter app
app_name <- "mwk_twitter_app"

## copy and pasted *your* keys
consume_key = "OlSV6Hga9BRcuByA4ZUANlRdx"
consumer_secret = "eDsUTaxsxVPauQQdudSXQ13n43lWVtOEad41n3XmssPRDisxU5"

## create token
token <- create_token(app_name, consumer_key, consumer_secret)

## print token
token

## save token to home directory
path_to_token <- file.path(path.expand("~"), ".twitter_token.rds")
saveRDS(token, path_to_token)
## create env variable TWITTER_PAT (with path to saved token)
env_var <- paste0("TWITTER_PAT=", path_to_token)
## save as .Renviron file (or append if the file already exists)
cat(env_var, file = file.path(path.expand("~"), ".Renviron"), 
    fill = TRUE, append = TRUE)

## refresh .Renviron variables
readRenviron("~/.Renviron")

## search for tweets in english that are not retweets
valentinesday <- search_tweets("#valentine AND buying AND and", lang = "en", include_rts = FALSE, n = 10000)

# save to csv file
write.csv(valentinesday_df, "valentinesday.csv")