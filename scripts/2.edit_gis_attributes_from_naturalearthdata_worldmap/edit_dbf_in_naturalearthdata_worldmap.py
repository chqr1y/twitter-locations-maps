#!/usr/bin/env python3

import dbf
import json
import zipfile
import tempfile

f_json_locations_from_twitter_api = '../../raw_data/twitter_available_locations_countries.json'
filename_earthdata_in = '../../raw_data/ne_50m_admin_0_countries.zip'
filename_earthdata_out = 'ne_50m_admin_0_countries_with_twitter_locations.zip'


def edit_dbf_database(dbf_filename):
    def get_twitter_countries():
        def patch(locations):
            for loc in locations:
                if loc['name'] == 'United States':
                    loc['name'] = 'United States of America'
                elif loc['name'] == 'Korea':
                    loc['name'] = 'South Korea'
            return locations
        countries = {}
        f = open(f_json_locations_from_twitter_api, 'r')
        locations = json.load(f)

        # In order to make the country names match between both inputs,
        # we correct some names in the data coming from twitter.
        locations = patch(locations)

        for loc in locations:
            if loc['placeType']['name'] == 'Country':
                countries[loc['name']] = loc['woeid']

        # We sort by alphanum order the names of the countries.
        countries = dict(sorted(countries.items()))
        return countries
        
    def gen_world_countries(table):
        # As for twitter inputs,
        # we sort by alphanum order the names of the countries
        table_sorted = table.create_index(lambda rec: rec.name_en)
        for rec in table_sorted:
            yield rec

    twitter_countries = get_twitter_countries()
    table = dbf.Table(dbf_filename, codepage='utf8')
    table.open(mode=dbf.READ_WRITE)
    table.codepage = dbf.CodePage('utf8')
    table.add_fields('tw_woeid N(8,0)')
    
    # We browse the different countries present in the dataset provided by NE,
    # if the name of a country match with the twitter dataset,
    # we put his WOEID associated, otherwise -1.
    next_world_country = gen_world_countries(table)
    world_c = next(next_world_country)
    for key in twitter_countries:
        while(world_c.name_en.strip() < key):
            dbf.write(world_c, tw_woeid=-1)
            world_c = next(next_world_country)
        if world_c.name_en.strip() == key:
            dbf.write(world_c, tw_woeid=twitter_countries[key])
            world_c = next(next_world_country)
    for world_c in next_world_country:
        dbf.write(world_c, tw_woeid=-1)
        
    table.close()


zip_in = zipfile.ZipFile(filename_earthdata_in, 'r')
zip_out = zipfile.ZipFile(filename_earthdata_out, 'w')

for item in zip_in.infolist():
    file_content = zip_in.read(item.filename)
    if item.filename[-4:] == '.dbf':
        f_dbf = tempfile.NamedTemporaryFile()
        f_dbf.write(file_content)
        f_dbf.seek(0)
        edit_dbf_database(f_dbf.name)
        f_dbf.seek(0)
        file_content = f_dbf.read()
        f_dbf.close()
    zip_out.writestr(item, file_content)

zip_in.close()
zip_out.close()
