#!/usr/bin/env python

import rospy
from beginner_tutorials.srv import penghitungluasan, penghitungluasanResponse

def hitung_luasan(diameter):
    """
    Menghitung luas lingkaran dan insentif per meter persegi.
    Menggunakan rumus manual: luas = 0.25 * π * d^2
    """
    pi = 3.14
    luas = 0.25 * pi * diameter**2  # Rumus manual luas lingkaran
    return luas

def handle_penghitungluasan(req):
    """
    Callback untuk menangani permintaan dari client.
    """
    luas = hitung_luasan(req.diameter)
    # Log informasi di server
    rospy.loginfo(f"Diameter: {req.diameter} m")
    rospy.loginfo(f"Area: {luas:.2f} m^2")
    return penghitungluasanResponse(luas)

def penghitungluasan_server():
    """
    Server ROS untuk menghitung luas tanah.
    """
    rospy.init_node('penghitungluasan_server')
    service = rospy.Service('penghitungluasan', penghitungluasan, handle_penghitungluasan)
    rospy.loginfo("Penghitung Luasan Server siap.")
    rospy.spin()

if __name__ == "__main__":
    penghitungluasan_server()
