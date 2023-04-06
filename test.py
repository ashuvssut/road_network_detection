import numpy as np
import matplotlib.pyplot as plt
import cv2
image = cv2.imread("./z-output/skeleton.png")

# display image
# cv2.imshow("image", image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

plt.imshow(image)
plt.show()
