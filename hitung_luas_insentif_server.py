#!/usr/bin/env python
from __future__ import print_function
from beginner_tutorials.srv import HitungLuasInsentif, HitungLuasInsentifResponse
import rospy

def hitung_luas_dan_insentif(req):
    pi = 3.14
    diameter = req.diameter
    insentif_per_m2 = req.insentif_per_m2
    luas = (1/4) * pi * (diameter ** 2)  # Rumus luas lingkaran
    total_insentif = luas * insentif_per_m2
    print("Diameter: %s, Insentif/m2: %s, Luas: %s, Total Insentif: %s" % 
          (diameter, insentif_per_m2, luas, total_insentif))
    return HitungLuasInsentifResponse(luas, total_insentif)

def server_hitung_luas_insentif():
    rospy.init_node('hitung_luas_insentif_server')
    s = rospy.Service('hitung_luas_insentif', HitungLuasInsentif, hitung_luas_dan_insentif)
    print("Server siap menghitung luas dan total insentif.")
    rospy.spin()

if __name__ == "__main__":
    server_hitung_luas_insentif()
