from django.shortcuts import render
# from django.db.models import Q
from django.views.generic import ListView

from product.models import ProductTable


class SearchProductListView(ListView):  # class based listview
    template_name = 'search/Searchlist.html'

    def get_context_data(self, *args, **kwargs):
        context = super(SearchProductListView, self).get_context_data(*args, **kwargs)
        context['query'] = self.request.GET.get('q')
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        method_dic = request.GET
        query = method_dic.get('q', None)  # method_dic['q']# method_dic.get('q','shirt')if nothing shows shirt
        print(query)
        if query is not None:
            # lookups = Q(title__icontains=query) | Q(description__icontains=query)
            # return ProductTable.objects.filter(lookups).distinct()
            return ProductTable.objects.search(query)
        # return ProductTable.objects.features()
        # return ProductTable.objects.none()
        return ProductTable.objects.all()
# Create your views here.
