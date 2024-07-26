import cv2
import numpy as np

# Load and resize the image
image = cv2.imread("scan_test2.jpg")
image = cv2.resize(image, (0, 0), None, 0.6, 0.6)

pts = []
count = 0

def mouseclick(event, x, y, flags, param):
    global count
    if event == cv2.EVENT_LBUTTONDOWN:
        pts.append((x, y))
        print(f"pts no: {count}")
        count += 1

# Set the mouse callback function
cv2.namedWindow("Input Image")
cv2.setMouseCallback("Input Image", mouseclick)

# to negotiate the order or clicking either clk or antclk we have to form a function which takes input a list of tuples and then return pts in order 
def reorder(tuples_list):
    # Convert the list of tuples to a NumPy array
    array = np.array(tuples_list)
    
    # Calculate the sum and difference of the numbers in each tuple
    sums = np.sum(array, axis=1)
    differences = array[:, 0] - array[:, 1]
    
    # Identify corner points
    top_left = tuples_list[np.argmin(sums)]
    bottom_right = tuples_list[np.argmax(sums)]
    top_right = tuples_list[np.argmax(differences)]
    bottom_left = tuples_list[np.argmin(differences)]
    
    # Return the corner points in the specified order
    return [top_left, top_right, bottom_right, bottom_left]


while True:
    
    if count == 4:
        pts=reorder(pts)
        height, width = 500, 500
        pts1 = np.float32([pts[0], pts[1], pts[2], pts[3]])
        pts2 = np.float32([[0, 0], [width, 0], [width, height], [0, height]])
        matrix = cv2.getPerspectiveTransform(pts1, pts2)
        output = cv2.warpPerspective(image, matrix, (width, height))
        cv2.imshow("Final Output Image", output)
    
    # Draw circles at the clicked points
    for x in range(len(pts)):
        cv2.circle(image, (pts[x][0], pts[x][1]), 3, (0, 255, 255), -1)
    
    cv2.imshow("Input Image", image)
    
    
    if cv2.waitKey(1) & 0xFF == ord('1'):
        break

cv2.destroyAllWindows()
