from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'input'})
    )
    password2 = forms.CharField(
        label='Password confirmation',
        widget=forms.PasswordInput(attrs={'class': 'input'})
    )

    class Meta:
        model = User
        fields = ('email', 'nom', 'prenom', 'dateDeNaissance', 'profilePic')
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'input'}),
            'nom': forms.TextInput(attrs={'class': 'input'}), 
            'prenom': forms.TextInput(attrs={'class': 'input'}),
            'profilePic': forms.FileInput(attrs={'class': '', 'type': 'file'}),
            'dateDeNaissance': forms.DateInput(attrs={'type': 'date', 'class': 'input'}),
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
