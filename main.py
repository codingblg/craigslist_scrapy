from page_parsing import *
from multiprocessing import Pool
if __name__ == '__main__':
    url_list = list(url_list3.find({},{'url':1, '_id':0}))
    for url in url_list:
        print(url['url'])
        get_item_info(url['url'])