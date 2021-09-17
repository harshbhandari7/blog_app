from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm

def register(request):
	if request.method == 'POST':
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			# saves form data
			form.save()
			# format the data
			username = form.cleaned_data.get('username')
			# for displaying msg alerts
			messages.success(request,
				f'Your account has been created! You can now login!')
			return redirect('login')
	else:
		form = UserRegistrationForm()
	return render(request,
		'users/register.html',
		{ 'form': form },
	)
