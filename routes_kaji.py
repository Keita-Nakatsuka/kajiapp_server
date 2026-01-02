from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import models
import schemas

#エンドポイントの接頭辞とタグを設定
#例：GET　domain/kaji/
router = APIRouter(prefix="/kaji", tags=["kaji"])

#GET処理
@router.get("/", response_model=list[schemas.TblKaji])
def get_all_kaji(user_id: int = None, kaji_id: int = None, db: Session = Depends(get_db)):
    """家事記録一覧を取得"""
    query = db.query(models.TblKaji)
    if user_id:
        query = query.filter(models.TblKaji.user_id == user_id)
    if kaji_id:
        query = query.filter(models.TblKaji.kaji_id == kaji_id)
    return query.all()


@router.get("/{kaji_id}", response_model=schemas.TblKaji)
def get_kaji(kaji_id: int, db: Session = Depends(get_db)):
    """id指定した家事記録を取得"""
    kaji = db.query(models.TblKaji).filter(models.TblKaji.id == kaji_id).first()
    if not kaji:
        raise HTTPException(status_code=404, detail="Kaji record not found")
    return kaji

#POST処理
@router.post("/", response_model=schemas.TblKaji)
def create_kaji(kaji: schemas.TblKajiCreate, db: Session = Depends(get_db)):
    """新規家事記録を作成"""
    # user_id と kaji_id が存在するかチェック
    user = db.query(models.MstUser).filter(models.MstUser.id == kaji.user_id).first()
    if not user:
        raise HTTPException(status_code=400, detail="User not found")
    
    kaji_master = db.query(models.MstKaji).filter(models.MstKaji.id == kaji.kaji_id).first()
    if not kaji_master:
        raise HTTPException(status_code=400, detail="Kaji master not found")
    
    db_kaji = models.TblKaji(**kaji.model_dump())
    db.add(db_kaji)
    db.commit()
    db.refresh(db_kaji)
    return db_kaji

#PUT処理
@router.put("/{kaji_id}", response_model=schemas.TblKaji)
def update_kaji(kaji_id: int, kaji: schemas.TblKajiUpdate, db: Session = Depends(get_db)):
    """id指定で家事記録を更新"""
    db_kaji = db.query(models.TblKaji).filter(models.TblKaji.id == kaji_id).first()
    if not db_kaji:
        raise HTTPException(status_code=404, detail="Kaji record not found")
    
    # 更新するデータだけを処理
    update_data = kaji.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_kaji, key, value)
    
    db.commit()
    db.refresh(db_kaji)
    return db_kaji

#DELETE処理
@router.delete("/{kaji_id}")
def delete_kaji(kaji_id: int, db: Session = Depends(get_db)):
    """id指定で家事記録を削除"""
    db_kaji = db.query(models.TblKaji).filter(models.TblKaji.id == kaji_id).first()
    if not db_kaji:
        raise HTTPException(status_code=404, detail="Kaji record not found")
    
    db.delete(db_kaji)
    db.commit()
    return {"message": "Kaji record deleted successfully"}
