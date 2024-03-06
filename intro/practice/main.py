from bs4 import BeautifulSoup

with open("website.html", 'r', encoding='utf-8') as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

# print(soup)
# print(soup.prettify())
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.a.string)

# print(soup.find_all(name="a"))
# print(soup.find_all(name="p"))

tags = soup.find_all(name="a")

# for tag in tags:
#     print(tag.getText())

# for tag in tags:
#     print(tag.get("href"))

# # print(soup.find_all(name="h1", id="name"))
# print(soup.find_all(name="h3", class_="heading"))

company_url = soup.select_one(selector="p a")
# name = soup.select_one(selector="#name")
# print(company_url)

