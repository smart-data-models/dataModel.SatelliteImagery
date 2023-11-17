<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entidad: EOProducto    
===================<!-- /10-Header -->    
<!-- 15-License -->    
[Licencia abierta](https://github.com/smart-data-models//dataModel.SatelliteImagery/blob/master/EOProduct/LICENSE.md)    
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Descripción global: **Esta entidad contiene una descripción armonizada de un EOProducto genérico realizado para el dominio Satellite Imagerry. Esta entidad se asocia principalmente a los productos de satélite relacionados con las aplicaciones de análisis de observación de la Tierra.**.    
versión: 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## Lista de propiedades    
<sup><sub>[*] Si no hay un tipo en un atributo es porque puede tener varios tipos o diferentes formatos/patrones</sub></sup>.    
- `address[object]`: La dirección postal  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: El país. Por ejemplo, España  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: La localidad en la que se encuentra la dirección postal, y que está en la región  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: La región en la que se encuentra la localidad, y que está en el país  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: Un distrito es un tipo de división administrativa que, en algunos países, gestiona el gobierno local      
	- `postOfficeBoxNumber[string]`: El número del apartado de correos para las direcciones de apartados postales. Por ejemplo, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: El código postal. Por ejemplo, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: La dirección  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
- `alternateName[string]`: Un nombre alternativo para este artículo  - `areaServed[string]`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  . Model: [https://schema.org/Text](https://schema.org/Text)- `cloudCoverage[number]`: Porcentaje de cobertura de nubes. Todas las unidades se aceptan en código [CEFACT](https://www.unece.org/cefact.html)  . Model: [ https://schema.org/Number]( https://schema.org/Number)- `dataProvider[string]`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada  - `dateCreated[date-time]`: Fecha de creación de la entidad. Normalmente será asignada por la plataforma de almacenamiento  - `dateModified[date-time]`: Marca de tiempo de la última modificación de la entidad. Suele ser asignada por la plataforma de almacenamiento  - `description[string]`: Descripción de este artículo  - `hostedOn[uri]`: ID del concentrador de datos en el que está alojado el producto  - `id[*]`: Identificador único de la entidad  - `ingestionDate[date-time]`: Momento en que los datos estuvieron disponibles en el archivo en línea  . Model: [https://schema.org/Time](https://schema.org/Time)- `location[*]`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon.  - `name[string]`: El nombre de este artículo  - `observedBy[uri]`: ID del instrumento con el que se observó el producto  - `orbitDirection[string]`: La orientación del pase orbital  . Model: [https://schema.org/Text](https://schema.org/Text)- `orbitNumber[number]`: Número de órbita del pase del satélite. Todas las unidades se aceptan en código [CEFACT](https://www.unece.org/cefact.html)  . Model: [ https://schema.org/Number]( https://schema.org/Number)- `owner[array]`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios.  - `processingLevel[string]`: Cadena de texto obligatoria utilizada para declarar el nivel de procesamiento del producto.  . Model: [https://schema.org/Text](https://schema.org/Text)- `productFormat[string]`: Cadena de texto obligatoria utilizada para declarar el formato del producto.  . Model: [https://schema.org/Text](https://schema.org/Text)- `productID[string]`: Cadena de texto obligatoria utilizada para declarar el ID único del producto.  . Model: [https://schema.org/Text](https://schema.org/Text)- `productType[string]`: Cadena de texto obligatoria utilizada para declarar el tipo de producto  . Model: [https://schema.org/Text](https://schema.org/Text)- `productURL[string]`: Una url obligatoria utilizada para declarar el enlace de descarga del producto  . Model: [https://schema.org/url](https://schema.org/url)- `seeAlso[*]`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `sensingDate[date-time]`: Hora a la que el sensor tomó la imagen  . Model: [https://schema.org/Time](https://schema.org/Time)- `sensingStartedAt[date-time]`: Hora de la adquisición por satélite de la primera línea de la imagen del producto  . Model: [https://schema.org/Time](https://schema.org/Time)- `sensingStoppedAt[date-time]`: Hora de la adquisición a bordo del satélite de la última línea de la imagen del producto  . Model: [https://schema.org/Time](https://schema.org/Time)- `source[string]`: Secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen o la URL del objeto de origen.  - `timeliness[string]`: La puntualidad del producto  . Model: [https://schema.org/Text](https://schema.org/Text)- `type[string]`: Tipo de entidad NGSI-LD. Debe ser igual a EOProducto  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Propiedades requeridas    
- `id`  - `location`  - `productFormat`  - `productID`  - `productURL`  - `sensingDate`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## Descripción de las propiedades del modelo de datos    
Ordenados alfabéticamente (pulse para más detalles)    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
EOProduct:      
  description: This entity contains a harmonised description of a generic EOProduct made for the Satellite Imagerry domain. This entity is primarily associated with the satellite products related to Earth Observation Analysis applications.      
  properties:      
    address:      
      description: The mailing address      
      properties:      
        addressCountry:      
          description: 'The country. For example, Spain'      
          type: string      
          x-ngsi:      
            model: https://schema.org/addressCountry      
            type: Property      
        addressLocality:      
          description: 'The locality in which the street address is, and which is in the region'      
          type: string      
          x-ngsi:      
            model: https://schema.org/addressLocality      
            type: Property      
        addressRegion:      
          description: 'The region in which the locality is, and which is in the country'      
          type: string      
          x-ngsi:      
            model: https://schema.org/addressRegion      
            type: Property      
        district:      
          description: 'A district is a type of administrative division that, in some countries, is managed by the local government'      
          type: string      
          x-ngsi:      
            type: Property      
        postOfficeBoxNumber:      
          description: 'The post office box number for PO box addresses. For example, 03578'      
          type: string      
          x-ngsi:      
            model: https://schema.org/postOfficeBoxNumber      
            type: Property      
        postalCode:      
          description: 'The postal code. For example, 24004'      
          type: string      
          x-ngsi:      
            model: https://schema.org/https://schema.org/postalCode      
            type: Property      
        streetAddress:      
          description: The street address      
          type: string      
          x-ngsi:      
            model: https://schema.org/streetAddress      
            type: Property      
        streetNr:      
          description: Number identifying a specific property on a public street      
          type: string      
          x-ngsi:      
            type: Property      
      type: object      
      x-ngsi:      
        model: https://schema.org/address      
        type: Property      
    alternateName:      
      description: An alternative name for this item      
      type: string      
      x-ngsi:      
        type: Property      
    areaServed:      
      description: The geographic area where a service or offered item is provided      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    cloudCoverage:      
      description: 'The cloud coverage percentage. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code'      
      type: number      
      x-ngsi:      
        model: ' https://schema.org/Number'      
        type: Property      
        units: percent      
    dataProvider:      
      description: A sequence of characters identifying the provider of the harmonised data entity      
      type: string      
      x-ngsi:      
        type: Property      
    dateCreated:      
      description: Entity creation timestamp. This will usually be allocated by the storage platform      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    dateModified:      
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    description:      
      description: A description of this item      
      type: string      
      x-ngsi:      
        type: Property      
    hostedOn:      
      description: The ID of the data hub that the product is hosted on      
      format: uri      
      type: string      
      x-ngsi:      
        type: Relationship      
    id:      
      anyOf:      
        - description: Identifier format of any NGSI entity      
          maxLength: 256      
          minLength: 1      
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
          type: string      
          x-ngsi:      
            type: Property      
        - description: Identifier format of any NGSI entity      
          format: uri      
          type: string      
          x-ngsi:      
            type: Property      
      description: Unique identifier of the entity      
      x-ngsi:      
        type: Property      
    ingestionDate:      
      description: The time at which the data was made available in the online archive      
      format: date-time      
      type: string      
      x-ngsi:      
        model: https://schema.org/Time      
        type: Property      
    location:      
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'      
      oneOf:      
        - description: Geojson reference to the item. Point      
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
          title: GeoJSON Point      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. LineString      
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
          title: GeoJSON LineString      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. Polygon      
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
          title: GeoJSON Polygon      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. MultiPoint      
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
          title: GeoJSON MultiPoint      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. MultiLineString      
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
          title: GeoJSON MultiLineString      
          type: object      
          x-ngsi:      
            type: GeoProperty      
        - description: Geojson reference to the item. MultiLineString      
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
          title: GeoJSON MultiPolygon      
          type: object      
          x-ngsi:      
            type: GeoProperty      
      x-ngsi:      
        type: GeoProperty      
    name:      
      description: The name of this item      
      type: string      
      x-ngsi:      
        type: Property      
    observedBy:      
      description: The ID of the instrument that the product was observed by      
      format: uri      
      type: string      
      x-ngsi:      
        type: Relationship      
    orbitDirection:      
      description: The orbit pass orientation      
      enum:      
        - Ascending      
        - Descending      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    orbitNumber:      
      description: 'The orbit number of tha satellite pass. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code'      
      type: number      
      x-ngsi:      
        model: ' https://schema.org/Number'      
        type: Property      
    owner:      
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)      
      items:      
        anyOf:      
          - description: Identifier format of any NGSI entity      
            maxLength: 256      
            minLength: 1      
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$      
            type: string      
            x-ngsi:      
              type: Property      
          - description: Identifier format of any NGSI entity      
            format: uri      
            type: string      
            x-ngsi:      
              type: Property      
        description: Unique identifier of the entity      
        x-ngsi:      
          type: Property      
      type: array      
      x-ngsi:      
        type: Property      
    processingLevel:      
      description: A mandatory text string used to declare the processing level of the product      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    productFormat:      
      description: A mandatory text string used to declare the format of the product      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    productID:      
      description: A mandatory text string used to declare the unique ID of the product      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    productType:      
      description: A mandatory text string used to declare the type of the product      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    productURL:      
      description: A mandatory url used to declare the downlaod link of the product      
      type: string      
      x-ngsi:      
        model: https://schema.org/url      
        type: Property      
    seeAlso:      
      description: list of uri pointing to additional resources about the item      
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
      description: The time at which the image was taken by the sensor      
      format: date-time      
      type: string      
      x-ngsi:      
        model: https://schema.org/Time      
        type: Property      
    sensingStartedAt:      
      description: The time of the satellite on-board acquisition of the first line of the image in the product      
      format: date-time      
      type: string      
      x-ngsi:      
        model: https://schema.org/Time      
        type: Property      
    sensingStoppedAt:      
      description: The time of the satellite on-board acquisition of the last line of the image in the product      
      format: date-time      
      type: string      
      x-ngsi:      
        model: https://schema.org/Time      
        type: Property      
    source:      
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'      
      type: string      
      x-ngsi:      
        type: Property      
    timeliness:      
      description: The timeliness of the product      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    type:      
      description: NGSI-LD Entity Type. It must be equal to EOProduct      
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
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
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
## Ejemplo de carga útil    
#### EOProduct NGSI-v2 key-values Ejemplo    
He aquí un ejemplo de un EOProduct en formato JSON-LD como key-values. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.    
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
#### EOProducto NGSI-v2 normalizado Ejemplo    
He aquí un ejemplo de un EOProducto en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:EOProduct:123",  
  "type": "EOProduct",  
  "createdAt": {  
    "type": "DateTime",  
    "value": "2020-03-13T15:42:00Z"  
  },  
  "modifiedAt": {  
    "type": "DateTime",  
    "value": "2020-03-13T15:45:00Z"  
  },  
  "productID": {  
    "type": "Text",  
    "value": "S1B_IW_GRDH_1SDV_20210201T042950_20210201T043015_025408_0306B8_AE29"  
  },  
  "productURL": {  
    "type": "Text",  
    "value": "https://scihub.copernicus.eu/dhus/odata/v1/Products('561d85c3-5627-4f78-84f7-05d0a0c8db9c')/$value"  
  },  
  "productType": {  
    "type": "Text",  
    "value": "GRD"  
  },  
  "processingLevel": {  
    "type": "Text",  
    "value": "L1"  
  },  
  "location": {  
    "type": "geo:json",  
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
    "type": "Text",  
    "value": "SAFE"  
  },  
  "timeliness": {  
    "type": "Text",  
    "value": "Fast-24h"  
  },  
  "orbitDirection": {  
    "type": "Text",  
    "value": "Descending"  
  },  
  "orbitNumber": {  
    "type": "Number",  
    "value": 7  
  },  
  "ingestionDate": {  
    "type": "DateTime",  
    "value": "2021-02-01T08:26:25.020Z"  
  },  
  "sensingDate": {  
    "type": "DateTime",  
    "value": "2021-02-01T04:29:50.264Z"  
  },  
  "sensingStartedAt": {  
    "type": "DateTime",  
    "value": "2021-02-01T04:29:50.264Z"  
  },  
  "sensingStoppedAt": {  
    "type": "DateTime",  
    "value": "2021-02-01T04:30:15.263Z"  
  }  
}  
```  
</details>    
#### EOProduct NGSI-LD key-values Ejemplo    
He aquí un ejemplo de un EOProduct en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.    
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
#### EOProducto NGSI-LD normalizado Ejemplo    
He aquí un ejemplo de un EOProducto en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.    
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
Consulte [FAQ 10](https://smartdatamodels.org/index.php/faqs/) para obtener una respuesta sobre cómo tratar las unidades de magnitud.    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
