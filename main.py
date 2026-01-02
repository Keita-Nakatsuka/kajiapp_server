from fastapi import FastAPI
from database import engine, Base
import models
import routes_kaji

#このmainが常時起動してWebサーバー的な役割を果たす
app = FastAPI(
    title="Kaji Management API",
    description="FastAPI と SQLAlchemy を使った家事管理API",
    version="1.0.0"
)

# ルーターを登録
app.include_router(routes_kaji.router)


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
