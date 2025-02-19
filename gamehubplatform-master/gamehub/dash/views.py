
from django.shortcuts import render
from django.views import View, forms 
def home(request):
    print("home")
    return render(request, 'dash/home.html')
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
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Game, GameReview
from .forms import GameReviewForm

# View hiển thị chi tiết game và danh sách đánh giá
def game_detail(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    reviews = game.reviews.all()
    review_form = GameReviewForm()
    return render(request, 'game_detail.html', {'game': game, 'reviews': reviews, 'review_form': review_form})

# View xử lý gửi đánh giá
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



