# D_meta Image Cut & Merge

## 개발환경
- Visual studio code version 1.78
- python 3.10.8
```commandline
pip install -r requirements.txt
```

## 사용한 패키지
- opencv
- matplotlib
- numpy
- argparse


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

## 폴더 리스트
```bash
├── data
│   ├── house.jpeg
│   ├── sample.jpg
│   └── sample2.jpeg
├── result - cut_image.py 실행 시 생성 cut_image 결과
├── final - merge_image.py 실행 시 생성 최종 결과
├── cut_image.py
├── merge_image.py
├── utils
│   └── util.py
``` 

## 유의사항
![image](https://user-images.githubusercontent.com/80506107/236975415-ed4e8d02-6c60-4e9c-b529-8187f1ab861c.png)
- 위의 에러가 발생하시면 종료하시고 cut_image를 다시 실행시켜주시면 감사하겠습니다.
- 첫번째 사진의 특징점 추출에 따른 성능차이가 있습니다.
