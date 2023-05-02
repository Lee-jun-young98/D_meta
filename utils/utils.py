import cv2
import os
import random
import matplotlib as plt
import sys


def resize(img, n, m):
    h, w = img.shape[0], img.shape[1] # img 높이, 넓이 알기
    while w % n != 0: # 이미지 크기 맞추기
        w -= 1

    while h % m != 0: # 이미지 크기 맞추기
        h -= 1

    img = cv2.resize(img, (w, h)) # 크기에 맞춰 resize 하기
    
    return img

def cut_image(img, n, m):
    img_list = []
    for i in range(n):
        for j in range(m):
            img_list.append(img[(img.shape[0]//n)*i:(img.shape[0]//n)*(i+1), (img.shape[1]//m)*j:(img.shape[1]//m)*(j+1)])
    
    return img_list


def mirroring(img):
    img = cv2.flip(img, 1)
    return img


def flip(img):
    img = cv2.flip(img, 0)
    return img


def rotate(img):
    img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE) # 반시계방향으로 회전
    return img


def visualize(img_list):
    fig = plt.figure(figsize = (10,10))
    for i, k in enumerate(img_list):
        plt.subplot(1,len(img_list),i+1)
        plt.imshow(k)



def random_img_list(img_list):
    for i in range(len(img_list)):
        t_f = random.choice([0,1])
        if t_f == 1:
            img_list[i] = mirroring(img_list[i])
        
        t_f = random.choice([0,1])
        if t_f == 1:
            img_list[i] = flip(img_list[i])
        
        t_f = random.choice([0,1])
        if t_f == 1:
            img_list[i] = rotate(img_list[i])
    
    random.shuffle(img_list)

    return img_list
