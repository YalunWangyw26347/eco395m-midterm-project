import csv
import requests
from bs4 import BeautifulSoup

url_University_of_California_Berkeley = "https://www.econ.berkeley.edu/grad/program/placement-outcomes"
url_Princeton_University = "https://economics.princeton.edu/graduate-program/job-market-and-placements/statistics-on-past-placements/"
url_Harvard_University = "https://economics.harvard.edu/placement"
url_Stanford_University = "https://economics.stanford.edu/student-placement"
url_Yale_University = "https://economics.yale.edu/phd-program/placement/outcomes"
url_Columbia_University = "https://econ.columbia.edu/phd/placement/"
url_University_of_Pennsylvania = "https://economics.sas.upenn.edu/graduate/prospective-students/placement-information"
url_Boston_College="https://www.bc.edu/bc-web/schools/mcas/departments/economics/graduate/placements.html"
url_Pennsylvania_State_University="https://econ.la.psu.edu/ph-d-program/initial-placements-of-ph-d-graduates/"
url_University_of_Rochester="https://www.sas.rochester.edu/eco/graduate/placement.html"
url_University_of_Virginia="https://economics.virginia.edu/placement-history"
url_Vanderbilt_University="https://as.vanderbilt.edu/economics/phd-placements/"
url_Washington_University_in_St_Louis="https://economics.wustl.edu/job-market-and-placement"

def scrape_UCBerkeley():
    school = "University of California, Berkeley"
    url = url_University_of_California_Berkeley 
    data = []
    response = requests.get(url)
    soup=BeautifulSoup(response.text, "html.parser")
    years = soup.find_all('h3')
    for year_tag in years:
        year_text = year_tag.text.strip()
        # If the year text contains "2023" or "2022", then proceed
        if "2023" in year_text or "2022" in year_text:
            # Get the next <strong> tag after the h3, which indicates the type of placement, here we are only interested in the academia placement
            placement_type_tag = year_tag.find_next('strong')
            if placement_type_tag and "Academia" in placement_type_tag.text:  
                student_list = placement_type_tag.find_next("ul")
                if student_list:
                    placements = [li.get_text(strip=True) for li in student_list.find_all("li")]
                    data.append({"School Name": school, "Year": year_text,  "Placements": placements})
    # print(data)
    return data

def scrape_Princeton():
    school = "Princeton University"
    url = url_Princeton_University 
    data = []
    response = requests.get(url)
    soup=BeautifulSoup(response.text, "html.parser")
    rows = soup.find_all("tr", attrs={"data-year": True})
    for row in rows:
        year = row["data-year"]
        # Check if the year matches desired range
        if year in ["2022-2023", "2021-2022"]:
            institution = row["data-inst"]
            position = row["data-position"]
            data.append({
                "School": school, 
                "Year": year,
                "Placement": institution  +  position
            })
    print(data)
    return data

def scrape_Columbia():
    school = "Columbia University"
    url = url_Columbia_University 
    data = []
    response = requests.get(url)
    soup=BeautifulSoup(response.text, "html.parser")
    h3_tags = soup.find_all("h3")
    year_tags = [tag for tag in h3_tags if ("2022" in tag.text or "2023" in tag.text) and "Placement Information" in tag.text]
    for year_tag in year_tags:
        year_text = year_tag.text.split()[0]  # Split the text and take the first word which should be the year
        if year_text in ["2022", "2023"]:
            # Find the table that follows the h3 tag
            table = year_tag.find_next("table")
            if table:
                rows = table.find_all("tr")[1:]  # Skipping the header row
                for row in rows:
                    columns = row.find_all("td")
                    if len(columns) == 3:  # Ensure there are 3 columns for Name, Field, and Placement
                        name = columns[0].get_text(strip=True)
                        placement = columns[2].get_text(strip=True)
                        data.append({
                            "School": school,
                            "Year": year_text,
                            "Name": name,
                            "Placement": placement
                        })
    print(data)
    return data

def scrape_Yale():
    school = "Yale University"
    url = url_Yale_University 
    data = []
    response = requests.get(url)
    soup=BeautifulSoup(response.text, "html.parser")
    tables = soup.find_all("table")
    for table in tables:
        year_tag = table.find("h3")
        if year_tag:
            year_text = year_tag.text.strip()
            # If the year text matches the specified years, then proceed
            if year_text in ["Year: 2021-22", "Year: 2022-23"]:
                rows = table.find_all("tr")[1:]  # skip the first row which is the header
                for row in rows:
                    name_tag = row.find("strong")
                    placement_tag = row.find_all("td")[1]  # second column of the row

                    if name_tag and placement_tag:
                        data.append({
                            "School": school,
                            "Year": year_text.split(":")[1].strip(),  # Extracting the year only
                            "Student Name": name_tag.text.strip(),
                            "Placement": placement_tag.text.strip()
                        })
                
    # print(data)
    return data


def scrape_Stanford():
    school = "Stanford University"
    url = url_Stanford_University
    data = []
    response = requests.get(url)
    soup=BeautifulSoup(response.text, "html.parser")
    tables = soup.find_all("table", class_="cols-3")
    for table in tables:
        year_tag = table.find("time")
        if year_tag:
            year_text = year_tag.text.strip()
            
            # If the year text matches the specified years, then proceed
            if year_text in ["2022", "2023"]:
                rows = table.find_all("tr")[1:]  # skipping the header row
                for row in rows:
                    columns = row.find_all("td")
                    if len(columns) == 3:  # Ensure there are 3 columns for Name, Field, and Placement
                        name = columns[0].get_text(strip=True)
                        placement = columns[2].get_text(strip=True)
                        data.append({
                            "School": school, 
                            "Year": year_text,
                            "Name": name,
                            "Placement": placement
                        })

    # print(data)
    return data

def scrape_Harvard():
    school = "Harvard University"
    url = url_Harvard_University
    data = []
    response = requests.get(url)
    soup=BeautifulSoup(response.text, "html.parser")
    target_years = ["Graduate Student Placement 2023", "Graduate Student Placement 2022"]
    for target_year in target_years:
        # Find the h3 tag containing the year
        year_tag = soup.find("h3", text=target_year)
        if year_tag:
            # Try to find the table within the 'accordion-panel' following the year_tag
            table = year_tag.find_next("div", class_="accordion-panel").find("table", class_="os-table")
            if table:
                rows = table.find_all("tr")[1:]  # skipping the header row
                for row in rows:
                    columns = row.find_all("td")
                    if len(columns) == 3:  # Ensure there are 3 columns for Name, Field, and Placement
                        name = columns[0].get_text(strip=True)
                        placement = columns[2].get_text(strip=True)
                        data.append({
                            "School" : school,
                            "Year": target_year.split()[-1],  # Extract the year (last word) from the target_year string
                            "Name": name,
                            "Placement": placement
                        })

    # print(data)
    return data

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
    
    # print(data)
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
    
    return data

scraped_data_WL = scrape_Washington_University_in_St_Louis()
scraped_data_Van= scrape_Vanderbilt_University()
scrape_data_Rochester= scrape_University_of_Rochester()
scrape_data_UCBerkeley= scrape_UCBerkeley()
scrape_data_Yale= scrape_Yale()
scrape_data_Harvard = scrape_Harvard()
scrape_data_Stanford = scrape_Stanford()
scrape_data_Columbia = scrape_Columbia()
scrape_data_Princeton = scrape_Princeton()