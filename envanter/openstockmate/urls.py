from django.urls import path
from .views import home, user_login, user_register, password_reset_request, view_feedback, stock_table, add_component, submit_feedback

urlpatterns = [
    path('', home, name='home'),  
    path('home/', home, name='home'),
    path('login/', user_login, name='login'),
    path('register/', user_register, name='register'),
    path('password-reset/', password_reset_request, name='password_reset'),
    path('stock-table/', stock_table, name='stock_table'),
    path('add_component/', add_component, name='add_component'),
    path('submit_feedback/', submit_feedback, name='submit_feedback'),
    path('submit_feedback/', submit_feedback, name='submit_feedback'),
    path('view_feedback/', view_feedback, name='view_feedback'),
]




