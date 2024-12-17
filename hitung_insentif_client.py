#!/usr/bin/env python
from __future__ import print_function
import sys
import rospy
from beginner_tutorials.srv import HitungLuasInsentif

def client_hitung_luas_insentif(diameter, insentif_per_m2):
    rospy.wait_for_service('hitung_luas_insentif')
    try:
        hitung_luas_insentif = rospy.ServiceProxy('hitung_luas_insentif', HitungLuasInsentif)
        response = hitung_luas_insentif(diameter, insentif_per_m2)
        return response.luas, response.total_insentif
    except rospy.ServiceException as e:
        print("Gagal memanggil service: %s" % e)

def penggunaan():
    return "%s [diameter insentif_per_m2]" % sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 3:
        diameter = float(sys.argv[1])
        insentif_per_m2 = float(sys.argv[2])
    else:
        print(penggunaan())
        sys.exit(1)
    print("Menghitung luas lingkaran dan total insentif...")
    luas, total_insentif = client_hitung_luas_insentif(diameter, insentif_per_m2)
    print("Luas lingkaran: %s m2" % luas)
    print("Total insentif yang diperoleh: Rp. %s" % total_insentif)
