from django.core.files.base import ContentFile
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import transaction
from rest_framework import serializers

from api.models import ReviewNote


class ReviewNoteSerializer(serializers.ModelSerializer):
    file = serializers.FileField(required=True, write_only=True)
    textbook = serializers.CharField(max_length=100, required=True)
    grade = serializers.CharField(max_length=100, required=True)
    semester = serializers.IntegerField(required=True)
    chapter_number = serializers.IntegerField(required=True)
    chapter = serializers.CharField(max_length=100, required=True)
    status = serializers.CharField(max_length=2, read_only=True)

    class Meta:
        model = ReviewNote
        fields = "__all__"

    @transaction.atomic
    def save(self, **kwargs):
        name = self.validated_data.get("textbook", "")
        grade = self.validated_data.get("grade", "")
        semester = self.validated_data.get("semester", "")
        chapter_number = self.validated_data.get("chapter_number", "")
        chapter = self.validated_data.get("chapter", "")
        file = self.validated_data.get("file", "")

        file.name = f"{name}_{grade}_{semester}_{chapter_number}_{chapter}.{file.name.split('.')[-1]}"

        review_note = ReviewNote()
        review_note.textbook = name
        review_note.grade = grade
        review_note.semester = semester
        review_note.chapter_number = chapter_number
        review_note.chapter = chapter
        # make temp file
        temp_file = "temp"
        review_note.file = InMemoryUploadedFile(
            ContentFile(temp_file),
            None,
            file.name,
            "text/plain",
            len(temp_file),
            "utf-8"
        )

        review_note.status = "PR"

        review_note.save()

        return review_note
