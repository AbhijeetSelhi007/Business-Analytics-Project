# install.packages("pacman")
library(pacman)
pacman::p_load(gdata,openxlsx,readxl, tibble, plyr, dplyr, arules, arulesViz, ggplot2)
setwd("C:\\Users\\Abhijeet\\Desktop")


tr <- read.transactions('tweetitems.csv', format = 'basket', sep=',')
tr
summary(tr)

itemFrequencyPlot(tr, topN=20, type='absolute')

rules <- apriori(tr, parameter = list(supp=0.01, conf=0.15))
rules <- sort(rules, by='confidence', decreasing = TRUE)
summary(rules)
inspect(rules[1:10])

rules <- apriori(tr, parameter = list(supp=0.015, conf=0.15))
rules <- sort(rules, by='confidence', decreasing = FALSE)
summary(rules)
inspect(rules[1:10])


topRules <- rules[1:10]
plot(topRules)
plot(rules)

plot(topRules, method="graph")
plot(rules, method = "graph")

plot(topRules, method = "grouped")


