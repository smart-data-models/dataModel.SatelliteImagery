Entity: EOSatellitePlatform  
===========================  
[Open License](https://github.com/smart-data-models//dataModel.SatelliteImagery/blob/master/EOSatellitePlatform/LICENSE.md)  
Global description: **This entity contains a harmonised description of a generic EOSatellitePlatform made for the Satellite Imagerry domain. This entity is primarily associated with the Satellite platforms related to Earth Observation Analysis applications.**  

## List of properties  

- `platformID`: A mandatory text string used to declare the unique ID of the platform  - `platformNSSDCA`: A mandatory text string used to declare the unique mission id in the National Space Science Data Center Archive  - `platformName`: A mandatory text string used to declare the name of the platform  - `type`: NGSI-LD Entity Type. It must be equal to EOSatellitePlatform.    
Required properties  
- `id`  - `platformID`  - `platformNSSDCA`  - `platformName`  - `type`  ## Data Model description of properties  
Sorted alphabetically (click for details)  
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
## Example payloads    
#### EOSatellitePlatform NGSI V2 key-values Example    
Here is an example of a EOSatellitePlatform in JSON format as key-values. This is compatible with NGSI V2 when  using `options=keyValues` and returns the context data of an individual entity.  
```json  
{  
  "id": "urn:ngsi-ld:EOSatellitePlatform:154",  
  "type": "EOSatellitePlatform",  
  "operator": "European Space Agency",  
  "platformID": "A",  
  "platformName": "Sentinel-1",  
  "platformNSSDCA": "2018-039A"  
}  
```  
Not available the example of a EOSatellitePlatform in JSON format as normalized. This is compatible with NGSI V2 when not using options and returns the context data of an individual entity.  
Not available the example of a EOSatellitePlatform in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
#### EOSatellitePlatform NGSI-LD normalized Example    
Here is an example of a EOSatellitePlatform in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
```json  
{  
  "id": "urn:ngsi-ld:EOSatellitePlatform:154",  
  "type": "EOSatellitePlatform",  
  "createdAt": "2020-03-13T15:42:00Z",  
  "modifiedAt": "2020-03-13T15:45:00Z",  
  "operator": {  
    "type": "Property",  
    "value": "European Space Agency"  
  },  
  "platformID": {  
    "type": "Property",  
    "value": "A"  
  },  
  "platformName": {  
    "type": "Property",  
    "value": "Sentinel-1"  
  },  
  "platformNSSDCA": {  
    "type": "Property",  
    "value": "2018-039A"  
  },  
  "@context": [  
    "https://schema.lab.fiware.org/ld/context"  
  ]  
}  
```  
