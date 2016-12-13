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

BASEDIR = os.path.abspath(os.path.dirname(__file__))

# activate virtualenv
activate_this = os.path.join(BASEDIR, "../.python/bin/activate_this.py")
exec(open(activate_this).read(), {'__file__': activate_this})

import unittest
from flask_testing import TestCase

import ndn_fch
app = ndn_fch.create("%s/../config.py" % BASEDIR)

class TestServer(TestCase):

    def create_app(self):
        return app

    def test_config(self):
        self.assertIn('DEFAULT_LOCATION', app.config)
        self.assertEqual(2, len(app.config['DEFAULT_LOCATION']))
        self.assertTrue(isinstance(app.config['DEFAULT_LOCATION'][0], float))
        self.assertTrue(isinstance(app.config['DEFAULT_LOCATION'][1], float))

    def test_default(self):
        # Ensure Flask is setup.
        response = self.client.get('/')
        self.assert200(response)
        self.assertNotEqual(0, len(response.data))
        self.assertTemplateUsed("simple.txt")

        response = self.client.get('/', environ_base={'REMOTE_ADDR': '131.179.196.1'})
        self.assert200(response)
        self.assertNotEqual(0, len(response.data))
        self.assertTemplateUsed("simple.txt")

    def test_verbose(self):
        # Ensure Flask is setup.
        response = self.client.get('/?verbose')
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(0, len(response.data))
        self.assertTemplateUsed("verbose.html")

    def test_k(self):
        response = self.client.get('/?k=0')
        self.assert200(response)
        self.assertEqual(1, len(response.data.split(b',')))
        self.assertTemplateUsed("simple.txt")

        for k in range(1, 11):
            response = self.client.get('/?k=%d' % k)
            self.assert200(response)
            self.assertNotEqual(0, len(response.data))
            self.assertEqual(k, len(response.data.split(b',')))
            self.assertTemplateUsed("simple.txt")

        response = self.client.get('/?k=11')
        self.assert200(response)
        self.assertEqual(10, len(response.data.split(b',')))
        self.assertTemplateUsed("simple.txt")

        response = self.client.get('/?k=foobar')
        self.assert403(response)

    def test_lat_lon(self):
        self.assert200(self.client.get('/?lat=1&lon=2'))

        self.assert403(self.client.get('/?lat=91&lon=2'))
        self.assert403(self.client.get('/?lat=-91&lon=2'))

        self.assert200(self.client.get('/?lat=1&lon=91'))
        self.assert200(self.client.get('/?lat=1&lon=-91'))

        self.assert403(self.client.get('/?lat=1&lon=181'))
        self.assert403(self.client.get('/?lat=1&lon=-181'))

        self.assert403(self.client.get('/?lat=foo&lon=bar'))
        self.assert403(self.client.get('/?lat=foo'))

    def test_404(self):
        response = self.client.get('/test')
        self.assert404(response)

if __name__ == '__main__':
    unittest.main()
