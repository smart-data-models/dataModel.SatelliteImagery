Entity: EODataHub  
=================  
[Open License](https://github.com/smart-data-models//dataModel.SatelliteImagery/blob/master/EODataHub/LICENSE.md)  
Global description: **This entity contains a harmonised description of a generic EOInstrument made for the Satellite Imagerry domain. This entity is primarily associated with the data hub related to Earth Observation Analysis applications.**  

## List of properties  

- `dataHubName`: A mandatory text string used to declare the name of the used data hub  - `dataHubURL`: A mandatory text string used to declare the url of the used data hub  - `type`: NGSI-LD Entity Type. It must be equal to EODataHub.    
Required properties  
- `dataHubName`  - `dataHubURL`  - `id`  - `type`  ## Data Model description of properties  
Sorted alphabetically (click for details)  
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
## Example payloads    
#### EODataHub NGSI V2 key-values Example    
Here is an example of a EODataHub in JSON format as key-values. This is compatible with NGSI V2 when  using `options=keyValues` and returns the context data of an individual entity.  
```json  
{  
  "id": "EODataHub:123",  
  "type": "EODataHub",  
  "dataHubName": "ESA Copernicus Open Access Hub",  
  "dataHubURL": "http://scihub.copernicus.eu"  
}  
```  
Not available the example of a EODataHub in JSON format as normalized. This is compatible with NGSI V2 when not using options and returns the context data of an individual entity.  
Not available the example of a EODataHub in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
#### EODataHub NGSI-LD normalized Example    
Here is an example of a EODataHub in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
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
