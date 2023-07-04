import time

def focus_timer(minutes):
    seconds = minutes * 60
    start_time = time.time()
    end_time = start_time + seconds

    while time.time() < end_time:
        remaining_time = end_time - time.time()
        minutes = int(remaining_time // 60)
        seconds = int(remaining_time % 60)
        print(f"Remaining Time: {minutes:02d}:{seconds:02d}", end="\r")
        time.sleep(1)

    print("Focus Time is over!")

focus_timer(25)  # 设置专注时间为25分钟
