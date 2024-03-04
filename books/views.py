from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from .models import Book, Comment
from .forms import CommentForm
from django.views import generic


class BookListView(generic.ListView):
    paginate_by = 4
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'


def book_detail_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    comments = book.comments.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.book = book
            new_comment.user = request.user
            new_comment.save()
            form = CommentForm()
    else:
        form = CommentForm()
    return render(request, 'books/book_detail.html', {'book': book, 'comments': comments, 'form': form})


def edit_comment_view(request, pk, cid):
    book = get_object_or_404(Book, pk=pk)
    comments = book.comments.all()
    comment = get_object_or_404(Comment, pk=cid)
    if request.method == 'POST':
        form = CommentForm(request.POST or None, instance=comment)
        if form.is_valid() and form.has_changed():
            new_comment = form.save(commit=False)
            new_comment.book = book
            new_comment.user = request.user
            new_comment.save()
            form = CommentForm()
        return redirect('book_detail', pk)
    else:
        form = CommentForm(request.POST or None, instance=comment)
    return render(request, 'books/book_detail.html', {'book': book, 'comments': comments, 'form': form})


#     form = PostForm(request.POST or None, instance=post )
#     if form.is_valid() and form.has_changed():
#         form.save()
#         return redirect('post_detail', pk=post.id)
#     return render(request, 'blog/post_add.html', {'form':form})

# class BookDetailView(generic.DetailView):
#     model = Book
#     template_name = 'books/book_detail.html'


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
