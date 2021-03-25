# Into The Wilderness Dataset (ITW)


Into The Wilderness (ITW) is a dataset that contains diverse wild outdoor scenes comprising of high-resolution RGB images with accurate and dense depth measurements, as well as color segmented terrain maps. ITW is the first public dataset to include **RGBD images of completely outdoor and wild scenes obtained with a single RGBD camera**.

### Dataset Viewing

The train and test splits of Into The Wilderness are available for viewing, including RGB images, depth maps and terrain segmentation maps.

**Viewing links:**

1. **ITW Labelled Combined**

|     Partition      |                      RGB                      | Depth                                               |             Terrain Segmentation Map             |
| :----------------: | :-------------------------------------------: | :-------------------------------------------------: | :----------------------------------------------: |
|    Train (81GB)    | [train_rgb](http://diode-dataset.s3.amazonaws.com/train.tar.gz) | [train_depth](https://pan.baidu.com/s/1Ga9v6jVzyxfu1TUWJzo7mA) | [train_TM](https://pan.baidu.com/s/1Ga9v6jVzyxfu1TUWJzo7mA) |
|     Test (2.6GB)   | [test_rgb](http://diode-dataset.s3.amazonaws.com/val.tar.gz)     | [test_depth](https://pan.baidu.com/s/18IoX7f9W3F7acP0hjl7NSA) | [test_TM](https://pan.baidu.com/s/1Ga9v6jVzyxfu1TUWJzo7mA) |

2. **ITW Raw Depth**


|     Partition      |                      RGB                      |                  Grayscale Depth                    |                    Jet Depth                     |
| :----------------: | :-------------------------------------------: | :-------------------------------------------------: | :----------------------------------------------: |
|    Train (81GB)    | [train_rgb](http://diode-dataset.s3.amazonaws.com/train.tar.gz) | [train_depth](https://pan.baidu.com/s/1Ga9v6jVzyxfu1TUWJzo7mA) | [train_TM](https://pan.baidu.com/s/1Ga9v6jVzyxfu1TUWJzo7mA) |
|     Test (2.6GB)   | [test_rgb](http://diode-dataset.s3.amazonaws.com/val.tar.gz)     | [test_depth](https://pan.baidu.com/s/18IoX7f9W3F7acP0hjl7NSA) | [test_TM](https://pan.baidu.com/s/1Ga9v6jVzyxfu1TUWJzo7mA) |

### Terrain Segmentation Map Color Coding

|     Terrain Class      |                      Color Hex Code                      |
| :--------------------: | :------------------------------------------------------: |
|   Flat Surface    | FFFF00 |
|   Dirt Trail    | FA6404 |
|   Traversable Rocky    | 8D4205 |
|   Sandy Trail    | CC9D33 |
|   Traversable Vegetation    | 8ADA55 |
|   Semi-Traversable Rocky    | D97373 |
|   Semi-Traversable Vegetation    | 467302 |
|   Steps    | 646464 |
|   Non-Traversable Vegetation    | 235945 |
|   Non-Traversable Ditch    | 7A1631 |
|   Obstacle    | D11D05 |
|   Water    | 0D4CFF |
|   Background    | 04F1FA |


### Dataset Layout
ITW data is organized hierarchically. Detailed structure is shown as follows:
![Layout](dataset_layout.png)

### File Naming Conventions and Formats
The dataset consists of RGB images, depth maps and terrain segmentation maps. Their formats are as follows:

  RGB Images (`*.png`): RGB images with a resolution of 1920 × 1080.

  Depth Maps (`*_depth.png`): Depth ground truth with a resolution of 1280 × 720.

  Depth validity masks (`*_depth_mask.npy`): Binary depth validity masks where 1 indicates valid sensor returns and 0 otherwise.
  
  Terrain Segmentation Map (`*_TM.png`): Surface normal vector ground truth with the same resolution as the images. Invalid normals are represented as (0,0,0).

### Devkit
This development toolkit contains:
1. A JSON file that enumerates the data in ITW. The layout of this file is explained in itw.py. It serves as the single point of reference during dataloading.
2. A sample pytorch data loading module.
3. A python file for computation of metrics using numpy.
4. A python file for capturing images using the Intel RealSense D415 Camera.

### Contact
If you have any questions, please contact us at [iccv2021submission@gmail.com](iccv2021submission@gmail.com).
