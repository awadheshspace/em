"""
URL configuration for registration project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static
 
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('exammantra.urls')),   # remove 'exammantra/'
    path('ebook/', include('ebooks.urls')),
    path('practice/', include('practiceset.urls')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('live/', include('examresult.urls',namespace='examresult')),
    path('contact/', include('contact.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('courses/', include('courses.urls')),
    path('payments/', include('payments.urls')),
    # path('fee/',include('feemanagement.urls')),

] +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

