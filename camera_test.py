import cv2

video = cv2.VideoCapture(0)

while True:
	ret, frame = video.read()
	cv2.imshow('test', frame)

	key = cv2.waitKey(1)
	if key == 27:
		break
video.release()
cv2.destroyAllWindows()
