library(dplyr)
library(ggplot2)
library(jsonlite)

load("./prosper_df.Rda")
df <- prosper_df

df.Occupation <- df %>% 
  group_by(Occupation) %>%
  summarise(count = n()) %>%
  ungroup() %>%
  arrange(desc(count))

omit <- df.Occupation$Occupation != "Other" & df.Occupation$Occupation != "Professional" & df.Occupation$Occupation != "Unspecified"

occupations <- head(df.Occupation[omit,],20)$Occupation

df.Occupation_score <- df %>% 
  group_by(Occupation, ProsperScore) %>%
  summarise(count = n()) %>%
  ungroup()

mask <- df.Occupation_score$Occupation %in% occupations

jsonFile = toJSON(df.Occupation_score[mask,], pretty=TRUE, auto_unbox=TRUE)
fileConn<-file("output.json")
writeLines(jsonFile, fileConn)
close(fileConn)