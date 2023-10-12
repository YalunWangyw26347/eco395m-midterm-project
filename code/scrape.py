import os
import csv
import requests
from bs4 import BeautifulSoup

url_Northwestern_University = "https://economics.northwestern.edu/graduate/prospective/placement.html"
url_New_York_University = "https://as.nyu.edu/departments/econ/job-market/placements.html"
url_Boston_University = "https://www.bu.edu/econ/academics/phd/recent-phd-placements/"
url_University_of_California_Berkeley = "https://www.econ.berkeley.edu/grad/program/placement-outcomes"
url_Princeton_University = "https://economics.princeton.edu/graduate-program/job-market-and-placements/statistics-on-past-placements/"
url_Harvard_University = "https://economics.harvard.edu/placement"
url_Stanford_University = "https://economics.stanford.edu/student-placement"
url_Yale_University = "https://economics.yale.edu/phd-program/placement/outcomes"
url_Columbia_University = "https://econ.columbia.edu/phd/placement/"
url_University_of_Pennsylvania = "https://economics.sas.upenn.edu/graduate/prospective-students/placement-information"
url_Boston_College="https://www.bc.edu/bc-web/schools/mcas/departments/economics/graduate/placements.html"
url_University_of_Rochester="https://www.sas.rochester.edu/eco/graduate/placement.html"
url_University_of_Virginia="https://economics.virginia.edu/placement-history"
url_Vanderbilt_University="https://as.vanderbilt.edu/economics/phd-placements/"
url_Washington_University_in_St_Louis="https://economics.wustl.edu/job-market-and-placement"
url_UCLA="https://economics.ucla.edu/graduate/graduate-profiles/graduate-placement-history/"
url_Cornell = "https://economics.cornell.edu/historical-placement-phd-students"
url_Duke = "https://econ.duke.edu/phd-program/prospective-students/placements"
url_UC_Davis = "https://economics.ucdavis.edu/graduate-student-placements"
url_Minnesota = "https://cla.umn.edu/economics/graduate/job-placement-achievements"
url_Brown = 'https://economics.brown.edu/academics/graduate/job-placement-results'
url_UCSD = "https://economics.ucsd.edu/graduate-program/jobmarket-tab/placement-history.html"

def scrape_University_of_Pennsylvania():
    school = "University of Pennsylvania"
    url = url_University_of_Pennsylvania 
    data = []
    response = requests.get(url)
    soup=BeautifulSoup(response.text, "html.parser")
    panels = soup.find_all('div', class_='panel-title')
    for panel in panels:
        year = panel.get_text(strip=True)  # Get the placement year
        if '2022' in year or '2023' in year:# only collect data from 2023 and 2022
            associated_data = panel.find_next('div', class_='card-block panel-collapse collapse')
            if associated_data:
                placements = associated_data.find_all('p')# <p> have all information we want
                for placement in placements:
                    text_content = placement.get_text(strip=True)
                    if '-' in text_content: # this url use '-' to link name and placement
                        name = text_content.split('-')[0].strip() # name is the first part of this information splited by'-'
                        place = text_content.split('-')[1].strip()
                        data.append({'School': school, 'Year': year, 'Name': name, 'Placement': place})
    # print(data)
    return data

def scrape_New_York_University():
    school = "New York University"
    url = url_New_York_University 
    data = []
    response = requests.get(url)
    soup=BeautifulSoup(response.text, "html.parser")
    for year_range in ['2021 - 2022', '2022 - 2023']:
        year_section = soup.find('summary', string=year_range)
        if year_section:
            # Extract placements, which are separated by <br />
            placements_section = year_section.find_next('p').find('p')  # Considering nested <p> tags
            placements = [placement for placement in placements_section.stripped_strings]

            for placement in placements:
                data.append({
                    'School': school,
                    'Year': year_range,
                    "Name":"",
                    'Placement': placement
                })
    return data

def scrape_Northwestern_University():
    school = "Northwestern University"
    url = url_Northwestern_University 
    data = []
    response = requests.get(url)
    soup=BeautifulSoup(response.text, "html.parser")
    for year in ['2022', '2023']:
        year_section = soup.find('h3', string=year)
        if year_section:
            # Find the associated academic placements section
            academic_placements_section = year_section.find_next('div', class_='expander expander1')
            if academic_placements_section:
                # Extract placements
                placements = academic_placements_section.find_all('li')
                for placement in placements:
                    data.append({
                        'School': school,
                        'Year': year,
                        'Name' : "",
                        'Placement': placement.get_text(strip=True)
                    })
    return data

