Entità: EOProduct  
=================  
[Licenza aperta](https://github.com/smart-data-models//dataModel.SatelliteImagery/blob/master/EOProduct/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Descrizione globale: **Questa entità contiene una descrizione armonizzata di un EOProdotto generico realizzato per il dominio Satellite Imagerry. Questa entità è principalmente associata ai prodotti satellitari relativi alle applicazioni di Analisi dell'Osservazione della Terra.**  

## Elenco delle proprietà  

- `address`: L'indirizzo postale  - `alternateName`: Un nome alternativo per questa voce  - `areaServed`: L'area geografica in cui viene fornito un servizio o un articolo offerto  - `cloudCoverage`: La percentuale di copertura delle nuvole. Tutte le unità sono accettate in codice [CEFACT](https://www.unece.org/cefact.html).  - `dataProvider`: Una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata.  - `dateCreated`: Timestamp di creazione dell'entità. Questo sarà di solito assegnato dalla piattaforma di archiviazione.  - `dateModified`: Timestamp dell'ultima modifica dell'entità. Questo sarà di solito assegnato dalla piattaforma di archiviazione.  - `description`: Una descrizione di questo articolo  - `hostedOn`: L'ID dell'hub di dati su cui il prodotto è ospitato  - `id`: Identificatore unico dell'entità  - `ingestionDate`: Il momento in cui i dati sono stati resi disponibili nell'archivio online  - `location`: Riferimento Geojson all'elemento. Può essere Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `name`: Il nome di questo articolo.  - `observedBy`: L'ID dello strumento con cui il prodotto è stato osservato  - `orbitDirection`: L'orientamento del passaggio dell'orbita  - `orbitNumber`: Il numero di orbita del passaggio del satellite. Tutte le unità sono accettate in codice [CEFACT](https://www.unece.org/cefact.html).  - `owner`: Una lista contenente una sequenza di caratteri codificata in JSON che si riferisce agli ID unici dei proprietari  - `processingLevel`: Una stringa di testo obbligatoria usata per dichiarare il livello di lavorazione del prodotto  - `productFormat`: Una stringa di testo obbligatoria usata per dichiarare il formato del prodotto  - `productID`: Una stringa di testo obbligatoria usata per dichiarare l'ID unico del prodotto  - `productType`: Una stringa di testo obbligatoria usata per dichiarare il tipo di prodotto  - `productURL`: Un url obbligatorio usato per dichiarare il link di downlaod del prodotto  - `seeAlso`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `sensingDate`: Il tempo in cui l'immagine è stata presa dal sensore  - `sensingStartedAt`: L'ora dell'acquisizione a bordo del satellite della prima linea dell'immagine nel prodotto  - `sensingStoppedAt`: L'ora dell'acquisizione a bordo del satellite dell'ultima linea dell'immagine nel prodotto  - `source`: Una sequenza di caratteri che dà la fonte originale dei dati dell'entità come URL. Si raccomanda di essere il nome di dominio completamente qualificato del fornitore di origine, o l'URL dell'oggetto di origine.  - `timeliness`: La tempestività del prodotto  - `type`: Tipo di entità NGSI-LD. Deve essere uguale a EOProduct.    
Proprietà richieste  
- `id`  - `location`  - `productFormat`  - `productID`  - `productURL`  - `sensingDate`  - `type`  ## Descrizione del modello di dati delle proprietà  
Ordinati in ordine alfabetico (clicca per i dettagli)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
EOProduct:    
  description: 'This entity contains a harmonised description of a generic EOProduct made for the Satellite Imagerry domain. This entity is primarily associated with the satellite products related to Earth Observation Analysis applications.'    
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
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: string    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    cloudCoverage:    
      description: 'The cloud coverage percentage. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.'    
      type: number    
      x-ngsi:    
        model: ' https://schema.org/Number'    
        type: Property    
        units: percent    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    hostedOn:    
      description: 'The ID of the data hub that the product is hosted on'    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    id:    
      anyOf: &eoproduct_-_properties_-_owner_-_items_-_anyof    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Unique identifier of the entity'    
      x-ngsi:    
        type: Property    
    ingestionDate:    
      description: 'The time at which the data was made available in the online archive'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/Time    
        type: Property    
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
      x-ngsi:    
        type: Geoproperty    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    observedBy:    
      description: 'The ID of the instrument that the product was observed by'    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    orbitDirection:    
      description: 'The orbit pass orientation'    
      enum:    
        - Ascending    
        - Descending    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    orbitNumber:    
      description: 'The orbit number of tha satellite pass. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.'    
      type: number    
      x-ngsi:    
        model: ' https://schema.org/Number'    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *eoproduct_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    processingLevel:    
      description: 'A mandatory text string used to declare the processing level of the product'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    productFormat:    
      description: 'A mandatory text string used to declare the format of the product'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    productID:    
      description: 'A mandatory text string used to declare the unique ID of the product'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    productType:    
      description: 'A mandatory text string used to declare the type of the product'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    productURL:    
      description: 'A mandatory url used to declare the downlaod link of the product'    
      type: string    
      x-ngsi:    
        model: https://schema.org/url    
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
      x-ngsi:    
        type: Property    
    sensingDate:    
      description: 'The time at which the image was taken by the sensor'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/Time    
        type: Property    
    sensingStartedAt:    
      description: 'The time of the satellite on-board acquisition of the first line of the image in the product'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/Time    
        type: Property    
    sensingStoppedAt:    
      description: 'The time of the satellite on-board acquisition of the last line of the image in the product'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/Time    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    timeliness:    
      description: 'The timeliness of the product'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    type:    
      description: 'NGSI-LD Entity Type. It must be equal to EOProduct.'    
      enum:    
        - EOProduct    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - productID    
    - productURL    
    - location    
    - productFormat    
    - sensingDate    
  type: object    
```  
</details>    
## Esempio di payloads  
#### EOProduct NGSI-v2 valori chiave Esempio  
Ecco un esempio di un EOProduct in formato JSON-LD come key-values. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
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
#### EOProdotto NGSI-v2 normalizzato Esempio  
Ecco un esempio di un EOProduct in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non usa opzioni e restituisce i dati di contesto di una singola entità.  
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
#### EOProdotto NGSI-LD valori chiave Esempio  
Ecco un esempio di un EOProduct in formato JSON-LD come key-values. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
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
#### EOProdotto NGSI-LD normalizzato Esempio  
Ecco un esempio di un EOProduct in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non usa opzioni e restituisce i dati di contesto di una singola entità.  
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
