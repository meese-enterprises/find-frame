import cv2
import numpy as np
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--image", type=str, required=True, help="Path to the image")
parser.add_argument("-v", "--video", type=str, required=True, help="Path to the video")
parser.add_argument("-t", "--threshold", type=int, required=False, help="The percentage that the image must be similar to the frame")
args = parser.parse_args()

# Defaults to an 80% match if no threshold is provided
threshold = args.threshold / 100 if args.threshold else 0.8

# Creates the 'matches' directory if it doesn't exist
if not os.path.exists("matches"):
    os.mkdir("matches")

def process_image(img_rgb, image_to_find, frame_number, timestamp):
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    w, h = image_to_find.shape[::-1]

    res = cv2.matchTemplate(img_gray, image_to_find, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= threshold)

    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

    # This will write different image for each frame with a match
    if len(loc[0]) > 0:
        print("FOUND at frame: {}, timestamp: {}".format(frame_number, timestamp))
        cv2.imwrite("matches/{0}_{1}.png".format(frame_number, timestamp), img_rgb)
    else:
        print("No match at frame {0} at {1}".format(frame_number, timestamp))

def main():
    cap = cv2.VideoCapture(args.video)
    fps = cap.get(cv2.CAP_PROP_FPS)
    image_to_find = cv2.imread(args.image, 0)
    frame_number = 0
    while cap.isOpened():
        frame_exists, curr_frame = cap.read()
        if not frame_exists: break
        timestamp = frame_number / fps
        process_image(curr_frame, image_to_find, frame_number, timestamp)
        frame_number += 1

    cap.release()

if __name__ == "__main__":
    main()
