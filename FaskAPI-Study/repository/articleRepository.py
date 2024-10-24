from sqlalchemy.orm import Session  # 引入 SQLAlchemy 的 Session 類，用於與資料庫互動
from models.article import Article  # 引入文章資料模型（Article），與資料庫中的文章表進行映射操作

# 根據文章 ID 查詢特定文章
def get_article(db: Session, article_id: int):
    return db.query(Article).filter(Article.id == article_id).first()# 使用 ID 作為過濾條件，返回第一個符合條件的文章

# 查詢所有文章資料，支援分頁
def get_articles(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Article).offset(skip).limit(limit).all()        # 支援分頁查詢，從第 skip 個開始，取出 limit 個文章

# 創建新文章資料
def create_article(db: Session, article: Article):
    db.add(article)         # 將新文章加入資料庫會話
    db.commit()             # 提交會話變更到資料庫
    db.refresh(article)     # 刷新文章物件，以確保取得最新資料（例如自動生成的 ID）
    return article          # 回傳創建的文章物件

# 更新特定文章資料
def update_article(db: Session, article_id: int, name: str, price: int):
    article = db.query(Article).filter(Article.id == article_id).first()  # 查詢要更新的文章
    if article:                 # 如果該文章存在
        article.name = name     # 更新文章名稱
        article.price = price   # 更新文章價格
        db.commit()             # 提交變更
        db.refresh(article)     # 刷新資料
    return article              # 回傳更新後的文章物件

# 刪除特定文章資料
def delete_article(db: Session, article_id: int):
    article = db.query(Article).filter(Article.id == article_id).first()  # 查詢要刪除的文章
    if article:             # 如果該文章存在
        db.delete(article)  # 刪除文章
        db.commit()         # 提交變更
    return article          # 回傳已刪除的文章物件（或 None，如果該文章不存在）