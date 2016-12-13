#!/usr/bin/env python3
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

import os
import sys

BASEDIR = os.path.abspath(os.path.dirname(__file__))

# activate virtualenv
activate_this = os.path.join(BASEDIR, ".python/bin/activate_this.py")
exec(open(activate_this).read(), {'__file__': activate_this})

if BASEDIR not in sys.path:
   sys.path.append(BASEDIR)

import flask_script
import urllib
import gzip
import shutil

import ndn_fch

app = ndn_fch.create("%s/config.py" % os.path.abspath(os.path.dirname(__file__)))
manager = flask_script.Manager(app)

@manager.command
def update_hubs():
    """Fetch/update the hub list"""
    urllib.request.urlretrieve(manager.app.config['HUBS_URL'], filename=manager.app.config['HUBS_PATH'])
    return 0

@manager.command
def update_geodb():
    """Fetch/update the ip-location database"""
    tmpFile = "%s.gz" % manager.app.config['GEODB_PATH']
    urllib.request.urlretrieve(manager.app.config['GEODB_URL'], filename=tmpFile)
    with gzip.open(tmpFile, 'rb') as inF, open(manager.app.config['GEODB_PATH'], 'wb') as outF:
        shutil.copyfileobj(inF, outF)
    return 0

if __name__ == '__main__':
    manager.run()
