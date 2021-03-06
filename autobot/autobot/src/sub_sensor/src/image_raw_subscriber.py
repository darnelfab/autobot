#!/usr/bin/env python
# Import ROS libraries and messages
import rospy
from sensor_msgs.msg import Image

# Import OpenCV libraries and tools
import cv2
from cv_bridge import CvBridge, CvBridgeError

# Initialize the ROS Node named 'autobot_camera_node', allow multiple nodes to be run with this name
rospy.init_node('autobot_camera_node', anonymous=True)

# Initialize the CvBridge class
bridge = CvBridge()

# Define a function to show the image in an OpenCV Window
def show_image(img):
    cv2.imshow("Image Window", img)
    cv2.waitKey(3)

# Define a callback for the Image message
def image_callback(img_msg):
    # log some info about the image topic
    rospy.loginfo(img_msg.header)

    # Try to convert the ROS Image message to a CV2 Image
    try:
        cv_image = bridge.imgmsg_to_cv2(img_msg, "passthrough")
    except CvBridgeError, e:
        rospy.logerr("CvBridge Error: {0}".format(e))

      # Flip the image 90deg
        cv_image = cv2.transpose(cv_image)
        cv_image = cv2.flip(cv_image,1)

      # Show the converted image
        show_image(cv_image)

# Initalize a subscriber to the "/camera/rgb/image_raw" topic with the function "image_callback" as a callback
sub_image = rospy.Subscriber("/camera/rgb/image_raw", Image, image_callback)
pub_image = rospy.Publisher("autobot_camera", Image, queue_size=10) #publish linear acc obtained from imu subscriber
rate = rospy.Rate(100) # 100hz

# Initialize an OpenCV Window named "Image Window"
cv2.namedWindow("Image Window", 1)

# Loop to keep the program from shutting down unless ROS is shut down, or CTRL+C is pressed
while not rospy.is_shutdown():

    rospy.spin()
