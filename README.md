# Text to Photomosaic

This repository is associated with the work of the same name in the context of the CS-413 EPFL course "Computational Photography". 
It presents our approach to create photomosaics based on natural language input, first by creating the mosaic itself, than filling the generated mosaic with corresponding images.

## How to run (IMPORTANT)

This project is meant to run on Google Colab, not only for the hardware used but also because of some installation difficulties when trying to run it locally.

The notebook to run is called "Photomosaic.ipynb", and you need to follow the instructions on top of the notebook to be able to run it, as well as follow the short tutorial for the images in the next paragraph.

## Images for the photomosaic part

In order to be able to run the photomosaic part, you are going to need to do some manipulations on your Google Drive account. There are two datasets of images that are shared via links, and for both these datasets, you have to add a shortcut to that folder in the root of your Google Drive. The process is describe in the images "Step x" below.

Links to the datasets:

Cats: https://drive.google.com/drive/folders/1k4bR0nhJSBcqVH23JKRorbFj0wtuqAgY?usp=sharing

Imagenet mini: https://drive.google.com/drive/folders/18k6vgz4U-FGjL4NP9eJkc2gn5J3a87nV?usp=sharing

[Step 1](https://github.com/AttiaYoussef/PhotomosaicProject/blob/main/step1.jpg?raw=true)

[Step 2](https://github.com/AttiaYoussef/PhotomosaicProject/blob/main/step2.png?raw=true)

## Files

### Photomosaic.ipynb 

The main notebook of this project. Has to be ran on Google Colab. When running it, please follow the instructions at the top of the notebook (i.e restarting the kernel after running the "Pre installation cell")

### helpers.py

Script of helper functions, most notably contains the custom penalties that we defined.

### imagenet_colors.json 

Contains for each image from the training set of the "Imagenet mini" dataset, the mean RGB values of the left of the image and of its right

### cats_colors.json 

Contains for each image from the cat part of the "Dog & Cat" dataset, the mean RGB values of the left of the image and of its right

## Authors

@AttiaYoussef

@TorgemanTarak

@iserenko
## References

Li, Tzu-Mao, et al. "Differentiable vector graphics rasterization for editing and learning." ACM Transactions on Graphics (TOG) 39.6 (2020): 1-15, [PDF](https://people.csail.mit.edu/tzumao/diffvg/diffvg.pdf).

---
Radford, Alec, et al. "Learning transferable visual models from natural language supervision." International conference on machine learning. PMLR, 2021, [PDF](https://arxiv.org/pdf/2103.00020.pdf)

---

Frans, Kevin, Lisa Soros, and Olaf Witkowski. "Clipdraw: Exploring text-to-drawing synthesis through language-image encoders." Advances in Neural Information Processing Systems 35 (2022): 5207-5218, [PDF](https://arxiv.org/pdf/2106.14843.pdf)