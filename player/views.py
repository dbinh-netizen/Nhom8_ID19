from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm
from .models import Profile
from django.contrib import messages


# Trang chủ
def home(request):
    return render(request, 'player/base.html')

# Trang duyệt game
def brower(request):
    return render(request, 'player/brower.html')

# Trang chi tiết
def detail(request):
    return render(request, 'player/detail.html')


# Trang hồ sơ người dùng
@login_required
def profile(request):
    return render(request, 'player/profile.html')

# Cập nhật avatar trong hồ sơ
@login_required
def update_profile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Avatar của bạn đã được cập nhật!')
            return redirect('profile')  # Chuyển hướng về trang hồ sơ sau khi cập nhật
    else:
        form = ProfileUpdateForm(instance=request.user.profile)

    return render(request, 'profile_update.html', {'form': form})
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm  # Giả sử bạn có một form để cập nhật thông tin

