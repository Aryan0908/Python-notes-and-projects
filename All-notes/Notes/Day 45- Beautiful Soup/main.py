# Importing Beautiful Soup
from bs4 import BeautifulSoup

# Getting data from the website
with open("website.html", encoding="utf-8") as file:
    data = file.read()


# Getting hold of the content of the website
soup = BeautifulSoup(data, "html.parser")
""" In some websites html parsr don't work so try some other parsers """

# Getting entire soup object
print(soup)

# Getting a particular tag
print(soup.title)

# Getting string from a particular tag
print(soup.title.string)

# Getting the name of the tag
print(soup.title.name)

# Indenting the html code
print(soup.prettify())

# Getting all items of a tag
all_anchor_tag = soup.findAll(name="a")

for anchor in all_anchor_tag:
    # Getting text inside all anchor tags
    text = anchor.getText()

    # Getting attributes out of a tag
    attribute = anchor.get("href")


# Getting a tag with a id name
id = soup.find(name="h1", id="name")

# Getting hold of with the class
class_ = soup.find(name="h3", class_="heading")

# Getting a specific element
""" In the code below we are saying that select the one anchor tag that is inside paragraph tag """
name = soup.select_one(selector="p a")

# Selection the one with the id name
id1 = soup.select_one('#name')

# All elements with class heading
all_class = soup.select(selector=".heading")
print(all_class)