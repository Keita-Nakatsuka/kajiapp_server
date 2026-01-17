from pydantic import BaseModel
from datetime import datetime


class UserBase(BaseModel):
    name: str


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class TblKajiBase(BaseModel):
    kaji_id: int
    user_id: int
    done_date: datetime


class TblKajiCreate(TblKajiBase):
    pass


class TblKajiCreateMultiple(BaseModel):
    kaji_ids: list[int]
    user_id: int
    done_date: datetime


class TblKajiUpdate(BaseModel):
    kaji_id: int = None
    user_id: int = None
    done_date: datetime = None


class TblKaji(TblKajiBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True