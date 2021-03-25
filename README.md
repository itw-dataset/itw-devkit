# Into The Wilderness Dataset (ITW)


Into The Wilderness (ITW) is a dataset that contains diverse outdoor scenes comprising of high-resolution RGB images with accurate and dense depth measurements, as well as color segmented terrain maps. ITW is the first public dataset to include **RGBD images of completely outdoor and wild scenes obtained with a single RGBD camera**.

Refer to our [dataset sample gallery](https://photos.app.goo.gl/E5tNDDQLNnFhHrjEA)

### Dataset Viewing

The train and test splits of Into The Wilderness are available for viewing, including RGB images, depth maps and terrain segmentation maps.

**Viewing links:**

1. **ITW Depth** (RGB Images, Depth Maps and Depth validity masks):

|     Partition      |                      RGB                      | Depth                                               |             Terrain Segmentation Map             |
| :----------------: | :-------------------------------------------: | :-------------------------------------------------: | :----------------------------------------------: |
|    Train (81GB)    | [train.tar.gz](http://diode-dataset.s3.amazonaws.com/train.tar.gz) | [train.tar.gz](https://pan.baidu.com/s/1Ga9v6jVzyxfu1TUWJzo7mA) | 3a94632398fe1d002d89f11743f748b1 |
|     Test (2.6GB)   | [val.tar.gz](http://diode-dataset.s3.amazonaws.com/val.tar.gz)     | [val.tar.gz](https://pan.baidu.com/s/18IoX7f9W3F7acP0hjl7NSA) | 5c895d09201b88973c8fe4552a67dd85 |

2. **ITW Terrain** (Terrain Segmentation Maps only):

|     Partition      |                      Amazon Web Service                      | Baidu Cloud Storage                                               |             MD5 Hash             |
| :----------------: | :----------------------------------------------------------: | :------------------------------------------------------------: | :------------------------------: |
|    Train (126GB)    | [train_normals.tar.gz](http://diode-dataset.s3.amazonaws.com/train_normals.tar.gz) | [train_normals.tar.gz](https://pan.baidu.com/s/1ngYpSuHSC1rdLXu4edAaKA) | 9c0617ebe1eaf1928fdf3344e1c42aef |
| Validation (4.6GB) | [val_normals.tar.gz](http://diode-dataset.s3.amazonaws.com/val_normals.tar.gz) | [val_normals.tar.gz](https://pan.baidu.com/s/1TLb3hfgK7dAghEOS76ppvg) | 323ccaf60abebdb59705dcd8b529d709 |


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
3. A jupyter-notebook demo showcasing data loading, metadata querying and depth as well as terrain map visualization.
4. A python file for computation of metrics using numpy.
5. A python file for capturing images using the Intel RealSense D415 Camera.

### Contact
If you have any questions, please contact us at [iccv2021submission@gmail.com](iccv2021submission@gmail.com).
