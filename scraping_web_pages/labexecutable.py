import requests
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup 
# userful commands for lab 4 and star tribune website 

def go():

    print("program has started. Fetching a headline....")


    r = requests.get("http://www.startribune.com", timeout=3)
    soup = BeautifulSoup(r.content, "html5lib")
    return soup
# call everything in go


def display_headline(soup):
    title = soup.find("a", "tease-headline").string
    print(title)
    print("end")



try:
    soup = go()
    display_headline(soup)

except ConnectionError as connErr:
    print("Check your internet connection and try again. \n Detailed information : ", connErr)
except Exception as e:
    print("Something went wrong. Report bug to developer. Here is detailed information\n", e)

# command to pull headline from star tribune website

#upon reviewing the documentation i was able to find that If a tag has only one child, and that child is a NavigableString, 
#the child is made available as .string: