from django import forms
from home.models import Friends,Create_Post


class AddFriendForm(forms.ModelForm):
 #   name = forms.CharField(max_length=30, label='name', widget=forms.TextInput(attrs={"type":"text", "name":"name", "class":"form-control", "id":"name", "placeholder":"Enter name",}),)
    class Meta:
        model=Friends
        fields='__all__'

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model=Friends
        fields = '__all__'

class Post_form(forms.ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={'type':'text', 'class':'form-control','id':"title", 'rows':'3', 'placeholder':"Title",'required':True}),)
    message = forms.CharField(label='', widget=forms.Textarea(attrs={'type':'text', 'class':'form-control','id':"message", 'rows':'3', 'placeholder':"What are you thinking..?",}),)
    
    class Meta:
        model = Create_Post
        fields = [
            'title',
            'message',
            
        ]