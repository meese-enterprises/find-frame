# find-frame
Find an image within the frames of a video.

This project is based off of the code in this [Stack Overflow answer](https://stackoverflow.com/a/41337250/6456163), just extened for usability.

## usage

1. `pip3 install -r requirements.txt`
2. `python3 find-frame.py <video> <image>`

Example with the included video and image:

```shell
python3 find-frame.py -v demo/mario_gameplay.mp4 -i demo/world_1-1.png
```

Optionally, a threshold integer can be specified to determine how close the image must be to the frame. The default is 80, which translates to 0.8. The closer to 100, the more strict the search will be.

```shell
python3 find-frame.py -v demo/mario_gameplay.mp4 -i demo/world_1-1.png -t 60
```
