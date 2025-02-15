from django.shortcuts import render

# Create your views here.
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
