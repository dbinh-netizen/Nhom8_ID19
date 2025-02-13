from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.utils import timezone
from .models import RegisterForm  # Đảm bảo rằng bạn đã tạo một form đăng ký đúng

# Trang chủ
def home(request):
    return render(request, 'dash/home.html')

# Đăng nhập
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Đăng nhập người dùng vào session
            auth_login(request, user)

            # Lưu thông tin vào database (cập nhật thời gian đăng nhập cuối cùng)
            user.last_login = timezone.now()  # Lưu thời gian đăng nhập
            user.save()  # Lưu thay đổi vào cơ sở dữ liệu

            # Thêm thông báo thành công
            messages.success(request, "Đăng nhập thành công!")

            # Chuyển hướng đến trang home
            return redirect('player')  # Điều hướng đến trang home
        else:
            messages.error(request, "Sai tên hoặc mật khẩu!")
    
    return render(request, 'dash/login.html')

# Đăng ký
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Lưu tài khoản vào cơ sở dữ liệu
            user = form.save()
            messages.success(request, 'Tạo tài khoản thành công, xin hãy đăng nhập!.')

            # Sau khi đăng ký thành công, chuyển hướng đến trang login
            return redirect('login')
        else:
            messages.error(request, 'Xin hãy điền đúng thông tin!.')
    else:
        form = RegisterForm()  # Nếu là GET, khởi tạo form trống

    return render(request, 'dash/register.html', {'form': form})

def player(request):
    return render(request, 'player/base.html')


def play(request,index):
    print(index)
    link =""
    if index =="0":
        ## thêm mấy cái link game khác dô mỗi game tương đương một link và một if else
        ## file home.html thì thêm url cho thẻ a theo thứ tự từ 0 tới cuối rồi cứ mỗi cái là một cái link game <a href="{% url 'playgame' index=0 %}" class="play-button">Play</a>

        link ='https://cloud.onlinegames.io/games/2024/phaser/snake/index-og.html'
    if index =="1":
        link='https://cloud.onlinegames.io/games/2021/2/monster-truck-mountain-climb/index-og.html'
    if index =="2":
        link='https://www.onlinegames.io/games/2023/unity/archer-hero/index.html'
    if index =="3":
        link='https://www.onlinegames.io/games/2023/q2/capybara-clicker-pro/index.html'
    if index =="4":
        link='https://cloud.onlinegames.io/games/2024/unity3/block-blast/index-og.html'
    
        
    return render(request=request,template_name= "dash/playgame.html",context={
        "link":link
    })