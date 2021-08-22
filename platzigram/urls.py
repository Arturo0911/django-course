
# Django imports
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path
from django.conf import settings

from platzigram import views as local_views
from posts import views as posts_views
from users import views as users_views

urlpatterns = [

    path("admin/", admin.site.urls),
    path("hello-world/", local_views.helloworld, name="hello_world"),
    path("sorted/", local_views.sorted_integers, name="sorted"),
    path("hi/<str:name>/<int:age>/", local_views.say_hi, name="hi"),

    path("posts/", posts_views.list_posts, name="feed"),
    path("users/login/", users_views.login_view, name="login")
]

urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
