from django.shortcuts import render


# Create your views here

from django.http import HttpResponse
from django.template import loader
from django.urls import reverse_lazy
from django.views import generic
from .forms import ContactForm
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.core.mail import EmailMessage

def top(request):
    context = {
        'name': 'ちびはる',
    }
    return render(request, 'myprofile/top.html', context)

def works(request):
    return render(request, 'myprofile/works.html')


def portfolio(request):
    return render(request, 'myprofile/portfolio.html')


class Form(generic.FormView):
    form_class = ContactForm
    success_url = reverse_lazy('myprofile:thanks')
    template_name = 'myprofile/form.html'

    def form_valid(self, form):
        subject = 'お問い合わせがあったよ'
        message = render_to_string('myprofile/mail.txt', form.cleaned_data, self.request)
        from_email = 'chibiharujijimasa@gmail.com'
        recipient_list = []
        bcc = ['chibiharujijimasa@gmail.com']
        email = EmailMessage(subject, message, from_email, recipient_list, bcc)
        email.send()
        return redirect('myprofile:thanks')

class Thanks(generic.TemplateView):
    template_name = 'myprofile/thanks.html'