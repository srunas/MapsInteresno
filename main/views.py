from django.shortcuts import render
from .models import Journal
from django.views.generic import ListView, CreateView, UpdateView,DeleteView
from django.urls import reverse_lazy


class JournalListView(ListView):
    model = Journal
    template_name = 'maps/journal_list.html'
    context_object_name = 'journal_list'


class JournalCreateView(CreateView):
    model = Journal
    template_name = 'maps/create_journal_form.html'
    fields = ['title', 'description']
    success_url = reverse_lazy('journallist')


class JournalUpdateView(UpdateView):
    model = Journal
    template_name = 'maps/update_journal_form.html'
    fields = ['title', 'description']


class JournalDeleteView(DeleteView):
    model = Journal
    template_name = 'maps/delete_journal_form.html'
    success_url = reverse_lazy('journallist')


def index(request):
    return render(request,  'maps/index.html')


def Maps(request):
    return render(request, 'maps/Maps.html')
