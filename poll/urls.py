from . import views
from django.urls import path
from poll.views import MyCustomLoginView,VoteView,ResultsView
urlpatterns=[
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/delete/', views.DeleteView.as_view(), name='delete'),
    path('login/', MyCustomLoginView.as_view(), name='login'),
    path('vote/<int:pk>', VoteView.as_view(), name='vote'),
    path('results/<int:pk>', ResultsView.as_view(), name='results'),

]