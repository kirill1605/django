from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.shortcuts import render, redirect

def profile(request):
    return render(request, 'home/profile.html')

def logout_view(request):
    logout(request)
    return redirect('main:index')

class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'login__input'})
        self.fields['password1'].widget.attrs.update({'class': 'login__input'})
        self.fields['password2'].widget.attrs.update({'class': 'login__input'})
        
        self.fields['username'].help_text = ''
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''

class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['username'].help_text = ''
        self.fields['password'].help_text = ''

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home:profile')
    else:
        form = CustomUserCreationForm()
    return render(request, 'home/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('home:profile')
    else:
        form = CustomAuthenticationForm()
        
    for field in form.fields.values():
        field.widget.attrs['class'] = 'login__input'
        
    return render(request, 'home/login.html', {'form': form})

