from models import Session, Youtuber
import csv
import time

# 打開csv文件
with open("youtubers.csv", "r", encoding="utf8") as csvfile:
    # 創建CSV Reader對象
    csv_reader = csv.reader(csvfile)
    # 跳過標題行
    next(csv_reader, None)
    session = Session()

    data_list = []
    for row in csv_reader:
        data_list.append(
            {
                "channel_name": row[0],
                "channel_link": row[1],
                "channel_startdate": row[2],
                "totalviews_in_10K": row[3],
                "subscribers_in_10K": row[4],
                "location": row[5],
                "other_links": row[6],
                "videos_links": row[7],
            }
        )

    # 開始插入數據前記錄時間
    start_time = time.time()

    try:
        session.bulk_insert_mappings(Youtuber, data_list)
        session.commit()

        # 數據插入完成後記錄時間
        end_time = time.time()

    except Exception as e:
        print(f"An error occurred: {e}")
        session.rollback()
    finally:
        session.close()

    # 計算插入數據所花費的總時間
    total_time = end_time - start_time
    print(f"Total Insertion Time: {total_time} seconds")
