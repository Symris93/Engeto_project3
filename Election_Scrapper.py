"""
projekt_3.py: třetí projekt do Engeto Online Python Akademie
 
author: Lukáš Fúzik
email: fuzik@atlas.cz
discord: Symris93
"""
import requests, re, csv, sys
from bs4 import BeautifulSoup
 
def extract_info(soup_html):
    #town code, location, and org names
    town_code = [td.text for td in soup_html.find_all("td", {"class": "cislo"})]
    town_name = [td.text for td in soup_html.find_all("td", {"class": "overflow_name"})]
    org_names = []
    for headers in ["t1sa1 t1sb2", "t2sa1 t2sb2"]:
        org_names.extend([td.text for td in soup_html.find_all("td", {"headers": headers})])
    return town_code, town_name, org_names
 
def extract_votes(soup_html):
    #votes for each org
    votes = []
    for headers in ["t1sa2 t1sb3", "t2sa2 t2sb3"]:
        votes.extend([td.text for td in soup_html.find_all("td", {"headers": headers})])
    return votes
 
def extract_summ_values(soup_html):
    #registered, envelopes, valid
    get_summ_table = soup_html.find("table", {"id": "ps311_t1"})
    get_summ_values = get_summ_table.find_all("td", {"class": "cislo"})
    registered, envelopes, valid = [get_summ_values[i].text for i in [3, 4, 7]]
    return registered, envelopes, valid
 

 
def election_scrapper(votes_source, output_name):
    if output_name[-4:] != ".csv":
        print("Špatná koncovka - 2. parametr musí končit \".csv\"")
        exit
 
    try:
        print(f"Stahuji data z URL \"{votes_source}\"")
        get_html_parent = requests.get(votes_source)
        soup_html_parent = BeautifulSoup(get_html_parent.text, features="html.parser")
 
        town_code, town_name, org_names = extract_info(soup_html_parent)
        filtered_links = ["https://volby.cz/pls/ps2017nss/" + link.get("href") for link in soup_html_parent.find_all("a", attrs={"href": re.compile("ps311")})]
 
        with open(output_name, "w", encoding="utf-8", newline="") as csv_file:
            csv_file_writer = csv.writer(csv_file)
            header = ["valid", "envelopes", "registered", "location", "code"] + org_names
            csv_file_writer.writerow(header)
 
            for link_specific in filtered_links:
                get_html = requests.get(link_specific)
                soup_html = BeautifulSoup(get_html.text, features="html.parser")
 
                votes = extract_votes(soup_html)
                registered, envelopes, valid = extract_summ_values(soup_html)
 
                whole_row = [town_code.pop(0), town_name.pop(0), registered, envelopes, valid] + votes
                csv_file_writer.writerow(whole_row)
 
        print("Ukončuji election scrapper")
    except IndexError:
        print("Špatný link - 1. parametr musí být link ze sloupce \"Výběr obce\" na stránce https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ")
        exit
 
if __name__ == "__main__":
    election_scrapper(sys.argv[1], sys.argv[2])
