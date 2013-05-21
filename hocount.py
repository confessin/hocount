#!/usr/bin/env python
# encoding: utf-8

"""
Urls class for HoCount.
"""

__author__ = 'confessin@gmail.com (Mohammad Rafi)'


import webapp2
import views


app = webapp2.WSGIApplication([('/', views.MainPage),
                              ('/dawg/(\d)/', views.Dawg)],
                              debug=True)
