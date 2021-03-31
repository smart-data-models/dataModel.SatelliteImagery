Entité : EOProduct  
==================  
[Licence ouverte](https://github.com/smart-data-models//dataModel.SatelliteImagery/blob/master/EOProduct/LICENSE.md)  
Description globale : **Cette entité contient une description harmonisée d'un produit générique d'OPE réalisé pour le domaine de l'imagerie par satellite. Cette entité est principalement associée aux produits satellitaires liés aux applications d'analyse de l'observation de la Terre.**  

## Liste des biens  

- `areaLocation`:   - `cloudCoverage`: Le pourcentage de couverture nuageuse. Toutes les unités sont acceptées en code [CEFACT](https://www.unece.org/cefact.html).  - `ingestionDate`:   - `orbitDirection`: L'orientation de la passe d'orbite  - `orbitNumber`: Le numéro d'orbite du passage du satellite. Toutes les unités sont acceptées en code [CEFACT](https://www.unece.org/cefact.html).  - `processingLevel`: Une chaîne de texte obligatoire utilisée pour déclarer le niveau de transformation du produit  - `productFormat`: Une chaîne de texte obligatoire utilisée pour déclarer le format du produit  - `productID`: Une chaîne de texte obligatoire utilisée pour déclarer l'identification unique du produit  - `productType`: Une chaîne de texte obligatoire utilisée pour déclarer le type de produit  - `productURL`: Une url obligatoire utilisée pour déclarer le lien de téléchargement du produit  - `sensingDate`:   - `sensingStartedAt`:   - `sensingStoppedAt`:   - `timeliness`: L'opportunité du produit  - `type`: Type d'entité NGSI-LD. Il doit être égal à EOProduct.    
Propriétés requises  
- `areaLocation`  - `id`  - `processingLevel`  - `productFormat`  - `productID`  - `productType`  - `productURL`  - `type`  ## Modèle de données description des biens  
Classement par ordre alphabétique (cliquez pour plus de détails)  
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
## Exemples de charges utiles  
#### EOProduct NGSI V2 key-values Exemple  
Voici un exemple d'un produit EOP en format JSON comme valeurs clés. Il est compatible avec NGSI V2 lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:EOProduct:123",  
  "type": "EOProduct",  
  "productID": "S1B_IW_GRDH_1SDV_20210201T042950_20210201T043015_025408_0306B8_AE29",  
  "productURL": "https://scihub.copernicus.eu/dhus/odata/v1/Products('561d85c3-5627-4f78-84f7-05d0a0c8db9c')/$value",  
  "productType": "GRD",  
  "processingLevel": "L1",  
  "location": {  
    "type": "Polygon",  
    "coordinates": [  
      [  
        [ 25.4464, 41.887688 ],  
        [ 25.855984, 43.386223 ],  
        [ 22.690121, 43.786907 ],  
        [ 22.356091, 42.288685 ],  
        [ 25.4464, 41.887688 ]  
      ]  
    ]  
  },  
  "productFormat": "SAFE",  
  "timeliness": "Fast-24h",  
  "orbitDirection": "Descending",  
  "orbitNumber": 7,  
  "ingestionDate": "2021-02-01T08:26:25.020Z",  
  "sensingDate": "2021-02-01T04:29:50.264Z",  
  "sensingStartedAt": "2021-02-01T04:29:50.264Z",  
  "sensingStoppedAt": "2021-02-01T04:30:15.263Z",  
  "hostedOn": "urn:ngsi-ld:EODataHub:123",  
  "observedBy": "urn:ngsi-ld:EOInstrument:154"  
}  
```  
Non disponible l'exemple d'un EOProduct en format JSON comme normalisé. Il est compatible avec la version 2 du NGSI lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
Non disponible l'exemple d'un produit EOP en format JSON-LD comme valeurs clés. Il est compatible avec le format JSON-LD lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
#### EOProduit NGSI-LD normalisé Exemple  
Voici un exemple d'un produit EOP en format JSON-LD tel que normalisé. Ce format est compatible avec JSON-LD lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:EOProduct:123",  
  "type": "EOProduct",  
  "createdAt": "2020-03-13T15:42:00Z",  
  "modifiedAt": "2020-03-13T15:45:00Z",  
  "productID": {  
    "type": "Property",  
    "value": "S1B_IW_GRDH_1SDV_20210201T042950_20210201T043015_025408_0306B8_AE29"  
  },  
  "productURL": {  
    "type": "url",  
    "value": "https://scihub.copernicus.eu/dhus/odata/v1/Products('561d85c3-5627-4f78-84f7-05d0a0c8db9c')/$value"  
  },  
  "productType": {  
    "type": "Property",  
    "value": "GRD"  
  },  
  "processingLevel": {  
    "type": "Property",  
    "value": "L1"  
  },  
  "location": {  
    "type": "GeoProperty",  
    "value": {  
      "type": "Polygon",  
      "coordinates": [  
        [  
          [ 25.4464, 41.887688 ],  
          [ 25.855984, 43.386223 ],  
          [ 22.690121, 43.786907 ],  
          [ 22.356091, 42.288685 ],  
          [ 25.4464, 41.887688 ]  
        ]  
      ]  
    }  
  },  
  "productFormat": {  
    "type": "Property",  
    "value": "SAFE"  
  },  
  "timeliness": {  
    "type": "Property",  
    "value": "Fast-24h"  
  },  
  "orbitDirection": {  
    "type": "Property",  
    "value": "Descending"  
  },  
  "orbitNumber": {  
    "type": "Property",  
    "value": 7  
  },  
  "ingestionDate": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2021-02-01T08:26:25.020Z"  
    }  
  },  
  "sensingDate": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2021-02-01T04:29:50.264Z"  
    }  
  },  
  "sensingStartedAt": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2021-02-01T04:29:50.264Z"  
    }  
  },  
  "sensingStoppedAt": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2021-02-01T04:30:15.263Z"  
    }  
  },  
  "@context": [  
    "https://schema.lab.fiware.org/ld/context"  
  ]  
}  
```  
