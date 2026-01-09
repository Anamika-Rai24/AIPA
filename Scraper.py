import requests
from bs4 import BeautifulSoup
abc = "https://sarkariresult.com.cm"
response = requests.get(abc)
if response.status_code==200:
    print("Successfully fetched webpage")
else:
    print("Error fetched page")
html_contant = response.text
if html_contant:
    Soup = BeautifulSoup(html_contant,"html.parser")
    title = Soup.title.string
    print(title)

# 1. Extract all heading (h1-h6)
# for i in range(1,7):
#     for heading in Soup.find_all(f"h{i}"):
#         print(f"heading{i}{heading.get_text(strip=True)}")

# 2. Extract all content in webpage
# for paragraph in Soup.find_all("p"):
#     print(paragraph.get_text(strip=True))

# 3. Extract all link in webpage
# for a in Soup.find_all("a"):
#     text = a.get_text(strip=True)
#     href = a["href"]
#     print(text , href)

# 4.Extract all Images in webpage
for img in Soup.find_all("img"):
    src = img["src"]
    print(src) 



                 

