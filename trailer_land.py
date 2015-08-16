import webbrowser
import os
import re

# The base of this file is the fresh_tomatoes.py file given to us by Udacity through the Programming Foundations with Python course.
# It has been tweaked in select areas to suit the additions
# Styles and scripting for the page
main_page_head = '''
<head>
    <meta charset="utf-8">
    <title>Trailer Land</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            margin-bottom: 20px;
            padding-top: 20px;
        }
        .movie-tile:hover {
            background-color: #EEE;
            cursor: pointer;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the movies when the page loads
        // This has been altered to account for the new sections.
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next().show("fast", showNext);
         });
        });
    </script>
</head>
'''

# The main page layout and title bar
# in div class = "container" -- the {movie_titles} section will be replaced using the open_movies_page method, which will generate content using the 
# create_movie_titles_content(movies) method. The movies variable is filled in using data from the separate .py file 'entertainment_center' which defines the video data.
main_page_content = '''
<!DOCTYPE html>
<html lang="en">
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
          <div class="modal-body:">
             <div class="row">
                <p>Stuff</p>
             </div>
          </div>
        </div>
      </div>
    </div>
    
    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#"><b>Trailer Land Trailers</b></a>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      <div class="row">
         <div class="col-xs-12">
          <h1>Movies</h1>
         </div>
      </div>
      {movie_tiles}
      <hr>
      <div class="row">
         <div class="col-xs-12">
          <h1>TV Shows</h1>
         </div>
      </div>
      {tvshow_tiles}
      <hr>
      <div class="row">
         <div class="col-xs-12">
          <h1>Videogames</h1>
         </div>
      </div>
      {game_tiles}
    </div>
  </body>
</html>
'''

# A single movie entry html template
# This entry of HTML will be appended for each entry
movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center" data-trailer-youtube-id="{trailer}" data-toggle="modal" data-target="#trailer">
    <img src="{poster}" width="220" height="342">
    <h2>{title}</h2>
</div>
'''

def create_movie_tiles_content(videos):
    # The HTML content for this section of the page
    # For this section we are using videos[i] often because videos is actually a dictionary pointing to the memory location of
    # classes. the [i] itself is just a number spanning from 0 to the length of the dictionary.
    content = ''
    for i in videos:
        print videos[i].title
        # Extract the youtube ID from the url
        youtube_id_match = re.search(r'(?<=v=)[^&#]+', videos[i].trailer)
        youtube_id_match = youtube_id_match or re.search(r'(?<=be/)[^&#]+', videos[i].trailer)
        trailer_youtube_id = youtube_id_match.group(0) if youtube_id_match else None

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            title=videos[i].title,
            poster=videos[i].poster,
            trailer=trailer_youtube_id
        )
    print content
    return content

def open_movies_page(movies,tvshows,games):
  # Create or overwrite the output file
  output_file = open('trailer_land.html', 'w')

  # Replace the placeholder for the movie tiles with the actual dynamically generated content
  # Because of the additional sections, I needed to add these additional parameters.
  rendered_content = main_page_content.format(movie_tiles=create_movie_tiles_content(movies),
                                              tvshow_tiles=create_movie_tiles_content(tvshows),
                                                game_tiles=create_movie_tiles_content(games)
                                                )
  # Output the file
  output_file.write(main_page_head + rendered_content)
  output_file.close()

  # open the output file in the browser
  url = os.path.abspath(output_file.name)
  webbrowser.open('file://' + url, new=2) # open in a new tab, if possible