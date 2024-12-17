#!/usr/bin/env python

import rospy
from beginner_tutorials.srv import CircleLandArea, CircleLandAreaResponse
import math  # Untuk konstanta pi

def handle_circle_area(req):
    """
    Fungsi untuk menghitung luas tanah berbentuk lingkaran.
    """
    try:
        # Hitung luas lingkaran: π × r × r
        area = math.pi * req.radius ** 2
        rospy.loginfo(f"Radius: {req.radius}, Area: {area}")
        return CircleLandAreaResponse(area)
    except Exception as e:
        rospy.logerr(f"Error calculating area: {e}")
        return CircleLandAreaResponse(0.0)

def circle_land_area_server():
    """
    Inisialisasi server ROS.
    """
    rospy.init_node('circle_land_area_server')
    service = rospy.Service('circle_land_area', CircleLandArea, handle_circle_area)
    rospy.loginfo("Circle Land Area Server is ready.")
    rospy.spin()

if __name__ == "__main__":
    circle_land_area_server()
