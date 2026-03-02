from django.shortcuts import redirect, render
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import AuthenticationForm, RegistrationForm, ProfilImageForm
from .models import Product

def main_page(request):
    product = Product.objects.all()

    q_search = request.GET.get("search")
    q_sort = request.GET.get("sort")
    q_category = request.GET.get("category")

    if q_search is not None and len(q_search) > 0:\
        product = product.filter(name__icontains=q_search)

    if q_sort is not None:
        if q_sort == "price_asc":
            product = product.order_by('price')
        elif q_sort == "price_desc":
            product = product.order_by('-price')

    if q_category is not None:
        product = product.filter(category__icontains=q_category)

    context = {
        "product": product
    }

    return render(request, "index.html", context)

def login_page(request):
    if request.method == "POST":
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            login(request, form.user)
            return redirect("main_page")
    else:
        form = AuthenticationForm()

    context = {
        "form": form
    }

    return render(request, "login.html", context)

def register_page(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = User.objects.create_user(
                email=email,
                username=username,
                password=password
            )
            login(request, user)
            return redirect("main_page")
    else:
        form = RegistrationForm()

    context = {
        'form': form
    }

    return render(request, 'register.html', context)

@login_required
def profil_page(request):
    if request.method == "POST":
        form = ProfilImageForm(request.POST)
        if form.is_valid():
            image = form.changed_data.get("image")
    user = User.objects.all()

    context = {
        user: user
    }

    return render(request, "profil.html", context)

def contacts_page(request):
    return render(request, "contacts.html", {})

def about_uss_page(request):
    return render(request, "about_uss.html", {})