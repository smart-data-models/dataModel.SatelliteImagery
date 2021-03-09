Entidad: EOInstrumento  
======================  
[Licencia abierta](https://github.com/smart-data-models//dataModel.SatelliteImagery/blob/master/EOInstrument/LICENSE.md)  
Descripción global: **Esta entidad contiene una descripción armonizada de un EOInstrument genérico realizado para el dominio de Satagerry. Esta entidad está asociada principalmente a los instrumentos de satélite relacionados con las aplicaciones de análisis de la observación de la Tierra.**  

## Lista de propiedades  

- `carriedOn`: El ID de la plataforma de satélite en la que se transporta el instrumento  - `instrumentID`: Cadena de texto obligatoria utilizada para declarar el ID de la carga útil del instrumento  - `instrumentName`: Cadena de texto obligatoria utilizada para declarar el nombre de la carga útil del instrumento  - `operationalMode`: Una cadena de texto utilizada para declarar los modos de sensor soportados si están disponibles  - `polarizationMode`: Una cadena de texto utilizada para declarar los modos de polarización si están disponibles  - `swathID`: Una cadena de texto utilizada para declarar el ID de la hilera si está disponible  - `type`: Tipo de entidad NGSI-LD. Debe ser igual a EOInstrument.    
Propiedades requeridas  
- `id`  - `instrumentID`  - `instrumentName`  - `operationalMode`  - `type`  ## Descripción del modelo de datos de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
EOInstrument:    
  description: 'This entity contains a harmonised description of a generic EOInstrument made for the Satellite Imagerry domain. This entity is primarily associated with the satellite instruments related to Earth Observation Analysis applications.'    
  properties:    
    carriedOn:    
      description: 'The ID of the satellite platform that the instrument is carried on'    
      format: uri    
      type: Relationship    
    instrumentID:    
      description: 'A mandatory text string used to declare the ID of the instrument payload'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    instrumentName:    
      description: 'A mandatory text string used to declare the name of the instrument payload'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    operationalMode:    
      description: 'A text string used to declare the supported sensor modes if available'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    polarizationMode:    
      description: 'A text string used to declare the polarization modes if available'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    swathID:    
      description: 'A text string used to declare the swath ID if available'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    type:    
      description: 'NGSI-LD Entity Type. It must be equal to EOInstrument.'    
      enum:    
        - EOInstrument    
      type: Property    
  required:    
    - id    
    - type    
    - instrumentID    
    - instrumentName    
    - operationalMode    
  type: object    
```  
</details>    
## Ejemplo de carga útil  
#### EOInstrument NGSI V2 key-values Ejemplo  
Aquí hay un ejemplo de un EOInstrument en formato JSON como key-values. Esto es compatible con NGSI V2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "urn:ngsi-ld:EOInstrument:154",  
  "type": "EOInstrument",  
  "instrumentID": "OLCI",  
  "instrumentName": "Ocean Land Colour Instrument",  
  "operationalMode": "INS-NOBS",  
  "polarizationMode": "HH+HV",  
  "swathID": "S1",  
  "carriedOn": "urn:ngsi-ld:EOSatellitePlatform:154"  
}  
```  
No está disponible el ejemplo de un EOInstrumento en formato JSON como normalizado. Esto es compatible con NGSI V2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
No está disponible el ejemplo de un EOInstrument en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
#### EOInstrument NGSI-LD normalizado Ejemplo  
Este es un ejemplo de un EOInstrument en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "urn:ngsi-ld:EOInstrument:154",  
  "type": "EOInstrument",  
  "createdAt": "2020-03-13T15:42:00Z",  
  "modifiedAt": "2020-03-13T15:45:00Z",  
  "carriedOn": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:EOSatellitePlatform:154"  
  },  
  "instrumentID": {  
    "type": "Property",  
    "value": "SAR-C"  
  },  
  "instrumentName": {  
    "type": "Property",  
    "value": "Synthetic Aperture Radar (C-band)"  
  },  
  "operationalMode": {  
    "type": "Property",  
    "value": "IW"  
  },  
  "polarizaionMode": {  
    "type": "Property",  
    "value": "VV + VH"  
  },  
  "swathID": {  
    "type": "Property",  
    "value": "S1"  
  },  
  "@context": [  
    "https://schema.lab.fiware.org/ld/context"  
  ]  
}  
```  
