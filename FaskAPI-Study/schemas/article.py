from pydantic import BaseModel # 引入 Pydantic 的 BaseModel 類

# 定義文章的基本模式（Base Schema），用於描述共通欄位結構
class ArticleBase(BaseModel):
    name: str       # 文章名稱
    price: int      # 文章價格

# 定義用於創建文章時的模式，繼承自 ArticleBase 並添加使用者 ID 欄位
class ArticleCreate(ArticleBase):
    userId: int  # 關聯的使用者 ID

# 定義用於回應查詢或操作結果的文章模式，繼承自 ArticleBase 並添加 ID 和使用者 ID 欄位
class Article(ArticleBase):
    id: int      # 文章 ID
    userId: int  # 關聯的使用者 ID
     # 配置 ORM 模式，允許從 SQLAlchemy 模型轉換為 Pydantic 模式
    class Config:
        orm_mode = True         # 設定 `orm_mode` 為 True，允許直接使用 ORM 模型物件作為輸入
        from_attributes = True  # 開啟從物件屬性轉換的功能（在 Pydantic v2 中適用）