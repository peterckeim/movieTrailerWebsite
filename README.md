# trailerWebsite
Movie Trailer Website -- Project 1 for Full-Stack Web Dev Udacity Program

**Assignment**:

You will write server-side code to store a list of your favorite movies, including box art imagery and a movie trailer URL. 
You will then serve this data as a web page allowing visitors to review their movies and watch the trailers.

----

This series of files seeks to do just that! This project takes an **.xls (excel file** with data containing info on a movie, tv show, or video game's box-art and trailer, then uses this information to output a mobile-friendly website which gives quick access to viewing box-art and trailers.

###Please note!!!:###

**The xlrd library is required to run this program**

xlrd can be downloaded on the official Python website at https://pypi.python.org/pypi/xlrd . This library is a standard in basic excel file manipulation for Python. For more information on xlrd, check out the documentation for it and its sister programs here: http://www.python-excel.org/

The base of this file is the fresh_tomatoes.py file (renamed to trailer_land.py) given to us by Udacity through the Programming Foundations with Python course. It has been tweaked in select areas to suit the additional styles and scripting for the page. Additionally, this project uses the files _media.py_ and _entertainment_center.py_ files which were created during the lessons of the Programming Foundations with Python Udacity course.

**What this version of the code does significantly different from the originally directed files is:**

-Read data from excel instead of having data stored on the .py file
-Create a dynamic dictionary based on the excel file for each video type (Movie, TV Show, Game)
-Create three total sections in the final outputted .html file.

----
##Running the Program##

Running this program is very straightforward. To begin, download this repository. You should only have 4 files in total:

_entertainment_center.py_, (The data extractor)

_media.py_, (The class holder)

_trailer_land.py_, (The HTML formatter)

_trailerWebsiteData.xls_ (The data)

To run the program, simply open any shell (I prefer Powershell or Spyder), navigate to the folder location, and run python on the file **_entertainment_center.py_**. The output website should pop up automatically in your default browser.

Any amount of movies, tv shows, or games in the Excel data are able to be parsed through this program. **When editing the excel data, you must be sure to fill in all 4 columns (Type, Title, Poster, Trailer). Currently the program does not have a catch for any missing data. Please be sure to also capitalize the first letter of the video type.

I do not have plans on revamping this code further, unless it does not meet specifications. Please let me know what more I can do to help.
