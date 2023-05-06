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
                            default="final_result.jpg",
                            type=str)
        
        self.cli_args = parser.parse_args()
    
    def main(self):
        data_dir = self.cli_args.input_filename_prefix
        output_name = self.cli_args.output_filename
        save_dir = "./final/"
        n, m = self.cli_args.column_num, self.cli_args.row_num

        imgs_list = []
        for data in os.listdir(data_dir):
            if data[-4:] == ".jpg":
                img = cv2.imread(data_dir + data)
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            imgs_list.append(img)

        
        imgs1, remain = total_merge(imgs_list)

        if len(remain) == 0:
            image_save(imgs1, save_dir, output_name)
        else:
            count = 0
            while len(remain) != 0:
                count += 1
                remain.insert(0, imgs1)
                imgs1, remain = total_merge(remain)
                print(f"남은 이미지의 개수는 {len(remain-1)}")
                if count == n*m:
                    break
            
        image_save(imgs1, save_dir, output_name)

if __name__ == '__main__':
    merge_image_app().main()

