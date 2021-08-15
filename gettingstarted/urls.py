from django.urls import path
import hello.views

from django.contrib import admin

admin.autodiscover()


# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", hello.views.index, name="index"),
    path("db/", hello.views.db, name="db"),
    path("admin/", admin.site.urls),
    path("create-edit/", hello.views.create_edit, name="create-edit"),
    path(
        "create-edit/<str:book_id>", hello.views.create_edit, name="create-edit"
    ),
    path("all-books/", hello.views.all_books, name="all-books"),
]
