#!/usr/bin/env python
# encoding: utf-8

"""
Views for HoCount App.
"""

__author__ = 'confessin@gmail.com (Mohammad Rafi)'

import os
import jinja2
import webapp2

# TODO: move em to settings.
DIRNAME = os.path.join(os.path.dirname(__file__), 'templates')
jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(DIRNAME))


class MainPage(webapp2.RequestHandler):
    def get(self):
        template_values = {
            'greetings': 'foo',
            'url': 'foo',
            'url_linktext': '',
        }

        template = jinja_environment.get_template('index.html')
        self.response.out.write(template.render(template_values))


class Dawg(webapp2.RequestHandler):
    """Docstring for Dawg: Dawg is the main entity for Ho's """

    def __init__(self):
        """@todo: to be defined1 """
        webapp2.RequestHandler.__init__(self)

    def get(self, dawg_id):
        """@todo: Docstring for get. This will show the profile page for Dawg.

        :dawg_id: Identifier for dawg.
        :returns: @todo

        """
        pass

    def post(self, dawg_id):
        """@todo: Docstring for post. This will update the profile of Dawg.

        This page will accept, a name, bio and photos.

        :dawg_id: Identifier for dawg.
        :returns: @todo

        """
        pass


class WhoseHo(webapp2.RequestHandler):
    """Docstring for WhoseHo. The connection/linkup between Dawgs. """

    def __init__(self):
        """@todo: to be defined1 """
        webapp2.RequestHandler.__init__(self)

    def get(self, conn_id):
        """@todo: Docstring for get. Represents a whoseHo info page.

        :conn_id: The vertex
        :returns: @todo

        """
        pass

    def post(self, arg1):
        """@todo: Docstring for post

        :arg1: @todo
        :returns: @todo

        """
        pass
