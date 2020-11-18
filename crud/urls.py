
from django.urls import path
from .import views


urlpatterns = [
    
    path('home',views.home,name='home'),
    path('post-like',views.like_unlike_post,name='post-like-view'),
    
    path('contact',views.ContactView,name='contact'),
    path('post-detail/<int:pk>',views.PostDetailView,name='post-detail'),
   
    path('post-create',views.PostCreateView,name='post-create'),
    path('post-edit/<int:pk>',views.PostUpdateView,name='post-update'),
    path('post-delete/<int:pk>',views.PostDeleteView,name='post-delete'),
    path('post-search',views.PostSearchView,name='post-search'),
    # path('post-like/<int:post_id>',views.like_unlike_post,name='post-like-view'),
    
    path('account-settings',views.Account_Settings,name='account-settings'),
    path('dashboard',views.Dashboard,name='dashboard'),
    path('user-profile/<int:pk>',views.User_Profile,name='user-profile'),
    # path('user-password-change',views.UserPasswordChange,name='password-change'),
    path('photos-gallary',views.photos_gallary,name='photos-gallary'),
    path('user-photos-gallary/<int:pk>',views.user_photos_gallary,name='user-photos-gallary'),
    
    path('contact',views.ContactView,name='contact'),

    path('validate-username',views.usernameValidationView,name='validate-username'),
    # path('register',views.User_Registration,name='register'),
    path('',views.User_Login_Register,name='login'),
    path('logout',views.User_Logout,name='logout'),
]