def scrape_Boston_University():
    school = "Boston University"
    url = url_Boston_University
    data = []
    response = requests.get(url)
    soup=BeautifulSoup(response.text, "html.parser")
    for year in ['2022', '2023']:
        year_section = soup.find('h3', string=year)
        if year_section:
            # Locate the table containing the placements
            table = year_section.find_next('table')
            rows = table.find_all('tr')
            
            for row in rows:
                columns = row.find_all('td')
                if len(columns) == 2:  # Ensure it's a row with placement and name
                    placement = columns[0].get_text(strip=True)
                    name = columns[1].get_text(strip=True)
                    data.append({
                        'School': school,
                        'Year': year,
                        'Name': name,
                        'Placement': placement
                        
                    })
    return data
 
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
                    for i in placements:
                        placement=i.split(";")[0]+ i.split(";")[1]
                        data.append({"School": school, "Year": year_text,"Name":"","Placement":placement})
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
                "Name": " ",
                "Placement": institution  +  position
            })
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
                            "Name": name_tag.text.strip(),
                            "Placement": placement_tag.text.strip()
                        })
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
    return data

def scrape_BC():
    school="Boston College"
    data_all=[]
    url=url_Boston_College
    response=requests.get(url)
    soup=BeautifulSoup(response.text, "html.parser")
    table_class_tags=soup.find("table")# information in this url are shown in one single table
    samples=table_class_tags.find_all("tr")# information we want are in <tr>
    for sample in samples[1:]:# skip the header
        information= sample.find_all("td")# information we want are in <td>
        StudentName=information[0].text.strip() # name is the first part of information we get
        Year=information[1].text.strip()
        placement=information[2].text.strip()
        if (Year== "2023") or (Year== "2022"): 
            data_all.append({"School":school,"Year":Year, "Name":StudentName, "Placement":placement})
    return data_all


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
                items = [li.get_text(strip=True) for li in ul.find_all("li")] # <li> strore information we want
                for i in items:
                    name=i.split("-")[0] # name is the first part of information splited by '-'
                    placement=i.split("-")[1]
                    data.append({"School": school, "Year": time, "Name": name, "Placement":placement})
    return data

def scrape_University_of_Virginia():
    data=[]
    school="University of Virginia"
    url=url_University_of_Virginia
    response=requests.get(url)
    soup=BeautifulSoup(response.text, "html.parser")
    table_class_tags=soup.find_all('table', class_="views-table cols-3") # in this url, information is stored in a table
    for table_class_tag in table_class_tags:
        time=table_class_tag.find("caption").get_text() #<caption> stores year information
        samples=table_class_tag.find_all("tr")
        if time=="2023" or time =="2022":
            for sample in samples:
                if sample.find('th'): # the header part have differnet tag, <th> carries information we want
                    continue
                else:
                    getname=sample.find("h4")
                    StudentName=getname.get_text().strip()
                    getplacement=sample.find("td", class_="views-field views-field-field-initial-placement")# information about placement is in <td>
                    Placement=getplacement.get_text().strip()
                    data.append({"School":school,"Year":time, "Name":StudentName,"Placement":Placement})
    return data

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
            content = p_tag.get_text()
            info_list = content.split('\r\n')#split the whole content by'\r\n' to get seperate information 
            data_all.append({
                            "School": school,
                            "Year": time,
                            "Name": info_list[0],
                            "Placement": str(info_list[1:])# mix information regarding with job title and university they work for
                        })

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
                for i in items:
                    name=i.split(",")[0]
                    placement=i.split(",")[1]
                    data.append({"School": school, "Year": time, "Name": name, "Placement":placement})

    return data

