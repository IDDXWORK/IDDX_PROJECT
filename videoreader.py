import cv2

video_path='sample_data\\20210812144231_0060_combined.mp4'
cap=cv2.VideoCapture('sample_data\\20210812144231_0060_combined.mp4')
print('started')
i=0
print(cap.isOpened())
while 1:
    print("frame: ",i)
    ret,frame=cap.read()
    if not ret:
        break
    cv2.imshow("FRAME:",frame)
    if cv2.waitKey(0)==ord('w'):
        i+=1
        continue
    elif cv2.waitKey(0)==ord('q'):
        print("ending")
        break

cap.release()
cv2.destroyAllWindows()

    