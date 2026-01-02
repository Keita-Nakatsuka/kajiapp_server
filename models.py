from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func
from database import Base

class MstUser(Base):
    __tablename__ = "mst_users"
    id = Column(Integer, primary_key=True, index=True)
    user = Column(String(100), nullable=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

class MstKaji(Base):
    __tablename__ = "mst_kaji"
    id = Column(Integer, primary_key=True, index=True)
    kaji = Column(String(100), nullable=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

class TblKaji(Base):
    __tablename__ = "tbl_kaji"
    id = Column(Integer, primary_key=True, index=True)
    kaji_id = Column(Integer, ForeignKey("mst_kaji.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("mst_users.id"), nullable=False)
    done_date = Column(DateTime, nullable=False, onupdate=func.convert_tz(func.now(), '+00:00', '+09:00'))
     # UTC時刻を JST に変換して保存
    created_at = Column(DateTime, default=func.convert_tz(func.now(), '+00:00', '+09:00'))
    updated_at = Column(DateTime, default=func.convert_tz(func.now(), '+00:00', '+09:00'), onupdate=func.convert_tz(func.now(), '+00:00', '+09:00'))