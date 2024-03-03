from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Book
from django.views import generic


class BookListView(generic.ListView):
    paginate_by = 4
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'books/book_detail.html'


class BookCreateView(generic.CreateView):
    model = Book
    template_name = 'books/book_create.html'
    fields = '__all__'


class BookUpdateView(generic.UpdateView):
    model = Book
    template_name = "books/book_update.html"
    fields = '__all__'

    def form_valid(self, form):
        if form.has_changed():
            form.save()
            return redirect('book_detail', self.object.pk)
        else:
            return redirect('book_update', self.object.pk)


class BookDeleteView(generic.DeleteView):
    model = Book
    template_name = 'books/book_delete.html'
    success_url = reverse_lazy('book_list')
    success_message = 'kir'
