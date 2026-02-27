from rest_framework import views, permissions
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.contrib.auth import get_user_model
from courses.models import Course
from enrollments.models import Enrollment
from django.db.models import Count

User = get_user_model()

class IsAdminUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.role == 'admin')

class AnalyticsView(views.APIView):
    permission_classes = [permissions.IsAuthenticated, IsAdminUser]

    def get(self, request):
        total_students = User.objects.filter(role='student').count()
        total_instructors = User.objects.filter(role='instructor').count()
        total_courses = Course.objects.count()
        total_enrollments = Enrollment.objects.count()
        
        return Response({
            "total_students": total_students,
            "total_instructors": total_instructors,
            "total_courses": total_courses,
            "total_enrollments": total_enrollments
        })

class TopCoursesView(views.APIView):
    permission_classes = [permissions.IsAuthenticated, IsAdminUser]

    @method_decorator(cache_page(60 * 60)) # cache for 1 hour
    def get(self, request):
        top_courses = Course.objects.annotate(
            enrollment_count=Count('enrollments')
        ).order_by('-enrollment_count')[:5]
        
        data = [
            {
                "id": course.id,
                "title": course.title,
                "enrollments": course.enrollment_count
            } for course in top_courses
        ]
        return Response(data)
