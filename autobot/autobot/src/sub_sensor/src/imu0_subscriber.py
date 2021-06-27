#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Imu
from geometry_msgs.msg import Vector3
from geometry_msgs.msg import AccelWithCovariance

imu0_acc_data_var = Vector3() #defines a imu0 linear acc global variable of type Vector3
imu0_angvel_data_var = Vector3() #defines a imu0 linear angular velocity global variable of type Vector3
#imu0_linear_acc_cov = float64[9] #defines a imu0 linear acc covariance mat global variable of type float64[9]
#imu0_angvel_cov = float64[9] #defines a imu0 linear acc covariance mat global variable of type float64[9]

imu1_acc_data_var = Vector3() #defines a imu1 linear acc global variable of type Vector3
imu1_angvel_data_var = Vector3() #defines a imu1 linear angular velocity global variable of type Vector3
#imu1_linear_acc_cov = float64[9] #defines a imu0 linear acc covariance mat global variable of type float64[9]
#imu1_angvel_cov = float64[9] #defines a imu0 linear acc covariance mat global variable of type float64[9]

imu2_acc_data_var = Vector3() #defines a imu2 linear acc global variable of type Vector3
imu2_angvel_data_var = Vector3() #defines a imu2 linear angular velocity global variable of type Vector3
#imu2_linear_acc_cov = float64[9] #defines a imu0 linear acc covariance mat global variable of type float64[9]
#imu2_angvel_cov = float64[9] #defines a imu0 linear acc covariance mat global variable of type float64[9]

#define linear_acceleration message 
def imucallback(msg):
    #imu0 global variable
    global imu0_acc_data_var
    global imu0_angvel_data_var
    #global imu0_linear_acc_cov_var
    #global imu0_angvel_cov_var    
    #imu0 subscriber
    rospy.loginfo("imu0 Linear_acc %s", msg.linear_acceleration)#subscribe linear acc sensor message
    imu0_acc_data_var = msg.linear_acceleration
    rospy.loginfo("imu0 angular_velocity %s", msg.angular_velocity)#subscribe angular velocity sensor message
    imu0_angvel_data_var = msg.angular_velocity
    #rospy.loginfo("imu0 Linear_acc_cov %s", msg.linear_acceleration_covariance)#subscribe linear acc cov sensor message
    #imu0_linear_acc_cov_var = msg.linear_acceleration_covariance
    #rospy.loginfo("imu0 angular_velocity_cov %s", msg.angular_velocity_covariance)#subscribe angular velocity cov sensor message
    #imu0_angvel_data_var = msg.angular_velocity_covariance

    #imu1 global variable
    global imu1_acc_data_var
    global imu1_angvel_data_var 
    #global imu1_linear_acc_cov
    #global imu1_angvel_cov 
    rospy.loginfo("imu1 Linear_acc %s", msg.linear_acceleration)#subscribe linear acc sensor message
    imu1_acc_data_var = msg.linear_acceleration
    rospy.loginfo("imu1 angular_velocity %s", msg.angular_velocity)#subscribe angular velocity sensor message
    imu1_angvel_data_var = msg.angular_velocity
    #rospy.loginfo("imu1 Linear_acc_cov %s", msg.linear_acceleration_covariance)#subscribe linear acc cov sensor message
    #imu1_linear_acc_cov_var = msg.linear_acceleration_covariance
    #rospy.loginfo("imu1 angular_velocity_cov %s", msg.angular_velocity_covariance)#subscribe angular velocity cov sensor message
    #imu1_angvel_data_var = msg.angular_velocity_covariance

    #imu2 global variable
    global imu2_acc_data_var
    global imu2_angvel_data_var 
    #global imu2_linear_acc_cov
    #global imu2_angvel_cov 
    rospy.loginfo("imu2 Linear_acc %s", msg.linear_acceleration)#subscribe linear acc sensor message
    imu2_acc_data_var = msg.linear_acceleration
    rospy.loginfo("imu2 angular_velocity %s", msg.angular_velocity)#subscribe angular velocity sensor message
    imu2_angvel_data_var = msg.angular_velocity
    #rospy.loginfo("imu2 Linear_acc_cov %s", msg.linear_acceleration_covariance)#subscribe linear acc cov sensor message
    #imu2_linear_acc_cov_var = msg.linear_acceleration_covariance
    #rospy.loginfo("imu2 angular_velocity_cov %s", msg.angular_velocity_covariance)#subscribe angular velocity cov sensor message
    #imu2_angvel_data_var = msg.angular_velocity_covariance

