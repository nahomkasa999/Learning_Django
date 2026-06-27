from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        print("This is the clean data:", self.cleaned_data)
        print("This is the data:", self.data)
        print(f"Sending email to {self.cleaned_data['email']} with message: {self.cleaned_data['message']}")