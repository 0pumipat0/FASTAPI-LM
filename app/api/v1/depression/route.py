from fastapi import APIRouter
from .schema import depressionRequest
from .service import assess_depression_sevice

router = APIRouter()

@router.post('/depression', tags=['Depression'])
def assess_depression(data:depressionRequest):
    return assess_depression_sevice()