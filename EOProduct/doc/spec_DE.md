<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entität: EOProdukt  
==================<!-- /10-Header -->  
<!-- 15-License -->  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.SatelliteImagery/blob/master/EOProduct/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Globale Beschreibung: **Diese Entität enthält eine harmonisierte Beschreibung eines generischen EOProdukts für den Bereich der Satellitenbilddaten. Diese Einheit ist in erster Linie mit den Satellitenprodukten im Zusammenhang mit Erdbeobachtungsanalyseanwendungen verbunden.**  
Version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste der Eigenschaften  

<sup><sub>[*] Wenn es für ein Attribut keinen Typ gibt, liegt das daran, dass es mehrere Typen oder unterschiedliche Formate/Muster haben kann</sub></sup>.  
- `address[object]`: Die Postanschrift  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: Ein alternativer Name für diesen Artikel  - `areaServed[string]`: Das geografische Gebiet, in dem eine Dienstleistung oder ein angebotener Artikel erbracht wird  . Model: [https://schema.org/Text](https://schema.org/Text)- `cloudCoverage[number]`: Der Prozentsatz der Wolkenbedeckung. Alle Einheiten werden im Code [CEFACT](https://www.unece.org/cefact.html) akzeptiert.  . Model: [ https://schema.org/Number]( https://schema.org/Number)- `dataProvider[string]`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit.  - `dateCreated[string]`: Zeitstempel der Entitätserstellung. Dieser wird in der Regel von der Speicherplattform zugewiesen.  - `dateModified[string]`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `description[string]`: Eine Beschreibung dieses Artikels  - `hostedOn[string]`: Die ID der Datendrehscheibe, auf der das Produkt gehostet wird  - `id[*]`: Eindeutiger Bezeichner der Entität  - `ingestionDate[string]`: Der Zeitpunkt, zu dem die Daten im Online-Archiv zur Verfügung gestellt wurden  . Model: [https://schema.org/Time](https://schema.org/Time)- `location[*]`: Geojson-Referenz auf das Element. Es kann Punkt, LineString, Polygon, MultiPoint, MultiLineString oder MultiPolygon sein  - `name[string]`: Der Name dieses Artikels.  - `observedBy[string]`: Die ID des Geräts, mit dem das Produkt beobachtet wurde  - `orbitDirection[string]`: Die Ausrichtung des Orbits  . Model: [https://schema.org/Text](https://schema.org/Text)- `orbitNumber[number]`: Die Nummer der Umlaufbahn des Satellitendurchgangs. Alle Einheiten werden im Code [CEFACT](https://www.unece.org/cefact.html) akzeptiert.  . Model: [ https://schema.org/Number]( https://schema.org/Number)- `owner[array]`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `processingLevel[string]`: Eine obligatorische Zeichenfolge zur Angabe der Verarbeitungsstufe des Produkts  . Model: [https://schema.org/Text](https://schema.org/Text)- `productFormat[string]`: Eine obligatorische Zeichenfolge zur Angabe des Formats des Produkts  . Model: [https://schema.org/Text](https://schema.org/Text)- `productID[string]`: Eine obligatorische Zeichenfolge zur Angabe der eindeutigen ID des Produkts  . Model: [https://schema.org/Text](https://schema.org/Text)- `productType[string]`: Eine obligatorische Zeichenfolge zur Angabe der Art des Produkts  . Model: [https://schema.org/Text](https://schema.org/Text)- `productURL[string]`: Eine obligatorische URL, mit der der Link zum Herunterladen des Produkts angegeben wird  . Model: [https://schema.org/url](https://schema.org/url)- `seeAlso[*]`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `sensingDate[string]`: Der Zeitpunkt, zu dem das Bild vom Sensor aufgenommen wurde  . Model: [https://schema.org/Time](https://schema.org/Time)- `sensingStartedAt[string]`: Der Zeitpunkt der satellitengestützten Erfassung der ersten Zeile des Bildes im Produkt  . Model: [https://schema.org/Time](https://schema.org/Time)- `sensingStoppedAt[string]`: Der Zeitpunkt der satellitengestützten Erfassung der letzten Zeile des Bildes im Produkt  . Model: [https://schema.org/Time](https://schema.org/Time)- `source[string]`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Es wird empfohlen, den voll qualifizierten Domänennamen des Quellanbieters oder die URL des Quellobjekts zu verwenden.  - `timeliness[string]`: Die Aktualität des Produkts  . Model: [https://schema.org/Text](https://schema.org/Text)- `type[string]`: NGSI-LD Entitätstyp. Er muss gleich EOProduct sein.  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Erforderliche Eigenschaften  
- `id`  - `location`  - `productFormat`  - `productID`  - `productURL`  - `sensingDate`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
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
        - description: 'GeoProperty. Geojson reference to the item. Point'    
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
        - description: 'GeoProperty. Geojson reference to the item. LineString'    
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
        - description: 'GeoProperty. Geojson reference to the item. Polygon'    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiPoint'    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiLineString'    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiLineString'    
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
        type: GeoProperty    
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
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.SatelliteImagery/blob/master/EOProduct/LICENSE.md    
  x-model-schema: https://raw.githubusercontent.com/smart-data-models/dataModel.SatelliteImagery/master/EOProduct/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Beispiel-Nutzlasten  
#### EOProdukt NGSI-v2 Schlüsselwerte Beispiel  
Hier ist ein Beispiel für ein EOProdukt im JSON-LD-Format als Schlüsselwerte. Dies ist kompatibel mit NGSI-v2, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### EOProdukt NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für ein EOProdukt im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### EOProdukt NGSI-LD Schlüsselwerte Beispiel  
Hier ist ein Beispiel für ein EOProdukt im JSON-LD-Format als Schlüsselwerte. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:EOProduct:123",  
    "type": "EOProduct",  
    "cloudCoverage": 19.125499,  
    "hostedOn": "urn:ngsi-ld:EODataHub:123",  
    "ingestionDate": "2021-01-18T18:29:16.884Z",  
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
    "observedBy": "urn:ngsi-ld:EOInstrument:154",  
    "orbitDirection": "Descending",  
    "orbitNumber": 93,  
    "processingLevel": "Level-2A",  
    "productFormat": "SAFE",  
    "productID": "S2A_MSIL2A_20210118T092321_N0214_R093_T34TGN_20210118T120704",  
    "productType": "S2MSI2A",  
    "productURL": "https://scihub.copernicus.eu/dhus/odata/v1/Products('698c2089-704f-4d4f-aa2f-977902e2d35e')/$value",  
    "sensingDate": "2021-01-18T09:23:21.024Z",  
    "sensingStartedAt": "2021-01-18T09:23:21.024Z",  
    "sensingStoppedAt": "2021-01-18T09:23:21.024Z",  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.SatelliteImagery/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### EOProdukt NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für ein EOProdukt im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:EOProduct:123",  
    "type": "EOProduct",  
    "cloudCoverage": {  
        "type": "Property",  
        "value": 19.125499,  
        "unitCode": "P1"  
    },  
    "createdAt": "2020-03-13T15:42:00Z",  
    "ingestionDate": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2021-01-18T18:29:16.884Z"  
        }  
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
    "modifiedAt": "2020-03-13T15:45:00Z",  
    "orbitDirection": {  
        "type": "Property",  
        "value": "Descending"  
    },  
    "orbitNumber": {  
        "type": "Property",  
        "value": 93  
    },  
    "processingLevel": {  
        "type": "Property",  
        "value": "L1"  
    },  
    "productFormat": {  
        "type": "Property",  
        "value": "SAFE"  
    },  
    "productID": {  
        "type": "Property",  
        "value": "S1B_IW_GRDH_1SDV_20210201T042950_20210201T043015_025408_0306B8_AE29"  
    },  
    "productType": {  
        "type": "Property",  
        "value": "GRD"  
    },  
    "productURL": {  
        "type": "Property",  
        "value": "https://scihub.copernicus.eu/dhus/odata/v1/Products('561d85c3-5627-4f78-84f7-05d0a0c8db9c')/$value"  
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
        "https://raw.githubusercontent.com/smart-data-models/dataModel.SatelliteImagery/master/context.jsonld"  
    ]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Siehe [FAQ 10] (https://smartdatamodels.org/index.php/faqs/), um eine Antwort auf die Frage zu erhalten, wie man mit Größeneinheiten umgeht  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
