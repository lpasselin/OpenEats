#!/usr/bin/env python
# encoding: utf-8
from __future__ import unicode_literals

from django.conf.urls import include, url

# import routers from apps urls.py
from rest_framework import routers
from api.v1.recipe_groups import urls as recipe_groupsUrls
from api.v1.ingredient import urls as ingredientUrls
from api.v1.list import urls as listUrls
from api.v1.news import urls as newsUrls
from api.v1.recipe import urls as recipeUrls

# register routers from cooking apps
routeLists = [
       recipe_groupsUrls.routeList,
       ingredientUrls.routeList,
       listUrls.routeList,
       newsUrls.routeList,
       recipeUrls.routeList,
]

router = routers.DefaultRouter()
for routes in routeLists:
    for r in routes:
        router.register(r[0], r[1])

# regular url pattern for accounts and router
urlpatterns = [
    url(r'^accounts/', include('api.v1.accounts.urls')),
    url(r'^', include(router.urls)),
]
