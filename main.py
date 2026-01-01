from fastapi import FastAPI
from database import engine, Base
import models
import routes_users

# テーブルを作成
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="User Management API",
    description="FastAPIとSQLAlchemyを使ったサンプルAPI",
    version="1.0.0"
)

# ルーターを登録
app.include_router(routes_users.router)


@app.get("/", tags=["root"])
def read_root():
    """ルートエンドポイント"""
    return {
        "message": "Welcome to Task Management API",
        "docs": "/docs",
        "redoc": "/redoc"
    }


@app.get("/health", tags=["health"])
def health_check():
    """ヘルスチェック"""
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
