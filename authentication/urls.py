from dj_rest_auth.registration.views import RegisterView, VerifyEmailView, ResendEmailVerificationView
from dj_rest_auth.views import LoginView, LogoutView, UserDetailsView
from authentication.views import email_confirm_redirect, password_reset_confirm_redirect
from django.urls import path, re_path
from dj_rest_auth.views import (PasswordResetConfirmView, PasswordResetView,)

urlpatterns = [
    path("account-confirm-email/<str:key>/", email_confirm_redirect, name="account_confirm_email"),
    path("register/", RegisterView.as_view(), name="rest_register"),
    path("login/", LoginView.as_view(), name="rest_login"),
    path("logout/", LogoutView.as_view(), name="rest_logout"),
    path("user/", UserDetailsView.as_view(), name="rest_user_details"),
    path("register/verify-email/", VerifyEmailView.as_view(), name="rest_verify_email"),
    path("register/resend-email/", ResendEmailVerificationView.as_view(), name="rest_resend_email"),
    path('register/account-confirm-email/<str:key>/', VerifyEmailView.as_view(), name='account_confirm_email'),
    path("account-confirm-email/", VerifyEmailView.as_view(), name="account_email_verification_sent"),

    path("password/reset/", PasswordResetView.as_view(), name="rest_password_reset"),
    path("password/reset/confirm/<str:uidb64>/<str:token>/", password_reset_confirm_redirect, name="password_reset_confirm"),
    path("password/reset/confirm/", PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
]
