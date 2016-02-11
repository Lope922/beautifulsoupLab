import requests 
from bs4 import BeautifulSoup 
# userful commands for lab 4 and star tribune website 

def go():

    r = requests.get("http://www.startribune.com")

    soup = beautifulSoup(r.content)

    print(soup.printify())



# thought this was helpful for looking at other code... 
# prints the html or js in a readable format. 

# call everything in go 
go()

# other commands soup.find_all("a")

# evolved into this thus far 
#soup.find_all(class_="tease-headline", limit = 1)

#now trying to narrow down to just data-linkname

# command that was able to get things tidied up in the end 
soup.find("a", "tease-headline").string

print("end")

#upon reviewing the documentation i was able to find that If a tag has only one child, and that child is a NavigableString, 
#the child is made available as .string: