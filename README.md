# Postp-ciclones
## Scripts de post procesamiento de netCDF de ciclones
Consta de varios scripts, cada uno genera diferente tipo de archivos.
Se requiere la biblioteca netCDF4

### gen_ciclo.py
Extrae información del archivo original y genera un archivo con datos de tipo trayectoria. Es de notar que el atributo coordinates tiene las variables intercambiadas en comparación con los archivos tipo grid. Se hizo de esta manera para seguir los ejemplos que se encuentran en la guia de la CFC.

### gen_freq.py
Extrae información del archivo original y genera un archivo con la única variable de tipo grid que se encuentra en este archivo. También se agregan las variables de referencias correspondientes y cierta información de encabezado (metadatos)


### gen_point.py
Extrae información del archivo original y divide la variable "coordenadas_por_ciclon" en variables de tipo punto. También se incluye información de metadatos y variables de referencia.

### gen_header.py
Se genera un archivo netcdf con únicamente información de metadatos (atributos globales).
