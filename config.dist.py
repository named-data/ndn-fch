# Enable debugging
# DEBUG = True

# GeoLite2 database location
GEODB_URL = 'http://geolite.maxmind.com/download/geoip/database/GeoLite2-City.mmdb.gz'

# Local path to where the geo database will be downloaded
GEODB_PATH = '.tmp/geodb.mmdb'

# URL to NDN hub information
HUBS_URL = 'http://ndnmap.arl.wustl.edu/json/geocode/'
# Expected format: JSON
# Expected structure:
#
#     {
#        "<id>": {
#            "site": "http://hobo.cs.arizona.edu:80/",
#            "position": [ 32.22896140, -110.94832260 ],
#            "_real_position": [ 32.22896140, -110.94832260 ], # optional
#        },
#        "<id2>": {
#            ...
#        },
#        ...
#     }

# Local path to where the hub information will be downloaded
HUBS_PATH = '.tmp/hubs.json'

# Default that is returned whenever the system cannot determine the location
DEFAULT_LOCATION = (34.1340213, -118.3238652)
