from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordResetForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ComponentForm
from .models import Feedback
from .forms import FeedbackForm
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.views import PasswordResetView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views import View
from django.contrib.auth.views import LoginView
from .forms import CustomAuthenticationForm


class AnaSayfaView(View):
    template_name = 'ana.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('stock_table')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('stock_table')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def password_reset_request(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            form.save(request=request)
            messages.success(request, 'A reset email has been sent.')
            return redirect('login')
    else:
        form = PasswordResetForm()
    return render(request, 'password_reset.html', {'form': form})

def add_component(request):
    if request.method == 'POST':
        form = ComponentForm(request.POST)
        if form.is_valid():
            component = form.save(commit=False)
            component.save()
            return redirect('stock_table')
    else:
        form = ComponentForm()
    return render(request, 'add_component.html', {'form': form})

def submit_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['text']
            Feedback.objects.create(user=request.user, content=content)
            messages.success(request, 'Thank you for your feedback!')
    return redirect('user_profile')  

def view_feedback(request):
    feedback_list = Feedback.objects.all()
    return render(request, 'view_feedback.html', {'feedback_list': feedback_list})


def stock_table(request):
    your_data = ComponentForm.objects.all()  # Veritabanından verileri çekme
    your_data = ComponentForm.objects.filter(name='Component')  # Belirli bir kriterlere göre filtreleme yapma
    your_data = ComponentForm.objects.order_by('-name')  # Verileri sıralama
    your_data = ComponentForm.objects.first()  # Veritabanından ilk kaydı alma
    your_data = ComponentForm.objects.last()  # Veritabanından son kaydı alma
    your_data = ComponentForm.objects.count()  # Veritabanında kayıt sayısını alma

    return render(request, 'stock_table.html', {'data': your_data})

def home(request):
    return render(request, 'home.html')



class CustomLoginView(LoginView):
    template_name = 'yourapp/login.html'  # login.html dosyanızın yolu
    form_class = CustomAuthenticationForm




class CustomPasswordResetView(PasswordResetView):
    email_template_name = 'registration/password_reset_email_tr.html'
    success_url = reverse_lazy('password_reset_done')
    form_class = PasswordResetForm