Entity: EOProduct  
=================  
[Open License](https://github.com/smart-data-models//dataModel.SatelliteImagery/blob/master/EOProduct/LICENSE.md)  
Global description: **This entity contains a harmonised description of a generic EOProduct made for the Satellite Imagerry domain. This entity is primarily associated with the satellite products related to Earth Observation Analysis applications.**  

## List of properties  

- `areaLocation`:   - `cloudCoverage`: The cloud coverage percentage. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.  - `ingestionDate`:   - `orbitDirection`: The orbit pass orientation  - `orbitNumber`: The orbit number of tha satellite pass. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.  - `processingLevel`: A mandatory text string used to declare the processing level of the product  - `productFormat`: A mandatory text string used to declare the format of the product  - `productID`: A mandatory text string used to declare the unique ID of the product  - `productType`: A mandatory text string used to declare the type of the product  - `productURL`: A mandatory url used to declare the downlaod link of the product  - `sensingDate`:   - `sensingStartedAt`:   - `sensingStoppedAt`:   - `timeliness`: The timeliness of the product  - `type`: NGSI-LD Entity Type. It must be equal to EOProduct.    
Required properties  
- `areaLocation`  - `id`  - `processingLevel`  - `productFormat`  - `productID`  - `productType`  - `productURL`  - `type`  ## Data Model description of properties  
Sorted alphabetically (click for details)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
EOProduct:    
  description: 'This entity contains a harmonised description of a generic EOProduct made for the Satellite Imagerry domain. This entity is primarily associated with the satellite products related to Earth Observation Analysis applications.'    
  properties:    
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
    cloudCoverage:    
      description: 'The cloud coverage percentage. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.'    
      type: Property    
      x-ngsi:    
        model: ' https://schema.org/Number'    
        units: percent    
    ingestionDate:    
      format: date-time    
      type: string    
    orbitDirection:    
      description: 'The orbit pass orientation'    
      enum:    
        - Ascending    
        - Descending    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    orbitNumber:    
      description: 'The orbit number of tha satellite pass. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.'    
      type: Property    
      x-ngsi:    
        model: ' https://schema.org/Number'    
        units: 'No unit'    
    processingLevel:    
      description: 'A mandatory text string used to declare the processing level of the product'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    productFormat:    
      description: 'A mandatory text string used to declare the format of the product'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    productID:    
      description: 'A mandatory text string used to declare the unique ID of the product'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    productType:    
      description: 'A mandatory text string used to declare the type of the product'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    productURL:    
      description: 'A mandatory url used to declare the downlaod link of the product'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/url    
    sensingDate:    
      format: date-time    
      type: string    
    sensingStartedAt:    
      format: date-time    
      type: string    
    sensingStoppedAt:    
      format: date-time    
      type: string    
    timeliness:    
      description: 'The timeliness of the product'    
      enum:    
        - 'Time critical'    
        - 'Not time critical'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    type:    
      description: 'NGSI-LD Entity Type. It must be equal to EOProduct.'    
      enum:    
        - EOProduct    
      type: Property    
  required:    
    - id    
    - type    
    - productType    
    - productID    
    - productURL    
    - processingLevel    
    - productFormat    
    - areaLocation    
  type: object    
```  
</details>    
## Example payloads    
#### EOProduct NGSI V2 key-values Example    
Here is an example of a EOProduct in JSON format as key-values. This is compatible with NGSI V2 when  using `options=keyValues` and returns the context data of an individual entity.  
```json  
{  
  "id": "urn:ngsi-ld:EOProduct:123",  
  "type": "EOProduct",  
  "productID": "S3B_OL_1_ERR____20201120T143017_20201120T151432_20201121T182138_2655_046_039______LN1_O_NT_002",  
  "productURL": "https://scihub.copernicus.eu/dhus/odata/v1/Products('af2b183a-e0d5-422d-be8a-eafee42ba5b1')/$value",  
  "productType": "OL_1_ERR___",  
  "processingLevel": "L1",  
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
  },  
  "productFormat": "SAFE",  
  "cloudCoverage": 25,  
  "timeliness": "Not time critical",  
  "orbitDirection": "Ascending",  
  "orbitNumber": 111,  
  "ingestionDate": "2020-12-24T12:00:00Z",  
  "sensingDate": "2020-12-24T12:00:00Z",  
  "sensingStartedAt": "2020-12-24T12:00:00Z",  
  "sensingStoppedAt": "2020-12-24T12:00:00Z"  
}  
```  
Not available the example of a EOProduct in JSON format as normalized. This is compatible with NGSI V2 when not using options and returns the context data of an individual entity.  
Not available the example of a EOProduct in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
#### EOProduct NGSI-LD normalized Example    
Here is an example of a EOProduct in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
```json  
{  
  "id": "urn:ngsi-ld:EOProduct:123",  
  "type": "EOProduct",  
  "createdAt": "2020-03-13T15:42:00Z",  
  "modifiedAt": "2020-03-13T15:45:00Z",  
  "productID": {  
    "type": "Property",  
    "value": "S3B_OL_1_ERR____20201120T143017_20201120T151432_20201121T182138_2655_046_039______LN1_O_NT_002"  
  },  
  "productURL": {  
    "type": "url",  
    "value": "https://scihub.copernicus.eu/dhus/odata/v1/Products('af2b183a-e0d5-422d-be8a-eafee42ba5b1')/$value"  
  },  
  "productType": {  
    "type": "Property",  
    "value": "OL_1_ERR___"  
  },  
  "processingLevel": {  
    "type": "Property",  
    "value": "L1"  
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
        [  
          -70.75,  
          43.08  
        ],  
        [  
          -67.137,  
          45.13  
        ]  
      ]  
    }  
  },  
  "productFormat": {  
    "type": "Property",  
    "value": "SAFE"  
  },  
  "cloudCoverage": {  
    "type": "Property",  
    "value": 25,  
    "unitCode": "P1"  
  },  
  "timeliness": {  
    "type": "Property",  
    "value": "Non Time Critical"  
  },  
  "orbitDirection": {  
    "type": "Property",  
    "value": [ "Ascending", "Descending" ]  
  },  
  "orbitNumber": {  
    "type": "Property",  
    "value": 111  
  },  
  "ingestionDate": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2020-12-24T12:00:00Z"  
    }  
  },  
  "sensingDate": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2020-12-24T12:00:00Z"  
    }  
  },  
  "sensingStartedAt": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2020-12-24T12:00:00Z"  
    }  
  },  
  "sensingStoppedAt": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2020-12-24T12:00:00Z"  
    }  
  },  
  "@context": [  
    "https://schema.lab.fiware.org/ld/context"  
  ]  
}  
```  
