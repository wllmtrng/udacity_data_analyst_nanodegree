# 2_Prosper_Score_Distribution_Export_D3js.Rmd
William Truong  
August 24, 2016  



```r
knitr::opts_chunk$set(fig.width=12, fig.height=8, fig.path='figs/',
                      echo=TRUE, warning=FALSE, message=FALSE, fig.retina = 2)
library(data.table)
library(dplyr)
```

```
## -------------------------------------------------------------------------
```

```
## data.table + dplyr code now lives in dtplyr.
## Please library(dtplyr)!
```

```
## -------------------------------------------------------------------------
```

```
## 
## Attaching package: 'dplyr'
```

```
## The following objects are masked from 'package:data.table':
## 
##     between, last
```

```
## The following objects are masked from 'package:stats':
## 
##     filter, lag
```

```
## The following objects are masked from 'package:base':
## 
##     intersect, setdiff, setequal, union
```

```r
library(lubridate)
```

```
## 
## Attaching package: 'lubridate'
```

```
## The following objects are masked from 'package:data.table':
## 
##     hour, mday, month, quarter, wday, week, yday, year
```

```
## The following object is masked from 'package:base':
## 
##     date
```

```r
library(ggplot2)
library(scales)
library(gridExtra)
```

```
## 
## Attaching package: 'gridExtra'
```

```
## The following object is masked from 'package:dplyr':
## 
##     combine
```

```r
library(jsonlite)

load("./prosper_df.Rda")
df <- prosper_df
```

Find out what the top 10 professions in terms of amount are

```r
df.Occupation <- df %>% 
               group_by(Occupation) %>%
               summarise(count = n()) %>%
               ungroup() %>%
               arrange(desc(count))

df.Occupation
```

```
## # A tibble: 68 x 2
##                  Occupation count
##                       <chr> <int>
## 1                     Other 21122
## 2              Professional 10445
## 3                 Executive  3437
## 4       Computer Programmer  3200
## 5                   Teacher  2858
## 6                   Analyst  2711
## 7  Administrative Assistant  2697
## 8            Accountant/CPA  2550
## 9        Sales - Commission  2318
## 10            Skilled Labor  2157
## # ... with 58 more rows
```


```r
omit <- df.Occupation$Occupation != "Other" & df.Occupation$Occupation != "Professional" & df.Occupation$Occupation != "Unspecified"

occupations <- head(df.Occupation[omit,],10)$Occupation
```



```r
df.ProsperScore_Occupation <- df %>% 
                           group_by(ProsperScore, Occupation) %>%
                           summarise(count = n()) %>%
                           ungroup()

mask <- df.ProsperScore_Occupation$Occupation %in% occupations

jsonFile = toJSON(df.ProsperScore_Occupation[mask,], pretty=TRUE, auto_unbox=TRUE)
fileConn<-file("output.json")
writeLines(jsonFile, fileConn)
close(fileConn)
```
