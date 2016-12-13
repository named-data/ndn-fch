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

class PointWithInfo:
    def __init__(self, point, info):
        self.point = point
        self.info = info

    def __len__(self):
        return 2

    def __getitem__(self, index):
        return self.point[index]

    def __str__(self):
        return "%s@%s" % (self.info, self.point)
