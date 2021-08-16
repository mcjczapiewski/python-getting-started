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
    path("", hello.views.all_books, name="all-books"),
    path("admin/", admin.site.urls),
    path("create-edit/", hello.views.create_edit, name="create-edit"),
    path(
        "create-edit/<str:book_id>", hello.views.create_edit, name="create-edit"
    ),
    path("bfg/", hello.views.books_from_google, name="bfg"),
    path(
        "delete-book/<str:book_id>",
        hello.views.delete_book,
        name="delete-book",
    ),
]
