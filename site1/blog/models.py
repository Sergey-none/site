from django.conf import settings
from django.db import models 
from django.utils import timezone 
from django.contrib.auth.models import User 
from django.urls import reverse
from django.db import models

class PublishedManager(models.Manager):  
    def get_queryset(self):  
        return super(PublishedManager,  
		     self).get_queryset()\
        		.filter(status='published')
def post_detail(request, year, month, day, post):  
    post = get_object_or_404(Post, slug=post,  
			     status='published',  
			     publish__year=year,  
			     publish__month=month,  
			     publish__day=day) 
    return render(request,  
		  'blog/post/detail.html',  
		  {'post': post})
class Post(models.Model): 
    STATUS_CHOICES = (
        ('draft', 'Draft'), 
        ('published', 'Published'),
        ('active','Active'),
    ) 
    title = models.CharField(max_length=250) 
    slug = models.SlugField(max_length=250, 
                            	unique_for_date='publish')
    file = models.FileField(null=True,blank=True)
    body = models.TextField()
    
    publish = models.DateTimeField(default=timezone.now) 
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now=True) 
    status = models.CharField(max_length=10, 
                              choices=STATUS_CHOICES, 
                              default='published')
    def get_absolute_url(self):  
        return reverse('blog:post_detail',  
		       args=[self.publish.year,  
		       self.publish.month,  
		       self.publish.day,  
		       self.slug])
    objects = models.Manager()  # Менеджер по умолчанию  
    published = PublishedManager() 
    def get_link(self):  
        name = settings.MEDIA_ROOT +'/'+ self.file.name
        print(name)
        return name
    class Meta: 
        ordering = ('-publish',) 

    def __str__(self): 
        return self.title