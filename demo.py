# A portion of a_music_xml_extract
# Copyright (C) 2025 paul mccombs
# Adapted from Python 2 to Python 3

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see http://www.gnu.org/licenses/.

# loads the code that parses the Library.XML and provides a handful of functions to list the data
import library_parse_mod as pmod
import datetime
import zoneinfo

# Produces two dictionaries
#    all_songs: the key is a unique integer assigned by Music to the song.
#               the value is a dictionary with descriptive keys and corresponding values, the value type vary depending on the key.
#               Note: see all_keys below
#    all_lists: the key is a string containing the play list title show in Music.
#               the value a set of song key integers
(all_songs, all_lists) = pmod.parse_XML()

# Produces a set of key strings that can be found in the values of the all_songs dictionary.
#    This set is created by exhaustively checking the values in all_songs
#    Note: the keys are sparsely populated, you can't count on them existing in every value
all_keys = pmod.collect_keys(all_songs)

# Ask the user for a string to search for artist name
name_input = input("Enter an artists name to query: ")

# Look in all_songs for artist strings that include the requested text
for key in all_songs:
    if 'Artist' in all_songs[key] and name_input.lower() in all_songs[key]['Artist'].lower():
        print(all_songs[key]['Artist'] + ": "+all_songs[key]['Name']+"\n")
        if 'Play Date UTC' not in all_songs[key]:
            pacdate = "Never"
        else:
            playdate = all_songs[key]['Play Date UTC']
            awaredate = playdate.replace(tzinfo=zoneinfo.ZoneInfo(key='UTC'))
            pacdate = awaredate.astimezone(zoneinfo.ZoneInfo(pmod.time_zone_string()))
        print("     Last played: "+str(pacdate)+"\n")
        print("     Key        : "+str(key)+"\n")
