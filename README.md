# 專案說明
## 目的：預測影片觀看數並探討影響觀看數之因素
### 1.資料蒐集
* 使用Selenium模擬人類操作，對Youtube(JavaScript渲染的網頁)進行爬取，總計9861筆資料。
* 實施斷點續傳功能，將已爬取資料存儲於CSV檔案中，以便於中斷後能繼續爬取。
### 2.資料清洗
* 使用Pandas進行單位轉換，將字串轉為數字或日期格式，便於後續分析。
### 3.建立資料庫
* 利用Docker建立MySQL server，以container形式運行。
* 在server上建立資料庫，使用SQLAlchemy建立表格結構（schema），並insert data。
* 為提升效率，採用批量插入(bulk insert)方法，提高了約97%的效率，優化了CRUD操作。
### 4.資料分析
* 應用one-hot encoding使特徵獨立。
* 最初使用決策樹模型進行預測，但有overfitting的問題。
* 嘗試Random Forest和Gradient Boosting Regressor，後者有最佳預測效果。
* 透過RandomizedSearchCV優化模型超參數，使模型的決定係數達到0.86。
* 使用K-means clustering並根據elbow method將YouTuber分成三群，對每群分別使用Gradient Boosting Regressor模型進行預測。
