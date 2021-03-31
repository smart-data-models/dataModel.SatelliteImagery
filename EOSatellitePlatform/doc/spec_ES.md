Entidad: EOSatellitePlatform  
============================  
[Licencia abierta](https://github.com/smart-data-models//dataModel.SatelliteImagery/blob/master/EOSatellitePlatform/LICENSE.md)  
Descripción global: **Esta entidad contiene una descripción armonizada de una EOSatellitePlatform genérica realizada para el dominio de Satagerry. Esta entidad está asociada principalmente a las plataformas de satélite relacionadas con las aplicaciones de análisis de la observación de la Tierra.**  

## Lista de propiedades  

- `platformID`: Cadena de texto obligatoria utilizada para declarar el ID único de la plataforma  - `platformNSSDCA`: Cadena de texto obligatoria utilizada para declarar el identificador único de la misión en el Archivo del Centro Nacional de Datos Científicos del Espacio  - `platformName`: Una cadena de texto obligatoria utilizada para declarar el nombre de la plataforma  - `type`: Tipo de entidad NGSI-LD. Debe ser igual a EOSatellitePlatform.    
Propiedades requeridas  
- `id`  - `platformID`  - `platformNSSDCA`  - `platformName`  - `type`  ## Descripción del modelo de datos de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
EOSatellitePlatform:    
  description: 'This entity contains a harmonised description of a generic EOSatellitePlatform made for the Satellite Imagerry domain. This entity is primarily associated with the Satellite platforms related to Earth Observation Analysis applications.'    
  properties:    
    platformID:    
      description: 'A mandatory text string used to declare the unique ID of the platform'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    platformNSSDCA:    
      description: 'A mandatory text string used to declare the unique mission id in the National Space Science Data Center Archive'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    platformName:    
      description: 'A mandatory text string used to declare the name of the platform'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    type:    
      description: 'NGSI-LD Entity Type. It must be equal to EOSatellitePlatform.'    
      enum:    
        - EOSatellitePlatform    
      type: Property    
  required:    
    - id    
    - type    
    - platformID    
    - platformName    
    - platformNSSDCA    
  type: object    
```  
</details>    
## Ejemplo de carga útil  
#### EOSatellitePlatform NGSI V2 key-values Ejemplo  
Aquí hay un ejemplo de un EOSatellitePlatform en formato JSON como key-values. Esto es compatible con NGSI V2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "urn:ngsi-ld:EOSatellitePlatform:154",  
  "type": "EOSatellitePlatform",  
  "platformID": "B",  
  "platformName": "Sentinel-1",  
  "platformNSSDCA": "2016-025A"  
}  
```  
No está disponible el ejemplo de un EOSatellitePlatform en formato JSON normalizado. Esto es compatible con NGSI V2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
No está disponible el ejemplo de una EOSatellitePlatform en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
#### EOSatellitePlatform NGSI-LD normalizado Ejemplo  
Este es un ejemplo de un EOSatellitePlatform en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "urn:ngsi-ld:EOSatellitePlatform:154",  
  "type": "EOSatellitePlatform",  
  "createdAt": "2020-03-13T15:42:00Z",  
  "modifiedAt": "2020-03-13T15:45:00Z",  
  "platformID": {  
    "type": "Property",  
    "value": "B"  
  },  
  "platformName": {  
    "type": "Property",  
    "value": "Sentinel-1"  
  },  
  "platformNSSDCA": {  
    "type": "Property",  
    "value": "2016-025A"  
  },  
  "@context": [  
    "https://schema.lab.fiware.org/ld/context"  
  ]  
}  
```  
