from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import Entry
from django.shortcuts import  render, redirect, HttpResponse
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages




# def register_request(request):
# 	if request.method == "POST":
# 		form = NewUserForm(request.POST)
# 		if form.is_valid():
# 			user = form.save()
# 			login(request, user)
# 			messages.success(request, "Registration successful." )
# 			return redirect("entries:entry_list")
# 		messages.error(request, "Unsuccessful registration. Invalid information.")
# 	form = NewUserForm()
# 	return render (request=request, template_name="entries/register.html", context={"register_form":form})

class LockedView(LoginRequiredMixin):
    login_url = "admin:login"

# class searchbar(LockedView, ListView):
#     def searchbar(request):
#         if request.method=='GET':
#             search=request.GET.get('search')
#             title=Entry.objects.all().filter(title=search)
#             return render(request, 'searchbar.html', {'title':title})

def searchbar(request):
    return HttpResponse("This is searchbar")
# class Searchbar(LockedView, ListView):
#     model = Entry
#     def searchbar(request):
#         return HttpResponse("This is searchbar")
        # if request.method=='GET':
        #     search=request.GET.get('search')
        #     title=Entry.objects.all().filter(title = search)
        #     return render(request, 'temples/entries/searchbar.html', {'title':title})

class EntryListView(LockedView, ListView):
    model = Entry
    queryset = Entry.objects.all().order_by("-date_created")


class EntryDetailView(LockedView, DetailView):
    model = Entry


class EntryCreateView(LockedView, SuccessMessageMixin, CreateView):
    model = Entry
    fields = ["title", "content"]
    success_url = reverse_lazy("entry-list")
    success_message = "Your new entry was created!"


class EntryUpdateView(LockedView, SuccessMessageMixin, UpdateView):
    model = Entry
    fields = ["title", "content"]
    success_message = "Your entry was updated!"

    def get_success_url(self):
        return reverse_lazy("entry-detail", kwargs={"pk": self.object.pk})


class EntryDeleteView(LockedView, SuccessMessageMixin, DeleteView):
    model = Entry
    success_url = reverse_lazy("entry-list")
    success_message = "Your entry was deleted!"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)
    
