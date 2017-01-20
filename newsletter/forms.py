from django import forms

from .models import SignUp


class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['full_name', 'email']
        #exclude can be used but not recommended

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_base, provider = email.split("@")
        domain, extension = provider.split(".")
        if len(email_base) <= 4:
            raise forms.ValidationError("Use a valid email, faggot")

        if len(domain) <= 2:
            raise forms.ValidationError("Provider's to short, faggot")

        if not extension=='com':
            raise forms.ValidationError("Please use a .com email adress, faggot")
        return email

class ContactForm(forms.Form):
    full_name = forms.CharField(required=False, max_length=120)
    email = forms.EmailField()
    message = forms.CharField(max_length=500)
