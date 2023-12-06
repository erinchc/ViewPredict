from models import Session, Video
import csv
import time

# 打開csv文件
with open("videos.csv", "r", encoding="utf8") as csvfile:
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
                "video_title": row[1],
                "views": row[2],
                "comments": row[3],
                "duration_in_sec": row[4],
                "likes": row[5],
                "publish_date": row[6],
                "category": row[7],
                "sensationalism_score": row[8],
            }
        )

    # 開始插入數據前記錄時間
    start_time = time.time()

    try:
        session.bulk_insert_mappings(Video, data_list)
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
