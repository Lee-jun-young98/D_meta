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
        data = self.cli_args.image_file_name
        img = cv2.imread(data)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        n, m = self.cli_args.column_num, self.cli_args.row_num

        img_resize = resize(img, n, m)
        img_list = cut_image(img_resize, n, m)
        img_list = random_img_list(img_list)

        if not os.path.exists("./result"):
            os.mkdir("./result")

        save_dir = "./result/"

        out_file = self.cli_args.prefix_output_filename

        if os.listdir("./result"):
            for i in os.listdir("./result"):
                os.remove("./result/" + i)

        for i in range(0, n*m):
            cv2.imwrite(save_dir + out_file + f"{i+1}.jpg", cv2.cvtColor(img_list[i], cv2.COLOR_BGR2RGB))
            print(save_dir + out_file + f"{i+1}.jpg가 저장되었습니다.")
    

if __name__ == '__main__':
    cut_image_app().main()

