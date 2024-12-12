from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.display, name='login'),
    path('register/', views.register, name='register'),
    path('forget/', views.forget, name='forget'),
    path('otp/', views.otp, name='otp'),
    path('verify-otp/', views.verify),
    path('change/', views.change),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),
    path('upload-image/', views.upload_image, name='upload_image'),
    path('myposts/',views.myposts,name='myposts'),
    path('like/<int:post_id>/', views.like_post, name='like_post'),
    path('comment/<int:post_id>/', views.add_comment, name='add_comment'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
