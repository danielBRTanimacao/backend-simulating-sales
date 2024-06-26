from django.urls import path
from project import views

app_name = 'sales'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_view, name='create'),
    path('login/', views.login_view, name='login'),

    path('product/<int:id_product>/<str:name_product>/', views.product, name='product')
]