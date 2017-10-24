  from django.conf.urls import url #This gives us access to the function url
  from . import views              # This explicitly imports views.py in the current folder.
  urlpatterns = [
    url(r'^$', views.index)        # Uses the url method in a way that’s very similar to the @app.route method in flask. The r after the ( tells Python to interpret the following as a raw string, so it won't escape any special characters -- useful when dealing with regex strings!
    #in this case, our regex will exactly match an empty string. That means if you were to go to localhost:8000/, Django (after removing the '/' automatically) will check if your url matches any of the patterns in the urlpattern list.
    #In this case, it does! An empty string is what r'^$' looks for. Since the pattern matches, we run the views.index method.
    #url() will eventually take another parameter, something like name='index'
    #Note that, unlike a Flask route where there is an HTTP method (e.g. “GET” and/or “POST”), Django doesn’t care. We (the developer) figure that out in the method by accessing request.method in our function.
  ]
