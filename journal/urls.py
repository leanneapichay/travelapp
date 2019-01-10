from django.urls import path
from . import views

urlpatterns = [
    path('new-journal/', views.JournalViews.post),
    path('alter-journal/', views.JournalViews.put),
    path('delete-journal/', views.JournalViews.delete),

    path('new-bucket-list-review/', views.ReviewBucketListViews.post),
    path('alter-bucket-list-review/', views.ReviewBucketListViews.put),
    path('delete-bucket-list-review/', views.ReviewBucketListViews.delete)
]
