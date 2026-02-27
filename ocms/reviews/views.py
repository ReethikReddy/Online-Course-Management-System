from rest_framework import generics, permissions
from django.db.models import Avg
from rest_framework.response import Response
from .models import Review
from .serializers import ReviewSerializer
from courses.models import Course

class CourseReviewsView(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Review.objects.filter(course_id=self.kwargs['course_id'])

    def get_serializer_context(self):
        context = super().get_serializer_context()
        if self.request.method == 'POST':
            context['course'] = Course.objects.get(id=self.kwargs['course_id'])
        return context

    def perform_create(self, serializer):
        course = Course.objects.get(id=self.kwargs['course_id'])
        serializer.save(student=self.request.user, course=course)
        
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        course_id = self.kwargs['course_id']
        avg_rating = Review.objects.filter(course_id=course_id).aggregate(Avg('rating'))['rating__avg']
        return Response({
            'average_rating': round(avg_rating, 2) if avg_rating else 0,
            'reviews': response.data
        })

class MyReviewsView(generics.ListAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Review.objects.filter(student=self.request.user)
