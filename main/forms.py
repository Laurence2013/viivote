from django import forms

class Ask_A_Question(forms.Form):
    ask_question = forms.CharField(widget = forms.Textarea(attrs={'cols':80, 'rows': 5}), label = 'Ask a question')
    vote_a = forms.CharField(widget = forms.Textarea(attrs={'cols':80, 'rows': 1}), label = 'Vote question A', required = True)
    vote_b = forms.CharField(widget = forms.Textarea(attrs={'cols':80, 'rows': 1}), label = 'Vote question B', required = True)
    vote_c = forms.CharField(widget = forms.Textarea(attrs={'cols':80, 'rows': 1}), label = 'Vote question C (optional)')

