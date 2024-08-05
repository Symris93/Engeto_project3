"""
projekt_3.py: třetí projekt do Engeto Online Python Akademie

author: Lukáš Fúzik
email: fuzik@atlas.cz
discord: Symris93
"""
import requests, re, csv, sys
from bs4 import BeautifulSoup

def election_scrapper(votes_source, output_name):

    town_code = []
    town_name = []
    org_names = []
    counter = 0


    #Error handling
    if output_name[-4:] != ".csv":
        print("Špatná koncovka - 2. parametr musí končit \".csv\"")
        exit
    try:
        print(f"Stahuji data z URL \"{votes_source}\"")
        #Links to each town
        filtered_links = []
        get_html_parent = requests.get(votes_source)
        soup_html_parent = BeautifulSoup(get_html_parent.text, features="html.parser")
        for link in soup_html_parent.find_all("a", attrs={"href": re.compile("ps311")}):
            if ("https://volby.cz/pls/ps2017nss/" + link.get("href")) not in filtered_links:
                filtered_links.append("https://volby.cz/pls/ps2017nss/" + link.get("href"))

        #Town code and name
        for town_code_ in soup_html_parent.find_all("td", {"class": "cislo"}):
            town_code.append(town_code_.text)
        for town_name_ in soup_html_parent.find_all("td", {"class": "overflow_name"}):
            town_name.append(town_name_.text)


        #Unnecessary soup just to get the org_names
        get_html = requests.get(filtered_links[0])
        soup_html = BeautifulSoup(get_html.text, features="html.parser")
        #Organization names
        get_org_names = soup_html.find_all("td", {"headers": "t1sa1 t1sb2"})
        for name in get_org_names:
            org_names.append(name.text)
        get_org_names = soup_html.find_all("td", {"headers": "t2sa1 t2sb2"})
        for name in get_org_names:
            org_names.append(name.text)

        #Make .CSV + header
        print(f"Vytvářím CSV \"{output_name}\"")
        csv_file = open(output_name, "w", encoding="utf-8", newline="")
        csv_file_writer = csv.writer(csv_file)
        for x in ["valid","envelopes","registered","location","code"]:
            org_names.insert(0,x)
        csv_file_writer.writerow(org_names)
        
        #.CSV data
        for link_specific in filtered_links:
        
            votes = []
            registered = []
            envelopes = []
            valid = []

            #Soup for a specific town
            get_html = requests.get(link_specific)
            soup_html = BeautifulSoup(get_html.text, features="html.parser")

            #Votes for each organization
            get_org_votes = soup_html.find_all("td", {"headers": "t1sa2 t1sb3"})
            for vote in get_org_votes:
                votes.append(vote.text)
            get_org_votes = soup_html.find_all("td", {"headers": "t2sa2 t2sb3"})
            for vote in get_org_votes:
                votes.append(vote.text)

            #Other vote information
            get_summ_table = soup_html.find("table", {"id": "ps311_t1"})
            get_summ_values = get_summ_table.find_all("td", {"class": "cislo"})
            registered.append(get_summ_values[3].text)
            envelopes.append(get_summ_values[4].text)
            valid.append(get_summ_values[7].text)

            whole_row = []
            whole_row.extend([town_code[counter],town_name[counter],registered[0],envelopes[0],valid[0]])
            for y in votes:
                whole_row.append(y)  
            csv_file_writer.writerow(whole_row)
            counter +=1

        csv_file.close()
        print("Ukončuji election scrapper")
    except IndexError:
        print("Špatný link - 1. parametr musí být link ze sloupce \"Výběr obce\" na stránce https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ")
        exit
        
    

if __name__ == "__main__":
    election_scrapper(sys.argv[1],sys.argv[2])