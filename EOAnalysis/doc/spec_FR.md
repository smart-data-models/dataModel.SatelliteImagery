Entité : EOAnalysis  
===================  
[Licence ouverte](https://github.com/smart-data-models//dataModel.SatelliteImagery/blob/master/EOAnalysis/LICENSE.md)  
Description globale : **Cette entité contient une description harmonisée d'une analyse générique de l'orbite effectuée pour le domaine de l'imagerie par satellite. Cette entité est principalement associée au processus d'analyse des applications d'observation de la Terre.**  

## Liste des biens  

- `analysedAt`: L'heure à laquelle l'analyse s'est terminée  - `analysisType`: Le type d'analyse de l'entité appliquée.  - `areaLocation`:   - `isAnalysisOf`: L'identification du produit qui a été utilisé dans l'analyse  - `provider`: Le fournisseur de l'algorithme  - `resultValues`: Explication des valeurs de sortie de l'entité.  - `type`: Type d'entité NGSI-LD. Il doit être égal à EOAnalysis.    
Propriétés requises  
- `analysedAt`  - `analysisType`  - `areaLocation`  - `id`  - `provider`  - `resultValues`  - `type`  ## Modèle de données description des biens  
Classement par ordre alphabétique (cliquez pour plus de détails)  
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
## Exemples de charges utiles  
#### EOAnalysis NGSI V2 key-values Example  
Voici un exemple d'analyse d'émissions en format JSON en tant que valeurs clés. Il est compatible avec NGSI V2 lorsque l'on utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
  "id": "EOAnalysis:02",  
  "type": "EOAnalysis",  
  "analyzedAt": "2020-12-24T12:00:00Z",  
  "provider": "aqua3S/CERTH",  
  "resultDescription": "The detected flooded areas cover 1000 square meters",  
  "analysisType": "Flood Detection",  
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
  "isAnalysisOf": "urn:ngsi-ld:EOProduct:123"  
}  
```  
Non disponible l'exemple d'une analyse d'urine en format JSON comme normalisé. Il est compatible avec NGSI V2 lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
Non disponible l'exemple d'une analyse d'émissions en format JSON-LD comme valeurs clés. Il est compatible avec le format NGSI-LD lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
#### EOAnalysis NGSI-LD normalisé Exemple  
Voici un exemple d'une analyse d'urine en format JSON-LD normalisé. Ce format est compatible avec le format JSON-LD lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:EOAnalysis:02",  
  "type": "EOAnalysis",  
  "createdAt": "2020-03-13T15:42:00Z",  
  "modifiedAt": "2020-03-13T15:45:00Z",  
  "analyzedAt": {  
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
    "value": "aqua3S/CERTH"  
  },  
  "resultDescription": {  
    "type": "Property",  
    "value": "The detected flooded areas cover 1000 square meters"  
  },  
  "analysisType": {  
    "type": "Property",  
    "value": "Flood Detection"  
  },  
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
