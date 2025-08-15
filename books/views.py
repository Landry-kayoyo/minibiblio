from django.shortcuts import render, get_object_or_404
from .models import Book, Category

# Accueil
def home(request):
    latest_books = Book.objects.all().order_by('-created_at')[:6]
    categories = Category.objects.all()
    return render(request, 'home.html', {'latest_books': latest_books, 'categories': categories})

# Liste des livres
def books_list(request):
    category_id = request.GET.get('category')
    if category_id:
        books = Book.objects.filter(category_id=category_id).order_by('-publication_date')
    else:
        books = Book.objects.all().order_by('-publication_date')
    categories = Category.objects.all()
    return render(request, 'books_list.html', {'books': books, 'categories': categories, 'selected_category': int(category_id) if category_id else None})

# Détail d'un livre
def book_detail(request, slug):
    book = get_object_or_404(Book, slug=slug)
    return render(request, 'book_detail.html', {'book': book})


