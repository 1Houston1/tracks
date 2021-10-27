#from math import atan2,degrees,sin,radians,cos,sqrt
import math

R = 6373.0

def f_CalcAngleDeg(point_1,point_2):
    ''' calculate the angle between two points, orienation is accorinding to
    https://de.wikipedia.org/wiki/Windrichtung, that means wind from north is 0°, hence an offset
    needs to be added finally. direction is from point_1 to point_2'''

    xDiff = point_2[1]-point_1[1]
    yDiff= point_2[0]-point_1[0]

    # calculate the angle between two points
    angle = math.degrees(math.atan2(yDiff,xDiff))
    # if angle is negative correct the angle by adding an offset to the absolute value
    if angle < 0:
        angle = 360-abs(angle)

    # return the calculated angle
    return angle

def f_CalWpDistance(point_1,point_2):
    lon1 = math.radians(point_1[0])
    lon2 = math.radians(point_2[0])
    lat1 = math.radians(point_1[1])
    lat2 = math.radians(point_2[1])

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c * 1000

    return distance

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
    #print(f_CalcAngleDeg((0,0),(1,1)))
    print(f_CalWpDistance((10.055605, 48.835271),(10.056681, 48.835347)))