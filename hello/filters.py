from django.forms.widgets import DateInput
import django_filters
from django_filters import DateFilter, CharFilter


class BooksFilter(django_filters.FilterSet):
    title = CharFilter(
        field_name="title", lookup_expr="icontains", label="Tytuł"
    )
    author = CharFilter(
        field_name="author", lookup_expr="icontains", label="Autor"
    )
    publication_language = CharFilter(
        field_name="publication_language",
        lookup_expr="icontains",
        label="Język publikacji",
    )
    start_date = DateFilter(
        field_name="publication_date",
        lookup_expr="gte",
        label="Od daty",
        widget=DateInput(attrs={"type": "date"}),
    )
    end_date = DateFilter(
        field_name="publication_date",
        lookup_expr="lte",
        label="Do daty",
        widget=DateInput(attrs={"type": "date"}),
    )
