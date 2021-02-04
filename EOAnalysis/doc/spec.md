Entity: EOAnalysis  
==================  
[Open License](https://github.com/smart-data-models//dataModel.SatelliteImagery/blob/master/EOAnalysis/LICENSE.md)  
Global description: **This entity contains a harmonised description of a generic EOAnalysis made for the Satellite Imagerry domain. This entity is primarily associated with the process of analysis of Earth Observation applications.**  

## List of properties  

- `analysedAt`: The time at which the analysis finished  - `analysisType`: Entity's type of analysis applied.  - `areaLocation`:   - `isAnalysisOf`: The ID of the product that was used in the analysis  - `provider`: The provider of the algorithm  - `resultValues`: Entity's output values explanation.  - `type`: NGSI-LD Entity Type. It must be equal to EOAnalysis.    
Required properties  
- `analysedAt`  - `analysisType`  - `areaLocation`  - `id`  - `provider`  - `resultValues`  - `type`  ## Data Model description of properties  
Sorted alphabetically (click for details)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
EOAnalysis:    
  description: 'This entity contains a harmonised description of a generic EOAnalysis made for the Satellite Imagerry domain. This entity is primarily associated with the process of analysis of Earth Observation applications.'    
  properties:    
    analysedAt:    
      description: 'The time at which the analysis finished'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Time    
    analysisType:    
      description: 'Entity''s type of analysis applied.'    
      enum:    
        - 'Oil spill detection'    
        - 'Flood detection'    
        - 'Alge bloom detection'    
      type: Property    
    areaLocation:    
      $id: https://geojson.org/schema/Polygon.json    
      $schema: "http://json-schema.org/draft-07/schema#"    
      properties:    
        bbox:    
          items:    
            type: number    
          minItems: 4    
          type: array    
        coordinates:    
          items:    
            items:    
              items:    
                type: number    
              minItems: 2    
              type: array    
            minItems: 4    
            type: array    
          type: array    
        type:    
          enum:    
            - Polygon    
          type: string    
      required:    
        - type    
        - coordinates    
      title: 'GeoJSON Polygon'    
      type: object    
    isAnalysisOf:    
      description: 'The ID of the product that was used in the analysis'    
      format: uri    
      type: Relationship    
    provider:    
      description: 'The provider of the algorithm'    
      type: Property    
      x-ngsi:    
        model: ' https://schema.org/Text'    
        units: 'No unit'    
    resultValues:    
      description: 'Entity''s output values explanation.'    
      items:    
        type: string    
      type: Property    
    type:    
      description: 'NGSI-LD Entity Type. It must be equal to EOAnalysis.'    
      enum:    
        - EOAnalysis    
      type: Property    
  required:    
    - id    
    - type    
    - analysedAt    
    - provider    
    - resultValues    
    - analysisType    
    - areaLocation    
  type: object    
```  
</details>    
## Example payloads    
#### EOAnalysis NGSI V2 key-values Example    
Here is an example of a EOAnalysis in JSON format as key-values. This is compatible with NGSI V2 when  using `options=keyValues` and returns the context data of an individual entity.  
```json  
{  
  "id": "EOAnalysis:03",  
  "type": "EOAnalysis",  
  "analysedAt": "2020-12-24T12:00:00Z",  
  "provider": "AQUA3s/CERTH",  
  "resultValues": [  
    "0:flooded",  
    "1:not flooded"  
  ],  
  "analysisType": "Flood detection",  
  "areaLocation": {  
    "type": "Polygon",  
    "coordinates": [  
      [  
        [  
          -67.137,  
          45.13  
        ],  
        [  
          -66.964,  
          44.8097  
        ],  
        [  
          -68.052,  
          44.3252  
        ],  
        [  
          -70.75,  
          43.08  
        ],  
        [  
          -67.137,  
          45.13  
        ]  
      ]  
    ]  
  }  
}  
```  
Not available the example of a EOAnalysis in JSON format as normalized. This is compatible with NGSI V2 when not using options and returns the context data of an individual entity.  
Not available the example of a EOAnalysis in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
#### EOAnalysis NGSI-LD normalized Example    
Here is an example of a EOAnalysis in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
```json  
{  
  "id": "urn:ngsi-ld:EOAnalysis:02",  
  "type": "EOAnalysis",  
  "createdAt": "2020-03-13T15:42:00Z",  
  "modifiedAt": "2020-03-13T15:45:00Z",  
  "analysedAt": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2020-12-24T12:00:00Z"  
    }  
  },  
  "isAnalysisOf": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:EOProduct:123"  
  },  
  "provider": {  
    "type": "Property",  
    "value": "AQUA3s/CERTH"  
  },  
  "resultValues": {  
    "type": "Property",  
    "value": [ "0:flooded", "1:not flooded" ]  
  },  
  "analysisType": {  
    "type": "Property",  
    "value": [ "Oil spill detection", "Flood detection", "Alge bloom detection" ]  
  },  
  "areaLocation": {  
    "type": "GeoProperty",  
    "value": {  
      "type": "Polygon",  
      "coordinates": [  
        [  
          -67.137,  
          45.13  
        ],  
        [  
          -66.964,  
          44.8097  
        ],  
        [  
          -68.052,  
          44.3252  
        ],  
        [ -70.75,  
          43.08   
        ],  
        [ -67.137,  
          45.13  
        ]  
      ]  
    }  
  },  
  "@context": [  
    "https://schema.lab.fiware.org/ld/context"  
  ]  
}  
```  
