from bs4 import BeautifulSoup
import requests
import pymongo


client = pymongo.MongoClient('localhost', 27017)
test = client['test']
url_list3 = test['url_list3']
item_info = test['item_info']

def get_links_from(channel, page, year):
    # https://sfbay.craigslist.org/search/cta?s=120&max_auto_year=2008&min_auto_year=2008
    list_view = '{}?s={}&min_auto_year={}&max_auto_year={}'.format(channel, str(page), str(year), str(year))
    wb_data = requests.get(list_view)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    for link in soup.select('ul.rows > li'):
        item_link = link.a.get('href')
        if link.find('a', class_='hdrlnk'):
            title = link.find('a', class_='hdrlnk').text
        else:
            title = None
        if link.find('span', class_='result-price'):
            price = link.find('span', class_='result-price').text
        else:
            price = None
        post_time = link.find('time', class_='result-date')['datetime']
        if link.find('span', class_='result-hood'):
            location = link.find('span', class_='result-hood').text
        else:
            location = None
        url_list3.insert_one({'url': item_link})
        print(item_link, price, post_time, location, title)


# for year in range(2008, 2019):
#         for page in range(0, 3000, 120):
#             get_links_from('https://sfbay.craigslist.org/search/cto', page, year)

def get_item_info(url):
    info = {}
    info['url'] = url
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    no_longer_exit = soup.find('div', class_='removed')
    if no_longer_exit:
        pass
    else:
        # find title, price and location
        info['title'] = soup.find('span', id='titletextonly').text if soup.find('span', id='titletextonly') else None
        info['price'] = soup.find('span', class_='price').text if soup.find('span', class_='price') else None
        info['loc'] = soup.find('small').text.strip() if soup.find('small') else None
        # find the details
        details = soup.find('p', class_='attrgroup').find_next_sibling('p') if soup.find('p', class_='attrgroup') else None
        items = details.find_all('span') if details.find_all('span') else None
        for item in items:
            if ':' in item:
                info[item.text.split(':')[0]] = item.text.split(':')[1].strip()
            else:
                pass
        item_info.insert_one(info)