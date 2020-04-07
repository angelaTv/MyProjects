from django.http import Http404, request
from django.utils import timezone
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404, redirect

from .models import ProductTable
from cart.models import Cart


# Create your views here.


class ProductDetailSlugView(DetailView):
    queryset = ProductTable.objects.all()
    template_name = 'product/details.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailSlugView, self).get_context_data(*args, **kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context["cart"] = cart_obj
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        # instance = get_object_or_404(ProductTable, slug=slug, active=True)  # id
        try:
            instance = ProductTable.objects.get(slug=slug, active=True)
        except ProductTable.DoesNotExist:
            raise Http404("Not found")
        except ProductTable.MultipleObjectsRetured:
            qs = ProductTable.objects.filter(slug=slug, active=True)
            instance = qs.first()
        except:
            raise Http404(".....")
        return instance


class ProductListView(ListView):  # class based listview
    template_name = 'product/lists.html'

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return ProductTable.objects.all()


def get_context_data(self, *args, **kwargs):
    context = super(ProductListView, self).get_context_data(*args, **kwargs)
    print(context)
    return context

# class ProductDetailSlugView(DetailView):
#     model = ProductTable
#     template_name = 'product/details.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['now'] = timezone.now()
#         return context
#
#
# class ProductListView(ListView):
#     model = ProductTable
#     template_name = 'product/lists.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['now'] = timezone.now()
#         return context


##################################################################################################
# def product_listview(request):  # function based listview
#     queryset = ProductTable.objects.all()
#     context = {'object_list': queryset}
#     return render(request, 'product/lists.html', context)
#
#
# class ProductDetailView(ListView):  # class based listview
#     queryset = ProductTable.objects.all()
#     template_name = 'product/details.html'
#
#
# def product_detailview(request, pk=None, *args, **kwargs):  # function based detailview
#     # instance = ProductTable.objects.get(pk=pk)  # id
#     # instance=get_object_or_404(ProductTable,pk=pk)
#     qs = ProductTable.objects.filter(id=pk)
#     print(qs)
#     if qs.exists() and qs.count() == 1:  # len of qs
#         instance = qs.first()
#     else:
#         raise Http404("product does not exists")
#     context = {'object': instance}
#     return render(request, 'product/productdetailview.html', context)
