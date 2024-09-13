<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entity: EOSatelliteImagery  
==========================<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://github.com/smart-data-models//dataModel.SatelliteImagery/blob/master/EOSatelliteImagery/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Global description: **This schema defines a unified entity within the SatelliteImagery domain, consolidating attributes from all existing entities related to satellite imagery, designed to offer a holistic view in the EO proccess**  
version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## List of properties  

<sup><sub>[*] If there is not a type in an attribute is because it could have several types or different formats/patterns</sub></sup>  
- `address[object]`: The mailing address  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: The country. For example, Spain  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: The locality in which the street address is, and which is in the region  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: The region in which the locality is, and which is in the country  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: A district is a type of administrative division that, in some countries, is managed by the local government    
	- `postOfficeBoxNumber[string]`: The post office box number for PO box addresses. For example, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: The postal code. For example, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: The street address  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: Number identifying a specific property on a public street    
- `alternateName[string]`: An alternative name for this item  - `analysisType[string]`: Entity's type of analysis applied  - `areaServed[string]`: The geographic area where a service or offered item is provided  . Model: [https://schema.org/Text](https://schema.org/Text)- `contentInformation[array]`: An array that describes for each layer (e.g. band1) or entity name, the type of information (e.g. categorical, numerical) and an array with the explanation of the depicted values (e.g. [1:oil, 0:no oil])  - `dataProvider[string]`: A sequence of characters identifying the provider of the harmonised data entity  - `dateCreated[date-time]`: Entity creation timestamp. This will usually be allocated by the storage platform  - `dateModified[date-time]`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform  - `description[string]`: A description of this item  - `id[*]`: Unique identifier of the entity  - `localServerPath[string]`: A mandatory text string used to declare the path that the output data layer is saved on the server  . Model: [https://schema.org/Text](https://schema.org/Text)- `location[*]`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  - `name[string]`: The name of this item  - `operationalMode[string]`: A text string used to declare the supported sensor modes if available  . Model: [https://schema.org/Text](https://schema.org/Text)- `orbitNumber[number]`: The orbit number of tha satellite pass. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code  . Model: [ https://schema.org/Number]( https://schema.org/Number)- `owner[array]`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `platformName[string]`: A mandatory text string used to declare the name of the platform  . Model: [https://schema.org/Text](https://schema.org/Text)- `processedBbox[*]`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  - `productBbox[*]`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  - `productFormat[string]`: A mandatory text string used to declare the format of the product  . Model: [https://schema.org/Text](https://schema.org/Text)- `productID[string]`: A mandatory text string used to declare the unique ID of the product  . Model: [https://schema.org/Text](https://schema.org/Text)- `productType[string]`: A mandatory text string used to declare the type of the product  . Model: [https://schema.org/Text](https://schema.org/Text)- `productURL[string]`: A mandatory url used to declare the download link of the product  . Model: [https://schema.org/url](https://schema.org/url)- `provider[string]`: The provider of the algorithm  . Model: [ https://schema.org/Text]( https://schema.org/Text)- `resultDescription[string]`: The description of the analysis outcome  - `seeAlso[*]`: list of uri pointing to additional resources about the item  - `sensingDate[string]`: The time at which the image was taken by the sensor  . Model: [https://schema.org/Time](https://schema.org/Time)- `source[string]`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object  - `storageFormat[string]`: Entity's satorage format  - `type[string]`: NGSI Entity type. It must be equal to EOSatelliteImagery  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Required properties  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## Data Model description of properties  
Sorted alphabetically (click for details)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
EOSatelliteImagery:    
  description: 'This schema defines a unified entity within the SatelliteImagery domain, consolidating attributes from all existing entities related to satellite imagery, designed to offer a holistic view in the EO proccess'    
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
    analysisType:    
      description: Entity's type of analysis applied    
      type: string    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: The geographic area where a service or offered item is provided    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    contentInformation:    
      description: 'An array that describes for each layer (e.g. band1) or entity name, the type of information (e.g. categorical, numerical) and an array with the explanation of the depicted values (e.g. [1:oil, 0:no oil])'    
      items:    
        properties:    
          layer_categorization:    
            description: 'A string that describes the type of information (e.g. categorical, numerical)'    
            enum:    
              - categorical    
              - numerical    
            type: string    
            x-ngsi:    
              type: Property    
          layer_name:    
            description: A string that states the layer name (e.g. band1)    
            type: string    
            x-ngsi:    
              type: Property    
          values_explanation:    
            description: 'An array with the explanation of the depicted values (e.g. [1:oil, 0:no oil])'    
            items:    
              type: string    
            type: array    
            x-ngsi:    
              type: Property    
        type: object    
      type: array    
      x-ngsi:    
        type: Property    
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
    localServerPath:    
      description: A mandatory text string used to declare the path that the output data layer is saved on the server    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
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
    operationalMode:    
      description: A text string used to declare the supported sensor modes if available    
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
    platformName:    
      description: A mandatory text string used to declare the name of the platform    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    processedBbox:    
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
    productBbox:    
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
      description: A mandatory url used to declare the download link of the product    
      type: string    
      x-ngsi:    
        model: https://schema.org/url    
        type: Property    
    provider:    
      description: The provider of the algorithm    
      type: string    
      x-ngsi:    
        model: ' https://schema.org/Text'    
        type: Property    
    resultDescription:    
      description: The description of the analysis outcome    
      type: string    
      x-ngsi:    
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
      type: string    
      x-ngsi:    
        model: https://schema.org/Time    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'    
      type: string    
      x-ngsi:    
        type: Property    
    storageFormat:    
      description: Entity's satorage format    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI Entity type. It must be equal to EOSatelliteImagery    
      enum:    
        - EOSatelliteImagery    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2024 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.SatelliteImagery/blob/master/EOSatelliteImagery/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.SatelliteImagery/EOSatelliteImagery/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Example payloads    
