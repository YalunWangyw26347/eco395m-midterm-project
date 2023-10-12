<h1 align="center" id="heading"> <span style="color:red"> <em> Hierarchy in US Faculty Hiring: </em> <br> Evidence from 2023-2021 Economics Ph.D. Placement </span> </h1>

# 12 October 2023 
# Python, Big Data, and Databases (ECO395m) 
# Yundi Xiao, Yalun Wang, Vimoli Mehta 

# Introduction 
This project is inspired by the finding of the paper “Quantifying Hierarchy and Dynamics in US Faculty Hiring and Retention” -- "Faculty hiring networks in the United States exhibit a steep hierarchy in academia and across all domains and fields, with only 5–23% of faculty employed at universities more prestigious than their doctoral university.” We are interested in whether faculty hiring in the Economics department in the U.S. established the same pattern — limited mobility between the tier of faculties’ Ph.D. school and academic placement. The project also aims to investigate if gender plays a role in Ph.D. hiring. 
<h3> Sources of Data </h3>
Sources of data include placement information from 24 top Economics departments across the US.  Ranking for the Economics PhD programs was obtained from US.News(2022), and we pick top 3 tiers of universities.The final list of universities considered were:

1.Harvard University

2.Stanford University

3.Princeton University

4.University of California—​Berkeley

5.University of Chicago

6.Yale University

7.Northwestern University

8.Columbia University

9.University of Pennsylvania

10.New York University

11.University of California—​Los Angeles

12.Cornell University

13.Boston_University

14.Boston_College

15.University_of_Rochester

16.University_of_Virginia

17.Vanderbilt_University

18.Washington_University_in_St_Louis

19.Duke University

20.Brown University

21.University of California—​Davis

22.University of Minnesota—​Twin Cities

23.University of California—​San Diego

24.Pennsylvania State University—​University Park

We only include part of the universities in the rank, and there can be a more comprehensive project by analyzing more universities.

From each university’s PhD placement page, information about student’s name, year they graduate, advisor’s name, dissertation name, placement etc. are shown. But we only pick student’s name, year they graduate and placement for analyzing. Besides, after scraping
Information we want and dropping some samples( those sample who do not worked as a professor after graduation), we also add the gender column by using Gender_Guesser. API, but it has some restrictions, and there can be improvements in further project.

<h3> Running the code </h3>
Our code will be executed in a Python environment and using packages specified in requirements.txt. You can install those packages we use in the project by using “pip install -r requirements.txt”. We have a sequence for running these .py files in the code folder.  You can get the result we have by doing so: 
First, run “scrape.py” to get rawdata from those universities’ url, the rawdata will be in artifacts/rawplacement.csv
Second, run “wrangling. py”, this file will first combine two data sets together( the one is rawdata we collect from first step, the other one is two universities’ data that are not scrappable and we collect it by hand, and it is artifacts/Uchi PSU.csv), the combined data is artifacts/rawplacement_combined.csv, and then clean the data by dropping some data we do not need. Besides, we add the gender column by prediction and finally write it into artifact/cleaned_placement.csv.
Third, run “panda.py”, to define the Tier of School, and adding Tier columns by classifying sample’s school tier(including the school he is from and the school he works for) and we will 
have a updated cleaned_placement.csv.
Forth, run “analysis.py”, and we will get analysis results in analysis folder.

<h3> Limitations </h3> 
<ol>
  <li>Proper Cleaning: While scraping, we realized that data provided by universities for their placement of PhD candidates differs widely. For example, UCSD (University of California - San Diego) directly displayed a candidate working at UT Austin LBJ School. This data was indeed valuable to us, but since the name of the school has been used as an acronym, it was difficult for us to find such acronyms while cleaning the scraped dataset. The cleaning code involves looking for keywords like "university" and "college," but it can't catch keywords like "UT" as it would be extremely specific.</li>
  <li>Imbalance of Dataset: This analysis could be improved by having an equal proportion of universities from different tiers. While we have a list of universities that can be categorized into Tier-1, Tier-2, and Tier-3, not all universities were scrapable. Also, from the list of Tier-1 universities, it might be possible that we have more PhD candidates pursuing the academic profession than the PhD candidates from Tier-2. This leads to an imbalance in the dataset and can lead to biased observations.</li>
  <li>Gender Detection and Prediction: For displaying the ratio of men and women candidates pursuing an academic profession, we used a Gender Detection library from Python to predict the gender based on names we scraped. The accuracy of the library is not going to be 100%, as there are many names that can be assigned to both genders.</li>
</ol>

In this project, we have collected 24 universities’ (including school data from Tier1, Tier2 and Tier3), this is not enough, since school in Tier4, Tier5 all also of high quality, and we only collect data from 2023 and 2022. Besides, when cleaning the data, we have error for some specific samples. For example, there is a placement :“Korea Capital Market Institute, South Korea, (Research Fellow)”, since it has “Institute” , code will include this sample to the cleaned_data. But the number of error samples is not so big. Moreover, we only define Tier1, Tier2, Tier3 with universities in the US, so when classifying placement into Tiers, we will treat top schools outside the US into “Other Tier”. In addition, for the gender_guessing part: (1) we have universities do not offer name information. For these data, we can not do the prediction. (2) the gender_guesser API has a limitation that it only work smoothly with European names and American names. For Chinese names and names from other countries, it can not make a good prediction. A further project can include: (1) collect data from more universities; (2) collect data from more years; (3) add more conditions for sifting the data we need; (4) add top schools outside the US, when defining the Tiers; (5) using specific gender_guesser API for people with different feature of name, or link Chat_GPT into this project to do the gender_guessing part if it can increase the accuracy of gender prediction.
Also, delivering such project with respect to other department will be also meaningful, and we can make comparison between departments in further study.

<h3> Methodology </h3> 
In this project, we scrape our Phd placement data from economics department. We have year, school_name, student’s name, placement, these 4 variables to restore information we need in analyze. For“placement” variable, it varies a lot among universities, so we have to make a list of words we want (like professor, university, and so on), and a list of words we do not want(like postdoc, because we do not want include postdoc samples into analysis). Then filter placements that have words we want and don’t have word we do not want, and add those samples in cleaned data. In addition, using gender_guesser API to get gender information. Then, classify universities into different tiers and add columns carrying tier information in data set, and the final data is [[university name, year, student name,placement, gender, school_tier,placement_tier ]... ...]
<h3> Results </h3> 

![image text](./analysis/overall_tier_distribution.png)

![image text](./analysis/female_tier_distribution.png)

![image text](./analysis/male_tier_distribution.png)
<h3> Conclusion </h3> 
