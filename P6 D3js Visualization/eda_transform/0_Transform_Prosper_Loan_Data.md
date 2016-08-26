# 0_Transform_Prosper_Loan_Data

# Loan Data From Prosper
This data set contains 113,937 loans with 81 variables on each loan, including loan amount, borrower rate (or interest rate), current loan status, borrower income, and many others. Refer to the Resources and References section for the dataset.

Before running this Rmd file, download [prosperLoanData.csv](https://www.google.com/url?q=https://s3.amazonaws.com/udacity-hosted-downloads/ud651/prosperLoanData.csv&sa=D&ust=1472233880775000&usg=AFQjCNEtEszWeoeAr-uKZrDAjVcJLmZ0qw).

```r
prosper_df = read.csv("./prosperLoanData.csv", stringsAsFactors=FALSE)
summary(prosper_df)
```

```
##   ListingKey        ListingNumber     ListingCreationDate
##  Length:113937      Min.   :      4   Length:113937      
##  Class :character   1st Qu.: 400919   Class :character   
##  Mode  :character   Median : 600554   Mode  :character   
##                     Mean   : 627886                      
##                     3rd Qu.: 892634                      
##                     Max.   :1255725                      
##                                                          
##  CreditGrade             Term        LoanStatus         ClosedDate       
##  Length:113937      Min.   :12.00   Length:113937      Length:113937     
##  Class :character   1st Qu.:36.00   Class :character   Class :character  
##  Mode  :character   Median :36.00   Mode  :character   Mode  :character  
##                     Mean   :40.83                                        
##                     3rd Qu.:36.00                                        
##                     Max.   :60.00                                        
##                                                                          
##   BorrowerAPR       BorrowerRate     LenderYield     
##  Min.   :0.00653   Min.   :0.0000   Min.   :-0.0100  
##  1st Qu.:0.15629   1st Qu.:0.1340   1st Qu.: 0.1242  
##  Median :0.20976   Median :0.1840   Median : 0.1730  
##  Mean   :0.21883   Mean   :0.1928   Mean   : 0.1827  
##  3rd Qu.:0.28381   3rd Qu.:0.2500   3rd Qu.: 0.2400  
##  Max.   :0.51229   Max.   :0.4975   Max.   : 0.4925  
##  NA's   :25                                          
##  EstimatedEffectiveYield EstimatedLoss   EstimatedReturn 
##  Min.   :-0.183          Min.   :0.005   Min.   :-0.183  
##  1st Qu.: 0.116          1st Qu.:0.042   1st Qu.: 0.074  
##  Median : 0.162          Median :0.072   Median : 0.092  
##  Mean   : 0.169          Mean   :0.080   Mean   : 0.096  
##  3rd Qu.: 0.224          3rd Qu.:0.112   3rd Qu.: 0.117  
##  Max.   : 0.320          Max.   :0.366   Max.   : 0.284  
##  NA's   :29084           NA's   :29084   NA's   :29084   
##  ProsperRating..numeric. ProsperRating..Alpha.  ProsperScore  
##  Min.   :1.000           Length:113937         Min.   : 1.00  
##  1st Qu.:3.000           Class :character      1st Qu.: 4.00  
##  Median :4.000           Mode  :character      Median : 6.00  
##  Mean   :4.072                                 Mean   : 5.95  
##  3rd Qu.:5.000                                 3rd Qu.: 8.00  
##  Max.   :7.000                                 Max.   :11.00  
##  NA's   :29084                                 NA's   :29084  
##  ListingCategory..numeric. BorrowerState       Occupation       
##  Min.   : 0.000            Length:113937      Length:113937     
##  1st Qu.: 1.000            Class :character   Class :character  
##  Median : 1.000            Mode  :character   Mode  :character  
##  Mean   : 2.774                                                 
##  3rd Qu.: 3.000                                                 
##  Max.   :20.000                                                 
##                                                                 
##  EmploymentStatus   EmploymentStatusDuration IsBorrowerHomeowner
##  Length:113937      Min.   :  0.00           Length:113937      
##  Class :character   1st Qu.: 26.00           Class :character   
##  Mode  :character   Median : 67.00           Mode  :character   
##                     Mean   : 96.07                              
##                     3rd Qu.:137.00                              
##                     Max.   :755.00                              
##                     NA's   :7625                                
##  CurrentlyInGroup     GroupKey         DateCreditPulled  
##  Length:113937      Length:113937      Length:113937     
##  Class :character   Class :character   Class :character  
##  Mode  :character   Mode  :character   Mode  :character  
##                                                          
##                                                          
##                                                          
##                                                          
##  CreditScoreRangeLower CreditScoreRangeUpper FirstRecordedCreditLine
##  Min.   :  0.0         Min.   : 19.0         Length:113937          
##  1st Qu.:660.0         1st Qu.:679.0         Class :character       
##  Median :680.0         Median :699.0         Mode  :character       
##  Mean   :685.6         Mean   :704.6                                
##  3rd Qu.:720.0         3rd Qu.:739.0                                
##  Max.   :880.0         Max.   :899.0                                
##  NA's   :591           NA's   :591                                  
##  CurrentCreditLines OpenCreditLines TotalCreditLinespast7years
##  Min.   : 0.00      Min.   : 0.00   Min.   :  2.00            
##  1st Qu.: 7.00      1st Qu.: 6.00   1st Qu.: 17.00            
##  Median :10.00      Median : 9.00   Median : 25.00            
##  Mean   :10.32      Mean   : 9.26   Mean   : 26.75            
##  3rd Qu.:13.00      3rd Qu.:12.00   3rd Qu.: 35.00            
##  Max.   :59.00      Max.   :54.00   Max.   :136.00            
##  NA's   :7604       NA's   :7604    NA's   :697               
##  OpenRevolvingAccounts OpenRevolvingMonthlyPayment InquiriesLast6Months
##  Min.   : 0.00         Min.   :    0.0             Min.   :  0.000     
##  1st Qu.: 4.00         1st Qu.:  114.0             1st Qu.:  0.000     
##  Median : 6.00         Median :  271.0             Median :  1.000     
##  Mean   : 6.97         Mean   :  398.3             Mean   :  1.435     
##  3rd Qu.: 9.00         3rd Qu.:  525.0             3rd Qu.:  2.000     
##  Max.   :51.00         Max.   :14985.0             Max.   :105.000     
##                                                    NA's   :697         
##  TotalInquiries    CurrentDelinquencies AmountDelinquent  
##  Min.   :  0.000   Min.   : 0.0000      Min.   :     0.0  
##  1st Qu.:  2.000   1st Qu.: 0.0000      1st Qu.:     0.0  
##  Median :  4.000   Median : 0.0000      Median :     0.0  
##  Mean   :  5.584   Mean   : 0.5921      Mean   :   984.5  
##  3rd Qu.:  7.000   3rd Qu.: 0.0000      3rd Qu.:     0.0  
##  Max.   :379.000   Max.   :83.0000      Max.   :463881.0  
##  NA's   :1159      NA's   :697          NA's   :7622      
##  DelinquenciesLast7Years PublicRecordsLast10Years
##  Min.   : 0.000          Min.   : 0.0000         
##  1st Qu.: 0.000          1st Qu.: 0.0000         
##  Median : 0.000          Median : 0.0000         
##  Mean   : 4.155          Mean   : 0.3126         
##  3rd Qu.: 3.000          3rd Qu.: 0.0000         
##  Max.   :99.000          Max.   :38.0000         
##  NA's   :990             NA's   :697             
##  PublicRecordsLast12Months RevolvingCreditBalance BankcardUtilization
##  Min.   : 0.000            Min.   :      0        Min.   :0.000      
##  1st Qu.: 0.000            1st Qu.:   3121        1st Qu.:0.310      
##  Median : 0.000            Median :   8549        Median :0.600      
##  Mean   : 0.015            Mean   :  17599        Mean   :0.561      
##  3rd Qu.: 0.000            3rd Qu.:  19521        3rd Qu.:0.840      
##  Max.   :20.000            Max.   :1435667        Max.   :5.950      
##  NA's   :7604              NA's   :7604           NA's   :7604       
##  AvailableBankcardCredit  TotalTrades    
##  Min.   :     0          Min.   :  0.00  
##  1st Qu.:   880          1st Qu.: 15.00  
##  Median :  4100          Median : 22.00  
##  Mean   : 11210          Mean   : 23.23  
##  3rd Qu.: 13180          3rd Qu.: 30.00  
##  Max.   :646285          Max.   :126.00  
##  NA's   :7544            NA's   :7544    
##  TradesNeverDelinquent..percentage. TradesOpenedLast6Months
##  Min.   :0.000                      Min.   : 0.000         
##  1st Qu.:0.820                      1st Qu.: 0.000         
##  Median :0.940                      Median : 0.000         
##  Mean   :0.886                      Mean   : 0.802         
##  3rd Qu.:1.000                      3rd Qu.: 1.000         
##  Max.   :1.000                      Max.   :20.000         
##  NA's   :7544                       NA's   :7544           
##  DebtToIncomeRatio IncomeRange        IncomeVerifiable  
##  Min.   : 0.000    Length:113937      Length:113937     
##  1st Qu.: 0.140    Class :character   Class :character  
##  Median : 0.220    Mode  :character   Mode  :character  
##  Mean   : 0.276                                         
##  3rd Qu.: 0.320                                         
##  Max.   :10.010                                         
##  NA's   :8554                                           
##  StatedMonthlyIncome   LoanKey          TotalProsperLoans
##  Min.   :      0     Length:113937      Min.   :0.00     
##  1st Qu.:   3200     Class :character   1st Qu.:1.00     
##  Median :   4667     Mode  :character   Median :1.00     
##  Mean   :   5608                        Mean   :1.42     
##  3rd Qu.:   6825                        3rd Qu.:2.00     
##  Max.   :1750003                        Max.   :8.00     
##                                         NA's   :91852    
##  TotalProsperPaymentsBilled OnTimeProsperPayments
##  Min.   :  0.00             Min.   :  0.00       
##  1st Qu.:  9.00             1st Qu.:  9.00       
##  Median : 16.00             Median : 15.00       
##  Mean   : 22.93             Mean   : 22.27       
##  3rd Qu.: 33.00             3rd Qu.: 32.00       
##  Max.   :141.00             Max.   :141.00       
##  NA's   :91852              NA's   :91852        
##  ProsperPaymentsLessThanOneMonthLate ProsperPaymentsOneMonthPlusLate
##  Min.   : 0.00                       Min.   : 0.00                  
##  1st Qu.: 0.00                       1st Qu.: 0.00                  
##  Median : 0.00                       Median : 0.00                  
##  Mean   : 0.61                       Mean   : 0.05                  
##  3rd Qu.: 0.00                       3rd Qu.: 0.00                  
##  Max.   :42.00                       Max.   :21.00                  
##  NA's   :91852                       NA's   :91852                  
##  ProsperPrincipalBorrowed ProsperPrincipalOutstanding
##  Min.   :    0            Min.   :    0              
##  1st Qu.: 3500            1st Qu.:    0              
##  Median : 6000            Median : 1627              
##  Mean   : 8472            Mean   : 2930              
##  3rd Qu.:11000            3rd Qu.: 4127              
##  Max.   :72499            Max.   :23451              
##  NA's   :91852            NA's   :91852              
##  ScorexChangeAtTimeOfListing LoanCurrentDaysDelinquent
##  Min.   :-209.00             Min.   :   0.0           
##  1st Qu.: -35.00             1st Qu.:   0.0           
##  Median :  -3.00             Median :   0.0           
##  Mean   :  -3.22             Mean   : 152.8           
##  3rd Qu.:  25.00             3rd Qu.:   0.0           
##  Max.   : 286.00             Max.   :2704.0           
##  NA's   :95009                                        
##  LoanFirstDefaultedCycleNumber LoanMonthsSinceOrigination   LoanNumber    
##  Min.   : 0.00                 Min.   :  0.0              Min.   :     1  
##  1st Qu.: 9.00                 1st Qu.:  6.0              1st Qu.: 37332  
##  Median :14.00                 Median : 21.0              Median : 68599  
##  Mean   :16.27                 Mean   : 31.9              Mean   : 69444  
##  3rd Qu.:22.00                 3rd Qu.: 65.0              3rd Qu.:101901  
##  Max.   :44.00                 Max.   :100.0              Max.   :136486  
##  NA's   :96985                                                            
##  LoanOriginalAmount LoanOriginationDate LoanOriginationQuarter
##  Min.   : 1000      Length:113937       Length:113937         
##  1st Qu.: 4000      Class :character    Class :character      
##  Median : 6500      Mode  :character    Mode  :character      
##  Mean   : 8337                                                
##  3rd Qu.:12000                                                
##  Max.   :35000                                                
##                                                               
##   MemberKey         MonthlyLoanPayment LP_CustomerPayments
##  Length:113937      Min.   :   0.0     Min.   :   -2.35   
##  Class :character   1st Qu.: 131.6     1st Qu.: 1005.76   
##  Mode  :character   Median : 217.7     Median : 2583.83   
##                     Mean   : 272.5     Mean   : 4183.08   
##                     3rd Qu.: 371.6     3rd Qu.: 5548.40   
##                     Max.   :2251.5     Max.   :40702.39   
##                                                           
##  LP_CustomerPrincipalPayments LP_InterestandFees LP_ServiceFees   
##  Min.   :    0.0              Min.   :   -2.35   Min.   :-664.87  
##  1st Qu.:  500.9              1st Qu.:  274.87   1st Qu.: -73.18  
##  Median : 1587.5              Median :  700.84   Median : -34.44  
##  Mean   : 3105.5              Mean   : 1077.54   Mean   : -54.73  
##  3rd Qu.: 4000.0              3rd Qu.: 1458.54   3rd Qu.: -13.92  
##  Max.   :35000.0              Max.   :15617.03   Max.   :  32.06  
##                                                                   
##  LP_CollectionFees  LP_GrossPrincipalLoss LP_NetPrincipalLoss
##  Min.   :-9274.75   Min.   :  -94.2       Min.   : -954.5    
##  1st Qu.:    0.00   1st Qu.:    0.0       1st Qu.:    0.0    
##  Median :    0.00   Median :    0.0       Median :    0.0    
##  Mean   :  -14.24   Mean   :  700.4       Mean   :  681.4    
##  3rd Qu.:    0.00   3rd Qu.:    0.0       3rd Qu.:    0.0    
##  Max.   :    0.00   Max.   :25000.0       Max.   :25000.0    
##                                                              
##  LP_NonPrincipalRecoverypayments PercentFunded    Recommendations   
##  Min.   :    0.00                Min.   :0.7000   Min.   : 0.00000  
##  1st Qu.:    0.00                1st Qu.:1.0000   1st Qu.: 0.00000  
##  Median :    0.00                Median :1.0000   Median : 0.00000  
##  Mean   :   25.14                Mean   :0.9986   Mean   : 0.04803  
##  3rd Qu.:    0.00                3rd Qu.:1.0000   3rd Qu.: 0.00000  
##  Max.   :21117.90                Max.   :1.0125   Max.   :39.00000  
##                                                                     
##  InvestmentFromFriendsCount InvestmentFromFriendsAmount   Investors      
##  Min.   : 0.00000           Min.   :    0.00            Min.   :   1.00  
##  1st Qu.: 0.00000           1st Qu.:    0.00            1st Qu.:   2.00  
##  Median : 0.00000           Median :    0.00            Median :  44.00  
##  Mean   : 0.02346           Mean   :   16.55            Mean   :  80.48  
##  3rd Qu.: 0.00000           3rd Qu.:    0.00            3rd Qu.: 115.00  
##  Max.   :33.00000           Max.   :25000.00            Max.   :1189.00  
## 
```


```r
str(prosper_df)
```

```
## 'data.frame':	113937 obs. of  81 variables:
##  $ ListingKey                         : chr  "1021339766868145413AB3B" "10273602499503308B223C1" "0EE9337825851032864889A" "0EF5356002482715299901A" ...
##  $ ListingNumber                      : int  193129 1209647 81716 658116 909464 1074836 750899 768193 1023355 1023355 ...
##  $ ListingCreationDate                : chr  "2007-08-26 19:09:29.263000000" "2014-02-27 08:28:07.900000000" "2007-01-05 15:00:47.090000000" "2012-10-22 11:02:35.010000000" ...
##  $ CreditGrade                        : chr  "C" "" "HR" "" ...
##  $ Term                               : int  36 36 36 36 36 60 36 36 36 36 ...
##  $ LoanStatus                         : chr  "Completed" "Current" "Completed" "Current" ...
##  $ ClosedDate                         : chr  "2009-08-14 00:00:00" "" "2009-12-17 00:00:00" "" ...
##  $ BorrowerAPR                        : num  0.165 0.12 0.283 0.125 0.246 ...
##  $ BorrowerRate                       : num  0.158 0.092 0.275 0.0974 0.2085 ...
##  $ LenderYield                        : num  0.138 0.082 0.24 0.0874 0.1985 ...
##  $ EstimatedEffectiveYield            : num  NA 0.0796 NA 0.0849 0.1832 ...
##  $ EstimatedLoss                      : num  NA 0.0249 NA 0.0249 0.0925 ...
##  $ EstimatedReturn                    : num  NA 0.0547 NA 0.06 0.0907 ...
##  $ ProsperRating..numeric.            : int  NA 6 NA 6 3 5 2 4 7 7 ...
##  $ ProsperRating..Alpha.              : chr  "" "A" "" "A" ...
##  $ ProsperScore                       : num  NA 7 NA 9 4 10 2 4 9 11 ...
##  $ ListingCategory..numeric.          : int  0 2 0 16 2 1 1 2 7 7 ...
##  $ BorrowerState                      : chr  "CO" "CO" "GA" "GA" ...
##  $ Occupation                         : chr  "Other" "Professional" "Other" "Skilled Labor" ...
##  $ EmploymentStatus                   : chr  "Self-employed" "Employed" "Not available" "Employed" ...
##  $ EmploymentStatusDuration           : int  2 44 NA 113 44 82 172 103 269 269 ...
##  $ IsBorrowerHomeowner                : chr  "True" "False" "False" "True" ...
##  $ CurrentlyInGroup                   : chr  "True" "False" "True" "False" ...
##  $ GroupKey                           : chr  "" "" "783C3371218786870A73D20" "" ...
##  $ DateCreditPulled                   : chr  "2007-08-26 18:41:46.780000000" "2014-02-27 08:28:14" "2007-01-02 14:09:10.060000000" "2012-10-22 11:02:32" ...
##  $ CreditScoreRangeLower              : int  640 680 480 800 680 740 680 700 820 820 ...
##  $ CreditScoreRangeUpper              : int  659 699 499 819 699 759 699 719 839 839 ...
##  $ FirstRecordedCreditLine            : chr  "2001-10-11 00:00:00" "1996-03-18 00:00:00" "2002-07-27 00:00:00" "1983-02-28 00:00:00" ...
##  $ CurrentCreditLines                 : int  5 14 NA 5 19 21 10 6 17 17 ...
##  $ OpenCreditLines                    : int  4 14 NA 5 19 17 7 6 16 16 ...
##  $ TotalCreditLinespast7years         : int  12 29 3 29 49 49 20 10 32 32 ...
##  $ OpenRevolvingAccounts              : int  1 13 0 7 6 13 6 5 12 12 ...
##  $ OpenRevolvingMonthlyPayment        : num  24 389 0 115 220 1410 214 101 219 219 ...
##  $ InquiriesLast6Months               : int  3 3 0 0 1 0 0 3 1 1 ...
##  $ TotalInquiries                     : num  3 5 1 1 9 2 0 16 6 6 ...
##  $ CurrentDelinquencies               : int  2 0 1 4 0 0 0 0 0 0 ...
##  $ AmountDelinquent                   : num  472 0 NA 10056 0 ...
##  $ DelinquenciesLast7Years            : int  4 0 0 14 0 0 0 0 0 0 ...
##  $ PublicRecordsLast10Years           : int  0 1 0 0 0 0 0 1 0 0 ...
##  $ PublicRecordsLast12Months          : int  0 0 NA 0 0 0 0 0 0 0 ...
##  $ RevolvingCreditBalance             : num  0 3989 NA 1444 6193 ...
##  $ BankcardUtilization                : num  0 0.21 NA 0.04 0.81 0.39 0.72 0.13 0.11 0.11 ...
##  $ AvailableBankcardCredit            : num  1500 10266 NA 30754 695 ...
##  $ TotalTrades                        : num  11 29 NA 26 39 47 16 10 29 29 ...
##  $ TradesNeverDelinquent..percentage. : num  0.81 1 NA 0.76 0.95 1 0.68 0.8 1 1 ...
##  $ TradesOpenedLast6Months            : num  0 2 NA 0 2 0 0 0 1 1 ...
##  $ DebtToIncomeRatio                  : num  0.17 0.18 0.06 0.15 0.26 0.36 0.27 0.24 0.25 0.25 ...
##  $ IncomeRange                        : chr  "$25,000-49,999" "$50,000-74,999" "Not displayed" "$25,000-49,999" ...
##  $ IncomeVerifiable                   : chr  "True" "True" "True" "True" ...
##  $ StatedMonthlyIncome                : num  3083 6125 2083 2875 9583 ...
##  $ LoanKey                            : chr  "E33A3400205839220442E84" "9E3B37071505919926B1D82" "6954337960046817851BCB2" "A0393664465886295619C51" ...
##  $ TotalProsperLoans                  : int  NA NA NA NA 1 NA NA NA NA NA ...
##  $ TotalProsperPaymentsBilled         : int  NA NA NA NA 11 NA NA NA NA NA ...
##  $ OnTimeProsperPayments              : int  NA NA NA NA 11 NA NA NA NA NA ...
##  $ ProsperPaymentsLessThanOneMonthLate: int  NA NA NA NA 0 NA NA NA NA NA ...
##  $ ProsperPaymentsOneMonthPlusLate    : int  NA NA NA NA 0 NA NA NA NA NA ...
##  $ ProsperPrincipalBorrowed           : num  NA NA NA NA 11000 NA NA NA NA NA ...
##  $ ProsperPrincipalOutstanding        : num  NA NA NA NA 9948 ...
##  $ ScorexChangeAtTimeOfListing        : int  NA NA NA NA NA NA NA NA NA NA ...
##  $ LoanCurrentDaysDelinquent          : int  0 0 0 0 0 0 0 0 0 0 ...
##  $ LoanFirstDefaultedCycleNumber      : int  NA NA NA NA NA NA NA NA NA NA ...
##  $ LoanMonthsSinceOrigination         : int  78 0 86 16 6 3 11 10 3 3 ...
##  $ LoanNumber                         : int  19141 134815 6466 77296 102670 123257 88353 90051 121268 121268 ...
##  $ LoanOriginalAmount                 : int  9425 10000 3001 10000 15000 15000 3000 10000 10000 10000 ...
##  $ LoanOriginationDate                : chr  "2007-09-12 00:00:00" "2014-03-03 00:00:00" "2007-01-17 00:00:00" "2012-11-01 00:00:00" ...
##  $ LoanOriginationQuarter             : chr  "Q3 2007" "Q1 2014" "Q1 2007" "Q4 2012" ...
##  $ MemberKey                          : chr  "1F3E3376408759268057EDA" "1D13370546739025387B2F4" "5F7033715035555618FA612" "9ADE356069835475068C6D2" ...
##  $ MonthlyLoanPayment                 : num  330 319 123 321 564 ...
##  $ LP_CustomerPayments                : num  11396 0 4187 5143 2820 ...
##  $ LP_CustomerPrincipalPayments       : num  9425 0 3001 4091 1563 ...
##  $ LP_InterestandFees                 : num  1971 0 1186 1052 1257 ...
##  $ LP_ServiceFees                     : num  -133.2 0 -24.2 -108 -60.3 ...
##  $ LP_CollectionFees                  : num  0 0 0 0 0 0 0 0 0 0 ...
##  $ LP_GrossPrincipalLoss              : num  0 0 0 0 0 0 0 0 0 0 ...
##  $ LP_NetPrincipalLoss                : num  0 0 0 0 0 0 0 0 0 0 ...
##  $ LP_NonPrincipalRecoverypayments    : num  0 0 0 0 0 0 0 0 0 0 ...
##  $ PercentFunded                      : num  1 1 1 1 1 1 1 1 1 1 ...
##  $ Recommendations                    : int  0 0 0 0 0 0 0 0 0 0 ...
##  $ InvestmentFromFriendsCount         : int  0 0 0 0 0 0 0 0 0 0 ...
##  $ InvestmentFromFriendsAmount        : num  0 0 0 0 0 0 0 0 0 0 ...
##  $ Investors                          : int  258 1 41 158 20 1 1 1 1 1 ...
```


```r
head(prosper_df, 10)
```

```
##                 ListingKey ListingNumber           ListingCreationDate
## 1  1021339766868145413AB3B        193129 2007-08-26 19:09:29.263000000
## 2  10273602499503308B223C1       1209647 2014-02-27 08:28:07.900000000
## 3  0EE9337825851032864889A         81716 2007-01-05 15:00:47.090000000
## 4  0EF5356002482715299901A        658116 2012-10-22 11:02:35.010000000
## 5  0F023589499656230C5E3E2        909464 2013-09-14 18:38:39.097000000
## 6  0F05359734824199381F61D       1074836 2013-12-14 08:26:37.093000000
## 7  0F0A3576754255009D63151        750899 2013-04-12 09:52:56.147000000
## 8  0F1035772717087366F9EA7        768193 2013-05-05 06:49:27.493000000
## 9  0F043596202561788EA13D5       1023355 2013-12-02 10:43:39.117000000
## 10 0F043596202561788EA13D5       1023355 2013-12-02 10:43:39.117000000
##    CreditGrade Term LoanStatus          ClosedDate BorrowerAPR
## 1            C   36  Completed 2009-08-14 00:00:00     0.16516
## 2                36    Current                         0.12016
## 3           HR   36  Completed 2009-12-17 00:00:00     0.28269
## 4                36    Current                         0.12528
## 5                36    Current                         0.24614
## 6                60    Current                         0.15425
## 7                36    Current                         0.31032
## 8                36    Current                         0.23939
## 9                36    Current                         0.07620
## 10               36    Current                         0.07620
##    BorrowerRate LenderYield EstimatedEffectiveYield EstimatedLoss
## 1        0.1580      0.1380                      NA            NA
## 2        0.0920      0.0820                 0.07960        0.0249
## 3        0.2750      0.2400                      NA            NA
## 4        0.0974      0.0874                 0.08490        0.0249
## 5        0.2085      0.1985                 0.18316        0.0925
## 6        0.1314      0.1214                 0.11567        0.0449
## 7        0.2712      0.2612                 0.23820        0.1275
## 8        0.2019      0.1919                 0.17830        0.0799
## 9        0.0629      0.0529                 0.05221        0.0099
## 10       0.0629      0.0529                 0.05221        0.0099
##    EstimatedReturn ProsperRating..numeric. ProsperRating..Alpha.
## 1               NA                      NA                      
## 2          0.05470                       6                     A
## 3               NA                      NA                      
## 4          0.06000                       6                     A
## 5          0.09066                       3                     D
## 6          0.07077                       5                     B
## 7          0.11070                       2                     E
## 8          0.09840                       4                     C
## 9          0.04231                       7                    AA
## 10         0.04231                       7                    AA
##    ProsperScore ListingCategory..numeric. BorrowerState     Occupation
## 1            NA                         0            CO          Other
## 2             7                         2            CO   Professional
## 3            NA                         0            GA          Other
## 4             9                        16            GA  Skilled Labor
## 5             4                         2            MN      Executive
## 6            10                         1            NM   Professional
## 7             2                         1            KS Sales - Retail
## 8             4                         2            CA        Laborer
## 9             9                         7            IL   Food Service
## 10           11                         7            IL   Food Service
##    EmploymentStatus EmploymentStatusDuration IsBorrowerHomeowner
## 1     Self-employed                        2                True
## 2          Employed                       44               False
## 3     Not available                       NA               False
## 4          Employed                      113                True
## 5          Employed                       44                True
## 6          Employed                       82                True
## 7          Employed                      172               False
## 8          Employed                      103               False
## 9          Employed                      269                True
## 10         Employed                      269                True
##    CurrentlyInGroup                GroupKey              DateCreditPulled
## 1              True                         2007-08-26 18:41:46.780000000
## 2             False                                   2014-02-27 08:28:14
## 3              True 783C3371218786870A73D20 2007-01-02 14:09:10.060000000
## 4             False                                   2012-10-22 11:02:32
## 5             False                                   2013-09-14 18:38:44
## 6             False                                   2013-12-14 08:26:40
## 7             False                                   2013-04-12 09:52:53
## 8             False                                   2013-05-05 06:49:25
## 9             False                                   2013-12-02 10:43:39
## 10            False                                   2013-12-02 10:43:39
##    CreditScoreRangeLower CreditScoreRangeUpper FirstRecordedCreditLine
## 1                    640                   659     2001-10-11 00:00:00
## 2                    680                   699     1996-03-18 00:00:00
## 3                    480                   499     2002-07-27 00:00:00
## 4                    800                   819     1983-02-28 00:00:00
## 5                    680                   699     2004-02-20 00:00:00
## 6                    740                   759     1973-03-01 00:00:00
## 7                    680                   699     2000-09-29 00:00:00
## 8                    700                   719     1999-02-25 00:00:00
## 9                    820                   839     1993-04-01 00:00:00
## 10                   820                   839     1993-04-01 00:00:00
##    CurrentCreditLines OpenCreditLines TotalCreditLinespast7years
## 1                   5               4                         12
## 2                  14              14                         29
## 3                  NA              NA                          3
## 4                   5               5                         29
## 5                  19              19                         49
## 6                  21              17                         49
## 7                  10               7                         20
## 8                   6               6                         10
## 9                  17              16                         32
## 10                 17              16                         32
##    OpenRevolvingAccounts OpenRevolvingMonthlyPayment InquiriesLast6Months
## 1                      1                          24                    3
## 2                     13                         389                    3
## 3                      0                           0                    0
## 4                      7                         115                    0
## 5                      6                         220                    1
## 6                     13                        1410                    0
## 7                      6                         214                    0
## 8                      5                         101                    3
## 9                     12                         219                    1
## 10                    12                         219                    1
##    TotalInquiries CurrentDelinquencies AmountDelinquent
## 1               3                    2              472
## 2               5                    0                0
## 3               1                    1               NA
## 4               1                    4            10056
## 5               9                    0                0
## 6               2                    0                0
## 7               0                    0                0
## 8              16                    0                0
## 9               6                    0                0
## 10              6                    0                0
##    DelinquenciesLast7Years PublicRecordsLast10Years
## 1                        4                        0
## 2                        0                        1
## 3                        0                        0
## 4                       14                        0
## 5                        0                        0
## 6                        0                        0
## 7                        0                        0
## 8                        0                        1
## 9                        0                        0
## 10                       0                        0
##    PublicRecordsLast12Months RevolvingCreditBalance BankcardUtilization
## 1                          0                      0                0.00
## 2                          0                   3989                0.21
## 3                         NA                     NA                  NA
## 4                          0                   1444                0.04
## 5                          0                   6193                0.81
## 6                          0                  62999                0.39
## 7                          0                   5812                0.72
## 8                          0                   1260                0.13
## 9                          0                   9906                0.11
## 10                         0                   9906                0.11
##    AvailableBankcardCredit TotalTrades TradesNeverDelinquent..percentage.
## 1                     1500          11                               0.81
## 2                    10266          29                               1.00
## 3                       NA          NA                                 NA
## 4                    30754          26                               0.76
## 5                      695          39                               0.95
## 6                    86509          47                               1.00
## 7                     1929          16                               0.68
## 8                     2181          10                               0.80
## 9                    77696          29                               1.00
## 10                   77696          29                               1.00
##    TradesOpenedLast6Months DebtToIncomeRatio    IncomeRange
## 1                        0              0.17 $25,000-49,999
## 2                        2              0.18 $50,000-74,999
## 3                       NA              0.06  Not displayed
## 4                        0              0.15 $25,000-49,999
## 5                        2              0.26      $100,000+
## 6                        0              0.36      $100,000+
## 7                        0              0.27 $25,000-49,999
## 8                        0              0.24 $25,000-49,999
## 9                        1              0.25 $25,000-49,999
## 10                       1              0.25 $25,000-49,999
##    IncomeVerifiable StatedMonthlyIncome                 LoanKey
## 1              True            3083.333 E33A3400205839220442E84
## 2              True            6125.000 9E3B37071505919926B1D82
## 3              True            2083.333 6954337960046817851BCB2
## 4              True            2875.000 A0393664465886295619C51
## 5              True            9583.333 A180369302188889200689E
## 6              True            8333.333 C3D63702273952547E79520
## 7              True            2083.333 CE963680102927767790520
## 8              True            3355.750 0C87368108902149313D53B
## 9              True            3333.333 02163700809231365A56A1C
## 10             True            3333.333 02163700809231365A56A1C
##    TotalProsperLoans TotalProsperPaymentsBilled OnTimeProsperPayments
## 1                 NA                         NA                    NA
## 2                 NA                         NA                    NA
## 3                 NA                         NA                    NA
## 4                 NA                         NA                    NA
## 5                  1                         11                    11
## 6                 NA                         NA                    NA
## 7                 NA                         NA                    NA
## 8                 NA                         NA                    NA
## 9                 NA                         NA                    NA
## 10                NA                         NA                    NA
##    ProsperPaymentsLessThanOneMonthLate ProsperPaymentsOneMonthPlusLate
## 1                                   NA                              NA
## 2                                   NA                              NA
## 3                                   NA                              NA
## 4                                   NA                              NA
## 5                                    0                               0
## 6                                   NA                              NA
## 7                                   NA                              NA
## 8                                   NA                              NA
## 9                                   NA                              NA
## 10                                  NA                              NA
##    ProsperPrincipalBorrowed ProsperPrincipalOutstanding
## 1                        NA                          NA
## 2                        NA                          NA
## 3                        NA                          NA
## 4                        NA                          NA
## 5                     11000                      9947.9
## 6                        NA                          NA
## 7                        NA                          NA
## 8                        NA                          NA
## 9                        NA                          NA
## 10                       NA                          NA
##    ScorexChangeAtTimeOfListing LoanCurrentDaysDelinquent
## 1                           NA                         0
## 2                           NA                         0
## 3                           NA                         0
## 4                           NA                         0
## 5                           NA                         0
## 6                           NA                         0
## 7                           NA                         0
## 8                           NA                         0
## 9                           NA                         0
## 10                          NA                         0
##    LoanFirstDefaultedCycleNumber LoanMonthsSinceOrigination LoanNumber
## 1                             NA                         78      19141
## 2                             NA                          0     134815
## 3                             NA                         86       6466
## 4                             NA                         16      77296
## 5                             NA                          6     102670
## 6                             NA                          3     123257
## 7                             NA                         11      88353
## 8                             NA                         10      90051
## 9                             NA                          3     121268
## 10                            NA                          3     121268
##    LoanOriginalAmount LoanOriginationDate LoanOriginationQuarter
## 1                9425 2007-09-12 00:00:00                Q3 2007
## 2               10000 2014-03-03 00:00:00                Q1 2014
## 3                3001 2007-01-17 00:00:00                Q1 2007
## 4               10000 2012-11-01 00:00:00                Q4 2012
## 5               15000 2013-09-20 00:00:00                Q3 2013
## 6               15000 2013-12-24 00:00:00                Q4 2013
## 7                3000 2013-04-18 00:00:00                Q2 2013
## 8               10000 2013-05-13 00:00:00                Q2 2013
## 9               10000 2013-12-12 00:00:00                Q4 2013
## 10              10000 2013-12-12 00:00:00                Q4 2013
##                  MemberKey MonthlyLoanPayment LP_CustomerPayments
## 1  1F3E3376408759268057EDA             330.43            11396.14
## 2  1D13370546739025387B2F4             318.93                0.00
## 3  5F7033715035555618FA612             123.32             4186.63
## 4  9ADE356069835475068C6D2             321.45             5143.20
## 5  36CE356043264555721F06C             563.97             2819.85
## 6  874A3701157341738DE458F             342.37              679.34
## 7  AA4535764146102879D5959             122.67             1226.70
## 8  737F347089545035681C074             372.60             3353.40
## 9  49A53699682291323D04D66             305.54              611.08
## 10 49A53699682291323D04D66             305.54              611.08
##    LP_CustomerPrincipalPayments LP_InterestandFees LP_ServiceFees
## 1                       9425.00            1971.14        -133.18
## 2                          0.00               0.00           0.00
## 3                       3001.00            1185.63         -24.20
## 4                       4091.09            1052.11        -108.01
## 5                       1563.22            1256.63         -60.27
## 6                        351.89             327.45         -25.33
## 7                        604.25             622.45         -22.95
## 8                       1955.89            1397.51         -69.21
## 9                        505.58             105.50         -16.77
## 10                       505.58             105.50         -16.77
##    LP_CollectionFees LP_GrossPrincipalLoss LP_NetPrincipalLoss
## 1                  0                     0                   0
## 2                  0                     0                   0
## 3                  0                     0                   0
## 4                  0                     0                   0
## 5                  0                     0                   0
## 6                  0                     0                   0
## 7                  0                     0                   0
## 8                  0                     0                   0
## 9                  0                     0                   0
## 10                 0                     0                   0
##    LP_NonPrincipalRecoverypayments PercentFunded Recommendations
## 1                                0             1               0
## 2                                0             1               0
## 3                                0             1               0
## 4                                0             1               0
## 5                                0             1               0
## 6                                0             1               0
## 7                                0             1               0
## 8                                0             1               0
## 9                                0             1               0
## 10                               0             1               0
##    InvestmentFromFriendsCount InvestmentFromFriendsAmount Investors
## 1                           0                           0       258
## 2                           0                           0         1
## 3                           0                           0        41
## 4                           0                           0       158
## 5                           0                           0        20
## 6                           0                           0         1
## 7                           0                           0         1
## 8                           0                           0         1
## 9                           0                           0         1
## 10                          0                           0         1
```
## Convert dates to datetime format


```r
date_variables<-c("ListingCreationDate","ClosedDate",    "DateCreditPulled","FirstRecordedCreditLine","LoanOriginationDate")

prosper_df[,date_variables] <-lapply(prosper_df[,date_variables], ymd_hms)
```

## Check For Duplicates and Remove

```r
# Remove duplicates since they represent a small proportion
duplicates <-prosper_df$ListingNumber[duplicated(prosper_df$ListingNumber)]
prosper_df <- prosper_df[!duplicated(prosper_df$ListingNumber),]
```

## Investigating Why Some Entries Don't Have a Prosper Score or Rating

```r
sum(prosper_df$ProsperRating..Alpha. != "")
```

```
## [1] 83982
```

```r
sum(!is.na(prosper_df$ProsperScore))
```

```
## [1] 83982
```

The reason for the missing prosper rating and scores is because Prosper rates operated on a variable rate model decided by the lenders and borrowers like Ebay. There was a relaunch in 2009 and Prosper switched to preset rates determined by borrower criteria.

From Wikipedia:

*Prosper has provided an increasing amount of information about prospective borrowers over time, while also making various changes to its credit policy. Prior to its 2008 'quiet period' and 2009 SEC registration, the company provided "Credit Grades" and other credit information about its prospective lenders. Following the SEC registration, the company created a new model that determined "Prosper Ratings" instead. Additionally, new prospective borrowers were required to have an FICO 8 credit score of at least 640, while returning borrowers only need a score of 600 to request a loan.*

### Remove Entries Without Prosper Scores

```r
prosper_df <- prosper_df[!is.na(prosper_df$ProsperScore),]
```

## Convert Columns into Categories

```r
setDT(prosper_df)
prosper_df[, ProsperRating..Alpha.:=factor(ProsperRating..Alpha.,
                                           levels=c('HR', 'E', 'D', 'C', 'B', 'A', 'AA'))]
prosper_df[, ProsperScore.factored:=factor(ProsperScore)]
```

## Convert Occupation Related Columns into Categories

```r
unique(prosper_df$Occupation)
```

```
##  [1] "Professional"                      
##  [2] "Skilled Labor"                     
##  [3] "Executive"                         
##  [4] "Sales - Retail"                    
##  [5] "Laborer"                           
##  [6] "Food Service"                      
##  [7] "Fireman"                           
##  [8] "Construction"                      
##  [9] "Computer Programmer"               
## [10] "Other"                             
## [11] "Sales - Commission"                
## [12] "Retail Management"                 
## [13] "Engineer - Mechanical"             
## [14] "Military Enlisted"                 
## [15] "Clerical"                          
## [16] ""                                  
## [17] "Teacher"                           
## [18] "Clergy"                            
## [19] "Attorney"                          
## [20] "Nurse (RN)"                        
## [21] "Accountant/CPA"                    
## [22] "Analyst"                           
## [23] "Investor"                          
## [24] "Flight Attendant"                  
## [25] "Nurse (LPN)"                       
## [26] "Military Officer"                  
## [27] "Truck Driver"                      
## [28] "Administrative Assistant"          
## [29] "Police Officer/Correction Officer" 
## [30] "Social Worker"                     
## [31] "Food Service Management"           
## [32] "Tradesman - Mechanic"              
## [33] "Medical Technician"                
## [34] "Professor"                         
## [35] "Postal Service"                    
## [36] "Waiter/Waitress"                   
## [37] "Civil Service"                     
## [38] "Pharmacist"                        
## [39] "Tradesman - Electrician"           
## [40] "Scientist"                         
## [41] "Dentist"                           
## [42] "Engineer - Electrical"             
## [43] "Architect"                         
## [44] "Landscaping"                       
## [45] "Bus Driver"                        
## [46] "Engineer - Chemical"               
## [47] "Doctor"                            
## [48] "Chemist"                           
## [49] "Teacher's Aide"                    
## [50] "Pilot - Private/Commercial"        
## [51] "Nurse's Aide"                      
## [52] "Religious"                         
## [53] "Homemaker"                         
## [54] "Realtor"                           
## [55] "Student - College Senior"          
## [56] "Principal"                         
## [57] "Psychologist"                      
## [58] "Biologist"                         
## [59] "Tradesman - Carpenter"             
## [60] "Judge"                             
## [61] "Car Dealer"                        
## [62] "Student - College Graduate Student"
## [63] "Student - College Freshman"        
## [64] "Student - College Junior"          
## [65] "Tradesman - Plumber"               
## [66] "Student - College Sophomore"       
## [67] "Student - Community College"       
## [68] "Student - Technical School"
```

```r
# Change "" to unspecified
prosper_df[Occupation=="", Occupation:="Unspecified"]
prosper_df[, Occupation.factored:=factor(Occupation)]
prosper_df[, EmploymentStatus:=factor(EmploymentStatus)]
levels(prosper_df$Occupation.factored)
```

```
##  [1] "Accountant/CPA"                    
##  [2] "Administrative Assistant"          
##  [3] "Analyst"                           
##  [4] "Architect"                         
##  [5] "Attorney"                          
##  [6] "Biologist"                         
##  [7] "Bus Driver"                        
##  [8] "Car Dealer"                        
##  [9] "Chemist"                           
## [10] "Civil Service"                     
## [11] "Clergy"                            
## [12] "Clerical"                          
## [13] "Computer Programmer"               
## [14] "Construction"                      
## [15] "Dentist"                           
## [16] "Doctor"                            
## [17] "Engineer - Chemical"               
## [18] "Engineer - Electrical"             
## [19] "Engineer - Mechanical"             
## [20] "Executive"                         
## [21] "Fireman"                           
## [22] "Flight Attendant"                  
## [23] "Food Service"                      
## [24] "Food Service Management"           
## [25] "Homemaker"                         
## [26] "Investor"                          
## [27] "Judge"                             
## [28] "Laborer"                           
## [29] "Landscaping"                       
## [30] "Medical Technician"                
## [31] "Military Enlisted"                 
## [32] "Military Officer"                  
## [33] "Nurse (LPN)"                       
## [34] "Nurse (RN)"                        
## [35] "Nurse's Aide"                      
## [36] "Other"                             
## [37] "Pharmacist"                        
## [38] "Pilot - Private/Commercial"        
## [39] "Police Officer/Correction Officer" 
## [40] "Postal Service"                    
## [41] "Principal"                         
## [42] "Professional"                      
## [43] "Professor"                         
## [44] "Psychologist"                      
## [45] "Realtor"                           
## [46] "Religious"                         
## [47] "Retail Management"                 
## [48] "Sales - Commission"                
## [49] "Sales - Retail"                    
## [50] "Scientist"                         
## [51] "Skilled Labor"                     
## [52] "Social Worker"                     
## [53] "Student - College Freshman"        
## [54] "Student - College Graduate Student"
## [55] "Student - College Junior"          
## [56] "Student - College Senior"          
## [57] "Student - College Sophomore"       
## [58] "Student - Community College"       
## [59] "Student - Technical School"        
## [60] "Teacher"                           
## [61] "Teacher's Aide"                    
## [62] "Tradesman - Carpenter"             
## [63] "Tradesman - Electrician"           
## [64] "Tradesman - Mechanic"              
## [65] "Tradesman - Plumber"               
## [66] "Truck Driver"                      
## [67] "Unspecified"                       
## [68] "Waiter/Waitress"
```


## Create Month Variable for Aggregations

```r
prosper_df[, ListingCreationMonth:=cut(prosper_df$ListingCreationDate, breaks="month")]
```


## Save

```r
save(prosper_df, file="prosper_df.Rda")
```

## Resources and References
- [Prosper Loan Data](https://www.google.com/url?q=https://s3.amazonaws.com/udacity-hosted-downloads/ud651/prosperLoanData.csv&sa=D&ust=1470535594989000&usg=AFQjCNFnP-1MaAOimLzkxa8Wjq5TC7Ez-Q)
- [Prosper Loan Data Dictionary](https://www.google.com/url?q=https://docs.google.com/spreadsheet/ccc?key%3D0AllIqIyvWZdadDd5NTlqZ1pBMHlsUjdrOTZHaVBuSlE%26usp%3Dsharing&sa=D&ust=1470535594992000&usg=AFQjCNE55Bq3n5BUUUUn6t_0QAQ7GxqkSA)
- [2009 Post Relaunch - Wikipedia](https://en.wikipedia.org/wiki/Prosper_Marketplace#2009_post_SEC_relaunch)
