# DBにマスターデータを入れるシードスクリプト
import sys
from pathlib import Path
# 親ディレクトリをパスに追加
sys.path.insert(0, str(Path(__file__).parent.parent))

from database import SessionLocal
import models

db = SessionLocal()
try:
    # mst_users にシード値を挿入
    if db.query(models.MstUser).count() == 0:
        users = [
            models.MstUser(user="夫"),
            models.MstUser(user="妻"),
            models.MstUser(user="外部"),
        ]
        db.add_all(users)
        db.commit()
        print("✓ mst_users にシード値を挿入しました")
    
    # mst_kaji にシード値を挿入
    if db.query(models.MstKaji).count() == 0:
        kajis = [
            models.MstKaji(kaji="朝ごはん"),
            models.MstKaji(kaji="昼ごはん"),
            models.MstKaji(kaji="晩ごはん"),
            models.MstKaji(kaji="洗濯"),
            models.MstKaji(kaji="洗濯干し"),
            models.MstKaji(kaji="掃除"),
            models.MstKaji(kaji="ゴミ捨て"),
            models.MstKaji(kaji="散歩"),
        ]
        db.add_all(kajis)
        db.commit()
        print("✓ mst_kaji にシード値を挿入しました")
    
    print("シード完了")
    
except Exception as e:
    print(f"エラー: {e}")
    db.rollback()
finally:
    db.close()