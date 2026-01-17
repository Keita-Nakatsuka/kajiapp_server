## 概要
FastAPIとSQLAlchemyを使ったデータベース接続のプログラムです
これはFlutterの家事アプリで使われるサーバープログラムです。
主に記録とマスターデータをDBから読み書きする処理です。

## API仕様
python main.pyを起動後swaggerUIを参照
http://localhost:8000/docs#/

## ファイル構成
- `main.py` - FastAPIアプリケーションのメインファイル
- `database.py` - データベース接続設定
- `models.py` - SQLAlchemyのモデル定義
- `schemas.py` - Pydanticスキーマ定義
- `routes_users.py` - ユーザーエンドポイント
- `routes_tasks.py` - タスクエンドポイント
- `.env` - 環境変数設定
- `requirements.txt` - 依存パッケージ

## セットアップ

### 1. パッケージのインストール
```bash
pip install -r requirements.txt
```

### 2. 環境変数の設定
`.env`ファイルにDATABASE_URLを設定します。

**SQLiteを使う場合（デフォルト）:**
```
DATABASE_URL=sqlite:///./test.db
```

**PostgreSQLを使う場合:**
```
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
```

**MySQLを使う場合:**
```
DATABASE_URL=mysql+pymysql://user:password@localhost:3306/dbname
```

### 3. アプリケーションの起動
```bash
python main.py
```

または

```bash
uvicorn main:app --reload
```

サーバーは `http://localhost:8000` で起動します。

## API ドキュメント

起動後、以下のURLでSwagger UIドキュメントを確認できます:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## エンドポイント一覧

### ユーザー関連
- `GET /users/` - 全ユーザー取得
- `GET /users/{user_id}` - 特定ユーザー取得
- `POST /users/` - ユーザー作成
- `PUT /users/{user_id}` - ユーザー更新
- `DELETE /users/{user_id}` - ユーザー削除

### タスク関連
- `GET /tasks/` - タスク一覧取得（user_idでフィルター可能）
- `GET /tasks/{task_id}` - 特定タスク取得
- `POST /tasks/` - タスク作成
- `PUT /tasks/{task_id}` - タスク更新
- `PATCH /tasks/{task_id}/complete` - タスク完了
- `DELETE /tasks/{task_id}` - タスク削除

## 使用例

### ユーザー作成
```bash
curl -X POST http://localhost:8000/users/ \
  -H "Content-Type: application/json" \
  -d '{"name": "John Doe", "email": "john@example.com"}'
```

### タスク作成
```bash
curl -X POST http://localhost:8000/tasks/ \
  -H "Content-Type: application/json" \
  -d '{"title": "My Task", "description": "Task description", "user_id": 1}'
```

## データベース変更について

モデルを編集した場合、データベーススキーマを更新するには、
新しいマイグレーションが必要です。

簡単な開発時は、`test.db`を削除して再度実行するだけで再作成されます：
```bash
rm test.db
python main.py
```

本番環境ではAlembicを使用したマイグレーション管理を推奨します。

## 拡張方法

### 新しいモデルを追加する場合
1. `models.py`に新しいクラスを追加
2. `schemas.py`に対応するPydanticスキーマを追加
3. `routes_*.py`に新しいルーターファイルを作成
4. `main.py`にルーターを登録

### 新しい機能を追加する場合
- 認証: `python-jose`、`passlib`を使用
- バリデーション: Pydanticの機能を活用
- ページネーション: skipとlimitパラメータを追加

### マスターデータ更新
seed.pyを実行する。
ただし、空のテーブルに対しての追加しか現状できないので一度テーブルをデリートしてから実行する
実行はEC2のターミナルから実行
コマンドはpython3 seed.py
