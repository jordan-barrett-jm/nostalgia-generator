#Helper script to save TV show info to the database
import requests
from bs4 import BeautifulSoup
import json
import configparser
import argparse


def saveShows(link, category, endpoint):
    headers = {
        'Content-Type':'application/json'
    }

    list_page = requests.get(link).text
    soup = BeautifulSoup(list_page, 'html.parser')
    items = soup.findAll(class_="lister-item-content")

    for show in items:
        show_dct = {}
        show_dct['name'] = show.find(class_="lister-item-header").find("a").text
        show_dct['category'] = category
        run_time = show.find(class_="lister-item-year").text.replace("(","").replace(")","").split("–")
        print (run_time)
        show_dct['start_year'] = run_time[0]
        if len(run_time) > 1:
            if run_time[1] != " ":
                show_dct['end_year'] = run_time[1]
            else:
                show_dct['end_year'] = show_dct['start_year']
        else:
            show_dct['end_year'] = show_dct['start_year']
        print (json.dumps(show_dct))
        req = requests.post(endpoint, data=json.dumps(show_dct), headers=headers)
        print (req.text)

def main():
    #parse the arguments passed from the console
    parser = argparse.ArgumentParser(description="Provide link to list of TV shows as well as category")
    parser.add_argument('--link', help='Link to the IMDB list of shows')
    parser.add_argument('--category', help='Category the list falls under, be it 2010s, 2000s, 1990s, or 1980s')
    args = parser.parse_args()
    #parse the API endpoint from the config file
    config = configparser.ConfigParser()
    config.read("api_config.ini")
    endpoint = config["DEFAULT"]["endpoint"]
    #now, save the data
    saveShows(args.link, args.category, endpoint)

if __name__ == "__main__":
    main()



