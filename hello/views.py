import requests
from django.shortcuts import redirect, render
from django.http import HttpResponse

from .models import BooksModel
from .forms import BooksForm, GBooksForm
from .filters import BooksFilter


# Create your views here.
def index(request):

    # return HttpResponse('Hello from Python!')
    r = requests.get("http://httpbin.org/status/418")
    print(r.text)
    return HttpResponse("<pre>" + r.text + "</pre>")


def create_edit(request, book_id=""):
    context = {"book_id": book_id}
    if book_id:
        form = BooksForm()
        single_book = BooksModel.objects.get(pk=book_id)
        form = BooksForm(request.POST or None, instance=single_book)
    else:
        form = BooksForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("all-books")

    context["form"] = form
    return render(request, "create-edit.html", context)


def all_books(request):
    books = BooksModel.objects.all()
    myFilter = BooksFilter(request.GET, queryset=books)
    books = myFilter.qs
    context = {"books": books, "myFilter": myFilter}
    return render(request, "all-books.html", context)


def delete_book(self, book_id):
    BooksModel.objects.get(pk=book_id).delete()
    return redirect("all-books")


def books_from_google(request):
    q = intitle = inauthor = isbn = ""
    form = GBooksForm(request.POST or None)
    if form.is_valid():
        q = form.cleaned_data["q"]
        if form.cleaned_data["intitle"] != "":
            intitle = f"+intitle:{form.cleaned_data['intitle']}"
        if form.cleaned_data["inauthor"] != "":
            inauthor = f"+inauthor:{form.cleaned_data['inauthor']}"
        if form.cleaned_data["isbn"] != "":
            isbn = f"+isbn:{form.cleaned_data['isbn']}"
        response = requests.get(
            f"https://www.googleapis.com/books/v1/volumes?q={q}{intitle}{inauthor}{isbn}"
        )
        if response.status_code == 200:
            data = response.json()
            if int(data["totalItems"]) > 0:
                for item in data["items"]:
                    book = BooksModel(
                        title=item["volumeInfo"]["title"],
                        author=", ".join(item["volumeInfo"]["authors"])
                        if "authors" in item["volumeInfo"]
                        else "",
                        publication_date=item["volumeInfo"]["publishedDate"]
                        if "publishedDate" in item["volumeInfo"]
                        else "",
                        isbn_number=item["volumeInfo"]["industryIdentifiers"][
                            0
                        ]["identifier"]
                        if "industryIdentifiers" in item["volumeInfo"]
                        and len(item["volumeInfo"]["industryIdentifiers"]) > 0
                        else None,
                        pages_count=item["volumeInfo"]["pageCount"]
                        if "pageCount" in item["volumeInfo"]
                        else None,
                        cover_url=item["volumeInfo"]["imageLinks"]["thumbnail"]
                        if "imageLinks" in item["volumeInfo"]
                        and "thumbnail" in item["volumeInfo"]["imageLinks"]
                        else "",
                        publication_language=item["volumeInfo"]["language"]
                        if "language" in item["volumeInfo"]
                        else "",
                    )
                    book.save()
                return redirect("all-books")
            else:
                print("no such books")
        else:
            print("ups")
    return render(request, "bfg.html", {"form": form})
