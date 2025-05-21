## :) PanoStitch
---

## Introduction

Panorama is prevalent in camera software of smartphones. It is a method in which we first take a number of images, and then stitch them together to form a bigger and combined image, with significantly larger horizon.
- This project seamlessly stitches multiple overlapping images into a single panoramic image.
- Utilizing computer vision techniques such as SIFT, Homography estimation, RANSAC, and weighted blending, this project offers an efficient solution for panoramic image creation.

- ## Try it out


1. #### Clone and cd to the repository:

    ```sh
    git clone https://github.com/shifs999/PanoStitch.git
    cd PanoStitch
     ```


2. #### Create and activate the conda environment:

    ```sh
    conda env create -f environment.yml
    conda activate panorama
    ```
    
   ** Install the requirements.txt file.
   

3. #### Add your custom images to the `input_img/` folder manually or using the command line:
    ```sh
    mv left.jpg middle.jpg right.jpg inputs/
    ```
   I have provided some images in the [input_img](https://github.com/shifs999/PanoStitch/tree/main/input_img) folder for trial purposes.

`Alert:` The sequence of images should be ordered `left to right` from the viewing point. So, in order to get desired panorama image, please name and insert the images in correct order for the model to grasp the order lexograpicaly.


5. #### Run the script
    Can provide the path to each file(in order)
    ```sh
    python panorama.py input_img/pano_test/left.jpg input_img/pano_test/right.jpg
    ```
    or provide the entire folder
    ```sh
    python panorama.py input_img/
    ```
6. #### Output

   ```sh
   Initializing...
   Images that will be stitched (in order):
   input_img\pano_test\left.jpg
   input_img\pano_test\right.jpg
   Saved to outputs\pano_test/
   ```

- The above output will be stored in the folder [outputs/pano_test](https://github.com/shifs999/PanoStitch/tree/main/outputs/pano_test)
---
## Results

 ### 1. Input Images (Test 1)
   #### Image 1
   
   <img src = "https://github.com/shifs999/PanoStitch/blob/main/input_img/pano_test/left.jpg" width="400"/>
   
   #### Image 2
   
   <img src = "https://github.com/shifs999/PanoStitch/blob/main/input_img/pano_test/right.jpg" width="400"/>

 ### 2. Mapped Image

   <img src = "https://github.com/shifs999/PanoStitch/blob/main/outputs/pano_test/mapped.jpg" height="300" width="400">

 ### 3. Stitched Image (Output)
   <img src = "https://github.com/shifs999/PanoStitch/blob/main/outputs/pano_test/panorama.jpg" height="300" width="400"/>


 ### 1. Input Images (Test 2)
   #### Image 1
   
   <img src = "https://github.com/shifs999/PanoStitch/blob/main/pano_test_img/mt_1.jpg" width="500"/>
   
   #### Image 2
   
   <img src = "https://github.com/shifs999/PanoStitch/blob/main/pano_test_img/mt_2.jpg" width="500"/>

 ### 2. Mapped Image

   <img src = "https://github.com/shifs999/PanoStitch/blob/main/my_pano_results/mt_mapped.jpg" height="350" width="500">

 ### 3. Stitched Image (Output)
   <img src = "https://github.com/shifs999/PanoStitch/blob/main/my_pano_results/mt_panorama.jpg" height="350" width="500"/>


 ### 1. Input Images (Test 3)
   #### Image 1
   
   <img src = "https://github.com/shifs999/PanoStitch/blob/main/pano_test_img/offc_left.jpg" height="350" width="500"/>
   
   #### Image 2
   
   <img src = "https://github.com/shifs999/PanoStitch/blob/main/pano_test_img/offc_right.jpg" height="350" width="500"/>

 ### 2. Mapped Image

   <img src = "https://github.com/shifs999/PanoStitch/blob/main/my_pano_results/offc_mapped.jpg" height="350" width="500">

 ### 3. Stitched Image (Output)
   <img src = "https://github.com/shifs999/PanoStitch/blob/main/my_pano_results/offc_panorama.jpg" height="350" width="500"/>
