from django.urls import path

from . import views

urlpatterns = [
    path("", views.calendar_view, name="calendar"),
    path("day/<str:date>/", views.day_view, name="day_view"),
    path(
        "reserve/<str:date>/<str:hour>/<int:washing_machine_id>/",
        views.reserve_view,
        name="reserve",
    ),
    path(
        "reservation/delete/<int:reservation_id>/",
        views.delete_reservation,
        name="delete_reservation",
    ),
]
