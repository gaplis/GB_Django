from django import forms
from seminar_3_app.models import Author, Post, Comment


class GamesForm(forms.Form):
    GAME_CHOICES = (
        ('HeadsOrTails', 'Heads or Tails'),
        ('Dice', 'Dice'),
        ('RandomNumber', 'Random Number'),
    )

    change_game = forms.ChoiceField(choices=GAME_CHOICES)
    count = forms.IntegerField(min_value=1, max_value=64)


class AddAuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'email', 'bio', 'bd']


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'post', 'author', 'category']


class AddComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'post', 'comment']