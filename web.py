import requests

from bs4 import Beautiful Soup

import pandas import argparse

parser = argparse. ArgumentParser)

parser.add_argument ("-page_num_max", help="Enter the number of pages to parse", type=int)

args = parser.parse_args()

oyo_url = "https://www.oyorooms.com/hotels-in-bangalore/?page="

page num_MAX = args.page_num_max scraped_info_list = 11

for page_num in range (1, page_num_MAX):

req = requests.get logo url + str(page_num)) content = req.content

soup = BeautifulSoup(content, "html.parser")

all_hotels = soup.find_all("div", "class": "hotelcardlisting" })

for hotel in all hotels:

hotel_dict = 0)

hotel_dict ["name"] = hotet. find ("h3", ("class": "ListingHotelDescription_hote lName")}). text
hotel_dict ["address" = batel.find("span", ("itemprop": "streetAddress"}).text

hotel_dict "price") = hotel.find("span", ("class": "ListingPrice_finaLPrice"}). text

try in except

try: hotel_dict ["rating"] = hotel.find("span", {"class" : "hotelRating_rating Summary"}).text
