<h1 align="center" id="heading"> <span style="color:red"> <em> Title </span> </h1>
<h3 align="center" id="heading"> 12 October 2023 <br> 
<em> Python, Big Data, and Databases (ECO395m)  </em> <br> <h3>
<h3 align="center" id="heading"> Yundi Xiao, Yalun Wang, Vimoli Mehta </h3>

<h3> Introduction </h3>

<h3> Sources of Data </h3>

<h3> Running the code </h3>

<h3> Limitations </h3> 
<ol>
  <li>Proper Cleaning: While scraping, we realized that data provided by universities for their placement of PhD candidates differs widely. For example, UCSD (University of California - San Diego) directly displayed a candidate working at UT Austin LBJ School. This data was indeed valuable to us, but since the name of the school has been used as an acronym, it was difficult for us to find such acronyms while cleaning the scraped dataset. The cleaning code involves looking for keywords like "university" and "college," but it can't catch keywords like "UT" as it would be extremely specific.</li>
  <li>Imbalance of Dataset: This analysis could be improved by having an equal proportion of universities from different tiers. While we have a list of universities that can be categorized into Tier-1, Tier-2, and Tier-3, not all universities were scrapable. Also, from the list of Tier-1 universities, it might be possible that we have more PhD candidates pursuing the academic profession than the PhD candidates from Tier-2. This leads to an imbalance in the dataset and can lead to biased observations.</li>
  <li>Gender Detection and Prediction: For displaying the ratio of men and women candidates pursuing an academic profession, we used a Gender Detection library from Python to predict the gender based on names we scraped. The accuracy of the library is not going to be 100%, as there are many names that can be assigned to both genders.</li>
</ol>

<h3> Methodology </h3> 

<h3> Results </h3> 

<h3> Conclusion </h3> 
