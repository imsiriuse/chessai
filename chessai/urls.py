from django.contrib import admin
from django.urls import path, include
from chessai.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', ProfileView.as_view(), name='profile'),
    path('', HomeView.as_view(), name='home'),
]
