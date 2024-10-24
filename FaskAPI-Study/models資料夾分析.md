## User 與 Article 之間的一對多關聯
在這個模型中，User 與 Article 之間定義了一對多的關聯關係，這表示：

* 一個 User 可以擁有多個 Article。
* Article 中通過 userId 這個外鍵欄位來關聯到對應的 User，從而表示 Article 屬於哪一個用戶。

## relationship() 和 ForeignKey() 的用途

* ForeignKey("user.id")：用來定義 Article 模型中的 userId 欄位為外鍵，這個外鍵引用了 User 表的 id 欄位。這樣可以確保每個 Article 實例都能找到它對應的 User。
* relationship()：用來設置 ORM 模型之間的關聯。通過 relationship() 可以定義雙向或單向關聯。這個欄位在資料庫中不會有對應的欄位，它僅用於 ORM 層的對象間操作：
** User.articles: 返回這個用戶所擁有的所有 Article。
** Article.user: 返回這篇文章的擁有者（用戶）。

## 關聯範例
假設我們有以下用戶和文章資料：

用戶表 User：
| id  | name  | account  | password | 
| :-: | :---: | :------: | :------: |
| 1  | Alice  | alice_01 | pass123  | 
| 2	 | Bob	  | bob_01	 | pass456  | 

文章表Article：
| id  | name      | price| userId |
| :-: | :-------: | :--: | :----: |
| 1   | Article 1 | 100  | 1      |
| 2   | Article 2 | 150  | 1      |
| 3   | Article 3 | 200  | 2      |


從這些資料可以看出：

* 用戶 Alice（userId = 1）擁有 Article 1 和 Article 2。
* 用戶 Bob（userId = 2）擁有 Article 3。

通過關聯欄位，我們可以執行以下操作來查詢資料：

* User 查詢：alice.articles -> 這個屬性可以查詢 Alice 的所有文章（Article 1 和 Article 2）。
* Article 查詢：article1.user -> 這個屬性可以查詢 Article 1 的作者（Alice）。
## ORM 使用注意事項
* 使用 ForeignKey 時需要確保關聯的表（User）已經存在，否則在建表時會報錯。
* 在操作資料時需要考慮事務的提交（session.commit()）以及關聯的刪除（例如刪除 User 時如何處理其 Article）。
## 最佳實踐
1. 設置雙向關聯：通常建議雙向設置 relationship，以便可以從雙方進行查詢。
2. 保持欄位名稱一致性：在設置外鍵時，欄位名稱應與被引用的欄位一致（如 userId 指向 user.id）。
3. 規劃資料庫表結構：在設計多表關聯時，考慮業務需求，選擇一對一、一對多或多對多關聯。

以上是 User 和 Article 模型的詳細解釋及其關聯方式。