from pydantic import BaseModel # 引入 Pydantic 的 BaseModel 類，作為所有模式類別的基底

# 定義使用者的基本模式（Base Schema），用於描述共通欄位結構
class UserBase(BaseModel):
    name: str       # 使用者名稱
    account: str    # 使用者帳號

# 定義用於創建使用者時的模式，繼承自 UserBase 並添加密碼欄位
class UserCreate(UserBase):
    password: str   # 使用者密碼
    
# 定義用於回應查詢或操作結果的使用者模式，繼承自 UserBase 並添加 ID 欄位
class User(UserBase):
    id: int         # 使用者 ID
     # 配置 ORM 模式，允許從 SQLAlchemy 模型轉換為 Pydantic 模式
    class Config:
        orm_mode: True  # 設定 `orm_mode` 為 True，允許直接使用 ORM 模型物件作為輸入