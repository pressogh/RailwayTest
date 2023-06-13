from rest_framework.response import Response
from rest_framework import status

import logging

class ErrorCollection:
    def __init__(self, code: str = "", status: int = status.HTTP_400_BAD_REQUEST, detail: str = ""):
        self.code = code
        self.status = status
        self.detail = detail

    def as_res(self, detail=None):
        logging.getLogger("django").error(f"{self.code}: {self.detail}")
        return Response(
            {"error": {"detail": detail if detail else self.detail, "code": self.code}},
            status=self.status,
        )


API_EXCEPTION_0001 = ErrorCollection(
    code="API_EXCEPTION_0001",
    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
    detail="API 수행 중 오류가 발생했습니다.",
)
VALIDATION_ERROR_0001 = ErrorCollection(code="VALIDATION_ERROR_0001", detail="잘못된 요청 데이터 형식입니다.")

USER_GET_0001 = ErrorCollection(
    code="USER_GET_0001",
    status=status.HTTP_400_BAD_REQUEST,
    detail="해당하는 유저가 없거나 유저 정보를 조회할 권한이 없습니다."
)

FRANCHISE_POST_0001 = ErrorCollection(
    code="FRANCHISE_POST_0001",
    status=status.HTTP_400_BAD_REQUEST,
    detail="location_master에는 가맹 계정에만 등록이 가능합니다."
)

STUDENTGROUP_POST_0001 = ErrorCollection(
    code="STUDENTGROUP_POST_0001",
    status=status.HTTP_400_BAD_REQUEST,
    detail="중복되는 그룹 이름이 존재합니다."
)
STUDENTGROUP_POST_0002 = ErrorCollection(
    code="STUDENTGROUP_POST_0002",
    status=status.HTTP_400_BAD_REQUEST,
    detail="이미 그룹이 존재하는 학생이 있습니다."
)
STUDENTGROUP_POST_0003 = ErrorCollection(
    code="STUDENTGROUP_POST_0003",
    status=status.HTTP_400_BAD_REQUEST,
    detail="학생이 아니거나 db에 존재하지 않는 학생 id가 있습니다."
)

TEXTBOOK_GET_0001 = ErrorCollection(
    code="TEXTBOOK_GET_0001",
    status=status.HTTP_400_BAD_REQUEST,
    detail="해당 교재를 볼 수 있는 권한이 없습니다."
)
TEXTBOOK_GET_0002 = ErrorCollection(
    code="TEXTBOOK_GET_0002",
    status=status.HTTP_400_BAD_REQUEST,
    detail="다음에 해당하는 type만 사용할 수 있습니다. [PR, TE, RE]"
)
TEXTBOOK_GET_0003 = ErrorCollection(
    code="TEXTBOOK_GET_0003",
    status=status.HTTP_400_BAD_REQUEST,
    detail="다음에 해당하는 school_type만 사용할 수 있습니다. [EL, MI, HI]"
)

TEXTBOOK_POST_0001 = ErrorCollection(
    code="TEXTBOOK_POST_0001",
    status=status.HTTP_400_BAD_REQUEST,
    detail="파일이 업로드되지 않았습니다."
)
TEXTBOOK_POST_0002 = ErrorCollection(
    code="TEXTBOOK_POST_0002",
    status=status.HTTP_400_BAD_REQUEST,
    detail="확장자가 pdf인 파일만 업로드가 가능합니다."
)
TEXTBOOK_POST_0003 = ErrorCollection(
    code="TEXTBOOK_POST_0003",
    status=status.HTTP_400_BAD_REQUEST,
    detail="파일이 잘못되었거나 pdf가 아닌 파일입니다."
)

SEND_TEXTBOOK_0001 = ErrorCollection(
    code="SEND_TEXTBOOK_0001",
    status=status.HTTP_400_BAD_REQUEST,
    detail="textbook_id에 해당하는 교재가 없습니다."
)

TEXTBOOK_COMPLETE_0001 = ErrorCollection(
    code="TEXTBOOK_COMPLETE_0001",
    status=status.HTTP_400_BAD_REQUEST,
    detail="textbook_id에 해당하는 교재가 없습니다."
)
TEXTBOOK_COMPLETE_0002 = ErrorCollection(
    code="TEXTBOOK_COMPLETE_0002",
    status=status.HTTP_400_BAD_REQUEST,
    detail="해당 학생에게 textbook_id에 해당하는 교재가 없습니다."
)
TEXTBOOK_COMPLETE_0003 = ErrorCollection(
    code="TEXTBOOK_COMPLETE_0003",
    status=status.HTTP_400_BAD_REQUEST,
    detail="json 형태의 교재만 업로드가 가능합니다."
)

REVIEW_NOTE_GET_0001 = ErrorCollection(
    code="REVIEW_NOTE_GET_0001",
    status=status.HTTP_400_BAD_REQUEST,
    detail="본인의 오답노트 리스트만 조회할 수 있습니다."
)
REVIEW_NOTE_GET_0002 = ErrorCollection(
    code="REVIEW_NOTE_GET_0002",
    status=status.HTTP_400_BAD_REQUEST,
    detail="본인 학생의 오답노트만 조회할 수 있습니다."
)
REVIEW_NOTE_GET_0003 = ErrorCollection(
    code="REVIEW_NOTE_GET_0003",
    status=status.HTTP_400_BAD_REQUEST,
    detail="권한이 없는 사용자입니다."
)
REVIEW_NOTE_GET_0004 = ErrorCollection(
    code="REVIEW_NOTE_GET_0004",
    status=status.HTTP_400_BAD_REQUEST,
    detail="해당 가맹점 학생의 오답노트만 조회할 수 있습니다."
)
REVIEW_NOTE_POST_0001 = ErrorCollection(
    code="REVIEW_NOTE_POST_0001",
    status=status.HTTP_400_BAD_REQUEST,
    detail="확장자가 json인 파일만 업로드할 수 있습니다."
)

STUDENT_TEXTBOOK_LIST_0001 = ErrorCollection(
    code="STUDENT_TEXTBOOK_LIST_0001",
    status=status.HTTP_400_BAD_REQUEST,
    detail="본인의 교재만 조회할 수 있습니다."
)
STUDENT_TEXTBOOK_LIST_0002 = ErrorCollection(
    code="STUDENT_TEXTBOOK_LIST_0002",
    status=status.HTTP_400_BAD_REQUEST,
    detail="담당 학생의 교재만 조회할 수 있습니다."
)
STUDENT_TEXTBOOK_LIST_0003 = ErrorCollection(
    code="STUDENT_TEXTBOOK_LIST_0003",
    status=status.HTTP_400_BAD_REQUEST,
    detail="해당 가맹점 학생의 교재만 조회할 수 있습니다."
)
STUDENT_TEXTBOOK_LIST_0004 = ErrorCollection(
    code="STUDENT_TEXTBOOK_LIST_0004",
    status=status.HTTP_400_BAD_REQUEST,
    detail="student_id에 해당하는 학생이 존재하지 않습니다."
)
STUDENT_TEXTBOOK_LIST_0005 = ErrorCollection(
    code="STUDENT_TEXTBOOK_LIST_0005",
    status=status.HTTP_400_BAD_REQUEST,
    detail="다음에 해당하는 query만 사용할 수 있습니다. [PR, CO]"
)
STUDENT_TEXTBOOK_LIST_0006 = ErrorCollection(
    code="STUDENT_TEXTBOOK_LIST_0006",
    status=status.HTTP_400_BAD_REQUEST,
    detail="다음에 해당하는 type만 사용할 수 있습니다. [PR, TE, RE]"
)

TEACHER_BY_FRANCHISE_LIST_0001 = ErrorCollection(
    code="TEACHER_BY_FRANCHISE_LIST_0001",
    status=status.HTTP_400_BAD_REQUEST,
    detail="본인이 관리자인 franchise의 선생님만 조회할 수 있습니다."
)

REVIEW_NOTE_COMPLETE_0001 = ErrorCollection(
    code="REVIEW_NOTE_COMPLETE_0001",
    status=status.HTTP_400_BAD_REQUEST,
    detail="학생은 자신의 오답노트를 완료 처리할 수 없습니다."
)
REVIEW_NOTE_COMPLETE_0002 = ErrorCollection(
    code="REVIEW_NOTE_COMPLETE_0002",
    status=status.HTTP_400_BAD_REQUEST,
    detail="해당 오답노트가 존재하지 않습니다."
)
REVIEW_NOTE_COMPLETE_0003 = ErrorCollection(
    code="REVIEW_NOTE_COMPLETE_0003",
    status=status.HTTP_400_BAD_REQUEST,
    detail="본인의 학생의 오답노트만 완료 처리할 수 있습니다."
)
REVIEW_NOTE_COMPLETE_0004 = ErrorCollection(
    code="REVIEW_NOTE_COMPLETE_0004",
    status=status.HTTP_400_BAD_REQUEST,
    detail="본인의 가맹점에 속한 학생의 오답노트만 완료 처리할 수 있습니다."
)
REVIEW_NOTE_COMPLETE_0005 = ErrorCollection(
    code="REVIEW_NOTE_COMPLETE_0005",
    status=status.HTTP_400_BAD_REQUEST,
    detail="이미 완료된 오답노트입니다."
)