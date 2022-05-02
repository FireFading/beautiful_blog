from django.urls import path
from django.contrib.auth import views as auth_views
from .views import home, about, contact, posts, RegisterView, LoginView, LogoutView, author_profile, profile_information, post_share, search_posts, about_author, edit_and_publish, news_from_parser, news_details, add_new_post

urlpatterns = [
    path('', home, name="home"),
    path('about/', about, name="about"),
    path('contact/', contact, name="contact"),
    path('posts/<slug>/', posts, name="posts"),
    path('news/', news_from_parser, name="news"),
    path('news/<slug>/', news_details, name="news_details"),
    
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    
    path('profile/', author_profile, name="profile"),
    path('profile/author/', profile_information, name="profile_information"),
    path('posts/<slug>/share/', post_share, name='post_share'),
    path('posts/search/<tag_slug>/', search_posts, name='post_list_by_tag'),
    path('posts/author/<username>/', about_author, name="about_author"),
    path('add_new_post/', add_new_post, name="add_new_post"),
    path('edit_post/<slug>', edit_and_publish, name="edit_post"),
]
