import requests
from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting
from .models import BooksModel
from .forms import BooksForm
from .filters import BooksFilter


# Create your views here.
def index(request):

    # return HttpResponse('Hello from Python!')
    r = requests.get("http://httpbin.org/status/418")
    print(r.text)
    return HttpResponse("<pre>" + r.text + "</pre>")


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})


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

    context["form"] = form
    return render(request, "create-edit.html", context)


def all_books(request):
    books = BooksModel.objects.all()
    myFilter = BooksFilter(request.GET, queryset=books)
    books = myFilter.qs
    context = {"books": books, "myFilter": myFilter}

    return render(request, "all-books.html", context)
