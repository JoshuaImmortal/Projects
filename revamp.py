from bs4 import BeautifulSoup
import requests
space = ''
maze = ''
faze = ''
page = requests.get("https://cyclobold.com").text
soup = BeautifulSoup(page, "html5lib")
wrappers = soup.find_all("div", {"class": "col-md-6 col-lg-3 mb-4"})
for wrap in wrappers:
    wrap_img = wrap.find("img", {"class": "lazy img-fluid"})
    wrap_titles = wrap.find("h6", {"class": "mt-3 mb-0"}).text
    wrap_content = wrap.find("div", {"class": "small"}).text
    space += str(wrap_img)
    maze += (wrap_titles)
    faze += (wrap_content)
projekt = open("project.pdf", "w")
projekt.write(space)
projekt.write(maze)
projekt.write(faze)
projekt.close()