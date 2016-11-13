import unittest 

import http_and_web

class HttpandWebTestCase(unittest.TestCase):
	#Test against integer inputs
	def test_artist_name_is_int(self):
		int_test = http_and_web.get_name(20)
		self.assertEqual(int_test, "Operation cannot allow " + 
							str(type(20)) + ", artist_name is a string")
	#Test against various data structures
	def test_artist_name_is_dictionary(self):
		dict_test = http_and_web.get_name({})
		self.assertEqual(dict_test, "Operation cannot allow " +
							str(type({})) + ", artist_name is a string")
	def test_artist_name_is_list(self):
		list_test = http_and_web.get_name([])
		self.assertEqual(list_test, "Operation cannot allow " +
							str(type([])) + ", artist_name is a string")
	def test_artist_name_is_tuple(self):
		tuple_test = http_and_web.get_name(('arg1', 'arg2'))
		self.assertEqual(tuple_test, "Operation cannot allow " +
							str(type(("arg1", "arg2"))) +
										", artist_name is a string")
	def test_artist_name_is_set(self):
		set_test = http_and_web.get_name({'arg1', 'arg2'})
		self.assertEqual(set_test , "Operation cannot allow " +
							str(type({"arg1", "arg2"})) +
										", artist_name is a string")
	#Test against an empty string
	def test_artist_name_is_present(self):
		test_artist_name = http_and_web.get_name("")
		self.assertEqual(test_artist_name, "artist name is a requirement")
	def test_correct_url(self):
		test_url = http_and_web.get_name("kanye West")
		url = ("https://itunes.apple.com/search?term=kanyewest&entity=musicVideo",
				"kanyeWest")
		self.assertEqual(test_url, url)