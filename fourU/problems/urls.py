# -*- coding: utf-8 -*-

################################################################################
# Copyright (C) 2009 XYZ Textbooks                                             #
#                                                                              #
# This file is part of fourU.                                                  #
#                                                                              #
# This program is free software; you can redistribute it and/or modify it under#
# the terms of either: (a) the GNU General Public License as published by the  #
# Free Software Foundation; either version 3, or (at your option) any later    #
# version, or (b) the MIT License which comes with this package.               #
#                                                                              #
# fourU is distributed in the hope that it will be useful,                     #
# but WITHOUT ANY WARRANTY; without even the implied warranty of               #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See either the         #
# GNU General Public License or the MIT License for more details.              #
################################################################################

from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('',
	url(r'^$', direct_to_template, {'template': 'problems/edit_problem.html',}),
	
	# AJAX views
	url(r'^preview-problem/$', 'problems.views.preview_problem', name='preview_problem'),
	url(r'^save-problem/$', 'problems.views.save_problem', name='save_problem'),
)
