from django import forms
from .models import Post,Comment,MessageModel,Video

class PostForm(forms.ModelForm):
    # ici on crée un champ body avec ces attributs en definissant son type
    body = forms.CharField(
        label = '',
        widget=forms.Textarea(attrs={
            'rows':'3',
            'placeholder':'Say Something...'
        })
    )
    image = forms.ImageField(
        required=False,
        widget = forms.ClearableFileInput(attrs = {
            'multiple':True,
            'class':'form-control',
            'id':'formFile'
        })
    )
    video = forms.FileField(
        required=False,
        widget = forms.ClearableFileInput(attrs = {
            'multiple':True,
            'class':'form-control',
            'id':'formFile'
        })
    )
    # ici on dit le model qu'on vas utiliser et les champs qui iront avec dans le fichier HTML QUI vas l'Appeler
    class Meta:
        model = Post
        fields = ['body']

class CommentForm(forms.ModelForm):
    # ici on crée un champ body avec ces attributs en definissant son type
    comment = forms.CharField(
        label = '',
        widget=forms.Textarea(attrs={
            'rows':'3',
            'placeholder':'Say Something...'
        })
    )
    # ici on dit le model qu'on vas utiliser et les champs qui iront avec dans le fichier HTML QUI vas l'Appeler
    class Meta:
        model = Comment
        fields = ['comment']

class ThreadForm(forms.Form):
    username = forms.CharField(label='',max_length=100)

# ici c'Est le formulaire pour les tchat(creer les messages) ou on eut avoir soit une image ou du texte
class MessageForm(forms.ModelForm):
    body = forms.CharField(label='',max_length=1000)
    image = forms.ImageField(
        required=False,
        widget = forms.ClearableFileInput(attrs = {
            'multiple':True,
            'class':'form-control',
            'id':'formFile'
        })
    )

    class Meta:
        model = MessageModel
        fields = ['body','image']

class SharedForm(forms.Form):
    body = forms.CharField(
        label='',
        widget = forms.Textarea(attrs={
            'rows':'3',
            'placeholder':'Say Something...'
        }),
    )

# une classe fomulaire afin d'explorer les tags

class ExploreForm(forms.Form):
    query = forms.CharField(
        label='',
        widget = forms.TextInput(
           attrs={
            'placeholder':'Explore tags',
           } 
        )
    ) 