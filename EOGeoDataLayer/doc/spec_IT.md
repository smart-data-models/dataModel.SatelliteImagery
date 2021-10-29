Entità: EOGeoDataLayer  
======================  
[Licenza aperta](https://github.com/smart-data-models//dataModel.SatelliteImagery/blob/master/EOGeoDataLayer/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Descrizione globale: **Questa entità contiene una descrizione armonizzata di un generico EOGeoDataLayer realizzato per il dominio delle immagini satellitari. Questa entità è principalmente associata agli strati di dati in uscita relativi alle applicazioni di analisi dell'osservazione della Terra.  

## Elenco delle proprietà  

- `address`: L'indirizzo postale  - `alternateName`: Un nome alternativo per questa voce  - `areaServed`: L'area geografica in cui viene fornito un servizio o un articolo offerto  - `contentInformation`: Un array che descrive per ogni strato (ad esempio, banda1) o nome di entità, il tipo di informazione (ad esempio, categorico, numerico) e un array con la spiegazione dei valori rappresentati (ad esempio, [1:olio, 0:nessun olio])  - `dataProvider`: Una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata.  - `dateCreated`: Timestamp di creazione dell'entità. Questo sarà di solito assegnato dalla piattaforma di archiviazione.  - `dateModified`: Timestamp dell'ultima modifica dell'entità. Questo sarà di solito assegnato dalla piattaforma di archiviazione.  - `description`: Una descrizione di questo articolo  - `geoMetadata`: Una stringa di testo usata per dichiarare il file di metadati, se disponibile  - `id`: Identificatore unico dell'entità  - `isOutputOf`: L'ID dell'analisi che è stata eseguita per estrarre questo livello di dati  - `localServerPath`: Una stringa di testo obbligatoria usata per dichiarare il percorso in cui il livello di dati in uscita viene salvato sul server  - `location`: Riferimento Geojson all'elemento. Può essere Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `name`: Il nome di questo articolo.  - `owner`: Una lista contenente una sequenza di caratteri codificata in JSON che si riferisce agli ID unici dei proprietari  - `seeAlso`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source`: Una sequenza di caratteri che dà la fonte originale dei dati dell'entità come URL. Si raccomanda di essere il nome di dominio completamente qualificato del fornitore di origine, o l'URL dell'oggetto di origine.  - `storageFormat`: Formato satorage dell'entità.  - `type`: Tipo di entità NGSI-LD. Deve essere uguale a EOGeoDataLayer.    
Proprietà richieste  
- `id`  - `localServerPath`  - `storageFormat`  - `type`  ## Descrizione del modello di dati delle proprietà  
Ordinati in ordine alfabetico (clicca per i dettagli)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
EOGeoDataLayer:    
  description: 'This entity contains a harmonised description of a generic EOGeoDataLayer made for the Satellite Imagerry domain. This entity is primarily associated with the output data layers related to Earth Observation Analysis applications.'    
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
    contentInformation:    
      description: 'An array that describes for each layer (e.g. band1) or entity name, the type of information (e.g. categorical, numerical) and an array with the explanation of the depicted values (e.g. [1:oil, 0:no oil])'    
      items:    
        properties:    
          layer_categorization:    
            enum:    
              - categorical    
              - numerical    
            type: string    
          layer_name:    
            type: string    
          values_explanation:    
            items:    
              type: string    
            type: array    
        type: object    
      type: array    
      x-ngsi:    
        type: Property    
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
    geoMetadata:    
      description: 'A text string used to declare the metadata file if available'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    id:    
      anyOf: &eogeodatalayer_-_properties_-_owner_-_items_-_anyof    
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
    isOutputOf:    
      description: 'The ID of the analysis that was performed to extract this data layer'    
      format: uri    
      type: string    
      x-ngsi:    
        type: Relationship    
    localServerPath:    
      description: 'A mandatory text string used to declare the path that the output data layer is saved on the server'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
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
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *eogeodatalayer_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
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
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    storageFormat:    
      description: 'Entity''s satorage format.'    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: 'NGSI-LD Entity Type. It must be equal to EOGeoDataLayer.'    
      enum:    
        - EOGeoDataLayer    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
    - localServerPath    
    - storageFormat    
  type: object    
```  
</details>    
## Esempio di payloads  
#### EOGeoDataLayer NGSI-v2 valori chiave Esempio  
Ecco un esempio di un EOGeoDataLayer in formato JSON-LD come key-values. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
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
#### EOGeoDataLayer NGSI-v2 normalizzato Esempio  
Ecco un esempio di un EOGeoDataLayer in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non usa opzioni e restituisce i dati di contesto di una singola entità.  
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
    "value": "/data/www/oil_map.tif"  
  },  
  "storageFormat": {  
    "type": "Property",  
    "value": "GeoTIFF"  
  },  
  "geoMetadata": {  
    "type": "Property",  
    "value": "/data/www/metadata_oil.xml"  
  },  
  "contentInformation": [  
    {  
      "layer_name": "band1",  
      "layer_categorization": "categorical",  
      "values_explanation": [  
        "1:oil",  
        "0:water"  
      ]  
    }  
  ],  
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
#### EOGeoDataLayer NGSI-LD valori-chiave Esempio  
Ecco un esempio di un EOGeoDataLayer in formato JSON-LD come key-values. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
```json  
{  
  "id": "urn:ngsi-ld:EOGeoDataLayer:1",  
  "type": "EOGeoDataLayer",  
  "localServerPath": "/data/www/oil_map.tif",  
  "storageFormat": "GeoTIFF",  
  "geoMetadata": "/data/www/metadata_oil.xml",  
  "contentInformation": [  
    {  
      "layer_name": "band1",  
      "layer_categorization": "categorical",  
      "values_explanation": [  
        "1:oil",  
        "0:water"  
      ]  
    }  
  ],  
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
  "isOutputOf": "EOAnalysis:02",  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
#### EOGeoDataLayer NGSI-LD normalizzato Esempio  
Ecco un esempio di un EOGeoDataLayer in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non usa opzioni e restituisce i dati di contesto di una singola entità.  
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
    "type": "Property",  
    "value": "GeoTIFF"  
  },  
  "geoMetadata": {  
    "type": "Property",  
    "value": "/data/www/metadata.xml"  
  },  
  "contentInformation": {  
    "type": "Property",  
    "value": [  
      {  
        "layer_name": "band1",  
        "layer_categorization": "categorical",  
        "values_explanation": [  
          "1:inundated",  
          "0:non inundated"  
        ]  
      }  
    ]  
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
