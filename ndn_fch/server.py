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

from flask import Blueprint, render_template, request, abort, current_app
import geoip2.database
import kdtree
import json
import urllib.parse

from .point_with_info import PointWithInfo

# conversion factor km -> mi
KM_TO_MI = 0.621371

server = Blueprint('server', __name__, template_folder="_templates")

@server.record
def initializeState(appState):
    app = appState.app

    app.GEODB = geoip2.database.Reader(app.config['GEODB_PATH'])

    hubList = json.load(open(app.config['HUBS_PATH'], encoding="utf-8"))
    app.HUB_INDEX = kdtree.create([PointWithInfo(
        value['_real_position'] if '_real_position' in value else value['position'],
        {'name': value['name'], 'host': urllib.parse.urlparse(value['site']).hostname})
        for key,value in hubList.items() if value['fch-enabled'] != False])


def validateCoordintate(lat, lon):
    try:
        lat = float(lat)
        lon = float(lon)

        # check to make sure the latitude and longitude values are valid
        if lat < -90. or lat > 90. or lon < -180. or lon > 180.:
            return None

        return (lat, lon)
    except ValueError:
        return None

@server.route('/')
def getClosestHub():
    if "lat" in request.args and "lon" in request.args:
        location = validateCoordintate(request.args["lat"], request.args["lon"])
        if not location:
            return abort(403)
    else:
        if "lat" in request.args or "lon" in request.args:
            return abort(403)

        try:
            result = current_app.GEODB.city(request.remote_addr)
            location = (result.location.latitude, result.location.longitude)
        except:
            location = current_app.config['DEFAULT_LOCATION']

    try:
        k = int(request.args.get("k", 1))
        if k < 1:
            k = 1
        elif k > 10:
            k = 10
    except:
        return abort(403)

    result = current_app.HUB_INDEX.search_knn(location, k)
    hubs = [point.data.info for point,distance in result]
    if "verbose" in request.args:
        return render_template("verbose.html", hubs=hubs)
    else:
        return render_template("simple.txt", hubs=hubs), 200, {'Content-Type': 'text/plain; charset=utf-8'}
