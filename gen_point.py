'''
Generating point file from
'CiclonesTropicales1851_2016_V4_version_final.nc'
date reference: 1851/01/01
output filename: ciclones_point.nc
'''
from netCDF4 import Dataset
from netCDF4 import chartostring 
from netCDF4 import stringtochar
import numpy as np
import datetime as dt

filename='CiclonesTropicales1851_2016_V4_version_final.nc'
ofilename='ciclones_point.nc'
with Dataset(filename,'r') as root:
    coords=root['coordenadas_por_ciclon'][:]
    xtime=root['fechas_registro_calendario'][:]
obs=len(coords.T)
with Dataset(ofilename,'w', format="NETCDF4_CLASSIC") as root:
    #metadata
    root.title="Ciclones Tropicales del Golfo de México"
    root.summary="Información sobre Ciclones Tropicales del GoM en puntos"
    root.comment="Procesamiento de los datos HURDAT2 del National Hurricane Center para el Golfo de México. Periodo:1851:2016. Puntos correspondientes a primer impacto, segundo impacto y primer registro"
    root.featureType="point"
    root.cdm_data_type="Point"
    root.history='adapted to CF using gen_point.py'
    #root.calendar="gregorian"
    root.geospatial_lat_min="8.5"
    root.geospatial_lat_max="32.585857"
    root.geospatial_lon_min="-97.883835"
    root.geospatial_lon_max="0"
    #root.geospatial_lat_units="degrees_north"
    #root.geospatial_lon_units="degrees_east"
    #root.geospatial_lat_resolution="0.1"
    #root.geospatial_lon_resolution="0.1"
    #root.geospatial_bounds_crs= "EPSG:4326"
    #dimensions
    root.createDimension('obs',obs)

    #root.createVariable('time','f4',('obs'))
    #root['time'][:]=new_time
    #root['time'].standard_name='time'
    #root['time'].long_name='time'
    #root['time'].units='hours since 1851-01-01 00:00:00'
    #root['time'].axis='T'

    root.createVariable('latitude1','f4',('obs'))
    root['latitude1'][:]=coords[1]
    root['latitude1'].standard_name='latitude'
    root['latitude1'].long_name='latitud por punto'
    root['latitude1'].units='degrees_north'
    root['latitude1'].axis='Y'

    root.createVariable('longitude1','f4',('obs'))
    root['longitude1'][:]=coords[0]
    root['longitude1'].standard_name='longitude'
    root['longitude1'].long_name='longitud por punto'
    root['longitude1'].units='degrees_east'
    root['longitude1'].axis='X'

    varname='primer_impacto'
    root.createVariable(varname,'i1',('obs'))
    root[varname][:]=np.ones(obs)
    root[varname].long_name='punto de primer impacto'
    root[varname].units='1'
    root[varname].coverage_content_type='physicalMeasurement'
    root[varname].coordinates="longitude1 latitude1"

    root.createVariable('latitude2','f4',('obs'))
    root['latitude2'][:]=coords[3]
    root['latitude2'].standard_name='latitude'
    root['latitude2'].long_name='latitud por punto'
    root['latitude2'].units='degrees_north'
    root['latitude2'].axis='Y'

    root.createVariable('longitude2','f4',('obs'))
    root['longitude2'][:]=coords[2]
    root['longitude2'].standard_name='longitude'
    root['longitude2'].long_name='longitud por punto'
    root['longitude2'].units='degrees_east'
    root['longitude2'].axis='X'

    varname='segundo_impacto'
    root.createVariable(varname,'i1',('obs'))
    root[varname][:]=np.ones(obs)
    root[varname].long_name='punto de segundo impacto'
    root[varname].units='1'
    root[varname].coverage_content_type='physicalMeasurement'
    root[varname].coordinates="longitude2 latitude2 "

    root.createVariable('latitude3','f4',('obs'))
    root['latitude3'][:]=coords[5]
    root['latitude3'].standard_name='latitude'
    root['latitude3'].long_name='latitud por punto'
    root['latitude3'].units='degrees_north'
    root['latitude3'].axis='Y'

    root.createVariable('longitude3','f4',('obs'))
    root['longitude3'][:]=coords[4]
    root['longitude3'].standard_name='longitude'
    root['longitude3'].long_name='longitud por punto'
    root['longitude3'].units='degrees_east'
    root['longitude3'].axis='X'

    varname='primer_registro'
    root.createVariable(varname,'i1',('obs'))
    root[varname][:]=np.ones(obs)
    root[varname].long_name='punto de primer registro'
    root[varname].units='1'
    root[varname].coverage_content_type='physicalMeasurement'
    root[varname].coordinates="longitude3 latitude3 "

exit(0)
#extract and concat vars
def concat_var(var, row_size):
    new_var=var[0][:row_size[0]]
    print(new_var.shape)
    for i,e in enumerate(row_size):
        new_var=np.concatenate([new_var,var[i][:e]])
    return new_var[row_size[0]:]
