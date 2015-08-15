import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
						"A story of a boy and his toys that come to life",
						"http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
						"https://www.youtube.com/watch?v=vwyZH85NQC4")
#print(toy_story.storyline)
avatar = media.Movie("Avatar",
						"A marine on an alien planet",
						"http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
						"https://www.youtube.com/watch?v=5PSNL1qE6VY")
						
#print(avatar.storyline)
#avatar.show_trailer()
madmax_furyroad = media.Movie("Mad Max: Fury Road",
								"A story of trucks, sand, and chrome spray paint",
								"https://upload.wikimedia.org/wikipedia/en/2/23/Max_Mad_Fury_Road_Newest_Poster.jpg",
								"https://www.youtube.com/watch?v=hEJnMQG9ev8")
#print(madmax_furyroad.storyline)
#madmax_furyroad.show_trailer()
school_of_rock = media.Movie("School of Rock", "Storyline",
							"http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
							"https://www.youtube.com/watch?v=3PsUJFEBC74")

ratatouille = media.Movie("Ratatouille", "Storyline",
							"http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
							"https://www.youtube.com/watch?v+c3sBBRxDAqk")
							
shrek = media.Movie("Shrek", "The best movie ever",
					"https://upload.wikimedia.org/wikipedia/en/3/39/Shrek.jpg",
					"https://www.youtube.com/watch?v=W37DlG1i61s")

shrek2 = media.Movie("Shrek 2", "The best movie ever",
					"https://upload.wikimedia.org/wikipedia/en/b/b9/Shrek_2_poster.jpg",
					"https://www.youtube.com/watch?v=V6X5ti4YlG8")

shrek3 = media.Movie("Shrek 3", "The best movie ever",
					"https://upload.wikimedia.org/wikipedia/en/0/01/Shrek_the_third_ver2.jpg",
					"https://www.youtube.com/watch?v=3aZXVzUQGA4")
					
shrek4 = media.Movie("Shrek 4", "The best movie ever",
					"https://upload.wikimedia.org/wikipedia/en/7/75/Shrek_forever_after_ver8.jpg",
					"https://www.youtube.com/watch?v=u7__TG7swg0")

movies = [shrek, shrek2, shrek3, shrek4]
#fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
print(media.Movie.__doc__)
