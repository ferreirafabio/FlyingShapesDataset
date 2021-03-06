# Simulated Flying Shapes Dataset
The dataset consists of 90 000 grayscale videos that show two objects of equal shape and size in which one object approaches the other one. The object speed during the process of approaching is hereby modeled by a proportional-derivative controller. Overall, three different shapes (Rectangle, Triangle and Circle) are provided. Initial conﬁguration of the objects such as position and color were randomly sampled. Different from the moving MNIST dataset, the samples comprise a goal-oriented task, namely one object has to fully cover the other object rather than randomly moving, making it better suitable for testing prediction capabilities of an ML model.

For instance, one can use it as a toy dataset to investigate the capacity and output behavior of a deep neural network before testing it on real-world data. We have done this for a deep auto-encoder network:

![Square](/examples/000618_original_square.gif)
![Circle](/examples/001483_original_circle.gif)
![Triangle](/examples/007033_original_triangle.gif)  
![Square](/examples/000618_generated_square.gif)
![Circle](/examples/001483_generated_circle.gif)
![Triangle](/examples/007033_original_triangle.gif)

To accesss a similar dataset see [Simulated Planar Manipulator Dataset](https://github.com/ferreirafabio/PlanarManipulatorDataset)

# Download
Automatically download the data by using the included scripts:
- ```python download_videos.py``` (.tar files ~1.3GB, uncompressed ~23GB) or 
- ```python download_tfrecords.py``` for the tfrecords respectively (~89 GB)

or manually download them by invoking the download links in the files
- ```flyingshapes_videos.txt```
- ```flyingshapes_tfrecords.txt```

# Citing
If you use the dataset in your research, you should cite it as follows:

```
@misc{npde2018,
    author = {Fabio Ferreira, Jonas Rothfuss, Eren E. Aksoy, You Zhou, Tamim Asfour},
    title = {Introducing the Simulated Flying Shapes and Simulated Planar Manipulator Datasets},
    year = {2018},
    publisher = {arXiv},
    publication = {eprint arXiv:1807.00703},
    howpublished = {\url{https://arxiv.org/abs/1807.00703v1}},
}
```

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
The tfrecord files have been created with the pip package \texttt{video2tfrecord} and each file contains 1000 videos.
Due to the high computational cost of processing all original video frames in deep neural networks, we decided to reduce the number of extracted frames for the tfrecord files. As a result, every single tfrecord file entry consists of 10 RGB frames which were taken equally distributed over the video playtime. Assuming no prior knowledge about the video and its inherent scene dynamics, choosing frames equally spaced maximizes the chances of capturing most of the spatio-temporal dynamics. The files store both the videos itself and meta information from the file name (start location, eucl. distance etc.). The video data is stored in a ```feature``` dict (which is serialized as ```tf.train.Example```) which stores the following keys 
- feature[path] ('blob' + '/' + str(imageCount)
- feature['height']
- feature['width']
- feature['depth']
- feature['id']

Additional information is stored in a ```meta_dict``` (which is also serialized within the feature dict via the key 'metadata')
- meta_dict['shape']
- meta_dict['start_location']
- meta_dict['end_location']
- meta_dict['motion_location']
- meta_dict['eucl_distance']
