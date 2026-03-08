# gds_utils.py

import numpy as np
import torch
import gdstk
from matplotlib.path import Path

def load_gds_layers(filepath):
    lib = gdstk.read_gds(filepath)
    cell = lib.top_level()[0]
    layers = sorted(set([p.layer for p in cell.polygons]))
    return cell, layers

def rasterize(cell, layer, resolution):
    polys = [p for p in cell.polygons if p.layer == layer]
    if len(polys) == 0:
        return None
    (xmin, ymin), (xmax, ymax) = cell.bounding_box()

    img = np.zeros((resolution, resolution))
    xs = np.linspace(xmin, xmax, resolution)
    ys = np.linspace(ymin, ymax, resolution)

    XX, YY = np.meshgrid(xs, ys, indexing="ij")
    points = np.vstack((XX.flatten(), YY.flatten())).T

    for poly in polys:
        vertices = np.array(poly.points)
        path = Path(vertices)
        mask = path.contains_points(points)
        img += mask.reshape(resolution, resolution)

    img = (img > 0).astype(np.float32)
    return torch.tensor(img)