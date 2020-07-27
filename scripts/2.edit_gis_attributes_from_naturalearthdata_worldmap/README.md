## How it's work?

This script takes as input a zip file of th GIS map provide by Natural Earth and a JSON file containing the twitter trends locations provided by the twitter API.
Example :
1. Map : https://www.naturalearthdata.com/http//www.naturalearthdata.com/download/50m/cultural/ne_50m_admin_0_countries.zip
1. Twitter trends available : https://developer.twitter.com/en/docs/trends/locations-with-trending-topics/api-reference/get-trends-available

This script generates a new ZIP file containing the GIS map and for each country a "tw_woeid" field. The value of this field is either the whoid proved by twitter or '-1'.

## Install

```bash
$python3 -m venv venv
$source venv/bin/activate
(venv) $ pip install -r requirements.txt
```

## Usage
1. Check input files (f_json_locations_from_twitter_api and filename_earthdata_in) :
```bash
$ head -n 11 edit_dbf_in_naturalearthdata_worldmap.py
#!/usr/bin/env python3

import dbf
import json
import zipfile
import tempfile

f_json_locations_from_twitter_api = '../../raw_data/twitter_available_locations_countries.json'
filename_earthdata_in = '../../raw_data/ne_50m_admin_0_countries.zip'
filename_earthdata_out = 'ne_50m_admin_0_countries_with_twitter_locations.zip'
```
2. Run
```bash
(venv) $ python3 edit_dbf_in_naturalearthdata_worldmap.py
(venv) $ unzip -l ne_50m_admin_0_countries_with_twitter_locations.zip 
Archive:  ne_50m_admin_0_countries_with_twitter_locations.zip
  Length      Date    Time    Name
---------  ---------- -----   ----
    23632  2018-05-21 00:28   ne_50m_admin_0_countries.README.html
        7  2018-05-21 00:28   ne_50m_admin_0_countries.VERSION.txt
        5  2018-05-21 00:24   ne_50m_admin_0_countries.cpg
   548939  2018-05-21 00:24   ne_50m_admin_0_countries.dbf
      143  2018-05-21 00:24   ne_50m_admin_0_countries.prj
  1612740  2018-05-21 00:24   ne_50m_admin_0_countries.shp
     2028  2018-05-21 00:24   ne_50m_admin_0_countries.shx
---------                     -------
  2187494                     7 files

```
