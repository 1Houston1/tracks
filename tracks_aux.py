from math import atan2,degrees

def f_CalcAngleDeg(point_1,point_2):
    xDiff= point_2[0]-point_1[0]
    yDiff = point_2[1]-point_1[1]

    return degrees(atan2(yDiff,xDiff))


def f_closestPoint(pair,multiple):
    ''' identify a number out of a poir which is closest to a number'''

    #extract the tuple
    a,b=pair

    # based on the abs difference to a number return either a or b
    if abs(a-multiple) >= abs(b-multiple):
        return b
    else:
        return a

def f_FindValuesCloseToMultiple(list_of_disctances, multiple_of):
    ''' returns a list of TrueFalse which indicate where a multiple of "multiple_of"
        was found in distance list '''

    Match=[]                                               # definition of the return value
    multiple=multiple_of                                   # save the initial value of the multiple
    Match_l=[]

    # now check whether the given numer is included in the list of distances
    while(multiple<=max(list_of_disctances)):
        number=0

        # iterate of the list whith a window of two elements
        for i in range(0, len(list_of_disctances) - 1):
            a,b= list_of_disctances[i:i + 2]

            # if one number is below and the other number is above the multiple
            if a < multiple and b > multiple:
                # check which number of both is closest to the mulitple
                number = f_closestPoint((a,b),multiple)
            else:
                continue

        # append the found number to a list
        Match.append(number)

        # and update the number for the next cycle
        multiple+=multiple_of

    # create list where 1 indicates a multiple was found
    for i in list_of_disctances:
        if i in Match:
            Match_l.append(1)
        else:
            Match_l.append(0)
    Match_l[0]=1    # first ohne needs to be used allways

    return Match_l   # return the list of numbers which are close the the multiple



if __name__ == '__main__':
    distance= [0.0, 20.980497786662088, 26.079629491390477, 37.558960045814146, 48.94511476344146, 60.16043282555313,
     71.23185079258819, 77.06912961160076, 89.18151139802693, 104.76999916562302, 120.18205527598614,
     127.21967540499351, 139.68384520589603, 160.32042317984926, 171.97065081833992, 188.22862822415604,
     198.51571486302558, 207.4092353300977, 228.109510712109, 244.63785466066582, 255.81585687875176,
     267.46383666176365, 273.6550564326866, 294.88565103388595, 299.1128828302806, 305.7349617284699, 318.6020125428574,
     321.54994058187884, 332.5409077256877, 344.0757377168035, 359.8133852494163, 360.69969855234956,
     361.27529447968806, 362.13273766644465, 363.364765502228, 377.7318805054657, 402.82375805041005, 410.5344347458819,
     434.6892545438942, 451.3802048178801, 469.0571606220416, 487.1510721146455, 496.3843613209014, 514.8050627744384,
     576.8635812003837, 610.8435496137804, 619.2316984521507, 654.4306782165244, 663.4337627685866, 681.7049228759619,
     725.5329158483863, 742.9114398778713, 760.6211133442762, 794.7968437624816, 821.5883356840372, 839.1414657699844,
     857.0410279603486, 865.7839975115754, 883.3490658127264, 891.9057505218843, 908.9569374662245, 917.481593565552,
     934.4437268841468, 959.2402755072658, 967.4878987098314, 983.803261112274, 1007.7232414509865, 1022.9894533165909,
     1030.5467511108868, 1045.8522417364536, 1060.72373105588, 1082.7007971164169, 1097.5634781863153,
     1112.850118027087, 1157.4283789235385, 1218.8780010357568, 1225.2955898807043, 1250.2050122580815,
     1256.7721562193829, 1263.71241090167, 1278.0481067875494, 1294.00246395757, 1312.0612314022121, 1354.0452088624015,
     1365.46068527774, 1395.3520444703595, 1412.6575560895587, 1430.6026367567824, 1480.144971305923, 1533.935858794354,
     1571.2276194818128, 1607.9202723113976, 1616.9245213458762, 1634.68208386921, 1652.2772265277022,
     1661.0022654879356, 1678.3110097800284, 1717.3411060064439, 1732.792763955251, 1741.0925106207094]

    print(f_FindValuesCloseToMultiple(list_of_disctances=distance,multiple_of=100))


