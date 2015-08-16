import media
import trailer_land
import xlrd
import re
# PLEASE NOTE -- xlrd MUST BE INSTALLED for this to work -- 
# the data is pulled from an .xls sheet as a way to conveniently add and remove items.

#This file will first look through the data within 'trailerWebsiteData.xls', make the appropriate class for the appropriate video type, 
#and append it to 3 distinct lists of the server-side code

file_location = "trailerWebsiteData.xls"
workbook = xlrd.open_workbook(file_location)
sheet = workbook.sheet_by_index(0)
# This puts all of the sheet data from the first sheet in 'trailerWebsiteData.xls' into python.
# On to extracting...
movie_dict = {}
movie_string_int = 0
tvshow_dict = {}
tvshow_string_int = 0
game_dict = {}
game_string_int = 0

for row in range(1,sheet.nrows):
    row_list = []
    for col in range(sheet.ncols):
        row_list.append(sheet.cell_value(row, col))
    if row_list[0] == "Movie":
        print "This is a Movie"
        movie_dict[movie_string_int] = media.Video(row_list[1],row_list[2],row_list[3],row_list[4])
        movie_string_int += 1
    elif row_list[0] == "TVShow":
        print "This is a TV Show"
        tvshow_dict[tvshow_string_int] = media.Video(row_list[1],row_list[2],row_list[3],row_list[4])
        tvshow_string_int += 1
    elif row_list[0] == "Game":
        print "This is a Game"
        game_dict[game_string_int] = media.Video(row_list[1],row_list[2],row_list[3],row_list[4])
        game_string_int += 1
    else:
        print "there was an error with this one..."

trailer_land.open_movies_page(movie_dict,tvshow_dict,game_dict)

#for i in movie_dict:
#        movie_dict[i].print_info()
#for i in tvshow_dict:
#    tvshow_dict[i].print_info()
#for i in game_dict:
#    game_dict[i].print_info()
        