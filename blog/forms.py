from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)


class ContactForm(forms.Form):

    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    content = forms.CharField(
        required=True,
        widget=forms.Textarea
    )
    sport_list = (
        ('FB', 'football'),
        ('TNS', 'tennis'),

    )
    sport_type = forms.ChoiceField(choices=sport_list,required=True)

    Weekday = (
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday','Wednesday'),

    )

    weekday = forms.ChoiceField(choices=Weekday,required=True)
