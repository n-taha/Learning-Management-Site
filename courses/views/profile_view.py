from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..models import AdditionalInfo,UserCourse
from django.contrib.auth.models import User
from courses.forms.profile_forms import UserEditForm, AdditionalInfoForm

@login_required
def profile_view(request):
    """
    Profile page:
    - User এর সমস্ত মূল তথ্য দেখাবে (first_name, last_name, email, username)
    - AdditionalInfo fields দেখাবে (address, phone_number, school, district, upozilla, profile_picture, batch_year)
    - User যেসব course enroll করেছে, সেগুলো দেখাবে
    """
    user = request.user
    # AdditionalInfo object তৈরি করা, যদি না থাকে
    additional_info, created = AdditionalInfo.objects.get_or_create(user=user)

    # User এর enrolled courses
    user_courses = UserCourse.objects.filter(user=user).select_related('course')

    context = {
        'user': user,
        'additional_info': additional_info,
        'user_courses': user_courses,
    }
    return render(request, 'profile/profile.html', context)


@login_required
def edit_profile(request):
    user = request.user
    additional_info, created = AdditionalInfo.objects.get_or_create(user=user)

    if request.method == 'POST':
        user_form = UserEditForm(request.POST, instance=user)
        info_form = AdditionalInfoForm(
            request.POST,
            request.FILES,
            instance=additional_info
        )

        if user_form.is_valid() and info_form.is_valid():
            user_form.save()
            info_form.save()
            return redirect('profile')   # profile page url name
    else:
        user_form = UserEditForm(instance=user)
        info_form = AdditionalInfoForm(instance=additional_info)

    context = {
        'user_form': user_form,
        'info_form': info_form
    }
    return render(request, 'profile/edit_profile.html', context)