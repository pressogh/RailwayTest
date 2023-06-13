from django.db import models


class ReviewNote(models.Model):
    """
    오답노트 테이블
    textbook: 교재 이름
    grade: 학년
    semester: 학기
    chapter_number: 단원 번호
    chapter: 단원
    student: 학생
    created_at: 생성 시간
    updated_at: 업데이트된 시간
    status: 상태
        - PR: 오답노트 작성 완료
        - CO: 오답노트 완료
        - RJ: 오답노트 반려 -> 다시 작성 후 제출 필요
    file: 오답노트 파일(json)
    """

    def get_upload_path(instance, filename):
        return filename

    textbook = models.CharField(max_length=100, null=False, blank=False)
    grade = models.CharField(max_length=100, null=False)
    semester = models.IntegerField(null=False)
    chapter_number = models.IntegerField(null=False)
    chapter = models.CharField(max_length=100, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, null=False)     # PR, CO, RJ
    file = models.FileField(null=False, upload_to=get_upload_path)
