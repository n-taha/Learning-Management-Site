
from django.contrib import admin
from django.urls import path , include
from courses.views import  MyCoursesList,  HomePageView , coursePage , SignupView , LoginView , signout , checkout, submit_manual_payment, edit_profile
from django.conf.urls.static import static
from django.conf import settings
from .views import profile_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', HomePageView.as_view() , name = 'home'),
    path('logout', signout , name = 'logout'),
    path('my-courses', MyCoursesList.as_view() , name = 'my-courses'),
    path('signup', SignupView.as_view() , name = 'signup'),
    path('login', LoginView.as_view() , name = 'login'),
    path('course/<str:slug>', coursePage , name = 'coursepage'),
    path('check-out/<str:slug>', checkout , name = 'checkout'),
    # path('verify_payment', verifyPayment , name = 'verify_payment'),
    path('submit-manual-payment/<str:slug>/', submit_manual_payment, name='submit_manual_payment'),
    path('profile/', profile_view, name='profile'),
    path('profile/edit/', edit_profile, name='edit_profile'),
       path(
        'password/change/',
        auth_views.PasswordChangeView.as_view(
            template_name='profile/password_change.html',
            success_url='/password/change/done/'
        ),
        name='password_change'
    ),

    path(
        'password/change/done/',
        auth_views.PasswordChangeDoneView.as_view(
            template_name='profile/password_change_done.html'
        ),
        name='password_change_done'
    ),
     path(
        'password-reset/',
        auth_views.PasswordResetView.as_view(
            template_name='auth/password_reset.html',
            email_template_name='registration/password_reset_email.html',
        ),
        name='password_reset'
    ),

    # Email sent confirmation
    path(
        'password-reset/done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='auth/password_reset_done.html'
        ),
        name='password_reset_done'
    ),

    # Reset link (from email)
    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='auth/password_reset_confirm.html'
        ),
        name='password_reset_confirm'
    ),

    # Success page
    path(
        'reset/done/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='auth/password_reset_complete.html'
        ),
        name='password_reset_complete'
    ),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)