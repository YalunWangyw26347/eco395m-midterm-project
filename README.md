# Hierarchy in US Faculty Hiring: Evidence from 2023-2021 Economics Ph.D. Placement 
<h3 align="center" id="heading"> 12 October 2023 <br> 
<em> Python, Big Data, and Databases (ECO395m)  </em> <br> <h3>
<h3 align="center" id="heading"> Yundi Xiao, Yalun Wang, Vimoli Mehta </h3>

<h3>Introduction </h3>
The "academic prestige chain" is a phenomenon that's long been observed in academia. It suggests that the prestige of the institution from which a candidate obtains their Ph.D. plays a significant role in their subsequent academic placement. Research consistently indicates that Ph.D. graduates from top-tier (often termed as "elite" or "Ivy League") institutions are more likely to secure faculty positions at similarly prestigious institutions.
This project is also inspired by the finding of the paper “Quantifying Hierarchy and Dynamics in US Faculty Hiring and Retention” -- "Faculty hiring networks in the United States exhibit a steep hierarchy in academia and across all domains and fields, with only 5–23% of faculty employed at universities more prestigious than their doctoral university.” We are interested in the "academic prestige chain" and whether faculty hiring in the Economics department in the U.S. established the same pattern — limited mobility between the tier of faculties’ Ph.D. school and academic placement. The project also aims to investigate if gender plays a role in Ph.D. hiring. 

<h3> Sources of Data </h3>

We refer to the U.S News(2022) ranking and tier for Economics PhD across the US. And we scraped data from the first 3 tiers of universities.The final list of universities scraped were:

Tier 1:

1.Harvard University

2.Stanford University

3.Princeton University

4.University of California, ​Berkeley

5.University of Chicago

6.Yale University

7.Northwestern University

8.Columbia University

9.University of Pennsylvania

10.New York University

Tier 2:

11.University of California, ​Los Angeles

12.Cornell University

13.University of Minnesota, Twin Cities

14.Duke University

15.University of California, ​San Diego

16.Brown University

Tier 3: 

17.Boston University

18.Boston College

19.University of Rochester

20.University of Virginia

21.Vanderbilt University

22.Washington University in St Louis

23.University of California, Davis

24.Pennsylvania State University, ​University Park

We scraped data from each university’s Ph.D. placement page, focusing on the student’s name, placement year, and placement. We cleaned the data set by dropping the observations with non-academic placement. We also add the gender variable by using Gender_Guesser. API, which generates the guessed gender from the name of each observation. 

<h3> Running the code </h3>
Our code will be executed in a Python environment and using packages specified in requirements.txt. You can install those packages we use in the project by using “pip install -r requirements.txt”. We have a sequence for running these .py files in the code folder. You can get the result we have by doing so: 

First, run “scrape.py” to get data from those universities’ URLs, the data will be in artifacts/rawplacement.csv

Second, run “wrangling. py”, this file will first combine two data sets together( the one is data we collect from the first step, the other one is two universities’ data that are not scrappable and we collect it by hand, and it is artifacts/Uchi PSU.csv), the combined data is artifacts/rawplacement_combined.csv, and then clean the data by dropping some data we do not need. Besides, we add the gender column by prediction and finally write it into artifact/cleaned_placement.csv.

Third, run “panda.py”, to define the Tier of School, and add Tier columns by classifying the sample’s school tier(including the school this individual is from and the school this individual is hired) and we will have an updated cleaned_placement.csv.

Finally, run “analysis_graph.py”, and we will get 3 pie charts in the analysis folder.

<h3> Limitations </h3> 
In this project, we have collected 24 universities’ (including school data from Tier 1, Tier 2, and Tier 3), this is not enough, since schools in Tier 4, and Tier5 are all also of high quality, and we only collect data from 2023 and 2022. Besides, when cleaning the data, we have errors for some specific samples. For example, there is a placement: “Korea Capital Market Institute, South Korea, (Research Fellow)”, since it has “Institute”, the code will include this sample in the cleaned_data. However, the number of error samples is not so big. Moreover, we only define Tier 1, Tier 2, and Tier 3 with universities in the US, so when classifying placement into Tiers, we will treat top schools outside the US into “Other Tier”. 
In addition, for the gender_guessing part: 

(1) we have universities that do not offer name information. For these data, we can not do the prediction.

 (2) the gender_guesser API has a limitation in that it only works smoothly with European names and American names. For Chinese names and names from other countries, it can not make a good prediction. 
 
 A further project can include: 

(1) collect data from more universities;

 (2) collect data from more years;

 (3) add more conditions for sifting the data we need;

(4) add top schools outside the US, when defining the Tiers; 

(5) using specific gender_guesser API for people with different features of name, or link Chat_GPT into this project to do the gender_guessing part if it can increase the accuracy of gender prediction. Also, delivering such a project with respect to another department will be meaningful, and we can make comparisons between departments in further study.

<h3> Methodology </h3> 
In this project, we scrape our Ph.D. placement data from the economics department. We have 4 variables which are year, school, student’s name, and placement to restore the information we need to analyze. For“placement” variable, varies a lot among universities, so we have to make a list of words we want (like a professor, university, and so on), and a list of words we do not want(like postdoc, because we do not want to include postdoc samples into analysis). Then filter placements that have words we want and don’t have words we do not want, and add those samples in cleaned data. In addition, using gender_guesser API to get gender information. Then, classify universities into different tiers and add columns carrying tier information in the data set, and the final data is [[university name, year, student name, placement, gender, school_tier,placement_tier ]... ...]
<h3> Results </h3> 

Regardless of gender, for PhDs from tier 1 universities, 15.1% of them are employed by tier 1 universities (as prestigious as their doctoral university);  6.3%  of them are employed by tier 2 universities; and 2.4% of them are employed by tier 3 universities; 76.2% of them are employed by universities other than tier 1-3 universities. 

Similarly, for PhDs from tier 2 universities, 3.6% of them are employed by tier 1 universities;  5.4%  of them are employed by tier 2 universities (as prestigious as their doctoral university); and 3.6% of them are employed by tier 3 universities; 87.5% of them are employed by universities other than tier 1-3 universities.

For PhDs from tier 3 universities, 4% of them are employed by tier 1 universities (as prestigious as their doctoral university);  1.6%  of them are employed by tier 2 universities; and 4% of them are employed by tier 3 universities(as prestigious as their doctoral university); 90.5% of them are employed by universities other than tier 1-3 universities.

![image text](./analysis/overall_tier_distribution.png)

In regard to gender, we analyzed the observations that have the gender information (Generated from GuessGender API). For male PhDs, we have 97 male candidates and 18% i.e. 17 males were hired for Tier-1 placements. 9.09 % of the male PhDs are employed in Tier-2 and Tier-3 universities.

![image text](./analysis/male_tier_distribution.png)

Similarly, we were able to identify 35 females out of which 10 ( 30%) female PhDs were employed by tier-one universities. 7.69% of females secured placements in Tier-2 and Tier-3 each which is less in comparison to the male ratio.

![image text](./analysis/female_tier_distribution.png)

<h3> Conclusion </h3> 
Our results suggests that Ph.D. students from tier 1 universities are more likely to be hired by tier 1 universities. This result corresponds to the former literature that only 5–23% of faculty are employed at universities more prestigious than their doctoral university. In regard to gender, since the sample size of a female is much smaller the results did not establish the gender effect such that female PhDs are more likely to be higher by top-tier universities. The mobility between doctoral and placement universities and its potential gender bias remains an area that warrants further investigation. A larger and more diverse sample size would be crucial to draw more definitive conclusions regarding the role of gender in U.S. faculty hiring.
