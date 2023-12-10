from django import forms
from .models import Account
#from captcha.fields import ReCaptchaField 
#from captcha.widgets import ReCaptchaV2Checkbox



class ResitrationForm(forms.ModelForm):
  
    class Meta:
        model=Account
        fields=['name','email','password','country','phone_number']
        # captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox) 





