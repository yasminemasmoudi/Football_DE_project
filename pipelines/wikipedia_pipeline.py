def get_wikipedia_page(url):
    import requests

    print ("getting wikipedia page...", url)

    try:
        response = requests.get(url, timeout = 10)
        response.raise_for_status() #check if the request is successful

        return response.text

    except requests.RequestException as e:
        print(f"An error occured:{e}")

def get_wikipedia_data(html):
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find_all("table",{"class": "wikitable sortable"})[0]
    table_rows = table.find_all("tr")
    return table_rows   

def extract_wikipedia_data(**kwargs):
    url = kwargs['url']
    html = get_wikipedia_page(url)
    rows = get_wikipedia_data(html)
    
    data = []
    for i in range (1, len(rows)):
        tds = rows[i].find_all('td') #td table data
        values = {
            'rank': i,
            'stadium': tds[0].text, 
        }

