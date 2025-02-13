from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm
<<<<<<< HEAD
from .models import Profile
from django.contrib import messages

=======
from .models import PlayerScore, Profile
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Game, GameReview
from .forms import GameReviewForm
>>>>>>> code_cua_sang

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

<<<<<<< HEAD
=======
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Game, User, DeveloperProfile, DesignerProfile

@login_required
def dashboard(request):
    user = request.user
    context = {}

    if user.role == 'player':
        context['games'] = Game.objects.all()
        return render(request, 'player/dashboard.html', context)
    
    elif user.role == 'developer':
        context['developer_profile'] = DeveloperProfile.objects.get(user=user)
        return render(request, 'developer/dashboard.html', context)
    
    elif user.role == 'designer':
        context['designer_profile'] = DesignerProfile.objects.get(user=user)
        return render(request, 'designer/dashboard.html', context)
    
    elif user.role == 'admin':
        context['users'] = User.objects.all()
        return render(request, 'admin/dashboard.html', context)

    return render(request, 'guest/home.html', context)
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import DesignerProfile, SystemAdminProfile

# Trang Dashboard cho Designer
@login_required
def designer_dashboard(request):
    designer_profile = DesignerProfile.objects.get(user=request.user)
    return render(request, 'designer_dashboard.html', {'designer': designer_profile})

# Trang Dashboard cho Admin
@login_required
def admin_dashboard(request):
    admin_profile = SystemAdminProfile.objects.get(user=request.user)
    return render(request, 'admin_dashboard.html', {'admin': admin_profile})
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.shortcuts import render


from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def player_dashboard(request):
    return render(request, 'player/player_dashboard.html', {'username': request.user.username})
from django.contrib.auth.decorators import login_required

@login_required
def player_dashboard(request):
    return render(request, 'player/player_dashboard.html', {'username': request.user.username})
from django.http import HttpResponse

def game_detail(request, game_id):
    return HttpResponse(f"Game ID: {game_id}")
@login_required
def submit_review(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    if request.method == 'POST':
        form = GameReviewForm(request.POST)
        if form.is_valid():
            review, created = GameReview.objects.update_or_create(
                game=game,
                user=request.user,
                defaults={'rating': form.cleaned_data['rating'], 'comment': form.cleaned_data['comment']}
            )
            return JsonResponse({'success': True, 'rating': review.rating, 'comment': review.comment})
    return JsonResponse({'success': False, 'error': 'Invalid data'})


def leaderboard(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    top_scores = PlayerScore.objects.filter(game=game).order_by('-score')[:10]
    
    leaderboard_data = [
        {
            "player": score.player.username,
            "score": score.score,
            "date": score.date.strftime("%Y-%m-%d %H:%M:%S"),
        }
        for score in top_scores
    ]
    
    return JsonResponse({"game": game.title, "leaderboard": leaderboard_data})
from .models import PlayerScore
def leaderboard_view(request):
    players = PlayerScore.objects.order_by('-score')[:10]  # Lấy top 10 người chơi
    return render(request, 'player/leaderboard.html', {'players': players})
>>>>>>> code_cua_sang
