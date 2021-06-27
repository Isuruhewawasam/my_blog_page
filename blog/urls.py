
from django.contrib import admin
from django.urls import path
from . views import home, Post_details, Add_post, Update_post, Delete_post, Add_Category, likeView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home.as_view(), name='home'),
    path('details/<int:pk>', Post_details.as_view(), name='post_details'),
    path('add_post/', Add_post.as_view(), name='add_post'),
    path('update_post/<int:pk>', Update_post.as_view(), name='update_post'),
    path('delete_post/<int:pk>', Delete_post.as_view(), name='delete_post'),
    path('add_category/', Add_Category.as_view(), name='add_category'),
    path('like/<int:pk>', likeView, name='like_post'),

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
