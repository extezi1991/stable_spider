import furl
import csv
from scraping import *
def csv_read(data):
    with open('other.txt', 'r') as f:
        for line in f:
            url = str(line.strip('\n'))
            f = furl.furl(url)
            clear_file = str(f.path).split('/')
            data_file = clear_file[3]

        with open(data_file + 'csv', 'a') as file:
            writer = csv.writer(file)
            writer.writerow((data[clear_price], data[clear_stock]))
            csv_read(data)