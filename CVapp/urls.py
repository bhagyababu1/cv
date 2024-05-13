from django.urls import path
from  . import views


urlpatterns = [
        path("createcv/",views.CreateCV,name='create_cv'),
        path("",views.CVView,name='cvview'),
        path('index/',views.index)
]