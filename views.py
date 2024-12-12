import json
from django.http import JsonResponse
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import logout,login
from .forms import Registration
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate


def display(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Log the user in
            login(request, user)
            return redirect('dashboard')  # Redirect to dashboard on success
        else:
            return HttpResponse('Invalid username or password')
    
    return render(request, 'index.html')

def register(request):
    form = Registration()
    if request.method == "POST":
        form = Registration(request.POST)
        username = request.POST['username']
        password  = request.POST['password2']
        name = request.POST['name']
        email = request.POST['email']
        print(username,name,email)
        user = User.objects.create(username = username, first_name = name, email = email)
        user.set_password(password)
        user.save()
        return redirect('/')
    context = {
        'form': form,
    }
    return render(request,'register.html',context)

def forget(request):
    import random
    if request.method == 'POST':
        toemail = request.POST.get('email')
        if User.objects.filter(email=toemail).exists():
            # Generate a random 6-digit OTP
            otp = random.randint(100000, 999999)

            # Store OTP in the session (or use a database/cache)
            request.session['otp'] = otp
            request.session['email'] = toemail

            # Send OTP via email
            send_mail(
                'OTP Verification',
                f'Your OTP is {otp}',
                settings.EMAIL_HOST_USER,
                [toemail],
                fail_silently=False,
            )
            return redirect('otp')  # Redirect to the OTP input page
        else:
            return HttpResponse(f'No such email: {toemail}')
    return render(request, 'forget.html')


def otp(request):
    return render(request,'otp.html')

def verify(request):
    if request.method == 'POST':
        try:
            # Parse JSON body to get the OTP
            data = json.loads(request.body)
            otp_entered = data.get('otp')

            # Retrieve stored OTP from the session
            otp_stored = request.session.get('otp')

            # Check if entered OTP matches the stored OTP
            if str(otp_entered) == str(otp_stored):
                # Clear OTP from the session after successful verification
                # del request.session['otp']
                email = request.session.get('email')
                return JsonResponse({'status': 'success', 'message': 'OTP verified successfully.',})
            else:
                return JsonResponse({'status': 'error', 'message': 'Invalid OTP.'})
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON format.'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': f'Error: {str(e)}'})

    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})

def change(request):
    if request.method == 'POST':
        new = request.POST.get('new')
        print(new)
        ubj = request.session.get('email')
        print(ubj)
        userobj = User.objects.get(email = ubj)
        userobj.set_password(new)
        userobj.save()
        return redirect('login')
    return render(request,'changepassword.html')

@login_required(login_url='/') 
def dashboard(request):
    username = request.user.username
    posts = UserImage.objects.all().order_by('-uploaded_at')
    return render(request, 'dashboard.html', {'username': username,
                                              'posts': posts,})

from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout


from .forms import UserImageForm
from .models import UserImage


@login_required(login_url='/')
def upload_image(request):
    if request.method == 'POST':
        form = UserImageForm(request.POST, request.FILES)
        if form.is_valid():
            user_image = form.save(commit=False)
            user_image.user = request.user  # Associate the image with the logged-in user
            user_image.save()
            return redirect('dashboard')  # Redirect after successful upload
    else:
        form = UserImageForm()
    return render(request, 'upload_image.html', {'form': form})


@login_required(login_url='/')
def myposts(request):
    user_images = UserImage.objects.filter(user=request.user)
    print(request.user)
    print(user_images)
    return render(request,'myposts.html',{'images': user_images})


from django.http import JsonResponse
from .models import Like, UserImage

@login_required(login_url='/')
def like_post(request, post_id):
    post = get_object_or_404(UserImage, id=post_id)
    print(post.likes.count())
    like, created = Like.objects.get_or_create(user=request.user, post=post)
    if not created:
        like.delete()  # Unlike if already liked
        is_liked = False
    else:
        is_liked = True
    total_likes = post.likes.count()  # Cached result
    return JsonResponse({'is_liked': is_liked, 'total_likes': total_likes})




from .models import Comment, UserImage
from django.shortcuts import get_object_or_404


@login_required(login_url='/')
def add_comment(request, post_id):
    if request.method == 'POST':
        post = get_object_or_404(UserImage, id=post_id)
        text = request.POST.get('text')
        if text:
            Comment.objects.create(user=request.user, post=post, text=text)
    return redirect('myposts')  # Redirect back to the posts page


