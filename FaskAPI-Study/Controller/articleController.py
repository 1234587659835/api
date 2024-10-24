from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models.article import Article as ArticleModel
from schemas.article import Article, ArticleCreate
import service.articleService as articleService
from typing import List

router = APIRouter() # 建立 APIRouter 實例來定義路由

# Dependency - 建立資料庫會話
# 定義一個 `get_db` 函數來管理資料庫會話，每次 API 請求時建立並在操作完成後關閉
def get_db():
    db = SessionLocal() # 建立資料庫會話
    try:
        yield db        # 傳遞資料庫會話
    finally:
        db.close()      # 請求結束時關閉資料庫會話

# 創建文章
# 使用 POST 方法來接收一個新的文章創建請求
@router.post("/", response_model=Article)                               # 定義接收 ArticleCreate 資料結構的 API
def create_article(article: ArticleCreate, db: Session = Depends(get_db)):
    # 呼叫文章服務層來創建新文章，並將 Pydantic 模式轉換成 SQLAlchemy 模型結構進行資料庫操作
    return articleService.create_article(db=db, article=ArticleModel(**article.dict()))

# 查詢所有文章
# 使用 GET 方法來查詢文章列表，支援分頁查詢
@router.get("/", response_model=List[Article])                          # 定義回傳值為 List[Article]，即一個包含多篇文章的列表
def read_articles(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):# 預設從第 0 頁開始，每頁 10 筆
    articles = articleService.get_articles(db, skip=skip, limit=limit)  # 呼叫服務層查詢文章
    return articles                                                     # 回傳查詢結果

# 查詢特定文章
# 使用 GET 方法查詢特定文章 ID 的詳細內容
@router.get("/{article_id}", response_model=Article)                    # 定義回傳值為單篇 Article 資料結構
def read_article(article_id: int, db: Session = Depends(get_db)):       # 接收路徑參數 `article_id` 作為查詢條件
    db_article = articleService.get_article(db, article_id=article_id)  # 透過服務層查詢該 ID 的文章
    if db_article is None:                                              # 如果查無此文章，拋出 404 錯誤
        raise HTTPException(status_code=404, detail="Article not found")
    return db_article                                                   # 回傳查詢到的文章資料

# 更新文章
# 使用 PUT 方法來更新指定文章 ID 的內容
@router.put("/{article_id}", response_model=Article)
def update_article(article_id: int, name: str, price: int, db: Session = Depends(get_db)):
    # 呼叫服務層更新文章，並傳入新的 `name` 和 `price` 資料
    return articleService.update_article(db=db, article_id=article_id, name=name, price=price)

# 刪除文章
# 使用 DELETE 方法來刪除指定 ID 的文章
@router.delete("/{article_id}", response_model=Article)                 # 定義回傳值為被刪除的 Article 資料
def delete_article(article_id: int, db: Session = Depends(get_db)):     # 接收要刪除的 `article_id`
     # 呼叫服務層刪除文章，並回傳被刪除的文章資料
    return articleService.delete_article(db=db, article_id=article_id)