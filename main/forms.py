from django import forms

class Edit_Answer(forms.Form):
     edit = forms.CharField(widget = forms.Textarea(attrs={'cols':80, 'rows': 5}), label = 'Edit Answer')

class Answer_Vote_Form(forms.Form):
    answer = forms.CharField(widget = forms.Textarea(attrs={'cols':80, 'rows': 5}), label = 'Answer Vote')

class Ask_A_Question(forms.Form):
    ask_question = forms.CharField(widget = forms.Textarea(attrs={'cols':80, 'rows': 5}), label = 'Ask a question')
    vote_a = forms.CharField(widget = forms.Textarea(attrs={'cols':80, 'rows': 1}), label = 'Vote question A *', required = True)
    vote_b = forms.CharField(widget = forms.Textarea(attrs={'cols':80, 'rows': 1}), label = 'Vote question B *', required = True)
    vote_c = forms.CharField(widget = forms.Textarea(attrs={'cols':80, 'rows': 1}), label = 'Vote question C *', required = True)


