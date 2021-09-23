from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm

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

@login_required
def profile(request):
	user_update_form = UserUpdateForm()
	profile_update_form = ProfileUpdateForm()

	context = {
		'user_update_form': user_update_form,
		'profile_update_form': profile_update_form,
	}

	return render(request, 'users/profile.html', context)