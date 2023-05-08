# D_meta Image Cut & Merge

## 개발환경
- Visual studio code version 1.78
- python 3.10.8
```commandline
pip install -r requirements.txt
```

## 실행 방법
### cut_image.py
```commandline
python cut_image.py --image_file_name image_dir --column_num n --row_num m --prefix_output_filename output_filename
ex) python cut_image.py --image_file_name "./data/house.jpeg" --column_num 2 --row_num 2 --prefix_output_filename "test"
```

### merge_image.py
```commandline
python merge_image.py --input_filename_prefix data_dir --column_num n --column_num m --output_filename output_filename
ex) python merge_image.py --input_filename_prefix "./result/" --column_num 2 --column_num 2 --output_filename "final_result"
``` 

