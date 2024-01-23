#!/usr/bin/python3

import uvicorn
import rospy
from fastapi import FastAPI
from geometry_msgs.msg import Vector3, Twist
from std_msgs.msg import Float32MultiArray

app = FastAPI()


@app.get("/")
def root():
    ros_pub_angle_cmd.publish(Vector3(100, 100, 100))

    # msg = rospy.wait_for_message("/body_state", Float32MultiArray, timeout=None)
    # print(msg)

    return "test"


def update_angle_cmd(self, msg):
    print(msg)


@app.on_event("startup")
def startup_event():
    rospy.init_node('spot_micro_mobile_control')

    global ros_pub_angle_cmd
    ros_pub_angle_cmd = rospy.Publisher('/angle_cmd', Vector3, queue_size=1)

    rospy.Subscriber('lcd_angle_cmd', Twist, update_angle_cmd)

    rospy.loginfo("Mobile control node publishers corrrectly initialized")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
