from django.contrib import admin
from django.urls import path
from pollapp.views import home, create, vote, results

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home, name="home"),
    path("create/", create, name="create"),
    path("vote/<int:id>", vote, name="vote"),
    path("results/<int:id>", results, name="results"),
       
]
