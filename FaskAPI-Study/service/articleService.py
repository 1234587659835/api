from sqlalchemy.orm import Session  # 引入 SQLAlchemy 的 Session 類，用於資料庫連線管理
from repository import articleRepository  # 從 repository 引入 articleRepository，用於操作文章資料
from models.article import Article  # 引入文章模型，用於資料轉換

# 創建新文章
def create_article(db: Session, article: Article):
    return articleRepository.create_article(db, article)  # 呼叫 articleRepository 進行資料庫操作

# 取得特定 ID 的文章
def get_article(db: Session, article_id: int):
    return articleRepository.get_article(db, article_id) # 呼叫 articleRepository 取得指定 ID 的文章資料

# 取得所有文章列表
def get_articles(db: Session, skip: int = 0, limit: int = 10):
    return articleRepository.get_articles(db, skip, limit)  # 呼叫 articleRepository 查詢所有文章列表

# 更新指定 ID 的文章
def update_article(db: Session, article_id: int, name: str, price: int):
    return articleRepository.update_article(db, article_id, name, price) # 呼叫 articleRepository 更新文章資料

# 刪除指定 ID 的文章
def delete_article(db: Session, article_id: int):
    return articleRepository.delete_article(db, article_id)# 呼叫 articleRepository 刪除指定文章