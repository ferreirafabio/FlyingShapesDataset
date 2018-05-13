# Description
The dataset consists of 90 000 videos that show two objects of equal shape and size in which one object approaches the other one. The object speed during the process of approaching is hereby modelled by a proportional-derivative controller. Overall, three different shapes (Rectangle, Triangle and Circle) are provided. Initial conﬁguration of the objects such as position and color were randomly sampled. Different from the moving MNIST dataset, the samples comprise a goal-oriented task, namely one object has to fully cover the other object rather than random moving behavior, making it better suitable for testing prediction capabilities of an ML model.

For instance, one can use this dataset as a toy dataset to test the capacity and output behaviour of a deep neural network before addressing real-world data as we have done with a deep auto-encoder:

![Square](https://github.com/ferreirafabio/FlyingShapesDataset/blob/master/examples/000618_original_square.gif)
![Circle](https://github.com/ferreirafabio/FlyingShapesDataset/blob/master/examples/001483_original_circle.gif)
![Triangle](https://github.com/ferreirafabio/FlyingShapesDataset/blob/master/examples/007033_original_triangle.gif)  
![Square](https://github.com/ferreirafabio/FlyingShapesDataset/blob/master/examples/000618_generated_square.gif)
![Circle](https://github.com/ferreirafabio/FlyingShapesDataset/blob/master/examples/001483_generated_circle.gif)
![Triangle](https://github.com/ferreirafabio/FlyingShapesDataset/blob/master/examples/007033_original_triangle.gif)

# Specifications
We provide both the videos as .avi files as well as TensorFlow tfrecord files. The samples in the tfrecord files contain 10 frames of the original video which were taken equally distributed over the entire playtime. Here are some more details:
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


# Contributors
Fabio Ferreira, Jonas Rothfuss, Eren E. Aksoy, You Zhou
