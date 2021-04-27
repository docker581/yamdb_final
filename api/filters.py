import django_filters

from .models import Title


class TitleFilter(django_filters.rest_framework.FilterSet):
    genre = django_filters.CharFilter(field_name='genre__slug', )
    category = django_filters.CharFilter(field_name='category__slug', )
    name = django_filters.CharFilter(lookup_expr="contains", )

    class Meta:
        model = Title
        fields = ['genre', 'category', 'year']
