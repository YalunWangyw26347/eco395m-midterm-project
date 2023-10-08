import csv
import requests
from bs4 import BeautifulSoup


url_Boston_College="https://www.bc.edu/bc-web/schools/mcas/departments/economics/graduate/placements.html"
url_Pennsylvania_State_University="https://econ.la.psu.edu/ph-d-program/initial-placements-of-ph-d-graduates/"
url_University_of_Rochester="https://www.sas.rochester.edu/eco/graduate/placement.html"
url_University_of_Virginia="https://economics.virginia.edu/placement-history"
url_Vanderbilt_University="https://as.vanderbilt.edu/economics/phd-placements/"
url_Washington_University_in_St_Louis="https://economics.wustl.edu/job-market-and-placement"

def scrape_BC():
    school="Boston College"
    res=[]
    response_dict={}
    url=url_Boston_College
    response=requests.get(url)
    soup=BeautifulSoup(response.text, "html.parser")
    links=soup.find_all("td")
    for link in links:
        res.append(link)
    #print(res)
    return res
scraped_data_BC = scrape_BC()

def scrape_PSU():
    school="Pennsylvania State University"
    url=url_Pennsylvania_State_University
    response=requests.get(url)
    soup=BeautifulSoup(response.text, "html.parser")
    div_class_tags=soup.find_all('div',class_="jet-toggle__label-icon jet-toggle-icon-position-left")


    return

def scrape_University_of_Rochester():
    data=[]
    school="University of Rochester"
    url=url_University_of_Rochester
    response=requests.get(url)
    soup=BeautifulSoup(response.text, "html.parser")
    strong_tags = soup.find_all("strong")  # find all the <strong>, inside it is time information
    for strong in strong_tags: # check every <strong>
        time = strong.get_text() # get information in <strong>, the time information   
        if "2023" in time or "2022" in time: 
            ul = strong.find_next("ul") #we only focus on <ul> after <strong>
            if ul:
                items = [li.get_text(strip=True) for li in ul.find_all("li")]
                data.append({"School Name": school, "Year": time, "Students' Info": items})
    
    print(data)
    return

    return

def scrape_University_of_Virginia():
    school="University of Virginia"
    url=url_University_of_Virginia
    response=requests.get(url)
    soup=BeautifulSoup(response.text, "html.parser")


    return

def scrape_Vanderbilt_University():
    school="Vanderbilt_University"
    data=[]
    url=url_Vanderbilt_University
    response=requests.get(url)
    soup=BeautifulSoup(response.text, "html.parser")
    h4_tags=soup.find_all ('h4',class_="panel-title")
    for h4 in h4_tags:
        time = h4.get_text()
        if "2022" in time or "2021" in time:
             p_tag =h4.find_next("p")
             content = p_tag.get_text()
            
            # 将时间和内容组成一个字典，并添加到数据列表中
             data.append({"Year": time, "Content": content})
    #print(data)
    return data

def scrape_Washington_University_in_St_Louis():
    data = []
    school="Washington University in St Louis"
    url=url_Washington_University_in_St_Louis
    response=requests.get(url)
    soup=BeautifulSoup(response.text, "html.parser")
    strong_tags = soup.find_all("strong")  # find all the <strong>, inside it is time information
    for strong in strong_tags: # check every <strong>
        time = strong.get_text() # get information in <strong>, the time information   
        if "2022-2023" in time or "2021-2022" in time: 
            ul = strong.find_next("ul") #we only focus on <ul> after <strong>
            if ul:
                items = [li.get_text(strip=True) for li in ul.find_all("li")]
                data.append({"School Name": school, "Year": time, "Students' Info": items})
    
    #print(data)
    return data
scraped_data_WL = scrape_Washington_University_in_St_Louis()
scraped_data_Van= scrape_Vanderbilt_University()
scrape_data_Rochester= scrape_University_of_Rochester()


