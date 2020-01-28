from django import forms


class FbForm(forms.Form):
    about = forms.CharField(required=False,
                            widget=forms.Textarea(attrs={'rows': "5", 'class': "form-control form-control-line", }), )
    description = forms.CharField(required=False,
                                  widget=forms.Textarea(attrs={'rows': "5", 'class': "form-control form-control-line"}))
    id = forms.CharField()
    access_token = forms.CharField(widget=forms.Textarea)
