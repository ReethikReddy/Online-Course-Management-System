from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryListView, CourseListView, CourseDetailView, InstructorCourseViewSet

router = DefaultRouter()
router.register(r'instructor/courses', InstructorCourseViewSet, basename='instructor-courses')

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('courses/', CourseListView.as_view(), name='course-list'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course-detail'),
    path('', include(router.urls)),
]
