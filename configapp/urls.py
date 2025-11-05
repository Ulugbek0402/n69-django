from django.urls import path
from .views import *


urlpatterns = [
    # path('', HomeNews.as_view(), name='home'),
    path('', index, name="home"),
    # path('del_new/<int:pk>/', del_new, name="del_new"),
    path('add_news/', add_news, name="add_news"),
    # path('news/add_news/', CreateNews.as_view(), name='add_news'),
    # path('detail_new/<int:pk>/', detail_new, name="detail_new"),
    #path('detail_new/<int:pk>/', ViewNews.as_view(), name='detail_new'),
    path('category/<int:pk>/', category, name="category"),
    # path('category/<int:pk>/', NewsByCategory.as_view(), name='category'),
    # path('update_new/<int:pk>/', update_new, name="update_new"),
]
