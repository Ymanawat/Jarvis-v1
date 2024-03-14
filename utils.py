import time

last_log_time = None

def log(message):
    global last_log_time
    current_time = time.time()
    if last_log_time is not None:
        time_diff = current_time - last_log_time
    else:
        time_diff = 0
    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(current_time))} | +{time_diff:.2f}s] {message}")
    last_log_time = current_time
