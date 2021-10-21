from django.urls import path

from . import views


app_name = "api"

urlpatterns = [
    path('login/', views.login, name='login'),
    path('poll/view/', views.poll_view, name='poll_view'),
    path('poll/view/active', views.poll_active_view, name='poll_active_view'),
    path('poll/update/<int:pk>', views.poll_update_delete, name='poll_update_delete'),
    path('poll/create/', views.poll_create, name='poll_create'),
    #
    path('question/update/<int:pk>', views.question_update_delete, name='question_update_delete'),
    path('question/create/', views.question_create, name='question_create'),
    #
    path('option/update/<int:pk>', views.option_update_delete, name='option_update_delete'),
    path('option/create/', views.option_create, name='option_create'),
    #
    path('answer/view/<int:pk>/', views.user_answe_view, name='user_answe_view'),
    path('answer/update/<int:pk>/', views.user_answer_update_delete, name='user_answer_update_delete'),
    path('answer/create/', views.user_answer_create, name='user_answer_create'),
]