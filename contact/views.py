from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContactForm


def get_contact(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']

            recipients = ['p.neeves@gmail.com']
            if cc_myself:
                recipients.append(sender)

            send_mail(subject, message, sender, recipients)
            # return HttpResponseRedirect('/thanks/')
            return render(request, "contact/thanks.html", {"sender": sender})

    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})


def contact_thanks(request):
    return render(request, 'contact/thanks.html')
