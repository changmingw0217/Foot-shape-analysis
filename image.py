#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np
import matplotlib.pyplot as plt


def rotate(image, angle, center=None, scale=1.0):
    # 获取图像尺寸
    (h, w) = image.shape[:2]

    # 若未指定旋转中心，则将图像中心设为旋转中心
    if center is None:
        center = (w / 2, h / 2)

    # 执行旋转
    M = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpAffine(image, M, (w, h))

    # 返回旋转后的图像
    return rotated


def euclidean_distance(x1, y1, x2, y2):

    num1 = (x1 - y1) ** 2
    num2 = (x2 - y2) ** 2
    dist = np.sqrt(num1 + num2)
    return dist


def find_center_point(contour):

    x_coord_sum = 0
    y_coord_sum = 0

    for i in range(len(contour)):
        x_coord_sum += contour[i][0][0]
        y_coord_sum += contour[i][0][1]

    center_x = int(x_coord_sum / len(contour))
    center_y = int(y_coord_sum / len(contour))

    return [center_x, center_y]


def cut_image(image):

    src = image

    YCrCb = cv2.cvtColor(src, cv2.COLOR_RGB2YCrCb)

    Y, Cr, Cb = cv2.split(YCrCb)

    target = cv2.threshold(Cb, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    element = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))

    target = cv2.morphologyEx(target, cv2.MORPH_OPEN, element)

    contours = cv2.findContours(target, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)[1]

    a_max = 0

    max_contour = []

    for contour in contours:
        area = cv2.contourArea(contour)
        if area > a_max:
            a_max = area
            max_contour = contour

    center = find_center_point(max_contour)

    x_coord = []
    y_coord = []

    for i in range(len(max_contour)):
        x_coord.append(max_contour[i][0][0])
        y_coord.append(max_contour[i][0][1])

    x_coord.sort()
    y_coord.sort()

    x_min = x_coord[0]
    x_max = x_coord[-1]
    y_min = y_coord[0]
    y_max = y_coord[-1]

    height = center[1] - y_min
    width = x_max - x_min

    data = src[y_min:y_min+height, x_min:x_min+width]

    return data


def take_first(elem):
    return elem[0]


def find_two_most(y, contour):
    point = []
    for i in range(len(contour)):
        if y == (contour[i][0][1]):
            point.append((contour[i][0][0], contour[i][0][1]))
    point.sort(key=take_first)
    return point


def get_data(image):
    src = image

    YCrCb = cv2.cvtColor(src, cv2.COLOR_RGB2YCrCb)

    Y, Cr, Cb = cv2.split(YCrCb)

    target = cv2.threshold(Cb, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    element = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))

    target = cv2.morphologyEx(target, cv2.MORPH_OPEN, element)

    contours = cv2.findContours(target, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)[1]

    a_max = 0

    max_contour = []

    for contour in contours:
        area = cv2.contourArea(contour)
        if area > a_max:
            a_max = area
            max_contour = contour

    cv2.drawContours(src, max_contour, -1, (0, 0, 255), 3)

    center = find_center_point(max_contour)

    x_coord = []
    y_coord = []
    xy_coord = []

    for i in range(len(max_contour)):
        x_coord.append(max_contour[i][0][0])
        y_coord.append(max_contour[i][0][1])
        element = (max_contour[i][0][0], max_contour[i][0][1])
        xy_coord.append(element)

    x_coord.sort()
    y_coord.sort()
    # xy_coord.sort(key=take_first)

    x_min = x_coord[0]
    x_max = x_coord[-1]
    y_min = y_coord[0]
    y_max = y_coord[-1]

    # print(xy_coord)
    #
    # print(x_min)
    # print(x_max)
    # print(y_min)
    # print(y_max)

    y = int(center[1] + (y_max - center[1]) / 4)

    cv2.circle(src, (center[0], y), 4, (0, 255, 0), -1)

    dist_list = []

    # for i in range(len(max_contour)):
    #     if y > max_contour[i][0][1]:
    #         dist = euclidean_distance(center[0], y, max_contour[i][0][0], max_contour[i][0][1])
    #         dist_list.append(dist)

    # plt.bar(range(len(dist_list)), dist_list)
    # plt.show()

    # font = cv2.FONT_HERSHEY_SIMPLEX
    #
    # for i in range(len(max_contour)):
    #     if i % 30 == 0:
    #         cv2.putText(src, ('%s' % i), (max_contour[i][0][0], max_contour[i][0][1]), font, 1, (255, 0, 0), 1)

    start_points = find_two_most(y, max_contour)

    # print(start_point)

    index1 = xy_coord.index(start_points[0])
    index2 = xy_coord.index(start_points[1])

    # for i in range(index2, len(xy_coord)):
    #     if y > xy_coord[i][1]:
    #         dist = euclidean_distance(center[0], y, xy_coord[i][0], xy_coord[i][1])
    #         dist_list.append(dist)
    #
    # for i in range(0, index2):
    #     if y > xy_coord[i][1]:
    #         dist = euclidean_distance(center[0], y, xy_coord[i][0], xy_coord[i][1])
    #         dist_list.append(dist)
    #
    # print(dist_list)
    #
    # dist_list.reverse()
    #
    # plt.bar(range(len(dist_list)), dist_list)
    # plt.show()
    list1 = []
    list2 = []
    for i in range(0, index1):
        list1.append(xy_coord[i])

    list1.reverse()

    for i in range(index2, len(xy_coord)):
        list2.append(xy_coord[i])

    list2.reverse()

    list3 = list1 + list2

    scan_degree = int(len(list3) / 180 * 3)

    # for i in range(0, len(list3), scan_degree):
    #     dist = euclidean_distance(center[0], y, xy_coord[i][0], xy_coord[i][1])
    #     dist_list.append(dist)

    # font = cv2.FONT_HERSHEY_SIMPLEX
    # angel = 0
    # count = 0
    for i in range(0, len(list3), scan_degree):
        dist = euclidean_distance(center[0], y, xy_coord[i][0], xy_coord[i][1])
        dist_list.append(dist)
        # cv2.putText(src, ('%s' % count), (list3[i][0], list3[i][1]), font, 1, (255, 0, 0), 1)
        # angel += 3
        # count += 1

    # print(dist_list)
    # print(len(dist_list))
    # print(count)
    # plt.bar(range(len(dist_list)), dist_list)
    # plt.plot(range(len(dist_list)), dist_list, label='foot line', linewidth=3, color='r', marker='o',
    #          markerfacecolor='blue', markersize=5)
    # plt.show()
    #
    # cv2.namedWindow("c", 200)
    # cv2.imshow("c", src)
    return dist_list


# src = cv2.imread('./foot4.jpeg')
# src = rotate(src, -90)
# cv2.namedWindow("ori", 200)
# cv2.imshow("ori", src)
# src = cut_image(src)
#
# # cv2.namedWindow("cut", 200)
# # cv2.imshow("cut", src)
#
# get_data(src)
#
#
# cv2.waitKey(0)
#
# cv2.destroyAllWindows()


def get_distance():
    file_src = input("Please give me the file address: ")
    print("Please tell where you foot face: ")
    direction = input("North, south, east or west ")
    src = cv2.imread(file_src)
    if direction != 'North':
        if direction == 'South':
            src = rotate(src, -180)
        elif direction == 'West':
            src = rotate(src, -90)
        else:
            src = rotate(src, 90)
    src = cut_image(src)

    return get_data(src)
