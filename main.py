from bs4 import BeautifulSoup
import requests

def getHTMLdocument(url):
    response = requests.get(url)
    return response.text

url_to_scrape = "tourisme.exemple"
#https://www.bordeaux-tourisme.com/ville-patrimoine

soup = BeautifulSoup(getHTMLdocument(url_to_scrape), 'html.parser')

def getInMesh(mesh):
    title = mesh.find(class_="Card-title").text.strip()
    prehref = mesh.find('a')
    href = prehref.get('href')
    src = mesh.find('img')
    fsrc = src.get('data-src')
    return [title, href, "https://www.bordeaux-tourisme.com"+fsrc]


def getContent(link):
    soup_link = BeautifulSoup(getHTMLdocument(link), 'html.parser')
    infolist = len(soup_link.find_all(class_="Infos-list")) > 0
    information = []
    imgs = []
    if infolist:
        for info in soup_link.find_all(class_="Infos-list"):
            information.append(info.text.replace("\n", "").strip())
    if infolist:
        for info in soup_link.find_all(class_="SiteInfos-list"):
            information.append(info.text.replace("\n", "").strip())
    for images in soup_link.find_all('img'):
        if images.get('data-src') is not None:
            imgs.append("https://www.bordeaux-tourisme.com" + images.get('data-src'))
    return [information, imgs]

for meshitems in soup.find_all(class_="Mesh-item"):
    print(getInMesh(meshitems))
    print(getContent(getInMesh(meshitems)[1]))
    print("\n\n")