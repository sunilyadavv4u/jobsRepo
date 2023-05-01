from django.urls import path
from testapp import views
urlpatterns=[
path('',views.home_view,name="home"),
path('hyd/',views.hydJobs_view,name='hyd'),
path('bang/',views.bangJobs_view,name='bang'),
path('pune/',views.puneJobs_view,name='pune'),

]
