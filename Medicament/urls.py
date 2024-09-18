"""
URL configuration for Medicament project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from client.views import Dashboard,liste_cmd
from emailapp.views import create_view,Email
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('administration/', admin.site.urls),
    path('',include('client.urls')),
    path('',include('publicite.urls')),
    path('accounts/',include('accounts.urls')),
    path('SendEmail/',csrf_exempt(create_view.as_view())),
    path('email/',Email),
    path('admin/',Dashboard),
    path('admin/commandes',liste_cmd ),
    

]+ static (settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
