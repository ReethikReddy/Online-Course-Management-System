from django.urls import path
from .views import EnrollCourseView, MyCoursesView, UpdateProgressView

urlpatterns = [
    path('enroll/', EnrollCourseView.as_view(), name='enroll'),
    path('my-courses/', MyCoursesView.as_view(), name='my-courses'),
    path('course/<int:course_id>/progress/', UpdateProgressView.as_view(), name='update-progress'),
]
