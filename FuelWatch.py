
"""
Fuel Hook


The best fuel scrapper application out there!

Fuel Hook, scrapes the data from 'http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS' \n
and display the information in a nice table format, sorted by the lowest fuel price.\n



...workin progress
build 0.0.1

"""

import requests as rq
import feedparser as fparse
import os


def Url_edit():
    """
    Called upon twice to edit and return the edited url changing the the\n
    product type upon request and the da
    """

    starndard_url = w

    changed_url = starndard_url.format()

    return changed_url



def hooked ():
    """
    This is the main function being called, try and find what the best/more\n
    pythonic way of starting the script
    """

    starndard_url = 'https://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS'
    raw_rss_feed = rq.get(starndard_url)

    print(raw_rss_feed)

    feed_parsed = fparse.parse(raw_rss_feed.content)

    print(feed_parsed)

hooked()
