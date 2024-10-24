from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)# 定義主鍵 id 欄位
    name = Column(String(50)) # 定義用戶名稱欄位
    account = Column(String(50), unique=True, index=True) # 定義用戶帳號欄位，並設為唯一
    password = Column(String(50))# 定義用戶密碼欄位

    articles = relationship("Article", back_populates="user") # 定義與 Article 模型的一對多關聯

# 欄位解釋：

# id: 主鍵（Primary Key），唯一標識每個 User 實例。
# name: 用來表示用戶名稱的字串欄位。
# account: 用來表示用戶帳號的字串欄位，並設為唯一，這樣就不會有重複帳號。
# password: 用來表示用戶密碼的字串欄位。
# 關聯關係：

# articles: 使用 relationship() 定義與 Article 模型的一對多關聯。
# 通過 back_populates 來指定 Article 模型中與 User 關聯的 user 欄位，形成雙向引用。