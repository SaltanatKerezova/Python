import requests
import pandas as pd
import xlrd
from IPython.display import clear_output
import time

filePath = 'in/tables/DobijeciStanice.csv' #ZDE ZMĚŇTE CESTU KE VSTUPNÍMU SOUBORU
fileType = ['CSV', 'EXCEL'][0] #ZDE ZMĚŇTE POUZE INDEX (0 PRO CSV, 1 PRO EXCEL)
encoding = 'utf-8-sig' #ZDE ZMĚŇTE KÓDOVÁNÍ, ABY SEDĚLO S TÍM, KTERÉ JSTE POUŽILI VE VSTUPNÍM SOUBORU
delimiter = ',' #ZDE ZMĚŇTE ODDĚLOVAČ, ABY SEDĚL S TÍM, KTERÝ JSTE POUŽILI VE VSTUPNÍM SOUBORU
decimal = ',' #ZDE NASTAVTE ODDĚLOVAČ DESETINNÝCH MÍST, KTERÝ JSTE POUŽILI VE VSTUPNÍM SOUBORU

cityColumnName = 'obec' #ZDE NASTAVTE NÁZEV SLOUPCE S MĚSTEM
streetColumnName = 'ulice' #ZDE NASTAVTE NÁZEV SLOUPCE S ULICÍ

outputFile = 'out/tables/doplnene_souradnice.csv' #SOUBOR MUSÍ BÝT CSV

def preparePossibleAddresses( city, street):
    if 'Praha' in city:
        city = 'Praha'
    possibleStreets = list( set( [street] + street.split(' ') + street.split('.') ) )
    possibleStreets.sort(key=len, reverse = True)
    return [ str( city ) + ' ' + str( pStreet ) for pStreet in possibleStreets] + [ str( city ) + ' ' + str( pStreet ).split('/')[-1] for pStreet in possibleStreets]

def getGPSLocation( city, street ):
    preparedAddresses = preparePossibleAddresses( city, street)
    for address in preparedAddresses:
        try:
            URL = 'https://nominatim.openstreetmap.org/search?q=<<adresa>>&format=json'
            r = requests.get(url = URL.replace('<<adresa>>', address.replace( ' ', '+' ) ))
            data = r.json()
            return { 'latitude': data[0]['lat'], 'longitude': data[0]['lon'] }
        except Exception as e:
            pass
    return { 'latitude': 0, 'longitude': 0 }

def getEstimatedTimeString( estimatedTime ):
    hours = int( estimatedTime / 3600 )
    minutes = int( ( estimatedTime - hours * 3600 ) / 60 )
    seconds = int( estimatedTime - minutes * 60 - hours * 3600 )
    hoursStringPart = [str(hours), '0' + str(hours)][hours<10]
    minutesStringPart = [str(minutes), '0' + str(minutes)][minutes<10]
    secondsStringPart = [str(seconds), '0' + str(seconds)][seconds<10]
    return hoursStringPart + ':' + minutesStringPart + ':' + secondsStringPart

data = None
data = pd.read_csv( filePath, encoding = encoding, sep = delimiter, decimal = decimal )

df = pd.DataFrame(data).set_index('radek_c')

# oprava jednoho chybneho radku ve vstupnim souboru
df.loc[1322,'severni_sirka'] = float('NaN')

# Výběr řádků, kde obsah sloupce 'severni_sirka' je NaN
filtered = df[df['severni_sirka'].isna()]

filtered_df = filtered

newLatitudes = []
newLongitudes = []
actualRow = 0
startTime = time.time( )
for row in filtered_df.iloc:
    GPSCoordinates = getGPSLocation( row[cityColumnName], row[streetColumnName] )
    #row['severni_sirka'] = GPSCoordinates['latitude']
    newLatitudes.append( GPSCoordinates['latitude'] )
    newLongitudes.append( GPSCoordinates['longitude'] )
    actualTime = time.time( )
    oneRowTime = ( actualTime - startTime ) / ( actualRow + 1 )
    estimatedTime = oneRowTime * ( len( filtered_df ) - ( actualRow + 1 ) )
    clear_output(wait=True)
    print( 'Dokončeno: ', int( ( actualRow + 1 ) / len( filtered_df ) * 100 ), '% ... Odhadovaný čas: ' + getEstimatedTimeString( estimatedTime ) )
    print( row[cityColumnName])
    actualRow += 1

filtered_df = filtered_df.assign(severni_sirka = newLatitudes)
filtered_df = filtered_df.assign(vychodni_delka = newLongitudes)
filtered_df['severni_sirka'] = filtered_df['severni_sirka'].astype( 'float64' ).round( 6 )
filtered_df['vychodni_delka'] = filtered_df['vychodni_delka'].astype( 'float64' ).round( 6 )

filtered_df.to_csv( outputFile, encoding = encoding, sep = delimiter, decimal = decimal )

spravne = df[df['severni_sirka'].notna()]

spravne.to_csv( outputFile, encoding = encoding, sep = delimiter, decimal = decimal, mode = 'a', header = False )