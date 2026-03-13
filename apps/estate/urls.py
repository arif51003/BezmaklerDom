from django.urls import path

from apps.estate.views import home,about,property_grid,blog_grid,contact,agents


urlpatterns = [
    path("", home,name="home"),
    path("about/",about, name="about"),
    path("property-grid/",property_grid,name="property-grid"),
    path("blog-grid/",blog_grid,name="blog-grid"),
    path("contact/",contact,name="contact"),
    path("agents/",agents,name="agents")

    
]
