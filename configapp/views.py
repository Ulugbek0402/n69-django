from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from .forms import NewsForm, SearchForm
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Customer, Employee, Order
from .serializers import CustomerSerializer, EmployeeSerializer, OrderSerializer


# def index(request):
#     if request.method == "GET":
#         form = SearchForm(request.GET)
#         news = News.objects.all()
#         cat = Category.objects.all()
#         if form.is_valid():
#             query = form.cleaned_data.get("title")
#             name = news.filter(title__icontains = query)
#     return render(request, "index.html", {"news": news, "cat": cat, "form": form})

def category(request, pk):
    news = News.objects.filter(category=pk)
    category = Category.objects.all()
    context = {
        "news": news,
        "category": category,
        "title": "NEWS TITLE"
    }


    return render(request, 'category.html', context=context)


def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NewsForm()
    return render(request, 'add_news.html', {'form': form})


def detail_new(request, pk):
    new = get_object_or_404(News, id=pk)
    context = {
        "new": new
    }
    return render(request, 'detail_new.html', context=context)



def update_new(request, pk):
    new = get_object_or_404(News, id=pk)
    # new = News.objects.get(pk=new_id)
    if request.method == 'POST':
        form = NewsForm(request.POST, instance=new)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = NewsForm(instance=new)
    return render(request, 'update_new.html', {'form': form, 'new': new})



def del_new(request, pk):
    new = get_object_or_404(News, id=pk)
    new.delete()
    news = News.objects.all()
    category = Category.objects.all()
    context = {
        "news": news,
        "category": category,
        "title": "NEWS TITLE"
    }
    return render(request, 'index.html', context=context)



class HomeNews(ListView):
    model = News
    template_name = 'index.html'
    context_object_name = 'news'
    extra_context = {'title': 'Главная'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'NEWS TITLE'
        context['category'] = Category.objects.all()
        return context

    def get_queryset(self):
        return News.objects.filter(is_bool=True)


class NewsByCategory(ListView):
    model = News
    template_name = 'index.html'
    context_object_name = 'news'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context

    def get_queryset(self):
        return News.objects.filter(category=self.kwargs['pk'])


class ViewNews(DetailView):
    model = News
    context_object_name = 'news'
    template_name = 'index.html'
    pk_url_kwarg = 'pk'


class CreateNews(CreateView):
    form_class = NewsForm
    template_name = 'add_news.html'
    success_url = reverse_lazy('home')


class NewsUpdate(UpdateView):
    form_class = NewsForm
    template_name = "update_new.html"
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'pk'


def index(request):   return render(request, 'index.html')
def about(request):   return render(request, 'about.html')
def company(request): return render(request, 'company.html')
def contact(request): return render(request, 'contact.html')
def design(request):  return render(request, 'design.html')
def news(request):    return render(request, 'news.html')



class CustomerListCreateApi(APIView):

    def get(self, request):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CustomerDetailApi(APIView):

    def get(self, request, id):
        customer = get_object_or_404(Customer, id=id)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

    def put(self, request, id):
        customer = get_object_or_404(Customer, id=id)
        serializer = CustomerSerializer(customer, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, id):
        customer = get_object_or_404(Customer, id=id)
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class EmployeeListCreateApi(APIView):

        def get(self, request):
            employees = Employee.objects.all()
            serializer = EmployeeSerializer(employees, many=True)
            return Response(serializer.data)

        def post(self, request):
            serializer = EmployeeSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

class EmployeeDetailApi(APIView):

        def get(self, request, id):
            employee = get_object_or_404(Employee, id=id)
            serializer = EmployeeSerializer(employee)
            return Response(serializer.data)

        def put(self, request, id):
            employee = get_object_or_404(Employee, id=id)
            serializer = EmployeeSerializer(employee, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)

        def delete(self, request, id):
            employee = get_object_or_404(Employee, id=id)
            employee.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

class OrderListCreateApi(APIView):

    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class OrderDetailApi(APIView):

    def get(self, request, id):
        order = get_object_or_404(Order, id=id)
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def put(self, request, id):
        order = get_object_or_404(Order, id=id)
        serializer = OrderSerializer(order, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, id):
        order = get_object_or_404(Order, id=id)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


