#!/usr/bin/env python
from __future__ import print_function
from beginner_tutorials.srv import CalculateCircleArea, CalculateCircleAreaResponse
import rospy

def handle_circle_area(req):
    pi = 3.14
    diameter = req.diameter
    area = (1/4) * pi * (diameter ** 2)
    print("Diameter diterima: %s, Luas dihitung: %s" % (diameter, area))
    return CalculateCircleAreaResponse(area)

def circle_area_server():
    rospy.init_node('circle_area_server')
    s = rospy.Service('calculate_circle_area', CalculateCircleArea, handle_circle_area)
    print("Siap menghitung luas lingkaran.")
    rospy.spin()

if __name__ == "__main__":
    circle_area_server()
