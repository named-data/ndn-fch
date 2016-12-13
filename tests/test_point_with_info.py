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

from ndn_fch.point_with_info import PointWithInfo

class TestPointWithInfo(unittest.TestCase):

    def test_basic(self):
        point = PointWithInfo((5, 1), {'key': 'value'})
        self.assertEqual(2, len(point))
        self.assertEqual(5, point[0])
        self.assertEqual(1, point[1])
        self.assertEqual("{'key': 'value'}@(5, 1)", str(point))

if __name__ == '__main__':
    unittest.main()
    
