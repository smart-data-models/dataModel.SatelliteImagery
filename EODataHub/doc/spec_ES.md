Entidad: EODataHub  
==================  
[Licencia abierta](https://github.com/smart-data-models//dataModel.SatelliteImagery/blob/master/EODataHub/LICENSE.md)  
Descripción global: **Esta entidad contiene una descripción armonizada de un EOInstrument genérico realizado para el dominio de Satagerry. Esta entidad se asocia principalmente con el centro de datos relacionado con las aplicaciones de análisis de la observación de la Tierra.**  

## Lista de propiedades  

- `dataHubName`: Una cadena de texto obligatoria utilizada para declarar el nombre del centro de datos utilizado  - `dataHubURL`: Una cadena de texto obligatoria utilizada para declarar la url del centro de datos utilizado  - `type`: Tipo de entidad NGSI-LD. Debe ser igual a EODataHub.    
Propiedades requeridas  
- `dataHubName`  - `dataHubURL`  - `id`  - `type`  ## Descripción del modelo de datos de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
EODataHub:    
  description: 'This entity contains a harmonised description of a generic EOInstrument made for the Satellite Imagerry domain. This entity is primarily associated with the data hub related to Earth Observation Analysis applications.'    
  properties:    
    dataHubName:    
      description: 'A mandatory text string used to declare the name of the used data hub'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    dataHubURL:    
      description: 'A mandatory text string used to declare the url of the used data hub'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/url    
    type:    
      description: 'NGSI-LD Entity Type. It must be equal to EODataHub.'    
      enum:    
        - EODataHub    
      type: Property    
  required:    
    - id    
    - type    
    - dataHubName    
    - dataHubURL    
  type: object    
```  
</details>    
## Ejemplo de carga útil  
#### EODataHub NGSI V2 key-values Ejemplo  
Aquí hay un ejemplo de un EODataHub en formato JSON como key-values. Esto es compatible con NGSI V2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "EODataHub:123",  
  "type": "EODataHub",  
  "dataHubName": "ESA Copernicus Open Access Hub",  
  "dataHubURL": "http://scihub.copernicus.eu"  
}  
```  
No está disponible el ejemplo de un EODataHub en formato JSON como normalizado. Esto es compatible con NGSI V2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
No está disponible el ejemplo de un EODataHub en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
#### EODataHub NGSI-LD normalizado Ejemplo  
Aquí hay un ejemplo de un EODataHub en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{  
    "id": "urn:ngsi-ld:EODataHub:123",  
    "type": "EODataHub",  
    "createdAt": "2020-03-13T15:42:00Z",  
    "modifiedAt": "2020-03-13T15:45:00Z",  
    "dataHubName": {  
        "type": "Property",  
        "value": "ESA Copernicus Open Access Hub"  
    },  
    "dataHubURL": {  
        "type": "url",  
        "value": "http://scihub.copernicus.eu"  
    },  
    "@context": [  
        "https://schema.lab.fiware.org/ld/context"  
    ]  
}  
```  
