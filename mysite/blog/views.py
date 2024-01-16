from django.shortcuts import render , redirect
from django.contrib.auth import authenticate
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.shortcuts import render, redirect
from .models import UserAdmin
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth import login as auth_login
def registerView(request):
    return render(request,'blog/register.html')
def LoginView(request):
    return render(request,'blog/login.html')
def register(request):
    if request.method == 'POST':
        # Get form data from request.POST
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        conf_password = request.POST.get('conf_password', '')
        # Perform basic validation
        if not (first_name and last_name and email and password and conf_password):
            error_message = 'Invalid username or password.'
            return render(request, 'blog/register.html', {'error_message': error_message})
        if password != conf_password:
            error_message ='Passwords do not match.'
            return render(request, 'blog/register.html', {'error_message': error_message})
               # Check if the email already exists
        if UserAdmin.objects.filter(email=email).exists():  
            error_message = 'Email already exists. Please choose a different one.'
            return render(request, 'blog/register.html', {'error_message': error_message})
        # Create a new user
        user = UserAdmin(first_name=first_name, last_name=last_name, email=email)
        user.set_password(password)
        user.save()
        print(user)
        # You might want to customize this logic based on your requirements
        if user:
            error_message= 'Registration successful. Please log in.'
            return render(request, 'blog/login.html', {'error_message': error_message})
        else:
            messages.error(request, 'Registration failed. Please try again.')
            return render(request, 'blog/register.html', {'error_message': error_message})
    return redirect('login_url')


def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')

        # Authenticate the user using email as username
        user = authenticate(request, username=email, password=password)

        if user is not None:
            # Log in the user
            auth_login(request, user)

            # Redirect to a success page or home page
            return render(request,'blog/post_create.html')
        else:
            # Display an error message or redirect back to the login page
            error_message = 'Invalid email or password.'
            return render(request, 'blog/login.html', {'error_message': error_message})
    return render(request, 'blog/login.html')
def index(request):
    return render(request,'blog/post_create.html')
def about(request):
    return render(request,'blog/about.html')
def contact(request):
    return render(request,'blog/contact.html')
def home(request):
    posts = Post.objects.order_by('-published_date')
    return render(request, 'blog/index.html', {'posts': posts})
def post_list(request):
    posts = Post.objects.order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'blog/blog-grid.html', {'post': post})
def post_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        text = request.POST.get('text')
        author = request.POST.get('author')
        image = request.FILES.get('image')
        Post.objects.create(title=title, text=text, author=author, image=image,published_date=timezone.now() )
        return redirect('post_list')
    else:
        return render(request, 'post_create.html')
def post_update(request, id):
    if request.method == 'POST':
        update_post = Post.objects.get(id=id)
        update_post.title = request.POST.get('title')
        update_post.text = request.POST.get('text')
        update_post.author = request.POST.get('author')
        update_post.published_date=timezone.now()
        update_post.save()
        return redirect('post_list')  # 
def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect('post_list')