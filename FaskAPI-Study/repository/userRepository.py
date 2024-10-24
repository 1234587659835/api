from sqlalchemy.orm import Session  # 引入 SQLAlchemy 的 Session 類，用於與資料庫互動
from models.user import User  # 引入使用者資料模型（User），與資料庫中的使用者表進行映射操作

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()  # 使用 ID 作為過濾條件，返回第一個符合條件的使用者

# 根據帳號查詢特定使用者資料
def get_user_by_account(db: Session, account: str):
    return db.query(User).filter(User.account == account).first()  # 使用帳號進行過濾，查詢符合的使用者


# 查詢所有使用者資料，支援分頁
def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(User).offset(skip).limit(limit).all()   # 支援分頁查詢，從第 skip 個開始，取出 limit 個使用者

# 創建新使用者資料
def create_user(db: Session, user: User):
    db.add(user)        # 將新使用者加入資料庫會話
    db.commit()         # 提交會話變更到資料庫
    db.refresh(user)    # 刷新使用者物件，以確保取得最新資料（例如自動生成的 ID）
    return user         # 回傳創建的使用者物件

# 更新特定使用者資料
def update_user(db: Session, user_id: int, name: str, account: str, password: str):
    user = db.query(User).filter(User.id == user_id).first()  # 查詢要更新的使用者
    if user:                        # 如果該使用者存在
        user.name = name            # 更新使用者名稱
        user.account = account      # 更新使用者帳號
        user.password = password    # 更新使用者密碼
        db.commit()                 # 提交變更
        db.refresh(user)            # 刷新資料
    return user                     # 回傳更新後的使用者物件

# 刪除特定使用者資料
def delete_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()  # 查詢要刪除的使用者
    if user:                # 如果該使用者存在
        db.delete(user)     # 刪除使用者
        db.commit()         # 提交變更
    return user             # 回傳已刪除的使用者物件（或 None，如果該使用者不存在）