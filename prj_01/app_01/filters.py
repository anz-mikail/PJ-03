from django_filters import FilterSet, ChoiceFilter, ModelChoiceFilter

from .models import Response, Post


class ResponseFilter(FilterSet):

    categoryType = ModelChoiceFilter(
            field_name='post',
            label='Поиск по объявлению',
            queryset=Post.objects.all()
    )

   # class Meta:
   #     model = Response
   #     fields = {
   #         'title': ['icontains'],
   #
   #     }


