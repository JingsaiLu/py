from django.forms import ModelForm
from models import Moment
from models import Register

class MomentForm(ModelForm):
    class Meta:
        model = Moment
        fields = '__all__'

class RegisterForm(ModelForm):
    class Meta:
        model = Register
        fields = '__all__'
