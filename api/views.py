from django.core.files.base import ContentFile
from django.core.files.uploadedfile import InMemoryUploadedFile
from rest_framework import viewsets
from rest_framework.views import APIView

from api.errors import *
from api.models import ReviewNote
from api.serializers import ReviewNoteSerializer
from api.utils.etc import CustomResponse


class TestApiView(APIView):
	def get(self, request):
		return Response({'message': 'Hello!'})


class ReviewNoteViewSet(viewsets.ModelViewSet):
	queryset = ReviewNote.objects.all()
	serializer_class = ReviewNoteSerializer

	def create(self, request, *args, **kwargs):
		response = CustomResponse()

		name = request.data.get("textbook")
		grade = request.data.get("grade")
		semester = request.data.get("semester")
		chapter = request.data.get("chapter")
		chapter_number = request.data.get("chapter_number")
		file = request.data.get("file")

		if name is None or grade is None or semester is None or chapter is None or chapter_number is None or file is None:
			return VALIDATION_ERROR_0001.as_res()

		import base64
		file = base64.b64decode(file, validate=True)

		# check file is json
		try:
			import json
			temp_file = json.loads(file)
		except:
			return REVIEW_NOTE_POST_0001.as_res()

		file = InMemoryUploadedFile(
			ContentFile(file),
			None,
			f"{name}_{grade}-{semester}_{chapter_number}단원_{chapter}.json",
			"application/json",
			len(file),
			"utf-8"
		)
		request_data = {
			"textbook": name,
			"grade": grade,
			"semester": semester,
			"chapter": chapter,
			"chapter_number": chapter_number,
			"file": file,
		}

		serializer = self.get_serializer(data=request_data)
		serializer.is_valid(raise_exception=True)
		serializer.save()

		response.success = True
		response.message = "오답노트 생성이 성공적으로 완료되었습니다."
		response.response = [serializer.data]

		return Response(response.default_out(), status=status.HTTP_201_CREATED)
