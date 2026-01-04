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
import pandas as pd

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

############# Functions
# Returns a list of keys that match a query
def find_keys (search_choice, search_string):
    search_choices = { '1': "Artist", '2': "Name", '3': "Album"}
    keys = []

    for key in all_songs:
        if search_choices[search_choice] in all_songs[key] and search_string.lower() in all_songs[key][search_choices[search_choice]].lower():
            keys.append(key)

    return keys

# Returns a brief pandas data frame with one row for the provided song key
def brief_result (key):
    result = pd.DataFrame(columns=['SongKey', 'Title', 'Artist', 'Album',"LastPlay"])
    
    #print(str(key) + ") " +  all_songs[key]['Artist'] + ": "+all_songs[key]['Name'])
    #print(all_songs[key]['Album'])
    if 'Play Date UTC' not in all_songs[key]:
        pacdate = "Never"
    else:
        playdate = all_songs[key]['Play Date UTC']
        awaredate = playdate.replace(tzinfo=zoneinfo.ZoneInfo(key='UTC'))
        pacdate = awaredate.astimezone(zoneinfo.ZoneInfo(pmod.time_zone_string()))
    results.loc[len(results)] = [key, all_songs[key]['Name'], all_songs[key]['Artist'], all_songs[key]['Album'], pacdate]
    #print("     Last played: "+str(pacdate)+"\n")
    return result

# Print long song description given a song key
def long_print (key):
    print(all_songs[key])
    return

# Main Program Loop
while True:

    # Prompt user for a search type
    print("""
    1) Search by Artist
    2) Search by Song Title
    3) Search by Album Title
    4) All details for song key
    Q) Exit this demo
    """)

    choice = input("Press the number corresponding to the search you want:").lower()

    match choice:
        case "1":
            # Ask the user for a string to search for artist name
            name_input = input("Enter an artist's name to search: ")
            songs = find_keys(choice, name_input)
            results = pd.DataFrame(columns=['SongKey', 'Title', 'Artist', 'Album',"LastPlay"])
            for song_key in songs:
                result = brief_result(song_key)
                results = pd.concat([results, result], ignore_index=True)
            with pd.option_context('display.max_rows', None):
                print(results)
        case "2":
            # Ask the user for a string to search for song title
            name_input = input("Enter a song title to search: ")
            songs = find_keys(choice, name_input)
            results = pd.DataFrame(columns=['SongKey', 'Title', 'Artist', 'Album',"LastPlay"])
            for song_key in songs:
                result = brief_result(song_key)
                results = pd.concat([results, result], ignore_index=True)
            with pd.option_context('display.max_rows', None):
                print(results)
        case "3":
            # Ask the user for a string to search for album title
            name_input = input("Enter an album title to search: ")
            songs = find_keys(choice, name_input)
            results = pd.DataFrame(columns=['SongKey', 'Title', 'Artist', 'Album',"LastPlay"])
            for song_key in songs:
                result = brief_result(song_key)
                results = pd.concat([results, result], ignore_index=True)
            with pd.option_context('display.max_rows', None, 'display.max_columns', None):
                print(results)
        case "4":
            # Ask for the key to print details
            song_key = int(input("Enter the key of the song you want details for:"))
            long_print(song_key)
        case "q":
            print("Goodbye")
            break
        case _:
            print("You have made an invalid choice")

            
