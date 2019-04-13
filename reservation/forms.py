from django import forms
from reservation.models import Reservation
from django.contrib.admin import widgets
from django.contrib.auth.models import User


class contactForm(forms.Form):
    name = forms.CharField(required = False, max_length = 100,help_text = "100 characters max.")
    email = forms.EmailField(required = True)
    comment = forms.CharField(required = True, widget=forms.Textarea)


class ReservationForm(forms.ModelForm):
    date = forms.DateField(required = True)
    time_widget = forms.widgets.TimeInput(attrs={'class': 'time-pick'})
    valid_time_formats = ['%H:%M', '%I:%M%p', '%I:%M %p']
    details = forms.CharField(label='',
                        widget=forms.Textarea(
                        attrs={'placeholder': "Anything we should know?",
                            "class": "form-control"}
                    ))
    time = forms.TimeField(required=False, widget=time_widget, help_text='ex: 10:30AM', input_formats=valid_time_formats)
    class Meta:
        model = Reservation
        fields = [
            'date',
            'details',
            'time',
            #'number'
        ]

    def clean_time(self, *args,**kwargs) :
        import pdb; pdb.set_trace()
        time = self.cleaned_data.get('time')
        if (time.hour>0 and time.hour<12):
            raise forms.ValidationError("We need some sleep at that time!")
        else:
            return time


class UserForm(forms.ModelForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':"input--style-3", 'type':"text" ,'placeholder':"Username" ,'name':"username"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':"input--style-3", 'type':"password" ,'placeholder':"Password" ,'name':"password"}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':"input--style-3", 'type':"email" ,'placeholder':"Email" ,'name':"email"}))
    class Meta():
        model = User
        fields = ('username','password','email')
