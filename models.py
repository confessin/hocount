#!/usr/bin/env python
# encoding: utf-8

"""
Model class for HoCount App.
"""

__author__ = 'confessin@gmail.com (Mohammad Rafi)'


from google.appengine.ext import db
from google.appengine.api import users


class Dawg(db.Model):
    """Model class for Dawg."""
    name = db.StringProperty(required=True)
    bio = db.TextProperty(required=True)
    gender = db.StringProperty(required=True)
    location = db.StringProperty()
    ytmnds = db.IntegerProperty()
    # Adding it here coz our frequent operation would be to show Dawg's Hoes
    # this would be a list of WhoseHoe keys.
    dawgs = db.ListProperty(db.Key)

    added_date = db.DateTimeProperty(auto_now_add=True)
    added_by = db.ReferenceProperty(users)


# Each Dawg can have multiple photos.
# If we want to get all photos of a Dawg we would do somthing like:
# dawg_photos = dawg_obj.photo_set.get()
class Photo(db.Model):
    """Model class for Dawg Photos.

    It has many to one relationship with Dawg."""

    title = db.StringProperty()
    full_size_image = db.BlobProperty()
    dawg_id = db.ReferenceProperty(Dawg)


class WhoseHoe(db.Model):
    """Model class for relationships."""

    added_by = db.ReferenceProperty(users)
    added_date = db.DateTimeProperty(auto_now_add=True)
    vouches = db.IntegerProperty()
