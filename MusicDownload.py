import yt_dlp
import os

def download_youtube_audio(url, output_path='.'):
    """
    從指定的 YouTube URL 下載音訊並存為 MP3。

    :param url: YouTube 影片的網址。
    :param output_path: 下載檔案的儲存路徑，預設為當前目錄。
    """
    # 檢查輸出路徑是否存在，如果不存在就建立它
    if not os.path.exists(output_path):
        os.makedirs(output_path)
        print(f"已建立資料夾： {output_path}")

    # yt-dlp 的設定選項
    ydl_opts = {
        # 'format': 'bestaudio/best' -> 選擇最佳音質的音訊
        # 'postprocessors': [...] -> 後處理步驟，用於轉換格式
        # 'key': 'FFmpegExtractAudio' -> 使用 FFmpeg 提取音訊
        # 'preferredcodec': 'mp3' -> 偏好的音訊編碼為 mp3
        # 'preferredquality': '192' -> 音訊品質設定為 192kbps
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        # 'outtmpl': f'{output_path}/%(title)s.%(ext)s' -> 設定輸出的檔案名稱格式
        # %(title)s 會被影片標題取代
        # %(ext)s 會被副檔名 (mp3) 取代
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'noplaylist': True, # 如果是播放清單的網址，只下載單一影片
    }

    try:
        # 建立 YoutubeDL 物件並傳入設定
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"正在分析網址： {url}")
            # 執行下載
            ydl.download([url])
            print("\n下載完成！ MP3 檔案已儲存至指定路徑。")

    except yt_dlp.utils.DownloadError as e:
        print(f"\n下載失敗： {e}")
    except Exception as e:
        print(f"\n發生未預期的錯誤： {e}")


if __name__ == '__main__':
    # --- 請在這裡貼上你要下載的 YouTube 網址 ---
    video_url = input("請輸入 YouTube 影片網址： ")

    # --- 設定你想要儲存檔案的資料夾路徑 ---
    # 預設是 'YT_Downloads'，會建立在腳本所在的同一個目錄下
    download_folder = 'YT_Downloads'

    if video_url:
        download_youtube_audio(video_url, download_folder)
    else:
        print("未輸入網址，程式結束。")

