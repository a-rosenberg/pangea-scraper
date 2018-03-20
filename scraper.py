#!/usr/bin/emv python

from __future__ import print_function

import re
import requests
import os


def pangea_scrape(target, landing_zone=os.path.join('static', 'data')):
    with open(target) as fid:
        for line in fid:
            items = [x.strip() for x in line.split('\t')]
            if re.match('^\d{4}-.+', items[0]):
                link = items[-1]
                download = requests.get(link)
                with open(os.path.join(landing_zone, os.path.basename(link)), 'w') as fid:
                    print(link, download.status_code)
                    fid.write(download.content)


if __name__ == '__main__':
    target = os.path.join('static', 'download_lists',
                          'M139-em122_bathy_filelist.tab')
    pangea_scrape(target=target)