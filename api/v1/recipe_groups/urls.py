#!/usr/bin/env python
# encoding: utf-8
from __future__ import unicode_literals

from api.v1.recipe_groups import views

# routeList is registered in api.v1.urls
routeList = (
    (r'recipe_groups/cuisine', views.CuisineViewSet),
    (r'recipe_groups/course', views.CourseViewSet),
    (r'recipe_groups/tag', views.TagViewSet),
)
