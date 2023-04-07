import cv2

NODESIZERADIUS = 1
STROKEWIDTH = 1

def draw_graph(image, graph):
    """
    Draw the graph on the image by traversing the graph structure.

    Args:
        | *image* : the image where the graph needs to be drawn
        | *graph* : the graph information

    Returns:
        The image with the graph drawn on it
    """
    tmp = draw_edges(image, graph, (0, 0, 255), 1)
    return draw_nodes(tmp, graph, NODESIZERADIUS)


def draw_nodes(img, graph, radius=NODESIZERADIUS):
    """
    Draw all nodes on the input image.

    Args:
        | *img* : Input image where nodes are drawn
        | *graph* : Input graph containing the nodes

    Kwargs:
        | *radius* : Radius of drawn nodes

    Returns:
        Input image img with nodes drawn into it
    """
    
    for x, y in graph.nodes():
        cv2.rectangle(img, (y - radius, x - radius), (y + radius, x + radius),
                      (255, 0, 0), -1)
        # cv2.namedWindow('image', cv2.WINDOW_NORMAL)
        # cv2.addText(img, str(x) + "," + str(y), (y, x), "Arial", 10, (255, 0, 0))
    return img


def draw_edges(img, graph, col=(0, 0, 255), stoke_width=STROKEWIDTH):
    """
    Draw network edges on the input image.

    Args:
        | *img* : Input image where edges are drawn
        | *graph* : Input graph containing the edges
    Kwargs:
        | *col* : colour for drawing
        | *stoke_width* : width of the stroke

    Returns:
        Input image img with nodes drawn into it
    """

    for (x1, y1), (x2, y2) in graph.edges():
        start = (y1, x1)
        end = (y2, x2)

        cv2.line(img, start, end, col, stoke_width)

    return img
