from fastapi import APIRouter, Depends
from .models import User
from .data                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
router = APIRouter()

@router.post("/auth/signup")
def signup(user: UserCreate):
    # logic for creating new user
