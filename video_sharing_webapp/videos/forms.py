from django import forms

class CommentForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-cntrol',
            'placeholder' : 'Leave a Comment'
        }
    ))