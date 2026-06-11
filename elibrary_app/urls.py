from django.urls import path
from . import views


urlpatterns = [

    path('', views.home, name='home'),

    path('explore/', views.explore, name='explore'),

    path('register/', views.Registers, name='register'),

    path('login/', views.Login, name='login'),

    path('addBook/', views.addBook, name='addBook'),

    path('contri/', views.contri, name='contri'),

    path('logout/', views.logout, name='logout'),

    path(
        'deleteBook/<int:book_id>/',
        views.deleteBook,
        name='deleteBook'
    ),

    path(
        'editBook/<int:book_id>/',
        views.editBook,
        name='editBook'
    ),

    path(
        'viewBook/<int:book_id>/',
        views.viewBook,
        name='viewBook'
    ),
]