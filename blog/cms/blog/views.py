from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category
from .forms import CommentForm
# Create your views here.

def list_of_post_by_category(request, category_slug):
    categories = Category.objects.all()
    post = Post.objects.filter(status='published')
    if category_slug:
        category = get_object_or_404(Category, slug = category_slug)
        post = post.filter(category=category)
    template = 'blog/category/list_of_posts_by_category.html'
    context = {'categories' : categories, 'post': post, 'category' : category}
    return render(request, template, context)


def list_of_post(request):
    post = Post.objects.filter(status='published')
    template = 'blog/post/list_of_post.html'
    context = {'post':post}
    return render(request, template, context)
    #return render(request, 'blog/post/list_of_post.html', {'post':post})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    template = 'blog/post/post_detail.html'
    context = {'post':post}
    return render(request, template, context)

def add_comment(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('blog:post_detail', slug=post.slug)
    else:
        form = CommentForm()
    template = 'blog/post/add_comment.html'
    context = {'form': form}
    return render(request, template, context)