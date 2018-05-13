# Description
The dataset consists of 90 000 grayscale videos that show two objects of equal shape and size in which one object approaches the other one. The object speed during the process of approaching is hereby modeled by a proportional-derivative controller. Overall, three different shapes (Rectangle, Triangle and Circle) are provided. Initial conﬁguration of the objects such as position and color were randomly sampled. Different from the moving MNIST dataset, the samples comprise a goal-oriented task, namely one object has to fully cover the other object rather than randomly moving, making it better suitable for testing prediction capabilities of an ML model.

For instance, one can use it as a toy dataset to investigate the capacity and output behavior of a deep neural network before testing it on real-world data. We have done this for a deep auto-encoder network:

![Square](https://github.com/ferreirafabio/FlyingShapesDataset/blob/master/examples/000618_original_square.gif)
![Circle](https://github.com/ferreirafabio/FlyingShapesDataset/blob/master/examples/001483_original_circle.gif)
![Triangle](https://github.com/ferreirafabio/FlyingShapesDataset/blob/master/examples/007033_original_triangle.gif)  
![Square](https://github.com/ferreirafabio/FlyingShapesDataset/blob/master/examples/000618_generated_square.gif)
![Circle](https://github.com/ferreirafabio/FlyingShapesDataset/blob/master/examples/001483_generated_circle.gif)
![Triangle](https://github.com/ferreirafabio/FlyingShapesDataset/blob/master/examples/007033_original_triangle.gif)

# Specifications
We provide both the videos as .avi files as well as TensorFlow tfrecord files. The samples in the tfrecord files contain 10 frames of the original video which were taken equally distributed over the entire playtime. Here are some more details:
## Dataset as avi
- video resolution: 128x128
- fps: 30
- color depth: 24bpp (3 channels, grayscale)
- video codec: ffmjpeg
- compression format: mjpeg, color encoding: yuvj420p
- the samples follow the naming: 
  ```
  id_shape_startLocation_endLocation_motionDirection_euclideanDistance
  ```
  where:
    - ```id``` is a unique identifier
    - ```startLocation``` starting position of the object, e.g. righttop
    - ```endLocation``` destination position of the object, e.g. leftbottom
    - ```motionDirection``` e.g. left
    - ```euclideanDistance``` Euclidean distance between the two objects, e.g. 7.765617 

## Dataset as tfrecord
The tfrecord files store both the video itself and meta information from the file name (start location, eucl. distance etc.).
- the video data is stored in a ```feature``` dict (which is serialized as ```tf.train.Example```) which stores the following keys 
    - feature[path] #('blob' + '/' + str(imageCount)
    - feature['height']
    - feature['width']
    - feature['depth']
    - feature['id']
- additional information is stored in a ```meta_dict``` (which is also serialized within the feature dict via the key 'metadata')
    - meta_dict['shape']
    - meta_dict['start_location']
    - meta_dict['end_location']
    - meta_dict['motion_location']
    - meta_dict['eucl_distance']


# Contributors
Fabio Ferreira, Jonas Rothfuss, Eren E. Aksoy, You Zhou
