#IMAGE FACE DETECTION
import cv2 
import numpy

face_cascade = cv2.CascadeClassifier('C:\\Users\\dell\\Desktop\\cascade.xml')
#serialising the XML file
vid = cv2.VideoCapture(0)
scale_factor = 1.3
#bringing the image close to face, easy to detect
while 1:
	ret, pic = vid.read()
	faces = face_cascade.detectMultiScale(pic,scale_factor,5)
	#detect where the face is, '5' number of rectangles will be included in the face region where the classifier has been detected
	for (x,y,w,h) in faces:
		cv2.rectangle(pic,(x,y),(x+w,y+h),(255,255,0),2)
		#rectangle(pic,axes of face,color,thickness)
		font = cv2.FONT_HERSHEY_SIMPLEX
		cv2.putText(pic,'face',(x,y),font,2,(255,0,0),2,cv2.LINE_AA)
		#putText(image,name,point,font_type,font_size,color,thickness,Line_aa)
		#LINE_AA is used for a better looking outline
	print("Number of faces found {}".format(len(faces)))
	cv2.imshow('face',pic)
	k = cv2.waitKey(30) & 0xff
	if k==2:
		break
cv2.destroyAllWindows()



