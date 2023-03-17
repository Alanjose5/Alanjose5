from django.urls import path
from . import views
app_name='movie'
urlpatterns=[
    path('', views.demo, name="demo"),
    path('movie/<int:id>/',views.detail,name="detail"),
    path('ee',views.pict, name="pict"),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('f',views.movielistview.as_view(),name='f'),
    path('u/<int:pk>/',views.moviedeatilview.as_view(),name='u'),
    path("cbvupdate/<int:pk>/",views.movieupdateview.as_view(),name='cbvupdate'),
    path('cbvdelete/<int:pk>/',views.moviedeatilview.as_view(),name='cbvdelete')
]
