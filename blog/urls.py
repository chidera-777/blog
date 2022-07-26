from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('<slug:post>/', views.post_details, name='post_details'),
    path('<int:post_id>/share/', views.post_share, name='post_share')
 ]