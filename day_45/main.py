from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")

yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, "html.parser")
all_articles = soup.find_all(name = "span", class_ = "titleline")
article_text = []
article_link = []
for article in all_articles:
    artcl = article.find("a")
    text = article.find("a").getText()
    article_text.append(text)
    link = artcl.get("href")
    article_link.append(link)

article_upvote = soup.find_all(name="span", class_="score")
article_score = []
for upvote in article_upvote:
    score = upvote.getText().split()[0]
    article_score.append(int(score))
 
print(article_text[0])
print(article_link[0])    
sorted(article_score, reverse=True)
print(article_score[0])
































# with open("day_45\website.html") as file:
#     contents = file.read()
    
# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.title)
# # print(soup.title.string)
# # print(soup.prettify())  
# all_anchor_tags = soup.find_all(name = "a")
# # for tag in all_anchor_tags:
#     # print(tag.getText())
#     # print(tag.get("href"))
    
# heading = soup.find(name = "h1", id = "name")
# print(heading.get("id"))

# company_url = soup.select_one(selector = "p a")
# print(company_url)