from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index),
    path('Maps', views.Maps),
    path('accounts/', include('allauth.urls')),
    path('journal/list', views.JournalListView.as_view(), name="journallist"),
    path('journal/journalcreate', views.JournalCreateView.as_view(), name="createjournal"),
    path('journal/journalupdate/<int:pk>', views.JournalUpdateView.as_view(), name="updatejournal"),
    path('journal/journaldelete/<int:pk>', views.JournalDeleteView.as_view(), name="deletejournal"),
]