def scrape_UCLA_graduate_placement():
    school = "The University of California, Los Angeles"
    data = []

    response = requests.get(url_UCLA)
    soup = BeautifulSoup(response.text, "html.parser")

    # Find the year elements with 2023 and 2022
    year_elements = soup.find_all('h4', class_='av-special-heading-tag', itemprop='headline')
    relevant_years = ['2023', '2022']
    for year_element in year_elements:
        year = year_element.get_text(strip=True)

        # Check if the year is one of the relevant years
        if year in relevant_years:
            # Find the parent table of the year_element
            table = year_element.find_next('table')

            # Iterate through the table rows
            for row in table.find_all('tr'):
                columns = row.find_all('td')
                if len(columns) == 2:
                    name = columns[0].get_text(strip=True)
                    placement = columns[1].get_text(strip=True)
                    data.append({'School': school, 'Year': year, 'Name': name, 'Placement': placement})

    return data

def scrape_Cornell():
    school = "Cornell University"
    data = []

    response = requests.get(url_Cornell)
    soup = BeautifulSoup(response.text, "html.parser")

    # Find the table containing placement information
    table = soup.find('table')

    # Iterate through the table rows in the tbody
    for row in table.find('tbody').find_all('tr'):
        columns = row.find_all('td')

        # Check if there are enough columns and if the year is 2022 or 2023
        if len(columns) >= 5 and (columns[0].text.strip() in ['2022', '2023']):
            year = columns[0].text.strip()
            name = columns[1].text.strip()
            placement = columns[2].text.strip()

            data.append({'School': school, 'Year': year, 'Name': name, 'Placement': placement})

    return data

def scrape_Duke():
    school = "Duke University"
    data = []

    response = requests.get(url_Duke)
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all the panel-title elements
    panel_titles = soup.find_all('div', class_='panel-title')

    for panel_title in panel_titles:
        # Extract the year from the anchor tag inside the panel-title
        year_element = panel_title.find('a', class_='normal')
        if year_element:
            year = year_element.get_text(strip=True)

            # Check if the year is in the specified list
            if year in ['2022', '2023']:
                # Find the corresponding placement information
                placement = panel_title.find_next('div', class_='card-block')
                if placement:
                    # Extract the placement information from the table
                    table = placement.find('table', class_='tablesaw')
                    if table:
                        rows = table.find_all('tr')
                        for row in rows:
                            columns = row.find_all('td')
                            if len(columns) == 3:
                                name = columns[0].text.strip()
                                position = columns[1].text.strip()
                                institution = columns[2].text.strip()
                                if "Name" not in name:  # Check if it's not a header row
                                    placement_text = f"{position} + {institution}"
                                    data.append({'School': school, 'Year': year, 'Name': name, 'Placement': placement_text})

    return data

def scrape_Minnesota_Twin_cities():
    school = "University of Minnesota"
    data = []

    response = requests.get(url_Minnesota)
    soup = BeautifulSoup(response.text, "html.parser")

    # Find the first table containing placement information
    table = soup.find('table')

    if table:
        rows = table.find_all('tr')
        for row in rows[1:]:  # Skip the header row
            columns = row.find_all('td')
            if len(columns) == 3:
                name = columns[0].text.strip()
                institution = columns[1].text.strip()
                position = columns[2].text.strip()
                placement_text = f"{position} + {institution}"
                data.append({'School': school, 'Year': '2023', 'Name': name, 'Placement': placement_text})

    # Find the next table (if there is one)
    next_table = table.find_next('table')

    if next_table:
        rows = next_table.find_all('tr')
        for row in rows[1:]:  # Skip the header row
            columns = row.find_all('td')
            if len(columns) == 3:
                name = columns[0].text.strip()
                institution = columns[1].text.strip()
                position = columns[2].text.strip()
                placement_text = f"{position} + {institution}"
                data.append({'School': school, 'Year': '2022', 'Name': name, 'Placement': placement_text})


    return data

def scrape_UC_Davis():
    school = "UC Davis"
    data = []

    response = requests.get(url_UC_Davis)
    soup = BeautifulSoup(response.text, "html.parser")

    # Find the table containing placement information
    table = soup.find('table', class_='table--striped')

    if table:
        rows = table.find_all('tr')
        for row in rows[1:]:  # Skip the header row
            columns = row.find_all('td')
            if len(columns) == 5:
                try:
                    last_name = columns[0].text.strip()
                    first_name = columns[1].text.strip()
                    phd_date = columns[2].text.strip()
                    year = "20" + phd_date.split('-')[1]  # Extract year from PhD date
                    if year in ["2023", "2022"]:
                        placement = columns[3].text.strip() + " " + columns[4].text.strip()  # Combine First Placement and First Job Title
                        name = f"{first_name} {last_name}"
                        data.append({'School': school, 'Year': year, 'Name': name, 'Placement': placement})
                except IndexError:
                    pass  # Ignore rows with unexpected data

    return data

