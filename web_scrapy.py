from bs4 import BeautifulSoup
import requests


start_url = "https://sfbay.craigslist.org"     # main page


def get_channel_urls(url):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    links = soup.select('div#sss > div.cats > ul > li > a')
    for link in links:
        page_url = start_url + link.get('href')
        print(page_url)


get_channel_urls(start_url)

channel_list = '''
    https://sfbay.craigslist.org/d/antiques/search/ata
    https://sfbay.craigslist.org/d/appliances/search/ppa
    https://sfbay.craigslist.org/d/arts-crafts/search/ara
    https://sfbay.craigslist.org/d/atvs%2C-utvs%2C-snowmobiles/search/sna
    https://sfbay.craigslist.org/d/auto-parts/search/pta
    https://sfbay.craigslist.org/d/aviation/search/ava
    https://sfbay.craigslist.org/d/baby-kid-stuff/search/baa
    https://sfbay.craigslist.org/d/barter/search/bar
    https://sfbay.craigslist.org/d/health-and-beauty/search/haa
    https://sfbay.craigslist.org/d/bicycle-parts/search/bip
    https://sfbay.craigslist.org/d/bicycles/search/bia
    https://sfbay.craigslist.org/d/boat-parts-accessories/search/bpa
    https://sfbay.craigslist.org/d/boats/search/boo
    https://sfbay.craigslist.org/d/books-magazines/search/bka
    https://sfbay.craigslist.org/d/business/search/bfa
    https://sfbay.craigslist.org/d/cars-trucks/search/cta
    https://sfbay.craigslist.org/d/cds-dvds-vhs/search/ema
    https://sfbay.craigslist.org/d/cell-phones/search/moa
    https://sfbay.craigslist.org/d/clothing-accessories/search/cla
    https://sfbay.craigslist.org/d/collectibles/search/cba
    https://sfbay.craigslist.org/d/computer-parts/search/syp
    https://sfbay.craigslist.org/d/computers/search/sya
    https://sfbay.craigslist.org/d/electronics/search/ela
    https://sfbay.craigslist.org/d/farm-garden/search/gra
    https://sfbay.craigslist.org/d/free-stuff/search/zip
    https://sfbay.craigslist.org/d/furniture/search/fua
    https://sfbay.craigslist.org/d/garage-moving-sales/search/gms
    https://sfbay.craigslist.org/d/general-for-sale/search/foa
    https://sfbay.craigslist.org/d/heavy-equipment/search/hva
    https://sfbay.craigslist.org/d/household-items/search/hsa
    https://sfbay.craigslist.org/d/jewelry/search/jwa
    https://sfbay.craigslist.org/d/materials/search/maa
    https://sfbay.craigslist.org/d/motorcycle-parts-accessories/search/mpa
    https://sfbay.craigslist.org/d/motorcycles-scooters/search/mca
    https://sfbay.craigslist.org/d/musical-instruments/search/msa
    https://sfbay.craigslist.org/d/photo-video/search/pha
    https://sfbay.craigslist.org/d/recreational-vehicles/search/rva
    https://sfbay.craigslist.org/d/sporting-goods/search/sga
    https://sfbay.craigslist.org/d/tickets/search/tia
    https://sfbay.craigslist.org/d/tools/search/tla
    https://sfbay.craigslist.org/d/toys-games/search/taa
    https://sfbay.craigslist.org/d/trailers/search/tra
    https://sfbay.craigslist.org/d/video-gaming/search/vga
    https://sfbay.craigslist.org/d/wanted/search/waa
    https://sfbay.craigslist.org/d/auto-wheels-tires/search/wta

'''