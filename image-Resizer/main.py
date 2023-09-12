import cv2

# Configurable parameters
source = "image.jpg"
destination='New_image.png'
scale_percent = 50


src = cv2.imread(source,cv2.IMREAD_UNCHANGED)
# cv2.imshow("TITLE",src)

#percent by which image is resized

#calculate the 50 percent of original dimensions
new_width = int(src.shape[1]*scale_percent/100)
new_height = int(src.shape[0]*scale_percent/100)

#desize
dsize = (new_width, new_height)

#resize image
output = cv2.resize(src, dsize)

cv2.imwrite(destination, output)

cv2.waitKey(0)