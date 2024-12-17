#!/usr/bin/env python
from __future__ import print_function

import sys
import rospy
from beginner_tutorials.srv import *

def calculate_circle_area_client(diameter):
    rospy.wait_for_service('calculate_circle_area')
    try:
        calculate_circle_area = rospy.ServiceProxy('calculate_circle_area', CalculateCircleArea)
        resp1 = calculate_circle_area(diameter)
        return resp1.area
    except rospy.ServiceException as e:
        print("Service call failed: %s" % e)

def usage():
    return "%s [diameter]" % sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 2:
        diameter = float(sys.argv[1])
    else:
        print(usage())
        sys.exit(1)
    print("Requesting luas lingkaran dengan diameter %s" % diameter)
    print("Luas lingkaran untuk diameter %s adalah %s m2" % (diameter, calculate_circle_area_client(diameter)))
