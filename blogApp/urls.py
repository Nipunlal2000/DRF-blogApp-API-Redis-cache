from django.urls import path
from . views import *
urlpatterns = [
    path('blog/', BlogListCreateView.as_view(), name='blog' ),
    path('blog/<int:id>/', BlogDetailView.as_view(),name ='blog-detail')
]