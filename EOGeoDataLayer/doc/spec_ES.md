Entidad: EOGeoDataLayer  
=======================  
[Licencia abierta](https://github.com/smart-data-models//dataModel.SatelliteImagery/blob/master/EOGeoDataLayer/LICENSE.md)  
Descripción global: **Esta entidad contiene una descripción armonizada de una EOGeoDataLayer genérica realizada para el dominio de Satellite Imagerry. Esta entidad se asocia principalmente a las capas de datos de salida relacionadas con las aplicaciones de análisis de observación de la Tierra.**  

## Lista de propiedades  

- `areaLocation`:   - `isOutputOf`: El ID del análisis que se realizó para extraer esta capa de datos  - `localServerPath`: Una cadena de texto obligatoria utilizada para declarar la ruta en la que se guarda la capa de datos de salida en el servidor  - `metadata`: Metadatos. Contiene los metadatos principales de la capa de datos de los productos  - `storageFormat`: Formato de saturación de la entidad.  - `type`: Tipo de entidad NGSI-LD. Debe ser igual a EOGeoDataLayer.    
Propiedades requeridas  
- `areaLocation`  - `id`  - `localServerPath`  - `metadata`  - `storageFormat`  - `type`  ## Descripción del modelo de datos de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
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
## Ejemplo de carga útil  
#### EOGeoDataLayer NGSI V2 key-values Ejemplo  
Aquí hay un ejemplo de un EOGeoDataLayer en formato JSON como valores-clave. Esto es compatible con NGSI V2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "urn:ngsi-ld:EOGeoDataLayer:1",  
  "type": "EOGeoDataLayer",  
  "localServerPath": "/data/www/water_mask.tif",  
  "storageFormat": "GeoTIFF",  
  "geoMetadata": "/data/www/metadata.xml",  
  "contentInformation": [  
    {  
      "layer_name": "band1",  
      "layer_categorization": "categorical",  
      "values_explanation": [ "1:inundated", "0:non inundated" ]  
    }  
  ],  
  "location": {  
    "type": "Polygon",  
    "coordinates": [  
      [  
        [ 23.6627, 41.88768 ],  
        [ 25.85598, 43.38622 ],  
        [ 23.4899, 43.78691 ],  
        [ 22.35609, 42.28869 ],  
        [ 23.6627, 41.88769 ]  
      ]  
    ]  
  },  
  "isOutputOf": "EOAnalysis:02"  
}  
```  
No está disponible el ejemplo de un EOGeoDataLayer en formato JSON como normalizado. Esto es compatible con NGSI V2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
No está disponible el ejemplo de un EOGeoDataLayer en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
#### EOGeoDataLayer NGSI-LD normalizado Ejemplo  
Este es un ejemplo de un EOGeoDataLayer en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{  
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
    "value": "GeoTIFF",  
    "description": "Property. Model:'https://schema.org/Text'. The format of the processed data layer"  
  },  
  "geoMetadata": {  
    "type": "Property",  
    "value": "/data/www/metadata.xml"  
  },  
  "contentInformation": {[  
    {  
      "layer_name": "band1",  
      "layer_categorization": "categorical",  
      "values_explanation": [ "1:inundated", "0:non inundated" ]  
    }  
  ]},  
  "location": {  
    "type": "GeoProperty",  
    "value": {  
      "type": "Polygon",  
      "coordinates": [  
        [  
          [ 23.6627, 41.88768 ],  
          [ 25.85598, 43.38622 ],  
          [ 23.4899, 43.78691 ],  
          [ 22.35609, 42.28869 ],  
          [ 23.6627, 41.88769 ]  
        ]  
      ]  
    }  
  },  
  "@context": [  
    "https://schema.lab.fiware.org/ld/context"  
  ]  
}  
```  
