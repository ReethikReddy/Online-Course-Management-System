from rest_framework import serializers
from .models import Enrollment, Progress
from courses.serializers import CourseSerializer
from courses.models import Course, Lecture

class ProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Progress
        fields = '__all__'

class EnrollmentSerializer(serializers.ModelSerializer):
    course_detail = CourseSerializer(source='course', read_only=True)
    progress_percent = serializers.SerializerMethodField()

    class Meta:
        model = Enrollment
        fields = ['id', 'student', 'course', 'enrolled_at', 'is_completed', 'course_detail', 'progress_percent']
        read_only_fields = ['student', 'enrolled_at', 'is_completed']

    def get_progress_percent(self, obj):
        total_lectures = Lecture.objects.filter(module__course=obj.course).count()
        if total_lectures == 0:
            return 0
        completed_lectures = Progress.objects.filter(enrollment=obj).count()
        return int((completed_lectures / total_lectures) * 100)

    def validate(self, attrs):
        request = self.context.get('request')
        course = attrs.get('course')
        if Enrollment.objects.filter(student=request.user, course=course).exists():
            raise serializers.ValidationError("You are already enrolled in this course.")
        return attrs
