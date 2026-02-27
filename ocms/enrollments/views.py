from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import Enrollment, Progress
from .serializers import EnrollmentSerializer, ProgressSerializer
from courses.models import Course, Lecture

class EnrollCourseView(generics.CreateAPIView):
    serializer_class = EnrollmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(student=self.request.user)

class MyCoursesView(generics.ListAPIView):
    serializer_class = EnrollmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Enrollment.objects.filter(student=self.request.user)

class UpdateProgressView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, course_id):
        lecture_id = request.data.get('lecture_id')
        enrollment = get_object_or_404(Enrollment, student=request.user, course_id=course_id)
        lecture = get_object_or_404(Lecture, id=lecture_id, module__course_id=course_id)

        progress, created = Progress.objects.get_or_create(enrollment=enrollment, lecture=lecture)
        
        # Check if course is completed
        total_lectures = Lecture.objects.filter(module__course_id=course_id).count()
        completed_lectures = Progress.objects.filter(enrollment=enrollment).count()
        
        if total_lectures > 0 and total_lectures == completed_lectures:
            enrollment.is_completed = True
            enrollment.save()

        return Response({"detail": "Progress updated", "is_completed": enrollment.is_completed}, status=status.HTTP_200_OK)
