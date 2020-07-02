'''
Generating grid netcdf from
'CiclonesTropicales1851_2016_V4_version_final.nc'
date reference: 1851/01/01
output filename: ciclones_freq.nc
'''
from netCDF4 import Dataset
from netCDF4 import chartostring 
from netCDF4 import stringtochar
import numpy as np
import datetime as dt

filename='CiclonesTropicales1851_2016_V4_version_final.nc'
ofilename='ciclones_freq.nc'
with Dataset(filename,'r') as root:
    freq=root['frecuencia_anual'][:]
    lat=root['latitud_frecuencua'][:]
    lon=root['longitud_frecuencia'][:]
print('freq:',freq.T.shape)
print('lat:', lat.shape)
print('lon:', lon.shape)
#get dimensions
ncat=7
latd=len(lat)
lond=len(lon)
new_freq=np.empty((1,ncat,latd,lond),dtype=int)
for i in range(ncat):
    new_freq[0][i][:]=freq[i].T
print('Dimensions:')
print('ncat:{} lat:{} lon:{}'.format(ncat, latd, lond))

#create new file
with Dataset(ofilename,'w', format="NETCDF4_CLASSIC") as root:
    #metadata
    root.title="Frecuencia de Ciclones Tropicales del Golfo de México"
    root.summary="Cantidad de Ciclones Tropicales del GoM para cada punto de malla en un radio de 50 Km"
    root.comment="Procesamiento de los dato HURDAT2 del National Hurricane Center para el Golfo de México. Periodo:1851:2016"
    root.history='adapted to CF using gen_freq.py'
    #root.calendar="gregorian"
    root.geospatial_lat_min="16.121876"
    root.geospatial_lat_max="31.621876"
    root.geospatial_lon_min="-99.438995"
    root.geospatial_lon_max="-78.739"
    #root.geospatial_lat_units="degrees_north"
    #root.geospatial_lon_units="degrees_east"
    #root.geospatial_lat_resolution="0.1"
    #root.geospatial_lon_resolution="0.1"
    #root.geospatial_bounds_crs= "EPSG:4326"
    #dimensions
    root.createDimension('latitud_malla',latd)
    root.createDimension("longitud_malla",lond)
    root.createDimension('categoria_malla',ncat )
    root.createDimension('time',1)

    #Variables
    root.createVariable('time','i2',('time'))
    root['time'][:]=[0]
    root['time'].units='days since 1851-01-01 00:00:00'
    root['time'].axis='T'
    root['time'].standard_name='time'
    root['time'].long_name='time'

    root.createVariable('categoria','i2',('categoria_malla'))
    root['categoria'][:]=range(7)
    root['categoria'].long_name='Clasificación de ciclones tropicales'
    root['categoria'].comment='1->Tormenta Tropical, 2->Cat.1, 3->Cat.2, 4->Cat.3, 5->Cat.4, 6->Cat.5, 7->Ciclones Tropicales'
    root['categoria'].units='1'
    root['categoria'].axis='Z'
    root['categoria'].positive='up'

    root.createVariable('latitud','f4',('latitud_malla'))
    root['latitud'][:]=lat
    root['latitud'].standard_name='latitude'
    root['latitud'].long_name='latitud cada 0.1 grado'
    root['latitud'].units='degrees_north'
    root['latitud'].axis='Y'

    root.createVariable('longitud','f4',('longitud_malla'))
    root['longitud'][:]=lon
    root['longitud'].standard_name='longitude'
    root['longitud'].long_name='longitud cada 0.1 grado'
    root['longitud'].units='degrees_east'
    root['longitud'].axis='X'

    root.createVariable('frecuencia_anual','f4',('time','categoria_malla','latitud_malla', 'longitud_malla'))
    root['frecuencia_anual'][:]=new_freq
    root['frecuencia_anual'].comment='Número de ciclones para cada punto de malla en un radio de 50 Km'
    root['frecuencia_anual'].long_name='ciclones tropicales por categoria'
    root['frecuencia_anual'].units='1'
    root['frecuencia_anual'].coordinates="time categoria latitud longitud"
    root['frecuencia_anual'].coverage_content_type="thematicClassification"


print("sucess!")
