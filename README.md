## :) PanoStitch - Seamless panoramic stitching
---

## * Introduction *

Panorama is prevalent in camera software of smartphones. It is a method in which we first take a number of images, and then stitch them together to form a bigger and combined image, with significantly larger horizon.
- This project seamlessly stitches multiple overlapping images into a single panoramic image.
- Utilizing computer vision techniques such as SIFT, Homography estimation, RANSAC, and weighted blending, this project offers an efficient solution for panoramic image creation.
- By titching multiple images using `recursion`, a wider panorama can be obtained.

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
   ```sh
   !pip install -r requirements.txt
   

4. #### Add your custom images to the `input_img/` folder manually or using the command line:
    ```sh
    mv left.jpg middle.jpg right.jpg inputs/
    ```
   I have provided some images in the [input_img](https://github.com/shifs999/PanoStitch/tree/main/input_img) folder for trial purposes.

*Note:* Ensure that images have overlapping regions and the sequence of images must be ordered `left to right` from the viewing point. So, in order to get desired panorama image, please name and insert the images in correct order for the model to grasp the order lexograpically.


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
   
   <img src = "https://github.com/shifs999/PanoStitch/blob/main/input_img/pano_test/left.jpg" height="300" width="450"/>
   
   #### Image 2
   
   <img src = "https://github.com/shifs999/PanoStitch/blob/main/input_img/pano_test/right.jpg" height="300" width="450"/>

 ### 2. Mapped Image

   <img src = "https://github.com/shifs999/PanoStitch/blob/main/outputs/pano_test/mapped.jpg" height="300" width="500">

 ### 3. Stitched Image (Output)
   <img src = "https://github.com/shifs999/PanoStitch/blob/main/outputs/pano_test/panorama.jpg" height="300" width="500"/>

---

 ### 1. Input Images (Test 2)
   #### Image 1
   
   <img src = "https://github.com/shifs999/PanoStitch/blob/main/pano_test_img/mt_1.jpg" height="300" width="450"/>
   
   #### Image 2
   
   <img src = "https://github.com/shifs999/PanoStitch/blob/main/pano_test_img/mt_2.jpg" height="300" width="450"/>

 ### 2. Mapped Image

   <img src = "https://github.com/shifs999/PanoStitch/blob/main/my_pano_results/mt_mapped.jpg" height="300" width="500">

 ### 3. Stitched Image (Output)
   <img src = "https://github.com/shifs999/PanoStitch/blob/main/my_pano_results/mt_panorama.jpg" height="300" width="500"/>

---

 ### 1. Input Images (Test 3)
   #### Image 1
   
   <img src = "https://github.com/shifs999/PanoStitch/blob/main/pano_test_img/offc_left.jpg" height="300" width="450"/>
   
   #### Image 2
   
   <img src = "https://github.com/shifs999/PanoStitch/blob/main/pano_test_img/offc_right.jpg" height="300" width="450"/>

 ### 2. Mapped Image

   <img src = "https://github.com/shifs999/PanoStitch/blob/main/my_pano_results/offc_mapped.jpg" height="300" width="500">

 ### 3. Stitched Image (Output)
   <img src = "https://github.com/shifs999/PanoStitch/blob/main/my_pano_results/offc_panorama.jpg" height="300" width="500"/>

---

## References

- [First Principles of Computer Vision - Shree K. Nayar](https://fpcv.cs.columbia.edu/)
- https://github.com/OpenStitching/stitching.git
- [Distinctive Image Features from Scale-Invariant Keypoints(SIFT) Paper](https://people.eecs.berkeley.edu/~malik/cs294/lowe-ijcv04.pdf)

---


## Contributions 

Pull requests are welcome. For major changes, please open an issue first to discuss what you'd like to change.

---

## Contact

For any queries or collaborations, feel free to reach me out at **saizen777999@gmail.com**