#### EOSatelliteImagery NGSI-v2 key-values Example    
Here is an example of a EOSatelliteImagery in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "productID": "S2A_MSIL1C_20240427T082601_N0510_R021_T36SVD_20240427T103126",  
  "productURL": "https://catalogue.dataspace.copernicus.eu/odata/v1/Products(88f6e3c8-ae72-41dd-b5b9-014c3baa9634)/$value",  
  "type":"EOSatelliteImagery",  
  "productBbox": {  
    "type": "Polygon",  
    "coordinates": [  
      [  
        [  
          31.90052,  
          35.238084  
        ],  
        [  
          31.91356,  
          34.248107  
        ],  
        [  
          33.106002,  
          34.252876  
        ],  
        [  
          33.107275,  
          35.24303  
        ],  
        [  
          31.90052,  
          35.238084  
        ]  
      ]  
    ]  
  },  
  "sensingDate": "20240427T082601",  
  "productFormat": "SAFE",  
  "localServerPath": "algaemap-chl_wbl_kouris_20240427T082601.tif",  
  "storageFormat": "GeoTIFF",  
  "operationalMode": "MSI",  
  "productType": "S2MSI1C",  
  "orbitNumber": 21,  
  "platformName": "S2A",  
  "processedBbox": {  
    "type": "Polygon",  
    "coordinates": [  
      [  
        [  
          32.904684,  
          34.77082  
        ],  
        [  
          32.904684,  
          34.726095  
        ],  
        [  
          32.939337,  
          34.726095  
        ],  
        [  
          32.939337,  
          34.77082  
        ],  
        [  
          32.904684,  
          34.77082  
        ]  
      ]  
    ]  
  },  
  "id": "KOURIS_ALGAE",  
  "areaServed": "kouris",  
  "provider": "CERTH",  
  "analysisType": "chl-monitoring"  
}  
```  
</details>  
#### EOSatelliteImagery NGSI-v2 normalized Example    
Here is an example of a EOSatelliteImagery in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:EOGeoDataLayer:1234",  
  "type": "EOSatelliteImagery",  
  "dataProvider": {  
    "type": "Text",  
    "value": "CERTH"  
  },  
  "contentInformation": {  
    "type": "StructuredValue",  
    "value": [  
      {  
        "layer_name": "band1",  
        "layer_categorization": "numerical",  
        "values_explanation": [  
          "100: exceptional algae bloom",  
          "10: algae bloom"  
        ]  
      }  
    ]  
  },  
  "description": {  
    "type": "Text",  
    "value": "Unified data from EO Satellite Imagery analysis for algae"  
  },  
  "localServerPath": {  
    "type": "Text",  
    "value": "algaemap-chl_wbl_kouris_20240427T082601.tif"  
  },  
  "areaServed": {  
    "type": "Text",  
    "value": "kouris"  
  },  
  "productBbox": {  
    "type": "geo:json",  
    "value": {  
      "type": "Polygon",  
      "coordinates": [  
        [  
          [  
            31.90052,  
            35.238084  
          ],  
          [  
            31.91356,  
            34.248107  
          ],  
          [  
            33.106002,  
            34.252876  
          ],  
          [  
            33.107275,  
            35.24303  
          ],  
          [  
            31.90052,  
            35.238084  
          ]  
        ]  
      ]  
    }  
  },  
  "processedBbox": {  
    "type": "geo:json",  
    "value": {  
      "type": "Polygon",  
      "coordinates": [  
        [  
          [  
            32.904684,  
            34.77082  
          ],  
          [  
            32.904684,  
            34.726095  
          ],  
          [  
            32.939337,  
            34.726095  
          ],  
          [  
            32.939337,  
            34.77082  
          ],  
          [  
            32.904684,  
            34.77082  
          ]  
        ]  
      ]  
    }  
  },  
  "storageFormat": {  
    "type": "Text",  
    "value": "GeoTIFF"  
  },  
  "productFormat": {  
    "type": "Text",  
    "value": "SAFE"  
  },  
  "productType": {  
    "type": "Text",  
    "value": "S2MSI1C"  
  },  
  "operationalMode": {  
    "type": "Text",  
    "value": "MSI"  
  },  
  "productID": {  
    "type": "Text",  
    "value": "S2A_MSIL1C_20240427T082601_N0510_R021_T36SVD_20240427T103126"  
  },  
  "productURL": {  
    "type": "URI",  
    "value": "https://catalogue.dataspace.copernicus.eu/odata/v1/Products(88f6e3c8-ae72-41dd-b5b9-014c3baa9634)/$value"  
  },  
  "sensingDate": {  
    "type": "Date-Time",  
    "value": "2024-04-27T08:26:01Z"  
  },  
  "orbitNumber": {  
    "type": "Text",  
    "value": 21  
  },  
  "platformName": {  
    "type": "Text",  
    "value": "S2A"  
  },  
  "analysisType": {  
    "type": "Text",  
    "value": "chl-monitoring"  
  },  
  "provider": {  
    "type": "Text",  
    "value": "CERTH"  
  },  
  "resultDescription": {  
    "type": "Text",  
    "value": "description of the results"  
  }  
}  
```  
</details>  
#### EOSatelliteImagery NGSI-LD key-values Example    
Here is an example of a EOSatelliteImagery in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "productID": "S2A_MSIL1C_20240427T082601_N0510_R021_T36SVD_20240427T103126",  
  "productURL": "https://catalogue.dataspace.copernicus.eu/odata/v1/Products(88f6e3c8-ae72-41dd-b5b9-014c3baa9634)/$value",  
  "type":"EOSatelliteImagery",  
  "productBbox": {  
    "type": "Polygon",  
    "coordinates": [  
      [  
        [  
          31.90052,  
          35.238084  
        ],  
        [  
          31.91356,  
          34.248107  
        ],  
        [  
          33.106002,  
          34.252876  
        ],  
        [  
          33.107275,  
          35.24303  
        ],  
        [  
          31.90052,  
          35.238084  
        ]  
      ]  
    ]  
  },  
  "sensingDate": "20240427T082601",  
  "productFormat": "SAFE",  
  "localServerPath": "algaemap-chl_wbl_kouris_20240427T082601.tif",  
  "storageFormat": "GeoTIFF",  
  "operationalMode": "MSI",  
  "productType": "S2MSI1C",  
  "orbitNumber": 21,  
  "platformName": "S2A",  
  "processedBbox": {  
    "type": "Polygon",  
    "coordinates": [  
      [  
        [  
          32.904684,  
          34.77082  
        ],  
        [  
          32.904684,  
          34.726095  
        ],  
        [  
          32.939337,  
          34.726095  
        ],  
        [  
          32.939337,  
          34.77082  
        ],  
        [  
          32.904684,  
          34.77082  
        ]  
      ]  
    ]  
  },  
  "id": "KOURIS_ALGAE",  
  "areaServed": "kouris",  
  "provider": "CERTH",  
  "analysisType": "chl-monitoring",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.SatelliteImagery/master/context.jsonld"  
  ]  
}  
```  
</details>  
#### EOSatelliteImagery NGSI-LD normalized Example    
Here is an example of a EOSatelliteImagery in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:EOGeoDataLayer:1234",  
  "type": "EOSatelliteImagery",  
  "dataProvider": {  
    "type": "Property",  
    "value": "CERTH"  
  },  
  "contentInformation": {  
    "type": "StructuredValue",  
    "value": [  
      {  
        "layer_name": "band1",  
        "layer_categorization": "numerical",  
        "values_explanation": [  
          "100: exceptional algae bloom",  
          "10: algae bloom"  
        ]  
      }  
    ]  
  },  
  "description": {  
    "type": "Property",  
    "value": "Unified data from EO Satellite Imagery analysis for algae"  
  },  
  "localServerPath": {  
    "type": "Property",  
    "value": "algaemap-chl_wbl_kouris_20240427T082601.tif"  
  },  
  "areaServed": {  
    "type": "Property",  
    "value": "kouris"  
  },  
  "productBbox": {  
    "type": "GeoProperty",  
    "value": {  
      "type": "Polygon",  
      "coordinates": [  
        [  
          [  
            31.90052,  
            35.238084  
          ],  
          [  
            31.91356,  
            34.248107  
          ],  
          [  
            33.106002,  
            34.252876  
          ],  
          [  
            33.107275,  
            35.24303  
          ],  
          [  
            31.90052,  
            35.238084  
          ]  
        ]  
      ]  
    }  
  },  
  "processedBbox": {  
    "type": "GeoProperty",  
    "value": {  
      "type": "Polygon",  
      "coordinates": [  
        [  
          [  
            32.904684,  
            34.77082  
          ],  
          [  
            32.904684,  
            34.726095  
          ],  
          [  
            32.939337,  
            34.726095  
          ],  
          [  
            32.939337,  
            34.77082  
          ],  
          [  
            32.904684,  
            34.77082  
          ]  
        ]  
      ]  
    }  
  },  
  "storageFormat": {  
    "type": "Property",  
    "value": "GeoTIFF"  
  },  
  "productFormat": {  
    "type": "Property",  
    "value": "SAFE"  
  },  
  "productType": {  
    "type": "Property",  
    "value": "S2MSI1C"  
  },  
  "operationalMode": {  
    "type": "Property",  
    "value": "MSI"  
  },  
  "productID": {  
    "type": "Property",  
    "value": "S2A_MSIL1C_20240427T082601_N0510_R021_T36SVD_20240427T103126"  
  },  
  "productURL": {  
    "type": "Property",  
    "value": "https://catalogue.dataspace.copernicus.eu/odata/v1/Products(88f6e3c8-ae72-41dd-b5b9-014c3baa9634)/$value"  
  },  
  "sensingDate": {  
    "type": "Property",  
    "value": {  
      "@type": "date-time",  
      "@value": "2024-04-27T08:26:01Z"  
    }  
  },  
  "orbitNumber": {  
    "type": "Property",  
    "value": 21  
  },  
  "platformName": {  
    "type": "Property",  
    "value": "S2A"  
  },  
  "analysisType": {  
    "type": "Property",  
    "value": "chl-monitoring"  
  },  
  "provider": {  
    "type": "Property",  
    "value": "CERTH"  
  },  
  "resultDescription": {  
    "type": "Property",  
    "value": "description of the results"  
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
See [FAQ 10](https://smartdatamodels.org/index.php/faqs/) to get an answer on how to deal with magnitude units  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
