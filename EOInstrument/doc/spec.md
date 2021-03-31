Entity: EOInstrument  
====================  
[Open License](https://github.com/smart-data-models//dataModel.SatelliteImagery/blob/master/EOInstrument/LICENSE.md)  
Global description: **This entity contains a harmonised description of a generic EOInstrument made for the Satellite Imagerry domain. This entity is primarily associated with the satellite instruments related to Earth Observation Analysis applications.**  

## List of properties  

- `carriedOn`: The ID of the satellite platform that the instrument is carried on  - `instrumentID`: A mandatory text string used to declare the ID of the instrument payload  - `instrumentName`: A mandatory text string used to declare the name of the instrument payload  - `operationalMode`: A text string used to declare the supported sensor modes if available  - `polarizationMode`: A text string used to declare the polarization modes if available  - `swathID`: A text string used to declare the swath ID if available  - `type`: NGSI-LD Entity Type. It must be equal to EOInstrument.    
Required properties  
- `id`  - `instrumentID`  - `instrumentName`  - `operationalMode`  - `type`  ## Data Model description of properties  
Sorted alphabetically (click for details)  
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
## Example payloads    
#### EOInstrument NGSI V2 key-values Example    
Here is an example of a EOInstrument in JSON format as key-values. This is compatible with NGSI V2 when  using `options=keyValues` and returns the context data of an individual entity.  
```json  
{  
  "id": "urn:ngsi-ld:EOInstrument:154",  
  "type": "EOInstrument",  
  "instrumentID": "OLCI",  
  "instrumentName": "Ocean Land Colour Instrument",  
  "operationalMode": "INS-NOBS",  
  "polarizaionMode": "HH+HV",  
  "swathID": "S1",  
  "carriedOn": "urn:ngsi-ld:EOSatellitePlatform:154"  
}  
```  
Not available the example of a EOInstrument in JSON format as normalized. This is compatible with NGSI V2 when not using options and returns the context data of an individual entity.  
Not available the example of a EOInstrument in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
#### EOInstrument NGSI-LD normalized Example    
Here is an example of a EOInstrument in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
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
    "value": "OLCI"  
  },  
  "instrumentName": {  
    "type": "Property",  
    "value": "Ocean Land Colour Instrument"  
  },  
  "operationalMode": {  
    "type": "Property",  
    "value": "INS-NOBS"  
  },  
  "polarizaionMode": {  
    "type": "Property",  
    "value": "HH+HV"  
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
