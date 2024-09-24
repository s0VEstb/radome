from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . import models
from django.views import generic
from . import forms
from django.db.models import Q

# Create your views here.
class BooksListView(generic.ListView):
    model = models.Book
    template_name = 'books/books_list.html'
    context_object_name = 'books'

    def get_queryset(self):
        # Получаем поисковый запрос из GET параметров
        query = self.request.GET.get('q')

        # Если запрос существует, фильтруем книги по названию
        if query:
            return models.Book.objects.filter(Q(title__icontains=query))

        # Если нет запроса, возвращаем все книги
        return models.Book.objects.all()

    def get_context_data(self, **kwargs):
        # Добавляем запрос в контекст, чтобы сохранить его в строке поиска
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        return context


class BooksDetailView(generic.DetailView):
    model = models.Book
    template_name = 'books/books_detail.html'
    context_object_name = 'book'

    def get_object(self, **kwargs):
        book_id = self.kwargs.get('id')
        return get_object_or_404(models.Book, id=book_id)


class BooksCreateView(generic.CreateView):
    form_class = forms.BookForm
    template_name = 'books/books_create.html'
    success_url = '/books/books_list/'

    def form_valid(self, form):
        return super(BooksCreateView, self).form_valid(form)


class BooksUpdateView(generic.UpdateView):
    form_class = forms.BookForm
    template_name = 'books/books_update.html'
    success_url = '/books/books_list/'

    def get_object(self, **kwargs):
        book_id = self.kwargs.get('id')
        return get_object_or_404(models.Book, id=book_id)


class BooksDeleteView(generic.DeleteView):
    template_name = 'books/books_delete.html'
    success_url = '/books/books_list/'

    def get_object(self, **kwargs):
        book_id = self.kwargs.get('id')
        return get_object_or_404(models.Book, id=book_id)




def about_me(request):
    return HttpResponse('Hello, my name is Kanat')


def about_friend(request):
    return HttpResponse('My friends name  is Erbolot and Bektur')


def datetime_now(request):
    return HttpResponse(datetime.now())




