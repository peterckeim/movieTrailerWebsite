import webbrowser

#This file contains the classes which will be used in the entertainment_center.py file.
#The code was originally made in the udacity supplemental course on fundamentals of Python, and has been altered
#to suit more than Movies -- also variable names have been simplified for easier access. 
class Video():
    """This class provides a way to store video related information"""
    def __init__(self, title, poster, trailer):
        self.title = title
        self.poster = poster
        self.trailer = trailer
    
    def show_trailer(self):
        webbrowser.open(self.trailer)
        
    #quick way to print all information of the object
    #this was only used for debugging purposes, and does not show in the actual code.
    def print_info(self):
        print self.title
        print self.poster
        print self.trailer
