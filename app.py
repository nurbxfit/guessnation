import requests
import pyfiglet
import pycountry
import json 
from progress.bar import Bar

ascii_banner = pyfiglet.figlet_format("Guess My Nationality")
url="https://api.nationalize.io/"


headers = {
    "Accept": "application/json"
}



def display_bar(value):
    bar = Bar("probability:",max=100,suffix='%(percent)d%%')
    percent = int(value * 100)
    for i in range(percent):
        bar.next()
    bar.finish()

def display_probability(nation):
    # print(json.dumps(nation))
    country = pycountry.countries.get(alpha_2=nation['country_id'])
    print(f"\nNationality: {country.name}")
    display_bar(nation['probability'])

def display_info(jsondata):
    for i in jsondata['country']:
        display_probability(i)




def main():
    print(ascii_banner)
    print(f"Simple script, make use of https://nationalize.io/ API, to assume nationality.\n")
    name = input("What is your name? (single word): ")
    params = {
        "name" : name,
    }
    res = requests.get(url,params=params,headers=headers)

    if res.status_code == 200:
        jsondata = res.json()
        display_info(jsondata)
    elif res.status_code == 422:
        print("Missing 'name' parameter")
    elif res.status_code == 429:
        print("Too many request to API")
    else:
        print("Couldn't create request")

if __name__ == "__main__":
    main()