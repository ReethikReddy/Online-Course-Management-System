from django.urls import path
from .views import CourseReviewsView, MyReviewsView

urlpatterns = [
    path('courses/<int:course_id>/reviews/', CourseReviewsView.as_view(), name='course-reviews'),
    path('reviews/my/', MyReviewsView.as_view(), name='my-reviews'),
]
