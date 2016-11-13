import unittest 

import http_and_web

class HttpandWebTestCase(unittest.TestCase):
	#Test against integer inputs
	def test_artist_name_is_int(self):
		self.assertEqual(http_and_web.get_Name(20), "Operation cannot allow " + str(type(20)) + ", artist_name is a string")
	#Test against various data structures
	def test_artist_name_is_dictionary(self):
		self.assertEqual(http_and_web.get_Name({}), "Operation cannot allow " + str(type({})) + ", artist_name is a string")
	def test_artist_name_is_list(self):
		self.assertEqual(http_and_web.get_Name([]), "Operation cannot allow " + str(type([])) + ", artist_name is a string")
	def test_artist_name_is_tuple(self):
		self.assertEqual(http_and_web.get_Name(('arg1', 'arg2')), "Operation cannot allow " + str(type(("arg1", "arg2"))) + ", artist_name is a string")
	def test_artist_name_is_set(self):
		self.assertEqual(http_and_web.get_Name({'arg1', 'arg2'}), "Operation cannot allow " + str(type({"arg1", "arg2"})) + ", artist_name is a string")
	#Test against an empty string
	def test_artist_name_is_present(self):
		self.assertEqual(http_and_web.get_Name(""), "artist name is a requirement")
	def test_correct_url(self):
		self.assertEqual(http_and_web.get_Name("kanye West"), ("https://itunes.apple.com/search?term=kanyewest&entity=musicVideo", "kanyeWest"))