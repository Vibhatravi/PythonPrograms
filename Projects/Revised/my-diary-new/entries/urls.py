from django.urls import path
# from django.conf.urls import url
from . import views

# app_name = "Entries",

urlpatterns = [
    # url('upload',views.upload, name='upload'),
    
    path("", views.EntryListView.as_view(), name="entry-list"),
    path(
        "entry/<int:pk>", views.EntryDetailView.as_view(), name="entry-detail"
    ),
    path("create", views.EntryCreateView.as_view(), name="entry-create"),
    path(
        "entry/<int:pk>/update",
        views.EntryUpdateView.as_view(),
        name="entry-update",
    ),
    path(
        "entry/<int:pk>/delete",
        views.EntryDeleteView.as_view(),
        name="entry-delete",
    ),
    path("search", views.searchbar, name='searchbar')
    #path("searchbar/", views.Searchbar.as_view(), name='searchbar'),
    # path("", views.register_request, name="register")
]
