from bs4 import BeautifulSoup  # Web site kodları için ayrıştırma işlemleri
# import lxml

with open("website.html", 'r', encoding='utf-8') as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
# soup = BeautifulSoup(contents, "lxml")

# print(soup)
# print(soup.prettify())  her sey tek bir satırda olduğu hali

# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)

# print(soup.a)
# print(soup.p)
# print(soup.li)
# print(soup.ul)

# all_anchor_tags = soup.find_all(name="a")
# # print(all_anchor_tags)  # Bu şekilde hepsini yazdırabiliriz
# for tag in all_anchor_tags:
#     print(tag.getText())  # a tag'leri içerisindeki metinleri getirir.
#     print(tag.get("href"))  # href bağlantılarını yazdırır

# heading = soup.find(name="h1", id="name")
# print(heading)

# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)
# print(section_heading.get("class"))

# company_url = soup.select_one(selector="p a")
# print(company_url)

name = soup.select_one(selector="#name")  # id için '#' sembolu gerekir
print(name)

headings = soup.select(".heading")
print(headings)  # Çıktısı bir liste olur


