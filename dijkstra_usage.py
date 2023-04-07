import networkx as nx
import cv2

# draw the shortest path using dijkstra algorithm
def dijkstra_shortest_path(graph, background_image, node1, node2):
  dijkstra_path = nx.dijkstra_path(
      graph, node1, node2, weight='length')

  x = 0
  for i in range(len(dijkstra_path)-1):
      x1, y1 = dijkstra_path[i]
      x2, y2 = dijkstra_path[i+1]
      cv2.line(background_image, (y1, x1), (y2, x2), (0, 0, 255), 2)
      cv2.circle(background_image, (y1, x1), 5, (255, 192, 203), -1)
      if x % 5 == 0:
          cv2.namedWindow('image', cv2.WINDOW_NORMAL)
          # cv2.putText(image_orig, str(dijkstra_path[i]), (y1, x1),
          #             cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 1, cv2.LINE_AA)
          txt = str(dijkstra_path[i])
          cv2.addText(background_image, txt,
                      (y1, x1), "Arial", 20, (255, 0, 0))
      x = x + 1

  lastX, lastY = dijkstra_path[-1]
  cv2.circle(background_image, (lastY, lastX), 5, (255, 192, 203), -1)
  txt = str(dijkstra_path[-1])
  cv2.addText(background_image, txt,
              (lastY, lastX), "Arial", 20, (255, 0, 0))

  return background_image
