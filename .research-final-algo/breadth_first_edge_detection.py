import cv2
import numpy as np
from collections import defaultdict
from itertools import chain


def breadth_first_edge_detection(skel, segmented, graph):
    """
    (from nefi1)
    Detect edges in the skeletonized image.
    Also compute the following edge properties:

        | *pixels* : number of pixels on the edge in the skeleton
        | *length* : length in pixels, horizontal/vertikal steps count 1,
           diagonal steps count sqrt 2
        | *width* : the mean diameter of the edge
        | *width_var* : the variance of the width along the edge

    The runtime is linear in the number of pixels.
    White pixels are **much more** expensive though.
    """
    def neighbors(x, y):
        item = skel.item
        width, height = skel.shape
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                # the line below is ugly and is intended to be this way
                # do not try to modify it unless you know what you're doing
                if (dx != 0 or dy != 0) and \
                        0 <= x + dx < width and \
                        0 <= y + dy < height and \
                        item(x + dx, y + dy) != 0:
                    yield x + dx, y + dy

    def distance_transform_diameter(edge_trace, segmented):
        """
        (dev comments from nefi1)
        my cv2 lacks cv2.DIST_L2, it seems to have the value 2 though, so I use
        that, same for MASK_PRECISE
        <python3 cv2.DIST_L2 equals to 2>
        """
        dt = cv2.distanceTransform(segmented, 2, 0)
        edge_pixels = np.nonzero(edge_trace)
        diameters = defaultdict(list)
        for label, diam in zip(edge_trace[edge_pixels], 2.0 * dt[edge_pixels]):
            diameters[label].append(diam)
        return diameters

    # compute edge length
    # initialize: the neighbor pixels of each node get a distinct label
    # each label gets a queue
    label_node = dict()
    queues = []
    label = 1
    label_length = defaultdict(int)
    for x, y in graph.nodes():
        for a, b in neighbors(x, y):
            label_node[label] = (x, y)
            label_length[label] = 1.414214 if abs(x - a) == 1 and \
                abs(y - b) == 1 else 1
            queues.append((label, (x, y), [(a, b)]))
            label += 1

    # bfs over the white pixels.
    # One phase: every entry in queues is handled
    # Each label grows in every phase.
    # If two labels meet, we have an edge.
    edges = set()
    edge_trace = np.zeros(skel.shape, np.uint32)
    edge_value = edge_trace.item
    edge_set_value = edge_trace.itemset
    label_histogram = defaultdict(int)

    while queues:
        new_queues = []
        for label, (px, py), nbs in queues:
            for (ix, iy) in nbs:
                value = edge_value(ix, iy)
                if value == 0:
                    edge_set_value((ix, iy), label)
                    label_histogram[label] += 1
                    # TODO consider using cv2.arcLength for this
                    label_length[label] += 1.414214 if abs(ix - px) == 1 and \
                        abs(iy - py) == 1 else 1
                    new_queues.append((label, (ix, iy), neighbors(ix, iy)))
                elif value != label:
                    edges.add((min(label, value), max(label, value)))
        queues = new_queues

    # compute edge diameters
    diameters = distance_transform_diameter(edge_trace, segmented)
    # add edges to graph
    for l1, l2 in edges:
        u, v = label_node[l1], label_node[l2]
        if u == v:
            continue
        d1, d2 = diameters[l1], diameters[l2]
        diam = np.fromiter(chain(d1, d2), np.uint, len(d1) + len(d2))
        graph.add_edge(u, v, pixels=label_histogram[l1] + label_histogram[l2],
                       length=label_length[l1] + label_length[l2],
                       width=np.mean(diam),
                       width_var=np.var(diam))
    return graph
