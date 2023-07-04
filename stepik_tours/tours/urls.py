from django.urls import path
from tours.views import MainPageView, DepartureView, TourView

urlpatterns = [
    path('', MainPageView.as_view()),
    path('departure/<str:departure>', DepartureView.as_view()),
    path('tour/<int:tour_id>/', TourView.as_view()),
]
