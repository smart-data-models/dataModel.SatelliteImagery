Entité : EOAnalysis  
===================  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.SatelliteImagery/blob/master/EOAnalysis/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Description globale : **Cette entité contient une description harmonisée d'une EOAnalyse générique réalisée pour le domaine de l'imagerie satellitaire. Cette entité est principalement associée au processus d'analyse des applications d'observation de la Terre**.  

## Liste des propriétés  

- `address`: L'adresse postale  - `alternateName`: Un nom alternatif pour cet élément  - `analysisType`: Type d'analyse appliqué par l'entité.  - `analyzedAt`: L'heure à laquelle l'analyse s'est terminée  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `description`: Une description de cet article  - `id`: Identifiant unique de l'entité  - `isAnalysisOf`: L'identifiant du produit utilisé dans l'analyse.  - `location`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une ligne, d'un polygone, d'un point multiple, d'une ligne multiple ou d'un polygone multiple.  - `name`: Le nom de cet élément.  - `owner`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  - `provider`: Le fournisseur de l'algorithme  - `resultDescription`: La description du résultat de l'analyse.  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur l'élément  - `source`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.  - `type`: Type d'entité NGSI-LD. Il doit être égal à EOAnalysis.    
Propriétés requises  
- `analysisType`  - `id`  - `provider`  - `type`  ## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
EOAnalysis:    
  description: 'This entity contains a harmonised description of a generic EOAnalysis made for the Satellite Imagerry domain. This entity is primarily associated with the process of analysis of Earth Observation applications.'    
  properties:    
    address:    
      description: 'The mailing address'    
      properties:    
        addressCountry:    
          description: 'Property. The country. For example, Spain. Model:''https://schema.org/addressCountry'''    
          type: string    
        addressLocality:    
          description: 'Property. The locality in which the street address is, and which is in the region. Model:''https://schema.org/addressLocality'''    
          type: string    
        addressRegion:    
          description: 'Property. The region in which the locality is, and which is in the country. Model:''https://schema.org/addressRegion'''    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, 03578. Model:''https://schema.org/postOfficeBoxNumber'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, 24004. Model:''https://schema.org/https://schema.org/postalCode'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/streetAddress'''    
          type: string    
      type: Property    
      x-ngsi:    
        model: https://schema.org/address    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    analysisType:    
      description: 'Entity''s type of analysis applied.'    
      type: Property    
    analyzedAt:    
      description: 'The time at which the analysis finished'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Time    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    description:    
      description: 'A description of this item'    
      type: Property    
    id:    
      anyOf: &eoanalysis_-_properties_-_owner_-_items_-_anyof    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Unique identifier of the entity'    
      type: Property    
    isAnalysisOf:    
      description: 'The ID of the product that was used in the analysis'    
      format: uri    
      type: Relationship    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: 'Geoproperty. Geojson reference to the item. Point'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                type: number    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - Point    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON Point'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. LineString'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - LineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON LineString'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. Polygon'    
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
        - description: 'Geoproperty. Geojson reference to the item. MultiPoint'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPoint    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiPoint'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
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
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiLineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiLineString'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
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
                    items:    
                      type: number    
                    minItems: 2    
                    type: array    
                  minItems: 4    
                  type: array    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPolygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiPolygon'    
          type: object    
      type: Geoproperty    
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *eoanalysis_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    provider:    
      description: 'The provider of the algorithm'    
      type: Property    
      x-ngsi:    
        model: ' https://schema.org/Text'    
    resultDescription:    
      description: 'The description of the analysis outcome.'    
      type: Property    
    seeAlso:    
      description: 'list of uri pointing to additional resources about the item'    
      oneOf:    
        - items:    
            format: uri    
            type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
      type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    type:    
      description: 'NGSI-LD Entity Type. It must be equal to EOAnalysis.'    
      enum:    
        - EOAnalysis    
      type: Property    
  required:    
    - id    
    - type    
    - analysisType    
    - provider    
  type: object    
```  
</details>    
## Exemples de charges utiles  
#### EOAnalyse NGSI-v2 valeurs-clés Exemple  
Voici un exemple d'une EOAnalysis au format JSON-LD sous forme de valeurs-clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
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
#### EOAnalyse NGSI-v2 normalisée Exemple  
Voici un exemple d'une EOAnalysis au format JSON-LD tel que normalisé. Ce format est compatible avec la NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
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
    "value": "The detected oil covers 1000 square meters"  
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
          [  
            23.48993,  
            42.415  
          ],  
          [  
            23.66274,  
            42.415  
          ],  
          [  
            23.66274,  
            42.53524  
          ],  
          [  
            23.48993,  
            42.53524  
          ],  
          [  
            23.48993,  
            42.415  
          ]  
        ]  
      ]  
    }  
  }  
}  
```  
#### EOAnalyse des valeurs clés NGSI-LD Exemple  
Voici un exemple d'une EOAnalysis au format JSON-LD sous forme de valeurs-clés. Ceci est compatible avec NGSI-LD en utilisant `options=keyValues` et retourne les données contextuelles d'une entité individuelle.  
```json  
{  
  "id": "EOAnalysis:02",  
  "type": "EOAnalysis",  
  "analyzedAt": "2020-12-24T12:00:00Z",  
  "provider": "aqua3S/CERTH",  
  "resultDescription": "The detected oil covers 1000 square meters",  
  "analysisType": "Flood Detection",  
  "location": {  
    "type": "Polygon",  
    "coordinates": [  
      [  
        [  
          23.48993,  
          42.415  
        ],  
        [  
          23.66274,  
          42.415  
        ],  
        [  
          23.66274,  
          42.53524  
        ],  
        [  
          23.48993,  
          42.53524  
        ],  
        [  
          23.48993,  
          42.415  
        ]  
      ]  
    ]  
  },  
  "isAnalysisOf": "urn:ngsi-ld:EOProduct:123",  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
#### EOAnalyse NGSI-LD Exemple normalisé  
Voici un exemple d'une EOAnalysis au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
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
          [  
            23.6627,  
            41.88768  
          ],  
          [  
            25.85598,  
            43.38622  
          ],  
          [  
            23.4899,  
            43.78691  
          ],  
          [  
            22.35609,  
            42.28869  
          ],  
          [  
            23.6627,  
            41.88769  
          ]  
        ]  
      ]  
    }  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
