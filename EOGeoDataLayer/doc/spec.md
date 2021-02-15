Entity: EOGeoDataLayer  
======================







- `areaLocation`  

<details><summary><strong>full yaml details</strong></summary>    

EOGeoDataLayer:    
  description: 'This entity contains a harmonised description of a generic EOGeoDataLayer made for the Satellite Imagerry domain. This entity is primarily associated with the output data layers related to Earth Observation Analysis applications.'    
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
    isOutputOf:    
      description: 'The ID of the analysis that was performed to extract this data layer'    
      format: uri    
      type: Relationship    
    localServerPath:    
      description: 'A mandatory text string used to declare the path that the output data layer is saved on the server'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    metadata:    
      allOf:    
        - crs:    
            description: 'Property. Model:''https://schema.org/Text''. A mandatory text string used to declare the crs of the output data layer'    
            type: string    
          required:    
            - crs    
      description: 'Metadata. Contains core metadata of the produces data layer'    
      enum:    
        - https://inspire.ec.europa.eu/id/document/tg/ef    
        - https://inspire.ec.europa.eu/id/document/tg/am    
    storageFormat:    
      description: 'Entity''s satorage format.'    
      enum:    
        - GeoTIFF    
        - Shapefile    
      type: Property    
    type:    
      description: 'NGSI-LD Entity Type. It must be equal to EOGeoDataLayer.'    
      enum:    
        - EOGeoDataLayer    
      type: Property    
  required:    
    - id    
    - type    
    - localServerPath    
    - storageFormat    
    - areaLocation    
    - metadata    
  type: object    
```  
</details>    





  "id": "urn:ngsi-ld:EOGeoDataLayer:1",  
  "type": "EOGeoDataLayer",  
  "localServerPath": "/data/www/water_mask.tif",  
  "storageFormat": "GeoTIFF",  
  "areaLocation": {  
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
  },  
  "metadata": {  
    "type": "Property",  
    "value": [ "https://inspire.ec.europa.eu/id/document/tg/ef", "https://inspire.ec.europa.eu/id/document/tg/am" ],  
    "crs": {  
      "type": "Property",  
      "value": "EPSG:4326"  
    }  
  }  
}  
```  






  "id": "urn:ngsi-ld:EOGeoDataLayer:1",  
  "type": "EOGeoDataLayer",  
  "createdAt": "2020-03-13T15:42:00Z",  
  "modifiedAt": "2020-03-13T15:45:00Z",  
  "isOutputOf": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:EOAnalysis:02"  
  },  
  "localServerPath": {  
    "type": "Property",  
    "value": "/data/www/water_mask.tif"  
  },  
  "storageFormat": {  
    "type": "string",  
    "value": [ "GeoTIFF", "ESRI Shapefile"],  
    "description": "Property. Model:'https://schema.org/Text'. The format of the processed data layer"  
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
  "metadata": {  
    "type": "Property",  
    "value": [ "https://inspire.ec.europa.eu/id/document/tg/ef", "https://inspire.ec.europa.eu/id/document/tg/am" ],  
    "crs": {  
      "type": "Property",  
      "value": "EPSG:4326"  
    }  
  },  
  "@context": [  
    "https://schema.lab.fiware.org/ld/context"  
  ]  
}  
```  