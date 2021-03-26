# Into The Wilderness Dataset (ITW)
Into The Wilderness (ITW) is a dataset that contains diverse wild outdoor scenes comprising of high-resolution RGB images with accurate and dense depth measurements, as well as color segmented terrain maps. ITW is the first public dataset to include **RGB-D images of completely outdoor and wild scenes obtained with a single RGBD camera**.

- [1. Dataset Viewing](#1-dataset-viewing)
  - [1.1. Viewing links](#11-viewing-links)
  - [1.2. Terrain Segmentation Map Color Coding](#12-terrain-segmentation-map-color-coding)
- [2. Dataset Layout](#2-dataset-layout)
- [3. File Naming Conventions and Formats](#3-file-naming-conventions-and-formats)
- [4. DevKit](#4-devkit)
- [5. Contact](#5-contact)

## 1. Dataset Viewing

The train and test splits of Into The Wilderness are available for viewing, including RGB images, depth maps and terrain segmentation maps.

### 1.1. Viewing links

1. ITW Labelled Combined  

    |     Partition      |                      RGB                      | Depth                                               |             Terrain Segmentation Map             |
    | :----------------: | :-------------------------------------------: | :-------------------------------------------------: | :----------------------------------------------: |
    |    Train (81GB)    | [train_rgb](http://diode-dataset.s3.amazonaws.com/train.tar.gz) | [train_depth](https://pan.baidu.com/s/1Ga9v6jVzyxfu1TUWJzo7mA) | [train_TM](https://pan.baidu.com/s/1Ga9v6jVzyxfu1TUWJzo7mA) |
    |     Test (2.6GB)   | [test_rgb](http://diode-dataset.s3.amazonaws.com/val.tar.gz)     | [test_depth](https://pan.baidu.com/s/18IoX7f9W3F7acP0hjl7NSA) | [test_TM](https://pan.baidu.com/s/1Ga9v6jVzyxfu1TUWJzo7mA) |

2. ITW Raw Depth

    |     Partition      |                      RGB                      |                  Grayscale Depth                    |                    Jet Depth                     |
    | :----------------: | :-------------------------------------------: | :-------------------------------------------------: | :----------------------------------------------: |
    |    Train (81GB)    | [train_rgb](http://diode-dataset.s3.amazonaws.com/train.tar.gz) | [train_depth](https://pan.baidu.com/s/1Ga9v6jVzyxfu1TUWJzo7mA) | [train_TM](https://pan.baidu.com/s/1Ga9v6jVzyxfu1TUWJzo7mA) |
    |     Test (2.6GB)   | [test_rgb](http://diode-dataset.s3.amazonaws.com/val.tar.gz)     | [test_depth](https://pan.baidu.com/s/18IoX7f9W3F7acP0hjl7NSA) | [test_TM](https://pan.baidu.com/s/1Ga9v6jVzyxfu1TUWJzo7mA) |

### 1.2. Terrain Segmentation Map Color Coding

| Color Hex Code | Terrain Class |
| :-: | :-: |
| ![#FFFF00](https://via.placeholder.com/15/FFFF00/000000?text=+) `#FFFF00` | Flat Surface |  
| ![#FA6404](https://via.placeholder.com/15/FA6404/000000?text=+) `#FA6404` | Dirt Trail |  
| ![#8D4205](https://via.placeholder.com/15/8D4205/000000?text=+) `#8D4205` | Traversable Rocky |  
| ![#CC9D33](https://via.placeholder.com/15/CC9D33/000000?text=+) `#CC9D33` | Sandy Trail |  
| ![#8ADA55](https://via.placeholder.com/15/8ADA55/000000?text=+) `#8ADA55` | Traversable Vegetation |  
| ![#D97373](https://via.placeholder.com/15/D97373/000000?text=+) `#D97373` | Semi-Traversable Rocky |  
| ![#467302](https://via.placeholder.com/15/467302/000000?text=+) `#467302` | Semi-Traversable Vegetation |  
| ![#646464](https://via.placeholder.com/15/646464/000000?text=+) `#646464` | Steps |  
| ![#235945](https://via.placeholder.com/15/235945/000000?text=+) `#235945` | Non-Traversable Vegetation |  
| ![#7A1631](https://via.placeholder.com/15/7A1631/000000?text=+) `#7A1631` | Non-Traversable Ditch |  
| ![#D11D05](https://via.placeholder.com/15/D11D05/000000?text=+) `#D11D05` | Obstacle |  
| ![#0D4CFF](https://via.placeholder.com/15/0D4CFF/000000?text=+) `#0D4CFF` | Water |  
| ![#04F1FA](https://via.placeholder.com/15/04F1FA/000000?text=+) `#04F1FA` | Background |  


## 2. Dataset Layout
ITW data is organized hierarchically. Detailed structure is shown as follows:
![Layout](dataset_layout.png)

## 3. File Naming Conventions and Formats
The dataset consists of RGB images, depth maps and terrain segmentation maps. Their formats are as follows:
- **RGB Images `(*.png)` :** RGB images with a resolution of `1920*1080`
- **Depth Maps `(*_depth.png)` :** Depth ground truth with a resolution of `1280*720`
- **Depth validity masks `(*_depth_mask.npy)` :** Binary depth validity masks (1 indicates valid sensor returns and 0 otherwise)
- **Terrain Segmentation Map `(*_TM.png)` :** Surface normal vector ground truth with the same resolution as the images (Invalid normals are represented as `(0,0,0)`)

## 4. DevKit
This development toolkit contains:
1. A JSON file that enumerates the data in ITW. The layout of this file is explained in itw.py. It serves as the single point of reference during dataloading.
2. A sample pytorch data loading module.
3. A python file for computation of metrics using numpy.
4. A python file for capturing images using the Intel RealSense D415 Camera.

## 5. Contact
If you have any questions, please contact us at [iccv2021submission@gmail.com](iccv2021submission@gmail.com).
