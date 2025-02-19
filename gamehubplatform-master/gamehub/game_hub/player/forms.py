from django import forms
from .models import Profile, CustomUser

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar']

from django import forms
from .models import GameReview

class GameReviewForm(forms.ModelForm):
    class Meta:
        model = GameReview
        fields = ['rating', 'comment']
        widgets = {
            'rating': forms.Select(choices=[(i, str(i)) for i in range(1, 6)], attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Write your review here...'}),
        }

class GameReviewForm(forms.ModelForm):
    class Meta:
        model = GameReview
        fields = ['rating', 'comment']


class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser 
        fields = ['fullname', 'email', 'birthday', 'phone', 'address', 'gender','img']
        widgets = {
            'fullname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nhập họ và tên'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Nhập email'}),
            'birthday': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nhập số điện thoại'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Nhập địa chỉ', 'rows': 2}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'img': forms.FileInput(attrs={'class': 'form-control'}),
        }