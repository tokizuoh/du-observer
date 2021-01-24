import os
import sys
import time
import signal
import datetime

input_file_path = ""


def main():
    args = sys.argv

    if len(args) < 2:
        print("対象ファイルのパスを入力してください")
        return
    
    global input_file_path
    input_file_path = args[1]
    if not os.path.exists(input_file_path):
        print("パスの入力形式が正しくありません")
        return
    
    interval = int(input("- ファイル容量を監視する間隔(s): "))
    output_file_path = input("- 書き出し先: ")


    if not check_correct_format(path=output_file_path):
        print("書き出し先のファイル形式が正しくありません")

    
    signal.signal(signal.SIGALRM, scheculer)
    signal.setitimer(signal.ITIMER_REAL, interval, interval)
    time.sleep(interval * 1000)


def scheculer(arg1, arg2):
    now = datetime.datetime.fromtimestamp(time.time())
    now_formatted = now.strftime("%Y/%m/%d %H:%M:%S")
    file_size = os.path.getsize(input_file_path)
    print("{}  {}B".format(now_formatted,file_size))


def check_correct_format(path: str) -> bool :
    directory_path = '/'.join(path.split("/")[:-1])

    if not os.path.exists(directory_path):
        return False
    
    file_extension = path.split("/")[-1:][0].split(".")[1:][0]
    if not file_extension == "txt":
        return False

    return True

if __name__ == "__main__":
    main()