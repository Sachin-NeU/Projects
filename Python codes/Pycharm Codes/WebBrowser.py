import webbrowser
import time


for i in range(1,2):
    time.sleep(5)
    print("The first instance of loop ran on :"+time.ctime())
    webbrowser.open_new_tab("https://www.youtube.com/watch?v=Pkh8UtuejGw")
