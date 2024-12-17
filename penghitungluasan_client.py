#!/usr/bin/env python

import rospy
from beginner_tutorials.srv import penghitungluasan

def hitung_insentif_client(diameter):
    """
    Meminta server untuk menghitung luas tanah berdasarkan diameter.
    Menghitung insentif berdasarkan luas tanah.
    """
    rospy.wait_for_service('penghitungluasan')
    try:
        penghitungluasan_service = rospy.ServiceProxy('penghitungluasan', penghitungluasan)
        response = penghitungluasan_service(diameter)
        
        # Menghitung total insentif
        insentif_per_meter = 150000  # Insentif per meter persegi
        insentif_total = response.area * insentif_per_meter
        
        return insentif_total
    except rospy.ServiceException as e:
        rospy.logerr(f"Service call failed: {e}")
        return None

if __name__ == "__main__":
    rospy.init_node('penghitungluasan_client')

    # Diameter sudah ditentukan otomatis (misalnya 80 meter)
    diameter = 80.0  
    rospy.loginfo(f"Requesting incentive calculation for diameter: {diameter} m")

    # Panggil server
    insentif_total = hitung_insentif_client(diameter)
    if insentif_total is not None:
        rospy.loginfo(f"Total Insentif: Rp {insentif_total:.2f}")
        print(f"Total Insentif untuk diameter {diameter} m: Rp {insentif_total:.2f}")
    else:
        rospy.loginfo("Failed to retrieve incentive data.")
