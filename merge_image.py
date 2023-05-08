import cv2
import os
from utils.utils import *
import matplotlib.pyplot as plt
import argparse


class merge_image_app:
    def __init__(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--input_filename_prefix',
                            help="input image folder",
                            default="./result/",
                            type=str)
        parser.add_argument('--column_num',
                            help="input column count",
                            default=2,
                            type=int)
        parser.add_argument('--row_num',
                            help="input row count",
                            default=2,
                            type=int)
        parser.add_argument('--output_filename',
                            help="write output file name",
                            default="final_result",
                            type=str)
        
        self.cli_args = parser.parse_args()
    
    def main(self):
        print("=================이미지 합성 시작=================")
        data_dir = self.cli_args.input_filename_prefix # 데이터 디렉토리 로드
        output_name = self.cli_args.output_filename # 결과물 이름
        save_dir = "./final/" # 결과물 저장 디렉토리
        n, m = self.cli_args.column_num, self.cli_args.row_num

        imgs_list = image_load(data_dir) # 이미지 리스트 로드
        imgs1, remain = total_merge(imgs_list) # 이미지 결합

        if len(remain) == 0: # 남은 결과물이 없으면 바로 저장
            image_save(imgs1, save_dir, output_name)
        else:
            count = 0
            while len(remain) != 0:
                count += 1
                print("\n")
                print("===================================================") 
                print(f"{count}번째 반복 시작")
                print("===================================================")         
                remain.insert(0, imgs1)
                imgs1, remain = total_merge(remain)
                print(f"남은 이미지의 개수는 {len(remain)}")
                if count == n*m:
                    break
            
        image_save(imgs1, save_dir, output_name)

if __name__ == '__main__':
    merge_image_app().main()

