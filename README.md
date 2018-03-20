# Pangea file scraper
To grab German bathymetric data for NCEI archiving.

Will not work with data under a moratorium

## Example
https://doi.pangaea.de/10.1594/PANGAEA.881298?format=html#download
- 'Download dataset as tab-delimited text' in ASCII format.
- set target to this download file in main function of `scraper.py`
- downloads default to `static/data`
