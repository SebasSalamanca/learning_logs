from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

#Send an email in registration process. 
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import send_mail
from django.template.loader import render_to_string

from django.utils.http import urlsafe_base64_decode
from django.contrib.auth import get_user_model

from .forms import OfficialRegisterForm
# Create your views here.

User = get_user_model()


def register(request):
    """Register a new user"""
    if request.method != 'POST':
        #Display blank registration form. 
        form = OfficialRegisterForm()

    else:
        #Process completed form. 
        form = OfficialRegisterForm(data = request.POST)

        if form.is_valid():
            new_user = form.save(commit = False)
            #Log the user in and then redirect to the home page.

            new_user.is_active = False  #Block log in until confirmed 
            new_user.save()

            #Generate token and uid
            token = default_token_generator.make_token(new_user)
            uid = urlsafe_base64_encode(force_bytes(new_user.pk))
            
            #Send confirmation email
            activation_link = request.build_absolute_uri(f'/activate/{uid}/{token}/')
            email_body = render_to_string('emails/registration_email.html', {
                'user': new_user,
                'activation_link': activation_link,
            })
            send_mail('Confirm your account', email_body, 'jsebastian1119@gmail.com', [new_user.email])

            return redirect('confirmation_sent')

            #login(request, new_user)
            #return redirect('learning_logs:index')
        
    #Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'registration/register.html', context)

def confirmation_sent(request):
    return render(request, 'registration/confirmation_sent.html')

def activate(request, uidb64, token):
    try: 
        uid = urlsafe_base64_decode(uidb64).decode()
        new_user = User.objects.get(pk=uid)
    except (User.DoesNotExist, ValueError):
        new_user = None
    
    if new_user and default_token_generator.check_token(new_user, token):
        new_user.is_active = True
        new_user.save()
        
        return redirect('learning_logs:index')

    return render(request, 'registration/register.html')
