from django import forms
from .models import Contact
import re


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "email", "subject", "message"]

    def clean_name(self):
        name = self.cleaned_data.get("name", "").strip()

        if not name:
            raise forms.ValidationError("Please enter your full name.")

        # Numbers not allowed
        if re.search(r"\d", name):
            raise forms.ValidationError("Name cannot contain numbers.")

        # Only letters and spaces
        if not re.fullmatch(r"[A-Za-z ]+", name):
            raise forms.ValidationError(
                "Name can contain only letters and spaces."
            )

        return name

    def clean_email(self):
        email = self.cleaned_data.get("email", "").strip()

        if not email:
            raise forms.ValidationError("Please enter your email address.")
         
        if not re.fullmatch(r"[^@]+@[^@]+\.[^@]+", email):
            raise forms.ValidationError("Please enter a valid email address.")

        return email

    def clean_subject(self):
        subject = self.cleaned_data.get("subject", "").strip()

        if not subject:
            raise forms.ValidationError("Please enter a subject.")

        return subject

    def clean_message(self):
        message = self.cleaned_data.get("message", "").strip()

        if not message:
            raise forms.ValidationError("Please enter your message.")

        return message