
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
    product type upon request and the da
    """

    starndard_url = 'https://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?day={day_change}'

    changed_url = starndard_url.format(day_change = x)

    return changed_url



def hooked ():
    """
    This is the main function being called, try and find what the best/more\n
    pythonic way of starting the script
    """


    raw_rss_feed_today = rq.get(Url_edit('today'))
    raw_rss_feed_tomorrow = rq.get(Url_edit('tomrorow'))
    print(raw_rss_feed_today)
    print(raw_rss_feed_tomorrow)
    feed_parsed_today = fparse.parse(raw_rss_feed_today.content)
    print(feed_parsed_today)

hooked()
