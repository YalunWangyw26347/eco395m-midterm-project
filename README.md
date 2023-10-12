<h1 align="center" id="heading"> <span style="color:red"> <em> Title </span> </h1>
<h3 align="center" id="heading"> 12 October 2023 <br> 
<em> Python, Big Data, and Databases (ECO395m)  </em> <br> <h3>
<h3 align="center" id="heading"> Yundi Xiao, Yalun Wang, Vimoli Mehta </h3>

<h3> Introduction </h3>

<h3> Sources of Data </h3>

<h3> Running the code </h3>

<h3> Limitations </h3> 
1. Proper Cleaning : While scraping we realized that data provided by Universities for their placement of PhD candidates differs widely. For e.g, UCSD(University of California- San Diego) directly displayed a candidate working at UT Austin LBJ School, this data was indeed worthy for us but since the name of school has been used as an acronym , it was difficult for us to find such acronyms while cleaning the scraped dataset. The cleaning code involves looking at keywords like univeristy, college etc , however it can't catch keywords like UT has it would be extremely specific.

2. Imbalance of Dataset:This analysis could be improved by having an equal proportion of universities different tiers. While, we have a list of universities which can categorize to Tier-1,2 and 3 but all universities were not scrapable. Also, from list of tier-1 univerities it might be possible we have more PHD candidates pursuing the academic profession than the PHD candidates from Tier-2 this leads to an imbalance of dataset and it can lead to a biased observation.

3. Gender Detection and Prediction : For displaying ratio of Men and Women candidates pursuing academic profession we used a Gender Detection library from python to predict the gender based on names we scraped. The accuracy of the library is not going to be 100 % , as there are many names with can be assigned to both genders.

<h3> Methodology </h3> 

<h3> Results </h3> 

<h3> Conclusion </h3> 