def scrape_Brown_University():
    school = 'Brown University'
    data = []

    response = requests.get(url_Brown)
    soup = BeautifulSoup(response.text, 'html.parser')

    years = soup.find_all('div', class_='accordion_item')

    for year in years:
        year_text = year.find('button', class_='accordion_trigger').text.strip()

        if year_text in ['2023', '2022']:
            placements = year.find_all('li')

            for placement in placements:
                placement_text = placement.text.strip()
                name = placement_text.split('-')[0].strip()
                placement_info = '-'.join(placement_text.split('-')[1:]).strip()

                data.append({
                    'School': school,
                    'Year': year_text,
                    'Name': name,
                    'Placement': placement_info
                })
   
    return data

def scrape_UCSD():
    data = []

    response = requests.get(url_UCSD)
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all the sections with placement history data
    sections = soup.find_all('div', class_='drawer dark-theme')

    for section in sections:
        year = section.find('a').text.strip()
        if year in ['2022-23', '2021-22']:
            table = section.find('table', class_='styled')
            rows = table.find_all('tr')[1:]  # Skip the header row

            for row in rows:
                columns = row.find_all('td')
                if len(columns) == 4:
                    name = columns[1].text.strip()
                    placement = columns[3].text.strip()
                    data.append({'School': 'UCSD', 'Year': year, 'Name': name, 'Placement': placement})
    return data

scrape_data_UCBerkeley= scrape_UCBerkeley()
scrape_data_Yale= scrape_Yale()
scrape_data_Harvard = scrape_Harvard()
scrape_data_Stanford = scrape_Stanford()
scrape_data_Columbia = scrape_Columbia()
scrape_data_Princeton = scrape_Princeton()
scraped_data_New_York_University= scrape_New_York_University()
scraped_data_Northwestern_University= scrape_Northwestern_University()
scraped_data_University_of_Pennsylvania= scrape_University_of_Pennsylvania()
scraped_data_Boston_University= scrape_Boston_University()
scraped_data_WL = scrape_Washington_University_in_St_Louis()
scraped_data_Van= scrape_Vanderbilt_University()
scrape_data_Rochester= scrape_University_of_Rochester()
scraped_data_BC = scrape_BC()
scrape_data_Vir= scrape_University_of_Virginia()
scraped_data_UCLA = scrape_UCLA_graduate_placement()
scraped_data_Cornell = scrape_Cornell()
scraped_data_Duke = scrape_Duke()
scraped_data_Minesota = scrape_Minnesota_Twin_cities()
scraped_data_UC_Davis= scrape_UC_Davis()
scraped_data_Brown = scrape_Brown_University()
scraped_data_UCSD = scrape_UCSD()

def raw_output():
    raw_output = scrape_data_UCBerkeley + scrape_data_Yale + scrape_data_Harvard + scrape_data_Stanford\
    + scrape_data_Columbia + scrape_data_Princeton + scraped_data_New_York_University\
    + scraped_data_Northwestern_University + scraped_data_University_of_Pennsylvania\
    + scraped_data_Boston_University + scraped_data_WL + scraped_data_Van + scrape_data_Rochester\
    + scraped_data_BC + scrape_data_Vir + scraped_data_UCLA + scraped_data_Cornell\
    + scraped_data_Duke + scraped_data_Minesota + scraped_data_UC_Davis + scraped_data_Brown\
    + scraped_data_UCSD
    return raw_output

def write_data_to_csv(data, path):
    """Write the data to the csv.
    """
    with open(CSV_PATH, 'w', newline='') as csvfile:
        fieldnames = ["School", "Year", "Name", "Placement"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader() 
        for row in data:
            writer.writerow(row)


if __name__ == "__main__":
    data = raw_output()
    BASE_DIR = "artifacts"
    CSV_PATH = os.path.join(BASE_DIR, "rawplacement.csv")

    os.makedirs(BASE_DIR, exist_ok=True)
    write_data_to_csv(data, CSV_PATH)

