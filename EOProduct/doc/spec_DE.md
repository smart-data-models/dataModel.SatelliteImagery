Entität: EOProdukt  
==================  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.SatelliteImagery/blob/master/EOProduct/LICENSE.md)  
Globale Beschreibung: **Diese Entität enthält eine harmonisierte Beschreibung eines generischen EOProdukts, das für die Domäne "Satellitenbilder" erstellt wurde. Diese Entität ist in erster Linie mit den Satellitenprodukten im Zusammenhang mit Erdbeobachtungsanalyseanwendungen verbunden.**  

## Liste der Eigenschaften  

- `areaLocation`:   - `cloudCoverage`: Der Prozentsatz der Wolkenbedeckung. Alle Einheiten werden im Code [CEFACT](https://www.unece.org/cefact.html) akzeptiert.  - `ingestionDate`:   - `orbitDirection`: Die Orientierung des Orbitpasses  - `orbitNumber`: Die Orbitnummer des Satellitendurchgangs. Alle Einheiten werden im Code [CEFACT](https://www.unece.org/cefact.html) akzeptiert.  - `processingLevel`: Eine obligatorische Textzeichenfolge, die zur Angabe der Verarbeitungsstufe des Produkts verwendet wird  - `productFormat`: Eine obligatorische Textzeichenfolge, die das Format des Produkts angibt  - `productID`: Eine obligatorische Textzeichenfolge, die zur Angabe der eindeutigen ID des Produkts verwendet wird  - `productType`: Eine obligatorische Textzeichenfolge, die zur Deklaration des Produkttyps verwendet wird  - `productURL`: Eine obligatorische URL, die verwendet wird, um den Downlaod-Link des Produkts anzugeben  - `sensingDate`:   - `sensingStartedAt`:   - `sensingStoppedAt`:   - `timeliness`: Die Aktualität des Produkts  - `type`: NGSI-LD Entity Type. Er muss gleich EOProduct sein.    
Erforderliche Eigenschaften  
- `areaLocation`  - `id`  - `processingLevel`  - `productFormat`  - `productID`  - `productType`  - `productURL`  - `type`  ## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
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
## Beispiel-Nutzlasten  
#### EOProdukt NGSI-v2 Schlüsselwerte Beispiel  
Hier ist ein Beispiel für ein EOProdukt im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-v2 bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
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
#### EOProdukt NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für ein EOProdukt im JSON-LD-Format wie normalisiert. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
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
    "type": "Property",  
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
  }  
}  
```  
#### EOProdukt NGSI-LD Schlüsselwerte Beispiel  
Hier ist ein Beispiel für ein EOProdukt im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-LD bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "urn:ngsi-ld:EOProduct:123",  
  "type": "EOProduct",  
  "productID": "S2A_MSIL2A_20210118T092321_N0214_R093_T34TGN_20210118T120704",  
  "productURL": "https://scihub.copernicus.eu/dhus/odata/v1/Products('698c2089-704f-4d4f-aa2f-977902e2d35e')/$value",  
  "productType": "S2MSI2A",  
  "processingLevel": "Level-2A",  
  "location": {  
    "type": "Polygon",  
    "coordinates": [  
      [  
        [  
          24.7578584453215,  
          42.3024516155518  
        ],  
        [  
          24.8181237036864,  
          43.2890817991595  
        ],  
        [  
          23.4662891411315,  
          43.3262569717781  
        ],  
        [  
          23.4272955487519,  
          42.3383721018908  
        ],  
        [  
          24.7578584453215,  
          42.3024516155518  
        ]  
      ]  
    ]  
  },  
  "productFormat": "SAFE",  
  "cloudCoverage": 19.125499,  
  "orbitDirection": "Descending",  
  "orbitNumber": 93,  
  "ingestionDate": "2021-01-18T18:29:16.884Z",  
  "sensingDate": "2021-01-18T09:23:21.024Z",  
  "sensingStartedAt": "2021-01-18T09:23:21.024Z",  
  "sensingStoppedAt": "2021-01-18T09:23:21.024Z",  
  "hostedOn": "urn:ngsi-ld:EODataHub:123",  
  "observedBy": "urn:ngsi-ld:EOInstrument:154",  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
#### EOProdukt NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für ein EOProdukt im JSON-LD-Format wie normalisiert. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
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
    "type": "Property",  
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
          [  
            25.4464,  
            41.887688  
          ],  
          [  
            25.855984,  
            43.386223  
          ],  
          [  
            22.690121,  
            43.786907  
          ],  
          [  
            22.356091,  
            42.288685  
          ],  
          [  
            25.4464,  
            41.887688  
          ]  
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
    "value": 19.125499,  
    "unitCode": "P1"  
  },  
  "orbitDirection": {  
    "type": "Property",  
    "value": "Descending"  
  },  
  "orbitNumber": {  
    "type": "Property",  
    "value": 93  
  },  
  "ingestionDate": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2021-01-18T18:29:16.884Z"  
    }  
  },  
  "sensingDate": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2021-01-18T09:23:21.024Z"  
    }  
  },  
  "sensingStartedAt": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2021-01-18T09:23:21.024Z"  
    }  
  },  
  "sensingStoppedAt": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2021-01-18T09:23:21.024Z"  
    }  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
