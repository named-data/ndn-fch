"""
Copyright (c) 2016, Regents of the University of California.

This file is part of NDN-FCH (Find Closest NDN Hub).  See AUTHORS.md
for complete list of NFD authors and contributors.

NDN-FCH is free software: you can redistribute it and/or modify it under the terms
of the GNU General Public License as published by the Free Software Foundation,
either version 3 of the License, or (at your option) any later version.

NFD is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
NDN-FCH, e.g., in COPYING.md file.  If not, see <http://www.gnu.org/licenses/>.
"""

from flask import Flask
from .server import server

def create(configFile, name=__name__):
    app = Flask(name,
                template_folder='./_templates',
                static_folder='../_static')
    app.config.from_pyfile(configFile)

    try:
        app.register_blueprint(server)
    except:
        print ("Cannot initialize application.  Make sure geoip and hub databases are initialized")
        print ("    ./manage.py update_hubs && ./manage.py update_geodb")
    return app
