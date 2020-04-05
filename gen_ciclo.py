from netCDF4 import Dataset
from netCDF4 import chartostring 
import numpy as np

filename='CiclonesTropicales1851_2016_V4_version_final.nc'
with Dataset(filename,'r') as root:
    nombres=root['nombre_ciclones'][:]
    cat=root['categoria_registro'][:]
    lat=root['latitud_registro'][:]
    lon=root['longitud_registro'][:]
    time=root['fecha_registro_numerico'][:]
    xtime=root['fechas_registro_calendario'][:]
#time correction
time-=367
#grid creation
grid_lon=np.linspace(-99.4,-78.7,num=208,)
grid_lat=np.linspace(16.1,31.6,num=156, )

ofilename='ciclones2.nc'
#create new file
with Dataset(ofilename,'w', format="NETCDF4_CLASSIC") as root:
    #metadata
    root.geospatial_lat_min="16.1"
    root.geospatial_lat_max="31.6"
    root.geospatial_lon_min="-99.4"
    root.geospatial_lon_max="-78.7"
    root.geospatial_lat_units="degrees_north"
    root.geospatial_lon_units="degrees_east"
    root.geospatial_lat_resolution="0.1"
    root.geospatial_lon_resolution="0.1"
    root.geospatial_bounds_crs= "EPSG:4326"
    #dimensions
    root.createDimension("trajectory",710)
    #root.createDimension('Time',133)
    #time unlimited
    root.createDimension('Time',)
    root.createDimension('max_name', 10)
    root.createDimension('DateStrLen',19)
    root.createDimension('south_north',156)
    root.createDimension('west_east',208)
    #time=root.createDimension('Time',)

    #Variables
    root.createVariable('latitude','f4',('south_north'))
    root.createVariable('longitude','f4',('west_east'))
    #root.createVariable('times','S1',("Time", "DateStrLen"))
    #root.createVariable('names','S1', ("max_name"))
    #root.createVariable('intensity','i1',("Time"))

    #filling
    root['latitude'][:]=grid_lat
    root['latitude'].units="degrees_north"
    root['latitude'].long_name="latitude"
    root['latitude'].standard_name="latitude"
    root['latitude'].axis="Y"
    root['latitude']._CoordinateAxisType="Lat"
    root['longitude'][:]=grid_lon
    root['longitude'].units="degrees_east"
    root['longitude'].long_name="longitude"
    root['longitude'].standard_name="longitude"
    root['longitude'].axis="X"
    root['longitude']._CoordinateAxisType="Lon"
#data init
idata=0
print(nombres.T.shape,len(nombres.T))
for idata in range(len(nombres.T)):
    len_data,=np.argwhere(np.isnan(lat.T[idata]))[0]
    #j,=np.argwhere(np.isnan(lon.T[0]))[0]
    print(idata,'/',len(nombres.T),':',len_data)
    data=np.empty((len_data,len(grid_lat),len(grid_lon)))
    data[:]=np.NaN
    #fill data
    for n in range(len_data):
        try:
            xlat,=np.argwhere(np.isclose(grid_lat,lat.T[0][n]))
            xlon,=np.argwhere(np.isclose(grid_lon,lon.T[0][n]))
            data[n,xlat,xlon]=cat[0][n]
        except:
            #if index is out
            pass

    myname=nombres.T[idata].tostring().decode('utf-8')
    myname=myname.split()[0]
    myname+='_{:03d}'.format(idata)
    time_name='time_{:03d}'.format(idata)

    with Dataset(ofilename,'a', format="NETCDF4_CLASSIC") as root:
        root.createVariable(time_name,'f8',('Time'))
        root[time_name].long_name="time"
        root[time_name].axis="T"
        #root[time_name]._CoordinateAxisType="Time"
        root[time_name].standard_name="time"
        root[time_name].units= "days since 0001-01-01 00:00:00.000 UTC"
        root[time_name][:]=time.T[idata][0:len_data]
        root.createVariable(myname,'f8',("Time","south_north","west_east"))
        root[myname][:]=data
        root[myname].coordinates=time_name+" latitude longitude"
        #root['intensity'][:]=cat.T[0][0:1]
        #root['times'][:]=xtime.T[0][0:len_data]
#print(root)
#print(chartostring(a.T))
print("sucess!")
