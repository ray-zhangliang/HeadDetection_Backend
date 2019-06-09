# -*- coding: utf-8 -*-
# @Time : 2019/6/5 18:34
# @Author : Tom Chen
# @Email : chenbaocun@emails.bjut.edu.cn
# @File : test2.py
# @Software: PyCharm
from time import sleep
# from Home.tests import q

# def do():
#     sleep(2)
#     # print(1)
#     file=open('./queue.txt','w+')
#     # print(file.read())
#     file.write('1')
#     file.close()
#     # q.get()
# do()
abnormal_image=[-33, -122, 96, 59, -5, -9, -50, 56, -20, 14, 92, 120, 4, 14, -101, 79, -23, -100, 119, -49, -1, 0, -84, -13, -41, 50, -100, -105, -70, -102, 87, -78, 122, 36, -102, -68, 94, -86, -38, -18, -97, -83, -9, 106, -19, 127, 95, 47, -21, -2, 29, -116, 85, 28, -125, -41, 3, 28, -29, -5, -34, -25, -98, 57, -49, -5, 60, 100, -100, -118, -96, -28, 3, -19, -110, 61, 15, 111, -101, -65, -14, -90, -114, 115, -98, 122, -98, -3, -73, -5, -1, 0, -78, 15, -11, 60, -27, -15, -116, -125, -110, 120, 56, 28, -111, -21, -23, -49, -12, -28, -16, 78, 114, -3, -27, -52, -7, -75, 86, -65, -51, -55, 43, 105, -3, -35, 124, -102, -43, -22, 85, -102, -26, -41, -31, -27, -23, -33, -102, -42, -45, -55, -34, -6, -21, -69, -69, 5, 11, -37, 7, 30, -68, 103, -122, -25, 7, 61, -6, -98, -64, 99, -100, 82, -31, 57, -37, -56, 24, 39, -97, 119, -63, 61, 114, 120, 56, 30, -121, -109, -59, 52, 1, -6, -127, -8, 16, -92, -5, -13, -69, -41, -96, 29, -14, 75, -74, -116, -2, 29, -80, 7, -34, -57, -28, 123, -25, 63, 92, 84, 107, -35, -19, 110, -69, 93, -66, -1, 0, -121, -101, -43, -69, -73, 54, -2, -66, -17, -14, -4, -6, -73, 117, 28, 103, -114, 6, 2, -98, 51, -41, 7, -87, -17, -100, -25, 35, -126, 50, 79, 20, -48, -39, 36, 96, 117, 60, 116, -50, 55, 99, 60, -98, 126, 94, -65, -82, 78, 105, -93, -17, 126, 0, 125, 62, -24, -29, -16, 99, -41, 61, -69, -18, 44, -89, -128, 64, -17, -112, 79, 115, -75, -114, 59, -9, -49, 62, -40, 29, -86, -7, 82, -33, -83, -83, 109, -75, 81, 122, -21, 125, -97, 125, 91, 123, 104, -58, -110, 74, -6, -67, 44, -75, 123, -33, -83, -37, -7, -67, -35, -19, -94, 72, 119, 92, -109, -48, -127, -98, 120, -27, -104, -9, 32, 14, -104, -4, 71, 39, 2, -102, 6, 70, 48, 14, 49, -50, 112, 72, -55, -11, -25, -98, 9, -25, 30, -124, -110, 112, 3, -14, -25, 0, -15, -114, -3, 3, 46, 59, -1, 0, -75, -97, -5, -25, -109, -125, -108, -24, -69, -121, 92, -127, -45, -114, 14, 122, 103, -65, 127, -15, -26, -90, 59, -4, -46, -21, -4, -45, 87, -33, -5, -65, -7, 51, -75, -102, 109, -91, -90, -34, 86, -7, 115, 118, -73, 127, -49, -85, 98, -82, 121, 0, 30, 8, 56, -55, -23, -106, -49, 94, -34, -33, -19, 103, -99, -68, -124, 12, -80, -32, 0, 64, -17, -113, -30, -63, 61, -72, -57, 3, -44, -98, 112, 13, 46, 62, -14, -114, 6, 84, 113, -98, 115, -98, -66, -67, 122, 116, -10, 57, 52, -34, -123, -122, 127, -68, 15, -66, 15, -11, -17, 85, 5, 126, 119, -4, -86, 54, -21, -83, -27, 119, -81, 116, -101, -33, 71, 109, 93, -82, 84, 117, 111, -47, 121, -11, 105, -69, 54, -9, -34, -35, 52, -34, -62, -116, 1, -100, 103, 105, -58, 71, 67, -53, 114, 122, -6, -16, 51, -41, 60, -116, -102, 110, 71, 61, -77, -114, -100, -116, 2, 79, 115, -41, -89, -8, 3, -109, 75, -116, 38, 65, 63, 49, 57, 29, -66, 86, 76, 123, -9, -55, -4, 58, -32, -28, 60, 103, 31, -34, 35, -98, 71, 25, -20, 126, -65, -53, -72, -92, -67, -42, -34, -18, -5, -20, -18, -101, 123, 106, -75, -33, -83, -69, 39, 102, -87, 67, -30, -41, -86, -113, 107, -35, 77, -19, -81, -14, -85, 118, -69, -47, -67, 64, 17, -125, -100, 118, 29, -13, -128, 73, 56, -28, -114, 112, 61, -14, 122, -32, 19, 72, 8, -6, 30, -40, -23, -63, 98, 58, -100, -13, -98, 121, 61, -72, 36, 18, 76, 114, 7, -45, -1, 0, 100, -9, -9, -2, 93, 112, 114, -32, 1, 83, -20, -65, -5, 51, -3, 127, -70, 63, 51, -51, 9, -18, -42, -106, 113, -4, -102, 86, 87, -2, -20, -73, 119, -77, 74, -6, -51, -69, -124, 46, -90, -45, 126, -26, -34, 124, -83, 69, -19, -27, 36, -41, 93, -42, -105, -109, 104, -92, -116, -128, 112, 14, 1, 36, 118, 5, -79, -114, 79, 111, -26, 57, -56, 57, 67, -11, 39, 29, 58, -13, -55, -9, -29, -128, 15, -29, -114, 72, 52, -98, -66, -1, 0, -29, -37, -4, -12, -91, 3, 42, -57, -5, -69, 113, -8, -100, 122, -1, 0, 90, 105, -91, 119, 107, -20, -107, -3, 94, -70, -73, 109, 20, 118, 127, 37, 109, 101, 89, 38, -19, 126, 86, -106, -69, -69, 54, -81, 125, -42, -5, 94, -42, -20, -37, 5, 25, 61, 113, -17, -1, 0, 125, 15, 95, -10, 71, 127, -30, 28, -110, 50, 64, -92, -126, 71, 65, -41, -82, 122, -29, -1, 0, -81, -41, -89, -91, 72, -72, 56, -6, 15, -3, -87, -21, -97, 79, -44, -11, -59, 34, 40, 32, -25, -79, -1, 0, 31, -81, -81, -14, 4, -112, 41, 115, 61, 108, -38, -37, -17, 93, 94, -65, -95, 62, -46, -15, -45, 71, 123, -33, 125, 53, -78, -43, -39, 124, 50, 110, -35, -30, -82, -11, 96, 6, -48, -8, -28, -128, 50, 122, 99, 37, -15, -63, -49, -9, 71, 28, -14, 78, 73, -91, 80, 64, 60, -113, -31, -12, -29, -26, 97, -64, 36, 100, -27, -78, 64, -25, -82, 120, 4, -106, 127, 9, -9, -58, 120, 29, -117, 1, -113, 78, -65, 94, -100, -100, 28, -71, 122, -97, 125, -65, -88, -112, -28, 100, -100, 119, -17, -48, -111, -109, -42, -91, 108, -4, -83, -45, -91, -19, -90, -69, -3, -33, 50, 109, -93, 119, -65, 123, -18, -7, 90, -14, -17, 43, -3, -22, -10, -65, 49, -113, -67, -50, 115, -80, 103, 24, 35, -26, -111, 114, 58, -3, -18, -29, 60, 12, 14, 121, 52, -128, 49, -49, 0, -10, -55, 56, 60, 22, -20, 27, -113, 95, 94, 112, 115, -128, 74, -97, -7, 107, -1, 0, 108, -1, 0, -10, -89, -7, -2, -76, 32, 12, 24, -97, 95, 65, -22, 121, -28, 31, 94, -99, 63, 18, 105, -83, 63, 7, -41, -17, 86, 107, 93, 95, -4, 59, 98, 90, 94, -6, -37, -105, -70, -43, -90, -17, -92, -65, -85, -67, -11, 111, -1, -39]
img = bytearray.decode(abnormal_image)
print(img)
