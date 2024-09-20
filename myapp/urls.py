from django.urls import path

from myapp.views import CreateTGUser, ListTGUser, DeleteTGUser

urlpatterns = [
    path('api/v1/users/', CreateTGUser.as_view()),
    path('api/v1/users/delete/<int:tg_id>/', DeleteTGUser.as_view(), name='user-delete'),
    path('', ListTGUser, name='index'),
]
