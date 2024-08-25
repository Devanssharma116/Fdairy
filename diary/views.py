from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .models import DiaryEntry
from .forms import DiaryEntryForm

@login_required
def entry_list(request):
    entries = DiaryEntry.objects.filter(user=request.user)
    return render(request, 'diary/entry_list.html', {'entries': entries})

@login_required
def entry_create(request):
    if request.method == 'POST':
        form = DiaryEntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.save()
            return redirect('entry-list')
    else:
        form = DiaryEntryForm()
    return render(request, 'diary/entry_form.html', {'form': form})

@login_required
def entry_update(request, pk):
    entry = get_object_or_404(DiaryEntry, pk=pk, user=request.user)
    if request.method == 'POST':
        form = DiaryEntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('entry-list')
    else:
        form = DiaryEntryForm(instance=entry)
    return render(request, 'diary/entry_form.html', {'form': form})

@login_required
def entry_delete(request, pk):
    entry = get_object_or_404(DiaryEntry, pk=pk, user=request.user)
    if request.method == 'POST':
        entry.delete()
        return redirect('entry-list')
    return render(request, 'diary/entry_confirm_delete.html', {'entry': entry})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('entry-list')
    else:
        form = UserCreationForm()
    return render(request, 'diary/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('entry-list')
    else:
        form = AuthenticationForm()
    return render(request, 'diary/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')
