import os
import sys
import time
import pyautogui
import os
import img_match
import purchase
import pygetwindow as gw


def shift_mouse():
    # TODO 向下划动
    x, y = pyautogui.position()
    # 按下鼠标左键
    pyautogui.mouseDown(x, y, button='left')
    # 相对当前位置，向下移动100个单位
    pyautogui.moveRel(0, -100)
    # 释放鼠标左键
    pyautogui.mouseUp(button='left')
    time.sleep(0.5) # 防止匹配速度太快漏掉书签
    return

if __name__ == '__main__':
    print(f'程序开始')
    time.sleep(2)
    source = 'img'
    flu_btu = source + '/flu.jpg'
    comfirm_btu = source + '/comfirm.jpg'
    bookmark_btu = source + '/bookmark.jpg'
    mysterious_bookmark_btu = source + '/mysterious_bookmark.jpg'

    while True:
        time.sleep(1) # 防止网络卡顿造成慢响应引起的bug

        file_names = [bookmark_btu, mysterious_bookmark_btu] # 给定要匹配的书签路径
        # TODO 前后匹配两次，防止漏掉
        img_match.img_bookmark(file_names)
        shift_mouse()
        img_match.img_bookmark(file_names)

        has = img_match.img_match(flu_btu)  # 执行刷新操作，网络卡顿需要等0.5s
        time.sleep(0.5)
        img_match.img_match(comfirm_btu)
