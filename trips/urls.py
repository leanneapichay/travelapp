from django.urls import path
from . import views

urlpatterns = [
    path('create-trip/', views.TripViews.post),
    path('get-trip/', views.TripViews.get),
    path('delete-trip/', views.TripViews.delete),

    path('add-stop/', views.StopViews.post),
    path('get-stop-info/', views.StopViews.get),
    path('delete-stop', views.StopViews.delete),
    path('get-stops/', views.GetTripStops.get),

    path('create-budget',views.BudgetViews.post),
    path('update-budget', views.BudgetViews.put),

    path('add-bucket-list-item', views.BucketListViews.post),
    path('delete-bucket-list-item', views.BucketListViews.delete),

    path('add-to-packing-list', views.PackingListViews.post),
    path('remove-from-packing-list', views.PackingListViews.delete)
]