from urllib.parse import  urlparse
import requests,random
from bs4 import BeautifulSoup


query=input("enter place")
url = 'https://www.google.com/search?q='
urls = []
out_put = []
final_links = []
output = []
last = []
def search(query):
    data = requests.get(url+'best places to visite in' + f'{query}'+'from traveltriangle').text
    soup = BeautifulSoup(data, 'html.parser')
    for links in soup.find_all('a'):
        href = links.get('href')
        urls.append(href)
       # print(urls)
    for i in urls:
        clean_url = i.split('/url?q=')[1:]
        if len(clean_url) != 0:
            out_put.append(clean_url)
    for i in out_put:
        for j in i:
            final_links.append(j)
    for j in final_links:
        if 'https://support.google.com' not in j and 'https://accounts.google.com' not in j and 'https://www.youtube.com/' not in j:
            if 'https://stackoverflow.com/' not in j and 'https:/maps.google.com/' not in j:
                output.append(j)


search(query)
for i in output:
    parse = urlparse(i)
    url = parse.path
    last_slash_index = url.rfind('/')
    sa_index = url.find('&sa')
    url_without_param = url[:sa_index]
    a = 'https://', parse.netloc, url_without_param
    url = ''.join(a)
    last.append(url)



rand = random.choice(last)
r = requests.get(rand)
data = r.text
places=[]
soup = BeautifulSoup(data,'html.parser')
for link in soup.find_all('h3'):
    places = link.get_text()
    print(places)