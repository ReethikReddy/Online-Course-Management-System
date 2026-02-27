from rest_framework import serializers
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source='student.username', read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'course', 'student', 'student_name', 'rating', 'comment', 'created_at']
        read_only_fields = ['student', 'course']

    def validate(self, attrs):
        request = self.context.get('request')
        course = self.context.get('course')
        if Review.objects.filter(student=request.user, course=course).exists():
            raise serializers.ValidationError("You have already reviewed this course.")
        return attrs
