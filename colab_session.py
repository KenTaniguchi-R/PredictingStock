import time
import pyautogui as pgui

for _ in range(72):
    pgui.click(x=652, y=703, duration=1) # 指定した座標に1秒かけて移動してクリック
    time.sleep(1) # 1秒待機
    pgui.click(x=664, y=638, duration=1)
    time.sleep(600) # 10分待機