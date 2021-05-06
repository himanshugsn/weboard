from django import forms
from .models import Topic, Post, Board

class NewBoardForm(forms.ModelForm):
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={'row':3,'placeholder':'write description here!'}
        ),
        max_length=30,
        help_text='The max length of the text is 30.'
    )
    class Meta():
        model = Board
        fields = ('name','description')


class NewTopicForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 5, 'placeholder': 'What is on your mind?'}
        ),
        max_length=4000,
        help_text='The max length of the text is 4000.'
    )

    class Meta:
        model = Topic
        fields = ['subject', 'message']
        
# for post reply
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['message', ]