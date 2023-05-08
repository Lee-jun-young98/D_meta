import argparse
import cv2
import numpy as np
import os
import random
import sys
from utils.utils import *

class cut_image_app:
    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--image_file_name',
                            help="input image_file_name",
                            default="./data/house.jpeg",
                            type=str)
        parser.add_argument('--column_num',
                            help="input column count",
                            default=2,
                            type=int)
        parser.add_argument('--row_num',
                            help="input row count",
                            default=2,
                            type=int)
        parser.add_argument('--prefix_output_filename',
                            help="write output file name",
                            default="test",
                            type=str)
        
        self.cli_args = parser.parse_args()
    
    def main(self):
        data = self.cli_args.image_file_name # 데이터 불러오기
        img = cv2.imread(data) # 데이터 읽어오기
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # RGB형태로 변환
        n, m = self.cli_args.column_num, self.cli_args.row_num # n(column), m(row) 값 받기

        img_resize = resize(img, n, m) # 이미지 리사이즈 하기
        img_list = cut_image(img_resize, n, m) # 이미지 자르기
        img_list = random_img_list(img_list) # 이미지 랜덤으로 만들기 이 부분 주석 처리 시 원본 이미지로 생성

        save_dir = "./result/"
        out_file = self.cli_args.prefix_output_filename

        image_save(img_list, save_dir, out_file, n, m) # 결과 파일 저장
    

if __name__ == '__main__':
    cut_image_app().main()

