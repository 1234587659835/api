from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Article(Base):
    __tablename__ = "article"

    id = Column(Integer, primary_key=True, index=True)# 定義主鍵 id 欄位
    name = Column(String(50))# 定義文章的名稱欄位
    price = Column(Integer) # 定義文章價格欄位
    userId = Column(Integer, ForeignKey("user.id")) # 外鍵欄位，與 User 模型的 id 欄位建立關聯

    user = relationship("User", back_populates="articles")# 定義與 User 模型的一對多關聯

# 欄位解釋：
# id: 主鍵（Primary Key），唯一標識每個 Article 實例。
# name: 用來表示文章名稱的字串欄位。
# price: 用來表示文章價格的整數欄位。
# userId: 外鍵欄位，表示此 Article 屬於哪一個 User，用來指向 User 模型的 id 欄位。
# 關聯關係：
# user: 使用 relationship() 定義與 User 的一對多關聯，指向 User 模型。
# back_populates 用來設置雙向關聯，表明 User 模型中有一個 articles 欄位來表示這個關聯。

