import time
import cv2
import numpy as np
import pyautogui


def img_match(name):
    file_name = name
    # 从屏幕中获取截图并转换为numpy数组
    screenshot = pyautogui.screenshot()
    screenshot_np = np.array(screenshot)
    # 因为PyAutoGUI的截图是RGB格式，而OpenCV是BGR格式，所以需要转换
    screenshot_bgr = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2BGR)
    screenshot_gray = cv2.cvtColor(screenshot_bgr, cv2.COLOR_BGR2GRAY)  # 修复此处

    # 读取模板图像
    template = cv2.imread(file_name, cv2.IMREAD_GRAYSCALE)

    # 使用模板匹配方法找到最佳匹配位置
    result = cv2.matchTemplate(screenshot_gray, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    accuracy_x = 40
    accuracy_y = 10
    # 获取模板的宽度和高度
    w = template.shape[1]
    h = template.shape[0]

    # print(f"模版的长是{w}，宽是{h}")
    center_x = ((max_loc[0] + w) / 2) - accuracy_x
    center_y = ((max_loc[1] + h) / 2) - accuracy_y
    # print(f"中心x为{center_x},y为{center_y}")
    if max_val > 0.6:
        print(f"匹配成功，路径是{file_name}")
        pyautogui.click(center_x, center_y)
        return True
    return False

    # # 画一个矩形框来标记找到的位置
    # cv2.rectangle(screenshot_bgr, max_loc, (max_loc[0] + w, max_loc[1] + h), (0, 255, 0), 2)
    #
    # # 显示结果
    # cv2.imshow('Detected', screenshot_bgr)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


def img_bookmark(files):
    import purchase
    print("开始匹配")
    for file_name in files:
        # 从屏幕中获取截图并转换为numpy数组
        screenshot = pyautogui.screenshot()
        screenshot_np = np.array(screenshot)

        # 因为PyAutoGUI的截图是RGB格式，而OpenCV是BGR格式，所以需要转换
        screenshot_bgr = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2BGR)
        screenshot_gray = cv2.cvtColor(screenshot_bgr, cv2.COLOR_BGR2GRAY)

        matched = False  # 用于标记是否在此次循环中找到了匹配项
        # TODO 遍历查看传入的文件名字符串数组 对对应的图片检测

        # 读取模板图像
        template = cv2.imread(file_name, cv2.IMREAD_GRAYSCALE)

        # 使用模板匹配方法找到最佳匹配位置
        result = cv2.matchTemplate(screenshot_gray, template, cv2.TM_CCOEFF_NORMED)

        # # 获取模板的宽度和高度
        # w = template.shape[1]
        # h = template.shape[0]
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        if max_val > 0.7:
            loc = np.where(result > 0.7)  # 获取所有大于0.7的匹配项

            if loc[0].size > 0:  # 检查是否找到了匹配项
                print(f'找到书签啦')
                # TODO 如果是蓝书签，执行第一个购买操作函数 否则执行第二个
                if file_name == 'img/bookmark.jpg':
                    purchase.getgoods1()
                else:
                    purchase.getgoods2()

