
"""
Fuel Hook


The best fuel scrapper application out there!

Fuel Hook, scrapes the data from 'http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS' \n
and display the information in a nice table format, sorted by the lowest fuel price.\n



IDEAS
- matplotlib the previous days in a graph


...workin progress
build 0.0.1

"""

import requests as rq
import feedparser as fparse
import os


def Url_edit(x):
    """
    Called upon twice to edit and return the edited url changing the the\n
    product type upon request and the day.
    """

    starndard_url = 'https://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?day={day_change}'
    changed_url = starndard_url.format(day_change = x)
    return changed_url

def List_maker(x):
    """
    This function is to re iterate throught the passed data pull out the price data\n
    and place it in a list.
    """
    List_of_data = []

    for info in x:
        List_of_data.append({'Summary':info['summary_detail']['value'],
        'Price':info['price'],
         'Location':info['location']})

    print(List_of_data)

    return List_of_data


def hooked ():
    """
    This is the main function being called, try and find what the best/more\n
    pythonic way of starting the script.
    """

    raw_rss_feed_today = rq.get(Url_edit('today'))
    raw_rss_feed_tomorrow = rq.get(Url_edit('tomrorow'))
    print(raw_rss_feed_today, 'Pass: Today feed.')
    print(raw_rss_feed_tomorrow, 'Pass: Tomorrow feed.\n')

    feed_parsed_today = fparse.parse(raw_rss_feed_today.content)
    feed_parsed_tomorrow = fparse.parse(raw_rss_feed_tomorrow.content)
    List_maker(feed_parsed_today.entries)
    List_maker(feed_parsed_tomorrow.entries)

hooked()
