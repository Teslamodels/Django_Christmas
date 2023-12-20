from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CreateUser(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'middlename', 'birth_year', 'birth_month', 'birth_day', 'age']

class ChangeUser(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['birth_year', 'birth_month', 'birth_day', 'age']