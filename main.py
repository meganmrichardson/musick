# -*- coding: utf-8 -*-
# allows you to use irregular characters (chinese, emojis)

import os
import webapp2
import jinja2
from artist_service import artist_info

jinja_current_directory = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True) # helps to be immune to some attacks / hacks

class WelcomeHandler(webapp2.RequestHandler):
    def get(self):
        welcome_template = jinja_current_directory.get_template(
            "templates/welcome.html")
        self.response.write(welcome_template.render()) # put u before quotes to make a change

class ArtistsHandler(webapp2.RequestHandler):
    def get(self):
        artists_template = jinja_current_directory.get_template(
            "templates/artists.html")
        self.response.write(artists_template.render())

class ArtistHandler(webapp2.RequestHandler):
    def post(self):
        name = self.request.get("name")
        artist_template = jinja_current_directory.get_template("templates/artist.html")
        self.response.write(artist_template.render({
            "name": name,
            "image": artist_info[name]['image'],
            "spotify_link": artist_info[name]['spotify_link']
        }))

app = webapp2.WSGIApplication([ # WSGIApp is a class
    ('/', WelcomeHandler),
    ('/artists', ArtistsHandler),
    ('/artist', ArtistHandler)
], debug=True)
