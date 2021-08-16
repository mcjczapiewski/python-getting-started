from django.urls import path
import hello.views

from django.contrib import admin

admin.autodiscover()

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