def listener():
    rospy.init_node('listener', anonymous=True)#initialise subscriber 
    #linear acceleration
    rospy.Subscriber("/imu0", Imu, imucallback) #subscribe to imu sensor
    pub = rospy.Publisher('imu0_acc_data', Vector3, queue_size=10) #publish linear acc obtained from imu subscriber
    #angular velocity
    pub = rospy.Publisher('imu0_angvel_data', Vector3, queue_size=10) #publish angular velocity obtained from imu subscriber
    #linear acceleration cov
    #rospy.Subscriber("/imu0", Imu, imucallback) #subscribe to imu sensor
    #pub = rospy.Publisher('imu0_acc_cov_data', float64[9], queue_size=10) #publish linear acc obtained from imu subscriber
    #angular velocity cov
    #pub = rospy.Publisher('imu0_angvel_cov_data', float64[9], queue_size=10) #publish angular velocity obtained from imu subscriber
    #rate = rospy.Rate(100) # 100hz

    rospy.init_node('listener', anonymous=True)#initialise subscriber 
    #linear acceleration
    rospy.Subscriber("/imu1", Imu, imucallback) #subscribe to imu sensor
    pub = rospy.Publisher('imu1_acc_data', Vector3, queue_size=10) #publish linear acc obtained from imu subscriber
    #angular velocity
    pub = rospy.Publisher('imu1_angvel_data', Vector3, queue_size=10) #publish angular velocity obtained from imu subscriber
    #linear acceleration
    #rospy.Subscriber("/imu1", Imu, imucallback) #subscribe to imu sensor
    #pub = rospy.Publisher('imu1_acc_cov_data', float64[9], queue_size=10) #publish linear acc obtained from imu subscriber
    #angular velocity
    #pub = rospy.Publisher('imu1_angvel_cov_data', float64[9], queue_size=10) #publish angular velocity obtained from imu subscriber
    #rate = rospy.Rate(100) # 100hz

    rospy.init_node('listener', anonymous=True)#initialise subscriber 
    #linear acceleration
    rospy.Subscriber("/imu2", Imu, imucallback) #subscribe to imu sensor
    pub = rospy.Publisher('imu2_acc_data', Vector3, queue_size=10) #publish linear acc obtained from imu subscriber
    #angular velocity
    pub = rospy.Publisher('imu2_angvel_data', Vector3, queue_size=10) #publish angular velocity obtained from imu subscriber
    #linear acceleration cov
    #rospy.Subscriber("/imu2", Imu, imucallback) #subscribe to imu sensor
    #pub = rospy.Publisher('imu2_acc_cov_data', float64[9], queue_size=10) #publish linear acc obtained from imu subscriber
    #angular velocity cov
    #pub = rospy.Publisher('imu2_angvel_cov_data', float64[9], queue_size=10) #publish angular velocity obtained from imu subscriber
    
    rate = rospy.Rate(100) # 100hz

    while not rospy.is_shutdown():
        pub.publish(imu0_acc_data_var)
        pub.publish(imu0_angvel_data_var)
        #pub.publish(imu0_acc_cov_data_var)
        #pub.publish(imu0_angvel_cov_data_var)

        pub.publish(imu1_acc_data_var)
        pub.publish(imu1_angvel_data_var)
        #pub.publish(imu1_acc_cov_data_var)
        #pub.publish(imu1_angvel_cov_data_var)

        pub.publish(imu2_acc_data_var)
        pub.publish(imu2_angvel_data_var)
        #pub.publish(imu2_acc_cov_data_var)
        #pub.publish(imu2_angvel_cov_data_var)

        rate.sleep()
    rospy.spin()


if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass


