from typing import Union, List
from fastapi import APIRouter
import app.shemas.member as member_schema

router = APIRouter()


# ルート割り当て
@router.get("/member", tags=["member"], response_model=List[member_schema.Member])
async def getMemberList():
    return [
        member_schema.Member(
            id=1,
            first_name="山錦",
            second_name="拓郎",
            e_mail="test1234@example.com",
            status="m01",
        ),
        member_schema.Member(
            id=2,
            first_name="林田",
            second_name="久作",
            e_mail="98_test34@example.com",
            status="m01",
        ),
    ]


@router.get(
    "/member/{employee_id}", tags=["member"], response_model=member_schema.Member
)
async def getMember(employee_id: int):
    return member_schema.Member(
        id=employee_id,
        first_name="林田",
        second_name="久作",
        e_mail="98_test34@example.com",
        status="m01",
    )


@router.post(
    "/member", tags=["member"], response_model=member_schema.MemberCreateResponse
)
async def postMember(member_body: member_schema.MemberCreate):
    return member_schema.MemberCreateResponse(id=1, **member_body.dict())


@router.put(
    "/member/{employee_id}",
    tags=["member"],
    response_model=member_schema.MemberUpdateResponse,
)
async def putMember(employee_id: int, member_body: member_schema.MemberCreate):
    return member_schema.MemberUpdateResponse(id=employee_id)


@router.delete(
    "/member/{employee_id}",
    tags=["member"],
    response_model=member_schema.MemberDeleteResponse,
)
async def deleteMember(employee_id: int):
    return member_schema.MemberDeleteResponse(id=employee_id)
