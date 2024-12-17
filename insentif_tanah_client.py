#!/usr/bin/env python

import rospy
from beginner_tutorials.srv import CircleLandArea

def calculate_insentive(radius):
    """
    Fungsi untuk menghitung insentif berdasarkan luas.
    """
    rospy.wait_for_service('circle_land_area')
    try:
        # Panggil service untuk menghitung luas lingkaran
        circle_land_area = rospy.ServiceProxy('circle_land_area', CircleLandArea)
        response = circle_land_area(radius)

        # Hitung insentif: luas × 150.000
        insentive = response.area * 150000
        rospy.loginfo(f"Radius: {radius}, Area: {response.area}, Insentif: {insentive}")
        return insentive
    except rospy.ServiceException as e:
        rospy.logerr(f"Service call failed: {e}")
        return 0.0

if __name__ == "__main__":
    radius = float(input("Masukkan radius tanah (m): "))
    insentive = calculate_insentive(radius)
    print(f"Insentif yang diterima: Rp{insentive:,.2f}")
