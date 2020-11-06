from django.shortcuts import render, get_object_or_404 
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger 
import os
from django.utils import timezone 
from .forms import PostForm
from django.shortcuts import redirect
from django.db import models
from django.conf import settings
from django.core.files.storage import FileSystemStorage
# Imaginary function to handle an uploaded file.
'''def file(request,Post):
    newdoc = Document(docfile = request.FILES['file'])
    newdoc.save()
    f_url = iter(request.FILES)'''

def post_list(request):
    object_list = Post.published.all()  
    paginator = Paginator(object_list, 3)  # 3 поста на каждой странице  
    page = request.GET.get('page')  
    try:  
        posts = paginator.page(page)  
    except PageNotAnInteger:  
        # Если страница не явл	яется целым числом, поставим первую страницу  
        posts = paginator.page(1)  
    except EmptyPage:  
        # Если страница больше максимальной, доставить последнюю страницу результатов  
        posts = paginator.page(paginator.num_pages)  
    return render(request,  
	          'blog/post/list.html',  
		  {'page': page,  
		   'posts': posts})
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            '''post = form.save(commit=False)'''
            '''file_name = request.POST.get('file')
            post.file = request.FILES[file_name]
            fs = FileSystemStorage()
            filename = fs.save(file_name, post.file)'''
            #f = request.POST.get('file')
            #f.save()
            #print(f)
            form.save()
            '''filename = settings.MEDIA_URL + post.file()
            with open(settings.MEDIA_ROOT + filename, 'wb') as f:
                for chunk in request.FILES['file'].chunks():
                    f.write(chunk)
            return redirect(filename)'''
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_detail(request, year, month, day, post):
        post = get_object_or_404(Post,slug=post, status='published', publish__year=year, publish__month=month, publish__day=day) 
        return render(request,
        'blog/post/detail.html',
        {'post': post})



		#f_url = MEDIA_URL + '/files/' + iter(request.FILES)
		#global newdoc
        #newdoc = Document(docfile = request.FILES['file'])
        #newdoc.save()