
from .models import Article
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def post_list(request):
    articles = Article.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')

    sections = ['NZ', 'Sport', 'Tech', 'International']

    return render(request, 'np/post_list.html', {'articles': articles, 'sections': sections})



def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'np/article_detail.html', {'article': article})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.published_date = timezone.now()
            article.save()
            return redirect('article_detail', pk=article.pk)
    else:
        form = PostForm()
    return render(request, 'np/post_edit.html', {'form': form})

@login_required
def post_edit(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.created_date = timezone.now()
            article.save()
            return redirect('article_detail', pk=article.pk)
    else:
        form = PostForm(instance=article)
    return render(request, 'np/post_edit.html', {'form': form})

def post_remove(request, pk):
    post = get_object_or_404(Article, pk=pk)
    post.delete()
    return redirect('post_list')

def section_filtered(request, section=None):
    articles = Article.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')
    articlesFiltered = Article.objects.filter(section__contains=section).order_by('-created_date')
    return render(request, 'np/section_filtered.html', {'articlesFiltered': articlesFiltered, 'articles':articles})