new_lon=concat_var(lon.T, row_size)
print('longitude:',new_lon.shape)
print(new_lon)
new_lat=concat_var(lat.T, row_size)
print('latitude:', new_lat.shape)
print(new_lat)
new_xtime=concat_var(xtime.T, row_size)
print('xtime:', new_xtime.shape)
print(new_xtime)
#transform xtime to hours since new reference
ref_time=dt.datetime(1851,1,1)
new_time=[]
for nx in new_xtime:
    str_date, str_time=nx.tostring().decode('utf-8').split()[:2]
    str_date+=' '+str_time
    dt_time=dt.datetime.strptime(str_date,"%d/%m/%Y %H:%M")
    int_time=(dt_time-ref_time).total_seconds()/3600
    new_time.append(int_time)
    dt_time=dt.datetime(1851,1,1)+dt.timedelta(hours=int_time)
new_time=np.array(new_time)
print('time:', new_time.shape)
print(new_time)
#cat
new_cat=concat_var(cat.T, row_size)
print('cat:', new_cat.shape)
print(new_cat)
#wind
new_wind=concat_var(wind.T, row_size)
print('wind:', new_wind.shape)
print(new_wind)
#press
new_press=concat_var(press.T, row_size)
print('press:', new_press.shape)
print(new_press)
#traj id
trajectory=np.array(range(ntraj))
#row_size
row_size=np.array(row_size, )
#create new file
with Dataset(ofilename,'w', format="NETCDF4_CLASSIC") as root:
    #metadata
    root.title="Trayectorias de Ciclones Tropicales del Golfo de México"
    root.summary="Información sobre Ciclones Tropicales del GoM en trayectorias"
    root.comment="Procesamiento de los dato HURDAT2 del National Hurricane Center para el Golfo de México. Periodo:1851:2016"
    root.featureType="point"
    root.history='adapted to CF using gen_point.py'
    #root.calendar="gregorian"
    root.geospatial_lat_min="8.5"
    root.geospatial_lat_max="81.0"
    root.geospatial_lon_min="-109.5"
    root.geospatial_lon_max="63"
    #root.geospatial_lat_units="degrees_north"
    #root.geospatial_lon_units="degrees_east"
    #root.geospatial_lat_resolution="0.1"
    #root.geospatial_lon_resolution="0.1"
    #root.geospatial_bounds_crs= "EPSG:4326"
    #dimensions
    root.createDimension('obs',obs)
    #Hurricane number
    root.createDimension("trajectory",ntraj)
    #max name len
    root.createDimension('max_name', 10)
    #max date string len
    root.createDimension('DateStrLen',19)

    #Variables
    root.createVariable('cname','S1', ('trajectory',"max_name"))
    root['cname'][:]=nombres.T
    root['cname'].long_name='nombre ciclon'
    root['cname'].comment='nombre asignado a cada ciclon'
    root.createVariable('trajectory','i4', ('trajectory'))
    root['trajectory'].cf_role='trajectory_id'
    root['trajectory'].comment='id correspondiente a cada ciclon'
    root['trajectory'].long_name='id trajectory'
    root['trajectory'][:]=trajectory
    root.createVariable('row_size','i4',('trajectory'))
    root['row_size'].long_name='obs by trajectories'
    root['row_size'].comment='numero de observaciones de cada ciclon'
    root['row_size'].sample_dimension='obs'
    root.createVariable('time','f4',('obs'))
    root['time'][:]=new_time
    root['time'].standard_name='time'
    root['time'].long_name='time'
    root['time'].units='hours since 1851-01-01 00:00:00'
    root['time'].axis='T'

    root.createVariable('xtime','S1',('obs','DateStrLen'))
    root['xtime'][:]=new_xtime
    root['xtime'].long_name="fecha en formato texto"

    root.createVariable('latitude','f4',('obs'))
    root['latitude'][:]=new_lat
    root['latitude'].standard_name='latitude'
    root['latitude'].long_name='latitud por punto'
    root['latitude'].units='degrees_north'
    root['latitude'].axis='Y'

    root.createVariable('longitude','f4',('obs'))
    root['longitude'][:]=new_lon
    root['longitude'].standard_name='longitude'
    root['longitude'].long_name='longitud por punto'
    root['longitude'].units='degrees_east'
    root['longitude'].axis='X'

    root.createVariable('categoria_registro','i4',('obs'))
    root['categoria_registro'][:]=new_cat
    root['categoria_registro'].long_name='categoria determinada'
    root['categoria_registro'].units='1'
    root['categoria_registro'].coverage_content_type='physicalMeasurement'
    root['categoria_registro'].coordinates="time longitude latitude "

    root.createVariable('viento_sostenido_registro','f4',('obs'))
    root['viento_sostenido_registro'][:]=new_wind
    root['viento_sostenido_registro'].long_name='Magnitud del viento sostenida'
    root['viento_sostenido_registro'].units='kt'
    root['viento_sostenido_registro'].coverage_content_type='physicalMeasurement'
    root['viento_sostenido_registro'].coordinates="time longitude latitude "

    root.createVariable('presion_central_registro','f4',('obs'))
    root['presion_central_registro'][:]=new_press
    root['presion_central_registro'].long_name='Presión central mínima'
    root['presion_central_registro'].units='hPa'
    root['presion_central_registro'].coverage_content_type='physicalMeasurement'
    root['presion_central_registro'].coordinates="time longitude latitude "

print("sucess!")
