import torch
import numpy as np
import pandas as pd
import pydiffvg
import torch.nn.functional as F




def check_colinear(v, w): # check whether or not two vectors are colinear, useful to force a parallelogram
  return torch.abs((torch.norm(v) * torch.norm(w)) - torch.dot(v,w)) < 1e-12

def vectors_angle_cos(v,w): #computes the cosinus of the angle between vectors v and w
  return torch.dot(v,w)/(torch.norm(v) * torch.norm(w))


def create_polygon_from_center_and_orientation(center, angle, width, factor):
  """
    Creates, using a center and an angle, a polygon representing a square with that center and rotated by that angle

    center: a tensor, the center of the square
    angle: a tensor(float), the angle by which the square is turned
    width: int, the width of the canvas
    factor: float, the length of one diagonal of the square
  """
  factor = factor
  rotationMatrix = torch.zeros(2,2)
  rotationMatrix[0][0] = torch.cos(angle)
  rotationMatrix[0][1] = -torch.sin(angle)
  rotationMatrix[1][0] = torch.sin(angle)
  rotationMatrix[1][1] = torch.cos(angle)

  p1 = center  + (torch.tensor([-1,-1]) * factor) @ rotationMatrix
  p2 = center + (torch.tensor([1,-1])  * factor) @ rotationMatrix
  p3 = center + (torch.tensor([1,1])  * factor) @ rotationMatrix
  p4 = center + (torch.tensor([-1,1])   * factor) @ rotationMatrix

  points = torch.cat([p1, p2, p3, p4], dim = 0) * width
  return pydiffvg.Polygon(points = points, is_closed = True)



def centers_penalization(centers, threshold_distance):
  """
  center1: tensor corresponding to a given center
  other_centers: tensor containing all centers except center1
  threshold_distance: float over which the distance is not penalized, under which it is

  Penalizes the distance between centers to avoid overlapping of squares. It is done as:
  1) If the distance between two centers is big, it is not taken into account into penalization
  2) Otherwise it is, like some kind of reverse ReLU
  """
  final = 0
  for i, center1 in enumerate(centers):
      other_centers = torch.stack(centers[:i] + centers[i+1:])
      distances = torch.norm(center1 - other_centers, dim = 2) 
      distances_2 = F.relu(threshold_distance - distances) #This way, if a distance > threshold, then thershold - distance < 0 and relu will discard it, while still being able to compute grad
      distances_3 = torch.pow(distances_2, 2)
      final += distances_3.sum()
  return final


def penalizing_empty_space(centers):
  """ 
  applies the penalization of empty space, i.e the L = max(min(|| ci - cj||**2)), as per the TA's suggestion
  will also try the L = min(max(|| ci - cj||**2))
  
  """
  distances = torch.zeros(len(centers))
  for i in range(len(centers)):
      center = centers[i]
      tmp = torch.stack(centers[:i] + centers[i+1:]) #all centers except the current iteration
      tmp = torch.norm(center - tmp, dim = 2)
      min_distance = tmp.min()
      distances[i] = min_distance
  return distances.max()



def save_images_main_colors(tile_photos_path, all_paths = False, image_format = 'jpg', tiles_path = "./cats_colors.json"):
    """
    Method that is launched only once by us to save the images from either the Imagenet-Mini or the Dogs & Cats 
    dataset
    Do not launch it again
    """
    tiles_data = {}
    i = 0
    print("Saving images")
    if all_paths:
        for file in tile_photos_path:
            if i % 1000 == 0:
                print("Iteration {0}".format(i))
      
            tile = np.array(PIL.Image.open(file))
            left_color = tile[:,:15].mean(axis = 0).mean(axis = 0)/255
            right_color = tile[:][-16:-1].mean(axis = 0).mean(axis = 0)/255
            tiles_data[file] = [left_color.tolist(), right_color.tolist()]
            i+=1
    
        with open(tiles_path, 'w') as f:
            json.dump(tiles_data, f)
    else:

        for file in glob.glob(tile_photos_path + "/*.{0}".format(image_format)):
      #print(file)
            if i % 1000 == 0:
                print("Iteration {0}".format(i))
      
            tile = np.array(PIL.Image.open(file))
            left_color = tile[:,:15].mean(axis = 0).mean(axis = 0)/255
            right_color = tile[:][-16:-1].mean(axis = 0).mean(axis = 0)/255
            tiles_data[file] = [left_color.tolist(), right_color.tolist()]
            i+=1

        with open(tiles_path, 'w') as f:
            json.dump(tiles_data, f)