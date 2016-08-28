
View at http://bl.ocks.org/wllmtrng/ff72bf455078448e5e40ece3bff15354

## Design 
As I was performing the initial exploratory data analysis on the Prosper Loan Dataset, I decided I wanted to do a bit
more exploration on background of people who seek to find loans. My initial thoughts were that people who weren't
credit worthy were more likely to use something like Prosper Loans. I also wondered if there are occupations who are, as
a group, more credit worthy than others.

I chose to use this [dashboard](http://bl.ocks.org/NPashaP/96447623ef4d342ee09b) type of visualization because:

1. Bar plots are useful in showing the difference in frequency among the Proser Scores.
2. The Pie Chart and Legend on the right is able to provide secondary distribution of Occupation for a selected Prosper Score.
3. The Pie Chart can show drastic differences between the distribution of Occupation for a certain Prosper Score.
4. The Legend complements the Pie Chart by showing differences between Occupations with higher resolution.

There are a total of 68 occupations recorded in the Prosper Loan Dataset. I took the top ten occupations by count for
my visualization. Originally amongst the top ten, there were occupations that weren't clear, so I omitted them and
replaced them with the next occupation.

After some feedback from my submission and reading an [article](http://www.businessinsider.com/pie-charts-are-the-worst-2013-6) which 
discourages the use of pie charts, I sought to change the visualization to remove the pie chart. I came across a [hierarchical bar chart](http://bl.ocks.org/mbostock/1283663)
example and thought it conveyed my story better.

## Feedback

### Ronald Truong

What I see right away is a bar plot showing the distribution of Prosper Scores from 1 - 11. I noticed that by 
hovering over the bars, the pie chart and legend changes to account for how the occupations listed make up
percentage wise for that score.

What I don't like is that there are two Occupation types that the data is skewed towards. Other and Professional
Occupations don't give much value. Although they are indeed the top 10 Occupation, I believe they should be removed.

It's interesting to see that Computer Programmers are very credit worthy occupations. They have a high prosper score on
average compared to all the other professions, besides Executive.

### t0mkaka

Forum Mentor

@wllmtrng

Hi William,

Great work with all the plot and data in sync. I was testing how fast the numbers can be changed :slight_smile:

I can notice that there are few borowwers for the lower end and upper end of the scores and most of the loans are from mid -level. The pie-chart on the right is also showing the values and I can see the distribution for a particular profession by hovering over the pies

    Is there something you don’t understand in the graphic?

I would suggest you work more on this. Your plots are great but to a person who does not know about loan data this is very confusing.

    Title - A title tells information we are going to see. An appropriate title helps in better understanding.
    Axis Labels - There is no labels on axis in your bar plots. As a person unaware of the data it took me some time to understand whats on x-axis and what is on y-axis.
    Pie-Chart - I am not so against pie-chart when they convey clear information (which is usually the case when there are only 2-3 sections) . You have 10 and it is very difficult to interpret percentage numbers from that. The numbers are on the table to the right but again, one has to check table then match color.

These are all my suggestions but number 1 and 2 will definitely improve the readability.

Will wait for your iterations. All the best.

include all feedback you received from others on your visualization from the first sketch to the final 
visualization

### Dai Ying Wu
The title could be changed to reflect a more targetted story you're trying to get across. I'm assuming you want to show
people what professions are most credit worthy. One thing you can do to demonstrate that more properly is to maybe sort the legend when a Prosper Score is highlighted.

The things I do notice is that the distribution amongs occupations is pretty even in the midrange prosper scores. In the
higher end executives, nurses, and programmers dominate. On the lower end, Teachers, Administrative Assistants, Executives, 
and Accountants take much of the proportion. It is ironic that for the Prosper Score of 1 that 13% of them are Accountants.

## Resources and References
- [Prosper Loan Data](https://www.google.com/url?q=https://s3.amazonaws.com/udacity-hosted-downloads/ud651/prosperLoanData.csv&sa=D&ust=1470535594989000&usg=AFQjCNFnP-1MaAOimLzkxa8Wjq5TC7Ez-Q)
- [Prosper Loan Data Dictionary](https://www.google.com/url?q=https://docs.google.com/spreadsheet/ccc?key%3D0AllIqIyvWZdadDd5NTlqZ1pBMHlsUjdrOTZHaVBuSlE%26usp%3Dsharing&sa=D&ust=1470535594992000&usg=AFQjCNE55Bq3n5BUUUUn6t_0QAQ7GxqkSA)
- [2009 Post Relaunch - Wikipedia](https://en.wikipedia.org/wiki/Prosper_Marketplace#2009_post_SEC_relaunch)
- [1st Feedback](https://discussions.udacity.com/t/propser-loans-feedback-request/185271)
- [D3 Axis and Titles](http://www.d3noob.org/2013/01/adding-title-to-your-d3js-graph.html)
- [D3 Dashboard Example](http://bl.ocks.org/NPashaP/96447623ef4d342ee09b)
- [D3 Chart Example](http://www.alexrothenberg.com/2014/01/06/learning-d3-by-building-a-chart.js.html)
- [Estimated Vs. Realized Returns Prosper](https://angel.co/projects/289416-expected-vs-realized-returns-for-prosper-loans?src=user_profile)
- [D3 Gallery](https://github.com/d3/d3/wiki/gallery)
- [Hierarchical Bar Chart](http://bl.ocks.org/mbostock/1283663)
- [Pie Charts Are The Worst](http://www.businessinsider.com/pie-charts-are-the-worst-2013-6)
