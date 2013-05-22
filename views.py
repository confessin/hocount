#!/usr/bin/env python
# encoding: utf-8

"""
Views for HoCount App.
"""

__author__ = 'confessin@gmail.com (Mohammad Rafi)'

import os
import jinja2
import webapp2
import forms

from google.appengine.api import users

# TODO: move em to settings.
DIRNAME = os.path.join(os.path.dirname(__file__), 'templates')
jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(DIRNAME))


class MainPage(webapp2.RequestHandler):
    def get(self):
        template_values = {
            'url': 'foo',
            'url_linktext': '',
        }

        template = jinja_environment.get_template('dawg.html')
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


class AddDawg(webapp2.RequestHandler):
    """Docstring for AddDawg """

    def get(self):
        self.response.out.write('<html><body>'
                                '<form method="POST" '
                                'action="/dawg/add">'
                                '<table>')
        # This generates our shopping list form and writes it in the response
        self.response.out.write(forms.DawgForm())
        self.response.out.write('</table>'
                                '<input type="submit">'
                                '</form></body></html>')
        #template_values = {
        #    'url': 'foo',
        #    'url_linktext': '',
        #}
        #
        #template = jinja_environment.get_template('dawg.html')
        #self.response.out.write(template.render(template_values))

    def post(self):
        data = forms.DawgForm(data=self.request.POST)
        if data.is_valid():
            # Save the data, and redirect to the view page
            entity = data.save(commit=False)
            import pdb; pdb.set_trace()
            entity.added_by = users.get_current_user().user_id()
            entity.put()
            self.redirect('/items.html')
        else:
            # Reprint the form
            self.response.out.write('<html><body>'
                                    '<form method="POST" '
                                    'action="/">'
                                    '<table>')
            self.response.out.write(data)
            self.response.out.write('</table>'
                                    '<input type="submit">'
                                    '</form></body></html>')


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
