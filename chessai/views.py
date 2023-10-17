from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.shortcuts import render


class ProfileView(LoginRequiredMixin, View):
    template_name = 'profile.html'
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'

    @staticmethod
    def get(request):
        return render(request, 'profile.html')


class HomeView(View):
    template_name = 'home.html'

    @staticmethod
    def get(request):
        return render(request, 'home.html')
