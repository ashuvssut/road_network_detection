import networkx as nx

def zhang_suen_node_detection(skel):
    """
    (from nefi1)
    Node detection based on criteria put forward in "A fast parallel algorithm
    for thinning digital patterns" by T. Y. Zhang and C. Y. Suen. Pixels p of
    the skeleton are categorized as nodes/non-nodes based on the value of a
    function A(p) depending on the pixel neighborhood of p. Please check the
    above paper for details.

    A(p1) == 1: The pixel p1 sits at the end of a skeleton line, thus a node
    of degree 1 has been found.
    A(p1) == 2: The pixel p1 sits in the middel of a skeleton line but not at
    a branching point, thus a node of degree 2 has been found. Such nodes are
    ignored and not introduced to the graph.
    A(p1) >= 3: The pixel p1 belongs to a branching point of a skeleton line,
    thus a node of degree >=3 has been found.

    Args:
        *skel* : Skeletonised source image. The skeleton must be exactly 1
         pixel wide.

    Returns:
        *graph* : networkx Graph object with detected nodes.

    """
    def check_pixel_neighborhood(x, y, skel):
        """
        Check the number of components around a pixel.
        If it is either 1 or more than 3, it is a node.

        Args:
            | *x* : pixel location value
            | *y* : pixel location value
            | *skel* : skeleton Graph object

        Returns:
            *accept_pixel_as_node* : boolean value

        """
        accept_pixel_as_node = False
        item = skel.item
        p2 = item(x - 1, y) / 255
        p3 = item(x - 1, y + 1) / 255
        p4 = item(x, y + 1) / 255
        p5 = item(x + 1, y + 1) / 255
        p6 = item(x + 1, y) / 255
        p7 = item(x + 1, y - 1) / 255
        p8 = item(x, y - 1) / 255
        p9 = item(x - 1, y - 1) / 255

        # The function A(p1),
        # where p1 is the pixel whose neighborhood is beeing checked
        nbs_count = (p2 == 0 and p3 == 1) + (p3 == 0 and p4 == 1) + \
            (p4 == 0 and p5 == 1) + (p5 == 0 and p6 == 1) + \
            (p6 == 0 and p7 == 1) + (p7 == 0 and p8 == 1) + \
            (p8 == 0 and p9 == 1) + (p9 == 0 and p2 == 1)
        if (nbs_count >= 3) or (nbs_count == 1):
            accept_pixel_as_node = True
        return accept_pixel_as_node

    graph = nx.Graph()
    w, h = skel.shape
    item = skel.item
    for x in range(1, w - 1):
        for y in range(1, h - 1):
            if item(x, y) != 0 and check_pixel_neighborhood(x, y, skel):
                graph.add_node((x, y))
    return graph
