import imutils
import cv2

image = cv2.imread("G:\Camera pics\DSC_0002.JPG")
(h,w,d) = image.shape

print("width = {}, height ={}, depth={}".format(w,h,d))

#cv2.imshow("Image",image)
#cv2.waitKey(0)

roi = image[60:160, 320:420]
#cv2.imshow("ROI", roi)
#cv2.waitKey(0)

# resizing image
#resized = cv2.resize(image, (500, 350))
#cv2.imshow("Fixed Resizing", resized)
#cv2.waitKey(0)


# fixed resizing and distort aspect ratio so let's resize the width
# to be 300px but compute the new height based on the aspect ratio
r = 300.0 / w
dim = (300, int(h * r))
resized = cv2.resize(image, dim)
#cv2.imshow("Aspect Ratio Resize", resized)
#cv2.waitKey(0)


# manually computing the aspect ratio can be a pain so let's use the
# imutils library instead
resized = imutils.resize(image, width=300)
#cv2.imshow("Imutils Resize", resized)
#cv2.waitKey(0)

# let's rotate an image 45 degrees clockwise using OpenCV by first
# computing the image center, then constructing the rotation matrix,
# and then finally applying the affine warp
resized = imutils.resize(image, width=300)
(resized_h,resized_w,resized_d) = resized.shape
center = (resized_w // 2, resized_h // 2)
M = cv2.getRotationMatrix2D(center, -45, 1.0)
rotated = cv2.warpAffine(resized, M, (resized_w, resized_h))
#cv2.imshow("OpenCV Rotation", rotated)
cv2.waitKey(0)


# rotation can also be easily accomplished via imutils with less code
#rotated = imutils.rotate(image, -45)
#cv2.imshow("Imutils Rotation", rotated)
cv2.waitKey(0)

# OpenCV doesn't "care" if our rotated image is clipped after rotation
# so we can instead use another imutils convenience function to help
# us out
rotated = imutils.rotate_bound(image, 45)
#cv2.imshow("Imutils Bound Rotation", rotated)
#cv2.waitKey(0)


# apply a Gaussian blur with a 11x11 kernel to the image to smooth it,
# useful when reducing high frequency noise
blurred = cv2.GaussianBlur(resized, (11, 11), 0)
#cv2.imshow("Blurred", blurred)
#cv2.waitKey(0)

# draw a 2px thick red rectangle surrounding the face
output = resized.copy()
cv2.rectangle(output, (60, 10), (160, 100), (0, 0, 255), 2)
#cv2.imshow("Rectangle", output)
#cv2.waitKey(0)

# draw a blue 20px (filled in) circle on the image centered at
# x=300,y=150
cv2.circle(output, (60, 10), 20, (255, 0, 0), -1)
#cv2.imshow("Circle", output)
#cv2.waitKey(0)

# draw a 5px thick red line from x=60,y=20 to x=400,y=200
output = resized.copy()
cv2.line(output, (60, 20), (160, 100), (0, 0, 255), 5)
#cv2.imshow("Line", output)
#cv2.waitKey(0)

# draw green text on the image
output = resized.copy()
cv2.putText(output, "OpenCV + Saranya!!!", (10, 25),
	cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
cv2.imshow("Text", output)
cv2.waitKey(0)