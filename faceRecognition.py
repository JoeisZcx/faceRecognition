#!/usr/bin/env python  
# _*_ coding:utf-8 _*_
# 1.导入库
import cv2
# 2.加载人脸模型
face = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
# 3.打开摄像头
capture = cv2.VideoCapture(0)
# 4.创建窗口
cv2.namedWindow("camera")
# 5.获取摄像机实时画面
while True:
    # 5.1 读取摄像头的画面
    ret, frame = capture.read()
    # 5.2 图片灰度调整
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    # 5.3 检查人脸
    faces = face.detectMultiScale(gray, 1.1, 3, 0, (100, 100))
    # 5.4 标记人脸
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        # 5.5 显示图片
        cv2.imshow("camera", frame)
        # 5.6 暂停窗口
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break
# 6 释放资源
capture.release()
# 7 关闭窗口
cv2.destroyWindows()
