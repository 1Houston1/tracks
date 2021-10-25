import gpxpy
import gpxpy.gpx
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from pylab import figure
from datetime import timedelta
from statistics import mean
import os
from tracks_aux import f_CalcAngleDeg

cols_dict={0:'blue',1:'orange',2:'green',3:'red',4:'purple',5:'brown',6:'pink',7:'olive',8:'cyan'}

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)



SPEED_THRESH=2

# store the intermediate results in lists
lat=[]
lon=[]
elev=[]
sp=[]
times=[]
speed=[]
points=[]
dist_per_point=[]
distance=[]
cum_elevation=[]
speed_filt=[]
dur=[]
dur_s=[]
angle=[]

lat_all=[]
lon_all=[]
elev_all=[]
sp_all=[]
times_all=[]
speed_all=[]
points_all=[]
dist_per_point_all=[]
distance_all=[]
cum_elevation_all=[]
speed_filt_all=[]
dur_all=[]
dur_s_all=[]

f_list=[file for file in os.listdir() if '.gpx' in file]

print('reading files...')
for no,f in enumerate(f_list):
    print(f)
    gpx_file = open(f)
    gpx = gpxpy.parse(gpx_file)

    for track in gpx.tracks:
        for segment in track.segments:

            # read each point with data of lateral, longitudinal, elevation and time
            for point_nr, point in enumerate(segment.points):
                points.append(point)
                lat.append(point.latitude)
                lon.append(point.longitude)
                elev.append(point.elevation)
                times.append(point.time.time())

                # init values for the beginning - set all values to zero
                if point_nr == 0:
                    speed.append(0)
                    dist_per_point.append(0)
                    distance.append(0)
                    cum_elevation.append(0)
                    speed_filt.append(0)
                    dur.append(0)
                    dur_s.append('00:00:00')
                    angle.append('10')
                else:
                    speed.append(point.speed_between(segment.points[point_nr - 1]))  # speed between way points

                    dist_per_point.append(
                        point.distance_3d(segment.points[point_nr - 1]))  # distance between wasy points
                    distance.append(sum(dist_per_point))  # distance from start to qay point

                    # calculate the duration from start to current point_nr
                    dur.append(timedelta(hours=times[point_nr].hour,
                                         minutes=times[point_nr].minute,
                                         seconds=times[point_nr].second) -

                               timedelta(hours=times[0].hour,
                                         minutes=times[0].minute,
                                         seconds=times[0].second))

                    angle.append()

                    # filter speed and store it in list
                    last_speed_filt = speed_filt[-1]
                    if (speed[point_nr] - last_speed_filt) > SPEED_THRESH:
                        speed_filt.append((last_speed_filt + last_speed_filt + SPEED_THRESH) / 2)
                    elif (last_speed_filt - speed[point_nr]) > SPEED_THRESH:
                        speed_filt.append((last_speed_filt + (last_speed_filt - SPEED_THRESH)) / 2)
                    else:
                        speed_filt.append((last_speed_filt + speed[point_nr]) / 2)

                    # check whether hight has increased
                    if point.elevation > segment.points[point_nr - 1].elevation:

                        # calculate the increas between the last two way points
                        inc = point.elevation - segment.points[point_nr - 1].elevation

                        # get the last value
                        last_value = cum_elevation[-1]

                        # add increase of hight plus the reached hight at that waypoint
                        cum_elevation.append(last_value + inc)


                    else:
                        # get the last element and maintain it
                        cum_height = cum_elevation[-1]
                        cum_elevation.append(cum_height)

                dur_s = [str(s) for s in dur]
    lat_all.append(lat)
    lon_all.append(lon)
    elev_all.append(elev)

    lat,lon,elev=[],[],[]


#fig = figure()
#ax = Axes3D(fig)
#ax.set_xlabel('lon [°]')
#ax.set_ylabel('lat [°]')
#ax.set_zlabel('hight [m]')
#
#for i in range(len(lat_all)):
#    ax.plot(lon_all[i],lat_all[i],elev_all[i],c=cols_dict[i])
#for angle in range(0, 360):
#    ax.view_init(10, angle)
#    plt.draw()
#    plt.pause(0.001)


