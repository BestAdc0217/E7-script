import time
import cv2
import numpy as np
import pyautogui


def img_click(files):
    print("开始匹配")
    while True:
        # 从屏幕中获取截图并转换为numpy数组
        screenshot = pyautogui.screenshot()
        screenshot_np = np.array(screenshot)

        # 因为PyAutoGUI的截图是RGB格式，而OpenCV是BGR格式，所以需要转换
        screenshot_bgr = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2BGR)
        screenshot_gray = cv2.cvtColor(screenshot_bgr, cv2.COLOR_BGR2GRAY)

        matched = False  # 用于标记是否在此次循环中找到了匹配项

        for file_name in files:
            print("开始匹配")
            # 读取模板图像
            template = cv2.imread(file_name, cv2.IMREAD_GRAYSCALE)

            # 使用模板匹配方法找到最佳匹配位置
            result = cv2.matchTemplate(screenshot_gray, template, cv2.TM_CCOEFF_NORMED)

            # 获取模板的宽度和高度
            w = template.shape[1]
            h = template.shape[0]

            loc = np.where(result > 0.98)  # 获取所有匹配项的位置

            for pt in zip(*loc[::-1]):  # 遍历所有的匹配项
                print(f"匹配成功，路径是{file_name}，位置是{pt}")
                # cv2.rectangle(screenshot_bgr, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 2)

                # 使用pyautogui进行点击
                pyautogui.click((pt[0] + w)/2,(pt[1] + h)/2)  # 点击匹配区域的中心
                time.sleep(1)
                matched = True  # 在此次循环中找到了匹配项

        # 如果在此次循环中没有找到匹配项，跳出循环
        if not matched:
            break

if __name__ == '__main__':
    time.sleep(2)
    file_list = ['001.jpg', '002.jpg']
    img_click(file_list)

