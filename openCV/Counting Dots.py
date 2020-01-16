import cv2 as cv
path ="3.jpg"
  
# reading the image in grayscale mode
gray = cv.imread(path, 0) 
cv.imshow('im1',gray)
cv.waitKey(0)


# threshold 
th, threshed = cv.threshold(gray, 100, 255,  
          cv.THRESH_BINARY|cv.THRESH_OTSU) 




im2, contours, hierarchy = cv.findContours(threshed, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)


  
  
im1 = cv.drawContours(gray, contours, -1, (0,255,0), 3)

cv.imshow('img',im2)
cv.waitKey(0)
 


  
# printing output 
print("\nDots number:",(len(contours))) 
cv.destroyAllWindows()
