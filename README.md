# twitter-locations-maps
This repository provides topojson maps with twitter location identifiers (WOEID).

Why this repository ?
---------------------

The objective of this repository is to provide topojson maps mixing naturalearthdata world maps and twitter geographic informations.

Input DATA
----------

- World map : https://www.naturalearthdata.com/downloads/50m-cultural-vectors/

- Twitter Trending Places providing by twitter API https://developer.twitter.com/en/docs/trends/trends-for-location/api-reference/get-trends-place 

Output DATA
-----------

Those Topojson maps containing all the data provided by Natural Earth maps and for each country, a new field called tw_woeid containing the WOEID known by twitter or -1 if twitter does not use it for these trends.

Acknowledgement
---------------

Natural Earth Data : https://www.naturalearthdata.com/

Twitter : https://developer.twitter.com/
