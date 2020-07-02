'''
Generating header file 
output filename: header_ciclo.nc
'''
from netCDF4 import Dataset

ofilename='header_ciclo.nc'
#create new file
with Dataset(ofilename,'w', format="NETCDF4_CLASSIC") as root:
    #metadata
    root.keywords="Earth Science > Atmosphere > Weather Events > Tropical Cyclones"
    root.keywords_vocabulary="GCMD Science keywords"
    root.contributor_name='Daniel Robles Muñoz, danept@ciencias.unam.mx; Jorge Zavala Hidalgo, jzavala@atmosfera.unam.mx; María Elena Osorio Tai, tai@atmosfera.unam.mx; Miguel Angel Robles R., miguel.robles@atmosfera.unam.mx; Samantha Pantoja Ortiz, samantha.pantoja@atmosfera.unam.mx'
    root.contributor_role='Postprocesamiento; Postprocesamiento; Postprocesamiento; Revisión y Postprocesamiento; Revisión'
    root.processing_level='L4'
    root.source='best track information statistics'
    root.refereces='https://www.aoml.noaa.gov/hrd/data_sub/re_anal.html; '+\
    'https://www.nhc.noaa.gov/data/hurdat/hurdat2-format-nov2019.pdf; '+\
    'https://www.nhc.noaa.gov/data/#hurdat'
    root.Conventions='CF-1.6, ACDD-1.3'
    root.naming_authority="mx.unam.atmosfera.ioa"
    root.institution="CCA-UNAM"
    root.project="CONACyT - SENER - Hidrocarburos, proyecto 201441"
    root.license="Los datos de este dataset son privados y regidos bajo los términos del Consorcio de Investigación del Golfo de México"
    root.acknowledgment='Investigación financiada por el Fondo Sectorial CONACYT-SENER-Hidrocarburos, proyecto 201441. Contribución del Consorcio de Investigación del Golfo de México (CIGoM). Reconocimiento a PEMEX por promover ante el Fondo la demanda específica sobre los derrames de hidrocarburos y el medio ambiente.'
    root.standard_name_vocabulary="CF Standard Name Table v1.6"
    root.creator_name= "Grupo Interacción Océano Atmósfera"
    root.creator_email="ioa@atmosfera.unam.mx"
    root.creator_url="http://grupo-ioa.atmosfera.unam.mx/cigom"
    root.creator_institution="CCA-UNAM"
    root.creator_type="group"
    root.publisher_name="Grupo Interacción Océano Atmósfera"
    root.publisher_email="ioa@atmosfera.unam.mx"
    root.publisher_url="http://grupo-ioa.atmosfera.unam.mx/cigom"
    root.publisher_institution="CCA-UNAM"
    root.publisher_type="group"
    root.time_coverage_start="1851-01-01T00:00:00"
    root.time_coverage_end="2016-12-31T11:59:59"
    root.time_coverage_duration="P60630D"
    root.date_created="2019-11-23"
    root.date_modified="2020-06-09"
    root.date_issued="2020-06-10"
    root.id="gom_ciclo-1851/2017"
    root.time_coverage_resolution="P00Y00M00DT06H00M00S"

    #root.geospatial_lat_min="16.1"
    #root.geospatial_lat_max="31.6"
    #root.geospatial_lon_min="-99.4"
    #root.geospatial_lon_max="-78.7"
    root.geospatial_lat_units="degrees_north"
    root.geospatial_lon_units="degrees_east"
    root.geospatial_lat_resolution="0.1"
    root.geospatial_lon_resolution="0.1"
    root.geospatial_bounds_crs= "EPSG:4326"

print("sucess!")
