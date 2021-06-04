#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Imu
from geometry_msgs.msg import Vector3

imu0_acc_data_var = Vector3() #defines a imu linear acc global variable of type Vector3
imu0_angvel_data_var = Vector3() #defines a imu linear angular velocity global variable of type Vector3
#define linear_acceleration message 
def imucallback(msg):
    global imu0_acc_data_var
    global imu0_angvel_data_var 
    rospy.loginfo("imu Linear_acc %s", msg.linear_acceleration)#subscribe linear acc sensor message
    imu0_acc_data_var = msg.linear_acceleration
    rospy.loginfo("imu angular_velocity %s", msg.angular_velocity)#subscribe angular velocity sensor message
    imu0_angvel_data_var = msg.angular_velocity
def listener():
    rospy.init_node('listener', anonymous=True)#initialise subscriber 
    #linear acceleration
    rospy.Subscriber("/imu0", Imu, imucallback) #subscribe to imu sensor
    pub = rospy.Publisher('imu0_acc_data', Vector3, queue_size=10) #publish linear acc obtained from imu subscriber
    #angular velocity
    pub = rospy.Publisher('imu0_angvel_data', Vector3, queue_size=10) #publish angular velocity obtained from imu subscriber
    rate = rospy.Rate(100) # 100hz
    while not rospy.is_shutdown():
        pub.publish(imu0_acc_data_var)
        pub.publish(imu0_angvel_data_var)
        rate.sleep()
    rospy.spin()


if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass


