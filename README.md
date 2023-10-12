<h1 align="center" id="heading"> <span style="color:red"> <em> Title </span> </h1>
<h3 align="center" id="heading"> 12 October 2023 <br> 
<em> Python, Big Data, and Databases (ECO395m)  </em> <br> <h3>
<h3 align="center" id="heading"> Yundi Xiao, Yalun Wang, Vimoli Mehta </h3>

<h3> Introduction </h3>

<h3> Sources of Data </h3>

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


<h3> Conclusion </h3> 
