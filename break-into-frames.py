import cv2
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("-v", "--video", type=str, required=True, help="Path to the video")
parser.add_argument("-n", "--number", type=int, required=False, help="The number of frames to skip between each frame")
args = parser.parse_args()

# Defaults to 10 frames if no number is provided
number = args.number if args.number else 10

# Creates the 'frames' directory if it doesn't exist
if not os.path.exists("frames"):
    os.mkdir("frames")

def main():
    cap = cv2.VideoCapture(args.video)
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_number = 0
    while cap.isOpened():
        frame_exists, curr_frame = cap.read()
        if not frame_exists: break

        if frame_number % number == 0:
            print("Writing frame {0}...".format(frame_number))
            timestamp = frame_number / fps
            cv2.imwrite("frames/{0}_{1}.png".format(frame_number, timestamp), curr_frame)

        frame_number += 1

    cap.release()

if __name__ == "__main__":
    main()
