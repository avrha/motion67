import numpy as np
import cv2 as cv
import time

def main():
  cap = cv.VideoCapture(0, cv.CAP_V4L2)
  cap.set(cv.CAP_PROP_FOURCC, cv.VideoWriter_fourcc(*'MJPG'))
  cap.set(cv.CAP_PROP_FRAME_WIDTH, 1024)
  cap.set(cv.CAP_PROP_FRAME_HEIGHT, 768)
  cap.set(cv.CAP_PROP_FPS, 30)
  cap.set(cv.CAP_PROP_BUFFERSIZE, 1)

  if not cap.isOpened():
    print("Cannot open camera")
    exit()

  prev = time.time()

  while True:
    ret, frame = cap.read()

    if not ret:
      print("Can't receive frame (stream end?). Exiting ...")
      break

    now = time.time()
    fps = 1 / (now - prev)
    prev = now

    cv.putText(
      frame,
      f"FPS: {fps:1f}",
      (10,30),
      cv.FONT_HERSHEY_SIMPLEX,
      1,
      (0, 255, 0),
      2
    )
      
    cv.imshow('frame', frame)

    if cv.waitKey(1) == ord('q'):
      break

  cap.release()
  cv.destroyAllWindows()

if __name__ == "__main__":
  main()

