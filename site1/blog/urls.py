from django.urls import path  
from . import views
from django.contrib import admin
from django.conf import settings # new
from django.urls import path, include # new
from django.conf.urls.static import static # new
  
app_name = 'blog'  
  
urlpatterns = [  
    #t post views
#    path('<int:year>/<int:month>/<int:day>/<slug:post>/media/<str:f_url>',  
#         views.post_detail,
#         views.Post_f,  
#	 name='post_detail'),
    path('new/', views.post_new, name='post_new'),
    path('', views.post_list, name='post_list'),  
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',  
         views.post_detail,  
	 name='post_detail'),  
]
if settings.DEBUG == True: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)