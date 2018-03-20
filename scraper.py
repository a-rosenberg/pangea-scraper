#!/usr/bin/env python

from __future__ import print_function

import re
import requests
import os


def pangea_scrape(target, landing_zone=os.path.join('static', 'data')):
    """Main function to get files from Pangea generated download list to landing
    zone.

    Args:
        target (str): Data list path.  Download datalist from Pangea
            dataset page.
        landing_zone (str): Download location path.  Defaults to ./static/data.

    Returns:
        None
    """
    with open(target) as oid:
        for line in oid:
            items = [x.strip() for x in line.split('\t')]
            if re.match('^\d{4}-.+', items[0]):  # if download list line starts with a date
                link = items[-1]
                download = requests.get(link)
                download_path = os.path.join(landing_zone,
                                             os.path.basename(link))
                with open(download_path, 'w') as fid:
                    print(link, download.status_code)
                    fid.write(download.content)


if __name__ == '__main__':
    target = os.path.join('static', 'download_lists',
                          'M139-em122_bathy_filelist.tab')
    pangea_scrape(target=target)
