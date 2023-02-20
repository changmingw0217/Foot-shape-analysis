from DTW import *
from image import *
from database import *
from Feature_scaling import *


def comparison(distance_list):

    EGYPTIAN_list = Database["EGYPTIAN"]
    ROMAN_list = Database["ROMAN"]
    GREEK_list = Database["GREEK"]

    egyptian_val = Inf
    roman_val = Inf
    greek_val = Inf

    for test_case in EGYPTIAN_list:
        test_val = get_difference(distance_list, test_case)

        if test_val < egyptian_val:
            egyptian_val = test_val

    for test_case in ROMAN_list:
        test_val = get_difference(distance_list, test_case)

        if test_val < roman_val:
            roman_val = test_val

    for test_case in GREEK_list:
        test_val = get_difference(distance_list, test_case)

        if test_val < greek_val:
            greek_val = test_val

    res = min(egyptian_val, roman_val, greek_val)

    if res == egyptian_val:
        return "Egyptian Foot"
    elif res == roman_val:
        return "Roman Foot"
    else:
        return "Greek Foot"


def get_type():

    dis_list = get_distance()
    scaling_list = scaling(dis_list)
    res = comparison(scaling_list)
    print(res)


if __name__ == '__main__':

    scaling_list = scaling([167.0449041425688, 161.37224048763778, 160.0781059358212, 162.09873534361705, 165.67739737212196, 170.18813119603846, 175.45369759569047, 181.64801127455263, 190.2866259094422, 200.0, 211.29126815843574, 220.00227271553356, 230.5558500667463, 238.5979882563975, 248.39484696748443, 259.26048676958084, 270.4144966528237, 280.178514522438, 291.78073959739015, 304.4355432599814, 316.4316671889841, 330.3346787729075, 347.9669524538214, 365.8428624423333, 383.0195817448502, 398.5285435197835, 412.31056256176606, 427.10186138671884, 441.04534914223956, 455.0560405049031, 469.12791432614625, 454.1200281863816, 437.32024878800206, 420.61978079971465, 404.0309394093477, 387.5680585394003, 371.24789561693143, 355.09012940378955, 339.1179735726197, 323.35893369443187, 307.8457405909655, 293.4552776829887, 281.0, 274.4612905311057, 260.0480724789169, 250.69702830308938, 246.10770000144245, 256.12496949731394, 256.9065978132909, 251.46769176178478, 236.3810483097154, 229.12005586591496, 214.59030733003763, 208.0600874747485, 195.88006534611938, 186.07794065928394, 177.56407294269863, 170.18813119603846, 164.92422502470643, 163.1686244349691, 160.61133210331082, 160.0781059358212]
)
    res = comparison(scaling_list)
    print(res)
