#!/usr/bin/env python
# encoding: utf-8
from __future__ import unicode_literals

from . import views

# routeList is registered in api.v1.urls
routeList = (
    (r'ingredient/ingredient', views.IngredientViewSet),
)
