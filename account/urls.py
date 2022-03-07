from django.urls import path 


from .views import logout_user
from .views import login_user


app_name = "account"

urlpatterns = [
    path('logout/', logout_user, name='logout'),
    path('login/', login_user , name='login'),

]
