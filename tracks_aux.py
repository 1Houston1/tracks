from math import atan2,degrees

def f_CalcAngleDeg(point_1,point_2):
    ''' calculate the angle between two points, orienation is accorinding to
    https://de.wikipedia.org/wiki/Windrichtung, that means wind from north is 0°, hence an offset
    needs to be added finally '''
    xDiff= point_2[0]-point_1[0]
    yDiff = point_2[1]-point_1[1]

    return 90-degrees(atan2(yDiff,xDiff))


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
    print(f_CalcAngleDeg((1,1),(1,-1)))