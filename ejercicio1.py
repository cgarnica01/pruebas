import pandas as pd  #Cargamos el módulo de pandas

df = pd.read_csv('/vagrant/velocidades.csv') #Cargamos el archivo a analizar

print ("Nombre de las comlumnas es: " , df.keys()) #Obtenemos el nombre de las columnas del archivo
no_reg = df['Vehiculo'].count() #Obtenemos el No de registros de la BD
print ("No de registros de la bd", no_reg)
no_vehiculos = df.groupby(by=['Vehiculo']).count() #No de vehiculos unicos
print ("No de vehiculos en: ", no_vehiculos['id'].count())
no_dias = df.groupby(['fecha']).count() #No de días
print ("Cuantos dias aparecen: ",no_dias['id'].count())
df['fecha'] = pd.to_datetime(df['fecha']) #Conversión a fecha del campo fecha
print ("De que fecha a que fecha son los registros, de: ", df['fecha'].min(), "a: ", df['fecha'].max()) #Maximo y minimo de fecha
df['mes']=pd.DatetimeIndex(df['fecha']).month #Obtenemos el mes de la fecha y lo almacenamos en un nuevo campo (mes)
no_meses = df.groupby(['mes']).groups.keys() #Agrupamos por mes para obtener los meses con información
print ("Los meses con Informacion son: ", no_meses)
df['hora'] = pd.DatetimeIndex(df['hora']).hour #Convertimos el campo hora en tipo datetime
no_horas = df.groupby(['hora']).groups.keys() #Agrupamos las horas para obtener las horas de trabajo
print ("Las hora de trabajo son: ", no_horas)
velocidad_maxima = df['velocidad'].max() # Obtenemos la velocidad máxima registrada
print ("La velociad maxima es: ", velocidad_maxima)
vel_aux = df[df['velocidad'] == velocidad_maxima] #Buscamos el registro con la velocidad máxima registrada
print ("EL vehiculo con mayor velocidad fue: ", vel_aux.ix[:,'Vehiculo'].values) #Imprimimos sol el nombre del vehiculo con velocidad maxima
vel_rebasada = df[df['velocidad'] > 80] #Obtenemos los vehículos que rebasan el límite de 80 Km/h
print ("Los vehiculos que rebasaron el limite de 80 Km/h fueron: ", vel_rebasada.ix[:,'Vehiculo'].unique())
prom_mensual = df.groupby(['mes']).mean() #Obtenemos el promedio mensual de la velocidad
prom_mensual.index.name = ["Mes", "Velocidad"] #Ponemos nombre a las columnas
print ("El promedio mensual de la velocidad es: ", prom_mensual['velocidad'])
