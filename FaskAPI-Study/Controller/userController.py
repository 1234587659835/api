from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models.user import User as UserModel
from schemas.article import Article as ArticleSchema
from schemas.user import User, UserCreate
import service.userService as userService
from typing import List, Dict, Any

# 建立 APIRouter 實例
router = APIRouter() # 定義一個新的 APIRouter，用來組織使用者相關的 API 路由

# 資料庫會話管理函式
# 定義 get_db 函式來管理每個 API 請求期間的資料庫會話
def get_db():
    db = SessionLocal()  # 建立新的資料庫會話
    try:
        yield db         # 使用 yield 將資料庫會話傳遞給依賴項函式
    finally:
        db.close()       # 當請求結束時，自動關閉資料庫會話

# 使用者建立 API 端點
# 定義 POST 請求方法，用於創建新使用者
@router.post("/", response_model=User)                                  # response_model 指定回傳的 Pydantic 模式
def create_user(user: UserCreate, db: Session = Depends(get_db)):       # 依賴 get_db 獲取資料庫會話
    db_user = userService.get_user_by_account(db, account=user.account) # 呼叫 userService 查詢是否已存在該帳號
    if db_user:                                                         # 如果帳號已經存在，拋出 400 錯誤
        raise HTTPException(status_code=400, detail="Account already registered")
    return userService.create_user(db=db, user=UserModel(**user.dict())) # 創建並回傳新使用者資料

# 查詢所有使用者 API 端點
# 定義 GET 請求方法，用於查詢所有使用者，支援分頁參數（skip 和 limit）
@router.get("/", response_model=List[User])# response_model 指定回傳的資料類型為 List[User]
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)): # 定義 skip 和 limit 參數，設置預設值
    users = userService.get_users(db, skip=skip, limit=limit)                  # 呼叫 userService 獲取使用者列表
    return users                                                               # 回傳查詢到的使用者列表

# 查詢單個使用者 API 端點
# 定義 GET 請求方法，用於查詢指定 ID 的使用者
@router.get("/{user_id}", response_model=User)              # @router.get("/{user_id}") 指定路徑參數為 user_id
def read_user(user_id: int, db: Session = Depends(get_db)): # 接收路徑參數 user_id 和資料庫會話 db
    db_user = userService.get_user(db, user_id=user_id)     # 呼叫 userService 查詢特定 ID 的使用者
    if db_user is None:                                     # 如果查無該使用者，則拋出 404 錯誤
        raise HTTPException(status_code=404, detail="User not found")
    return db_user                                          # 回傳查詢到的使用者資料

# 更新使用者 API 端點
# 定義 PUT 請求方法，用於更新特定 ID 的使用者資料
@router.put("/{user_id}", response_model=User)
def update_user(user_id: int, name: str, account: str, password: str, db: Session = Depends(get_db)): #接收多個更新參數
    return userService.update_user(db=db, user_id=user_id, name=name, account=account, password=password)# 呼叫 userService 更新使用者資料


# 刪除使用者 API 端點
# 定義 DELETE 請求方法，用於刪除特定 ID 的使用者
@router.delete("/{user_id}", response_model=User)                # @router.put("/{user_id}") 指定路徑參數為 user_id
def delete_user(user_id: int, db: Session = Depends(get_db)):    #  接收路徑參數 user_id 和資料庫會話 db
    return userService.delete_user(db=db, user_id=user_id)       #  呼叫 userService 刪除指定 ID 的使用者

# 查詢特定使用者的文章 API 端點
# 定義 GET 請求方法，用於查詢特定使用者的所有文章
@router.get("/{user_id}/articles", response_model=Dict[str, Any])   # 回傳結構為 Dict，包含使用者名稱與文章列表
def read_user_articles(user_id: int, db: Session = Depends(get_db)):# 接收路徑參數 user_id 和資料庫會話 db
    db_user = userService.get_user(db, user_id=user_id)             # 呼叫 userService 查詢特定 ID 的使用者
    if db_user is None:                                             # 如果查無該使用者，則拋出 404 錯誤
        raise HTTPException(status_code=404, detail="User not found")
    articles = [ArticleSchema.from_orm(article) for article in db_user.articles]    # 透過 ORM 轉換文章資料格式
    return {"user_name": db_user.name, "articles": articles}                        # 回傳使用者名稱和其所有文章