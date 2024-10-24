from sqlalchemy.orm import Session  # 引入 SQLAlchemy 的 Session 類，用於處理資料庫連線
from repository import userRepository  # 從 repository 引入 userRepository，用於操作使用者資料
from models.user import User  # 引入使用者模型，用於資料轉換

# 創建新使用者
def create_user(db: Session, user: User):
    return userRepository.create_user(db, user)# 呼叫 userRepository 進行資料庫操作

# 取得特定 ID 的使用者
def get_user(db: Session, user_id: int):
    return userRepository.get_user(db, user_id) # 呼叫 userRepository 取得指定 ID 的使用者資料

# 透過帳號查詢使用者
def get_user_by_account(db: Session, account: str):
    return userRepository.get_user_by_account(db, account) # 呼叫 userRepository 查詢指定帳號的使用者

# 取得多個使用者列表
def get_users(db: Session, skip: int = 0, limit: int = 10):
    return userRepository.get_users(db, skip, limit)  # 呼叫 userRepository 查詢使用者列表

# 更新指定 ID 的使用者
def update_user(db: Session, user_id: int, name: str, account: str, password: str):
    return userRepository.update_user(db, user_id, name, account, password) # 呼叫 userRepository 更新使用者資料

# 刪除指定 ID 的使用者
def delete_user(db: Session, user_id: int):
    return userRepository.delete_user(db, user_id) # 呼叫 userRepository 刪除指定使用者