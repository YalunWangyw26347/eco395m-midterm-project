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
    response_dict={}
    data_all=[]
    url=url_Boston_College
    response=requests.get(url)
    soup=BeautifulSoup(response.text, "html.parser")
    table_class_tags=soup.find("table")
    samples=table_class_tags.find_all("tr")
    # print(samples)
    for sample in samples[1:]:
        data=[]
        information= sample.find_all("td")
        StudentName=information[0].text.strip()
        Year=information[1].text.strip()
        placement=information[2].text.strip()
        if (Year== 2023) or (Year== 2022):
            data.append(Year)
            data.append(school)
            data.append(StudentName)
            data.append(placement)
            data_all.append(data)
    #print(data_all)
    return data_all



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
    #print(strong_tags)
    for strong in strong_tags: # check every <strong>
        time = strong.get_text() # get information in <strong>, the time information   
        if "2023" in time or "2022" in time: 
            ul = strong.find_next("ul") #we only focus on <ul> after <strong>
            if ul:
                items = [li.get_text(strip=True) for li in ul.find_all("li")]
                data.append({"School Name": school, "Year": time, "Students' Info": items})
    
    #print(data)
    return data


def scrape_University_of_Virginia():
    data_all=[]
    school="University of Virginia"
    url=url_University_of_Virginia
    response=requests.get(url)
    soup=BeautifulSoup(response.text, "html.parser")
    table_class_tags=soup.find_all('table', class_="views-table cols-3")
    for table_class_tag in table_class_tags:
        time=table_class_tag.find("caption").get_text()
        samples=table_class_tag.find_all("tr")
        if time==2023 or time ==2022:
            for sample in samples:
                if sample.find('th'):
                    continue
                else:
                    data=[]
                    getname=sample.find("h4")
                    StudentName=getname.get_text()
                    getplacement=sample.find("td", class_="views-field views-field-field-initial-placement")
                    Placement=getplacement.get_text()
                    data.append(time)
                    data.append(school)
                    data.append(StudentName)
                    data.append(Placement)
                    data_all.append(data)
    print(data_all)
    return data_all

def scrape_Vanderbilt_University():
    school="Vanderbilt_University"
    data_all=[]
    url=url_Vanderbilt_University
    response=requests.get(url)
    soup=BeautifulSoup(response.text, "html.parser")
    div_years=soup.find_all('div', class_="panel panel-default")
    for div_year in div_years:
        h4_tag=soup.find('h4',class_="panel-title")
        time = h4_tag.get_text()
        p_tags=div_year.find_all('p')
        for p_tag in p_tags:
            data=[]
            content = p_tag.get_text()
            data.append(time)
            data.append(school)
            data.append(content)
            data_all.append(data)
        #print(data)
    #print(data_all)
    return data_all

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
# scraped_data_BC = scrape_BC()
# scraped_data_WL = scrape_Washington_University_in_St_Louis()
# scraped_data_Van= scrape_Vanderbilt_University()
# scrape_data_Rochester= scrape_University_of_Rochester()
scrape_data_Vir= scrape_University_of_Virginia()

