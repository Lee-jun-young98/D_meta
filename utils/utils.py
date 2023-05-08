import cv2
import random
import matplotlib.pyplot as plt
import os
import numpy as np

def resize(img, n, m):
    """
    input : 이미지, n, m
    output = n, m로 나눌 수 있도록 resize한 파일
    """
    h, w = img.shape[:2] # img 높이, 넓이 알기
    while w % n != 0: # 이미지 크기 맞추기
        w -= 1

    while h % m != 0: # 이미지 크기 맞추기
        h -= 1

    img = cv2.resize(img, (w, h)) # 크기에 맞춰 resize 하기
    
    return img



def cut_image(img, n, m): # 이미지 자르기
    """
    input : 이미지, n, m
    output : 공식에 맞춰 나눈 (n, m)에 해당하는 이미지 파일
            * (n, m)은 해당 파일의 위치 좌표임 ex) (0, 1)은 n이 0 m이 1에 해당
    """
    h, w = img.shape[:2]
    img_list = []
    for i in range(n): # x
        for j in range(m): # y 
                if i == 0 and j == 0: # 제일 왼쪽 위일때 
                    # img_h = img[(h//m)*j:(h//m)*(j+1)+(h//m)//m]
                    # img_w = img[(w//n)*i:(w//n)*(i+1)+(w//n)//n]
                    img_list.append(img[(h//m)*j:(h//m)*(j+1)+(h//m)//m, (w//n)*i:(w//n)*(i+1)+(w//n)//n])
                    print("Top left")
                
                elif i == 0 and j+1 == m: # 제일 왼쪽 아래일 때
                    # img_h = img[(h//m)*j-(h//m)//m:(h//m)*(j+1)]
                    # img_w = img[(w//n)*i:(w//n)*(i+1)+(w//n)//n]
                    img_list.append(img[(h//m)*j-(h//m)//m:(h//m)*(j+1), (w//n)*i:(w//n)*(i+1)+(w//n)//n])
                    print("Down left")
                

                elif  i+1 == n and j == 0: # 제일 오른쪽 위에 있을 때
                    # img_h = img[(h//m)*j:(h//m)*(j+1)+(h//m)//m]
                    # img_w = img[(w//n)*i-(w//n)//n:(w//n)*(i+1)]
                    img_list.append(img[(h//m)*j:(h//m)*(j+1)+(h//m)//m, (w//n)*i-(w//n)//n:(w//n)*(i+1)])
                    print("Top right")
                

                elif i+1 == n and j+1 == m: # 제일 오른쪽 아래에 있을 때
                    # img_h = img[(h//m)*j-(h//m)//m:(h//m)*(j+1)]
                    # img_w = img[(w//n)*i-(w//n)//n:(w//n)*(i+1)]
                    img_list.append(img[(h//m)*j-(h//m)//m:(h//m)*(j+1), (w//n)*i-(w//n)//n:(w//n)*(i+1)])
                    print("Down right")
                

                elif i == 0: # x가 0일 때 제일 왼쪽
                    # img_h = img[(h//m)*j-(h//m)//(m*2):(h//m)*(j+1)+(h//m)//(m*2)]
                    # img_w = img[(w//n)*i:(w//n)*(i+1)+(w//n)//n]
                    img_list.append(img[(h//m)*j-(h//m)//(m*2):(h//m)*(j+1)+(h//m)//(m*2), (w//n)*i:(w//n)*(i+1)+(w//n)//n])
                    print("Left")
                
                elif i+1 == n: # x가 최대일 때 오른쪽
                    # img_h = img[(h//m)*j-(h//m)//(m*2):(h//m)*(j+1)+(h//m)//(m*2)]
                    # img_w = img[(w//n)*i-(w//n)//n:(w//n)*(i+1)]
                    img_list.append(img[(h//m)*j-(h//m)//(m*2):(h//m)*(j+1)+(h//m)//(m*2), (w//n)*i-(w//n)//n:(w//n)*(i+1)])
                    print("Right")
                    
                elif j == 0: # y가 0일 때 제일 위쪽
                    # img_h = img[(h//m)*j:(h//m)*(j+1)+(h//m)//m]
                    # img_w = img[(w//n)*i-(w//n)//(n*2):(w//n)*(i+1)+(w//n)//(n*2)]
                    img_list.append(img[(h//m)*j:(h//m)*(j+1)+(h//m)//m, (w//n)*i-(w//n)//(n*2):(w//n)*(i+1)+(w//n)//(n*2)])
                    print("Top")


                elif j+1 == m: # y가 최대일 때 제일 아래쪽
                    # img_h = img[(h//m)*j-(h//m)//m:(h//m)*(j+1)]
                    # img_w = img[(w//n)*i-(w//n)//(n*2):(w//n)*(i+1)+(w//n)//(n*2)]
                    img_list.append(img[(h//m)*j-(h//m)//m:(h//m)*(j+1), (w//n)*i-(w//n)//(n*2):(w//n)*(i+1)+(w//n)//(n*2)])
                    print("Down")

                
                else: # 그 외 
                    # img_h = img[(h//m)*j-(h//m)//(m*2):(h//m)*(j+1)+(h//m)//(m*2)]
                    # img_w = img[(w//n)*i-(w//n)//(n*2):(w//n)*(i+1)+(w//n)//(n*2)]
                    img_list.append(img[(h//m)*j-(h//m)//(m*2):(h//m)*(j+1)+(h//m)//(m*2), (w//n)*i-(w//n)//(n*2):(w//n)*(i+1)+(w//n)//(n*2)])
                    print(f"{i},{j} Image")
    
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
    """
    input : n, m으로 자른 이미지가 저장된 리스트
    output : 이미지 리스트에 있는 파일 중 0.5의 확률로 mirroring, flip, rotate를 거친 파일들
    """
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



def image_load(data_dir):
    """
    input : imags_list
    output : 부른 이미지를 리스트로 저장
    """
    imgs_list = []
    for data in os.listdir(data_dir):
        if data[-4:] == ".jpg":
            img = cv2.imread(data_dir + data)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            imgs_list.append(img)

    return imgs_list



def image_save(img_list, save_dir, out_file, n=None, m=None):
    if not os.path.exists(save_dir):
            os.mkdir(save_dir)
    
    if os.listdir(save_dir):
        for i in os.listdir(save_dir):
            os.remove(save_dir + i)

    if n and m:
        for i in range(0, n*m):
            cv2.imwrite(save_dir + out_file + f"{i+1}.jpg", cv2.cvtColor(img_list[i], cv2.COLOR_BGR2RGB))
            print(save_dir + out_file + f"{i+1}.jpg가 저장되었습니다.")
    else:
        cv2.imwrite(save_dir + out_file + ".jpg", cv2.cvtColor(img_list, cv2.COLOR_BGR2RGB))



def image_stitch(imgs1, imgs2):
    """
    input : imgs1(image 파일), imgs2 파일(image 파일)
    output : stitcher_create를 이용하여 병합된 파일
             * 병합이 됐을 경우 status 0, 돼지 않았을 경우 status 1
    """
    imgs = [imgs1, imgs2]
    stitcher = cv2.Stitcher_create()
    try:
        status, dst = stitcher.stitch(imgs)
    except:
        status, dst = 0, imgs1

    return status, dst



def find_direction(img1, img2):
    """
    input : imgs1(image 파일), image2 파일(image 파일)
    output : sift 알고리즘을 사용하여 특징을 추출한 후 호모그래피와 회전 각도를 계산한 값, 좋은 결과가 매칭된 값의 길이
    """
    # SIFT 추출기 생성
    sift = cv2.SIFT_create()

    # ORB 추출기 생성
    # orb = cv2.ORB_create()

    # 특징점과 디스크립터 추출
    kp1, des1 = sift.detectAndCompute(img1, None)
    kp2, des2 = sift.detectAndCompute(img2, None)

    # FLANN 매처 생성
    flann = cv2.FlannBasedMatcher({'algorithm': 0, 'trees': 5}, {'checks': 50})

    # 매칭 결과 추출
    matches = flann.knnMatch(des1, des2, k=2)

    # 좋은 매칭 결과 필터링
    good_matches = []
    for m, n in matches:
        if m.distance < 0.7 * n.distance:
            good_matches.append(m)


    # 매칭된 특징점의 위치 추출
    points1 = np.array([kp1[m.queryIdx].pt for m in good_matches])
    points2 = np.array([kp2[m.trainIdx].pt for m in good_matches])
    
    try:
        # 호모 그래피 계산
        H, _ = cv2.findHomography(points1, points2, cv2.RANSAC)
        # 회전 각도 계산
        angle = np.rad2deg(np.arctan2(H[1, 0], H[0, 0]))
    except:
        return -9999, len(good_matches) # 특징점에 대한 오류 발생시 후 순위로 미룸
    
    return angle, len(good_matches)
    


def collect(imgs1, imgs2, angle):
    """
    input : imgs1(image 파일), image2 파일(image 파일), find_direction 함수로 만든 각도
    output : imgs1(image 파일), image2 파일(image 파일), 같은 방향을 보고 있을 때 True
    이미지의 각도 추정을 했을 경우 0도이면 같은 방향을 보고 있다 가정하고 이미지 스티칭을 진행
    나머지의 경우 각 각도 별로의 mirroring, flip, rotate 함수를 적용하여 원본 이미지와 같은 각도를 볼 수 있도록 진행함 
    """
    while True:
        if angle <= 10 and angle >= -10: # 같은 방향을 보고 있을 때
            break

        elif angle <= 100 and angle >= 80: # 90도 방향 차이
            imgs2 = rotate(imgs2)
            angle, _ = find_direction(imgs1, imgs2)
        
        elif angle <= -80 and angle >= -100: # -90도 방향 차이
            imgs2 = rotate(mirroring(imgs2))
            angle, _ = find_direction(imgs1, imgs2)
            
        elif angle <= 190 and angle >= 170: # 180도 방향차이
            imgs2 = mirroring(imgs2)
            angle, _ = find_direction(imgs1, imgs2)

        elif angle <= -170 and angle >= -190: # -180도 방향 차이
            imgs2 = flip(mirroring(imgs2))
            angle, _ = find_direction(imgs1, imgs2)
        
        else:
            return imgs1, imgs2, False
            
    return imgs1, imgs2, True
        


def merge_image(imgs1, imgs2, status):
    """
    input : imgs1(image 파일), image2 파일(image 파일), image_stitch 함수의 결과값
    output : image_stitch 함수의 결과값, 합친 이미지
    """
    status, img_stitch = image_stitch(imgs1, imgs2)
    if status == 1:
        status, img_stitch = image_stitch(imgs1, flip(imgs2))

    return status, img_stitch



def total_merge(imgs_list, remain=None, use_remain=False):
    """
    input : 이미지 리스트들
    output : 합친 이미지, 남은 이미지
    """
    if not remain:
        remain = []
    
    status = 0
    for i, k in enumerate(imgs_list.copy()):
        if i == 0:
            imgs1 = k
            continue

        imgs2 = k
        angle, good_match_len = find_direction(imgs1, imgs2)
        print(f"imgs1, imgs2의 angle은 {angle}이다.")
    

        if good_match_len >= 10: # 매칭된 특징이 10개 이상이면 각도 탐색 아닐 시 남은 이미지에 리스트 추가
            imgs1, imgs2, no_degree = collect(imgs1, imgs2, angle)
            if no_degree == False: # 각도 탐색이 이루어지지 않는 경우 후순위로 미룸
                remain.append(imgs2)
                print(f"{i+1}번째 이미지 리스트에 추가")
                print("---------------------------------------------------")
            else:
                status, img_stitch = merge_image(imgs1, imgs2, status)
                if status == 0: # 이미지 결합이 완료된 경우
                    imgs1 = img_stitch
                    plt.imshow(imgs1)
                    print(f"{i+1}번째 이미지 완료")
                    print("---------------------------------------------------")
                    if use_remain == True:
                        imgs_list.remove(k)
                else:
                    remain.append(imgs2)
        else:
            remain.append(imgs2)
            print(f"{i+1}번째 이미지 리스트에 추가")
            print("---------------------------------------------------")
            
    return imgs1, remain
