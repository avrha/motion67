import numpy as np
import cv2 as cv
import time

class FPSCounter:
  def __init__(self):
    self.prev = time.time()

  def tick(self):
    now = time.time()
    fps = 1 / (now - self.prev)
    self.prev = now
    return fps
  
  def display_fps(self, frame, fps):
    cv.putText(frame, f"FPS: {fps:.2f}", (10, 30), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

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

  fps_counter = FPSCounter()

  while True:
    ret, frame = cap.read()

    if not ret:
      print("Can't receive frame (stream end?). Exiting ...")
      break

    fps = fps_counter.tick()
    fps_counter.display_fps(frame, fps)

    cv.imshow('Camera', frame)

    if cv.waitKey(1) == ord('q'):
      break

  cap.release()
  cv.destroyAllWindows()

if __name__ == "__main__":
  main()

