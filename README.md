這個專案目的為預測影片觀看數，首先以Selenium爬取YouTube網頁資料，使用Pandas進行資料格式轉換。在資料分析方面，嘗試了決策樹、隨機森林和gradient boosting regressor三種模型，並藉由RandomizedSearchCV優化超參數。同時將YouTuber以K-means clustering分群，再分別對每組個別預測。
