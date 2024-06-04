from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator

from .forms import TagForm, QuoteForm, AuthorForm

from .models import Quote, Tag, Author


# from .utils import get_mongodb

# Create your views here.
def main(request, page=1):
    per_page = 10
    quotes = Quote.objects.all()
    tags = Tag.objects.all
    paginator = Paginator(quotes, per_page)
    quotes_on_page = paginator.get_page(page)
    return render(request, 'quotesapp/index.html', context={'quotes': quotes_on_page, 'tags':tags})

def quote(request):
    tags = Tag.objects.all()
    author = Author.objects.all()

    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            new_quote = form.save()

            choice_tags = Tag.objects.filter(name__in=request.POST.getlist('tags'))
            for tag in choice_tags.iterator():
                new_quote.tags.add(tag)

            choice_author = Author.objects.get(fullname=request.POST.get('author'))
            new_quote.author = choice_author
            new_quote.save()


            return redirect(to='quotesapp:main')
        else:
            return render(request, 'quotesapp/quote.html', {"tags": tags, 'form': form, 'author':author})

    return render(request, 'quotesapp/quote.html', {"tags": tags, 'author':author, 'form': QuoteForm()})

def author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quotesapp:main')
        else:
            return render(request, 'quotesapp/author.html', {'form': form})

    return render(request, 'quotesapp/author.html', {'form': AuthorForm()})

def tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quotesapp:main')
        else:
            return render(request, 'quotesapp/tag.html', {'form': form})

    return render(request, 'quotesapp/tag.html', {'form': TagForm()})


def detail(request, fullname):
    author = get_object_or_404(Author, fullname=fullname)
    return render(request, 'quotesapp/author_page.html', {"author": author})

