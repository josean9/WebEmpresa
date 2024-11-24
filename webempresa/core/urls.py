from django.urls import path
from . import views
urlpatterns = [
 path('', views.home, name="home"),
 path('about/', views.about, name="about"),
 path('services/', views.services, name="services"),
 path('store/', views.store, name="store"),
 path('contact/', views.contact, name="contact"),
 path('blog/', views.blog, name="blog"),
 path('sample/', views.sample, name="sample"),
]
"""urlpatterns = [
 path('', include('core.urls')),
 path('blog/', include('blog.urls')),
 path('services/', include('services.urls')),
 path('admin/', admin.site.urls),
]
"""
