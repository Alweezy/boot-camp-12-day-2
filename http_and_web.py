def get_name(artist_name):
	if isinstance(artist_name, str):
		name = "" + artist_name
		name = "".join(name.split())
		#elminate other data strucures/data types besides string
	elif type(artist_name) in [int, dict, list, tuple, set]:
		return "Operation cannot allow " + str(type(artist_name)) + ", artist_name is a string"
	else:
		return "Enter a valid artist_name: "
	if name:
		base_url = 'https://itunes.apple.com/search?term={}&entity=musicVideo'
		artist = name.lower()
		complete_url = base_url.format(artist)
		return complete_url, name
	return "artist name is a requirement"

def search_song(get_url):
	'''
		Use Url to perform a song search and return the list of songs.
	'''
	import requests
	my_url, name = get_name(get_url)
	if my_url:
		response = requests.get(my_url)
		results = response.json()['results']
		print "{:<15} {:<60} {:<5} {:>20} {:>15}".format("ArtistName",
											"TrackName", "Price",
											"Explicitness", "Kind")
		print "{:<15} {:<60} {:<5} {:>20} {:>15}".format("**********",
											"*********", "*****",
											"************", "****")
		for song in results:
			artist = song["artistName"]
			artist = "".join(artist.split())
			if artist == name:
				print "{:<15} {:<60} {:<5} {:>20} {:>15}"\
				.format(song['artistName'], song["trackName"],
					song["collectionPrice"], song["trackExplicitness"],
					song["kind"])
		return "********************End*******************************"

print search_song("Kanye West")
print search_song("Konshens")