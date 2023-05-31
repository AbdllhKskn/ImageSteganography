import cv2
import cv2 as cv
import imutils

# Fotoğraf Alma ve Resize İşleminin Yapılması
img = cv2.imread('resim7.png')

img_resize = cv2.resize(img, (800, 700))  # alınan görüntünün 800x700 olarak alınması daha iyi
#cv2.imshow('Resize Photo', img_resize)


# Diplomalar için kordinatlar
y = 589
x = 60
h = 770
w = 290
just_photo = img_resize[x:w, y:h]
Rotated_image = imutils.rotate(just_photo, angle=45)
cv2.imshow("Rotated", Rotated_image)

# Belirlediğim kordinatlar için
y = 621
x = 81
h = 734
w = 270
crop_image = img_resize[x:w, y:h]
Rotated1_image = imutils.rotate(crop_image, angle=0)
cv2.imshow("Cropped", Rotated1_image)

tus = cv.waitKey(0)

if tus == 27:
    cv.destroyAllWindows()
elif tus == ord('s'):
    cv.imwrite("new_img.png", crop_image)
    cv.destroyAllWindows()
