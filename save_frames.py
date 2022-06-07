import cv2
import os
import time
from glob import glob
from gray import getGray

from imutils.video import FileVideoStream
from imutils.video import FPS

file_name = "TV1"
base_path = "C:\\Users\\hunte\\Downloads\\test"

for file_path in sorted(glob(os.path.join(base_path, "*.avi"))):

    start_time = time.time()

    file_name = file_path.split("/")[-1].split(".")[0]
    depth_file_path = os.path.join(base_path, f"{file_name}.avi")
    rgb_file_path = os.path.join(base_path, f"{file_name}.mp4")

    print(depth_file_path)
    print(rgb_file_path)

    if not os.path.isfile(depth_file_path) or not os.path.isfile(rgb_file_path):
        print(f"RGB or Depth video file not found: {file_name}")
        continue


    depth_video = FileVideoStream(os.path.join(base_path, f'{file_name}.avi')).start()
    rgb_video = FileVideoStream(os.path.join(base_path, f'{file_name}.mp4')).start()

    fps = FPS().start()

    os.makedirs(os.path.join(base_path, "completed", f'{file_name}/rgb'))
    os.makedirs(os.path.join(base_path, "completed", f'{file_name}/gray'))

    count = 0

    while depth_video.more() and rgb_video.more():

        count += 1
        
        # Grab the frames from the threaded video file streams and convert depth image to grayscale
        rgb_image = rgb_video.read()
        depth_image = depth_video.read()

        grey_time = time.time()
        gray_img = getGray(depth_image)
        print(f'Time taken to convert to Grayscale: {(time.time() - grey_time):02}s', end='\r')
        #gray_img = np.dstack([gray_img, gray_img, gray_img])
        
        # Display the size of the queue on the frame
        cv2.putText(rgb_image, "Queue Size: {}".format(rgb_video.Q.qsize()),
            (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        
        # Save frames as PNG files
        cv2.imwrite(os.path.join(base_path, "completed", f"{file_name}/rgb/frame%d.png" % count), rgb_image)
        cv2.imwrite(os.path.join(base_path, "completed", f"{file_name}/gray/frame%d.png" % count), gray_img)


        print(f'Frame Count: {count} | Time : {int((time.time() - start_time)/60):02}:{ int((time.time() - start_time)%60):02}s', end='\r')

        if not rgb_video.more():
            print(f'Unable to read RGB frame {count}')
        elif not depth_video.more():
            print(f'Unable to read Depth frame {count}')

        fps.update()
    
    fps.stop()


