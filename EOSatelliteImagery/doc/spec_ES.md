<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entidad: EOSatelliteImagery  
===========================<!-- /10-Header -->  
<!-- 15-License -->  
[Licencia abierta](https://github.com/smart-data-models//dataModel.SatelliteImagery/blob/master/EOSatelliteImagery/LICENSE.md)  
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descripción global: **Este esquema define una entidad unificada dentro del dominio SatelliteImagery, consolidando atributos de todas las entidades existentes relacionadas con las imágenes de satélite, diseñadas para ofrecer una visión holística en el proceso EO**.  
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
	- `streetNr[string]`: Número que identifica una propiedad específica en una vía pública    
- `alternateName[string]`: Un nombre alternativo para este artículo  - `analysisType[string]`: Tipo de análisis aplicado por la entidad  - `areaServed[string]`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  . Model: [https://schema.org/Text](https://schema.org/Text)- `contentInformation[array]`: Una matriz que describe para cada capa (por ejemplo, banda1) o nombre de entidad, el tipo de información (por ejemplo, categórica, numérica) y una matriz con la explicación de los valores representados (por ejemplo, [1:aceite, 0:sin aceite]).  - `dataProvider[string]`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada  - `dateCreated[date-time]`: Fecha de creación de la entidad. Normalmente será asignada por la plataforma de almacenamiento  - `dateModified[date-time]`: Marca de tiempo de la última modificación de la entidad. Suele ser asignada por la plataforma de almacenamiento  - `description[string]`: Descripción de este artículo  - `id[*]`: Identificador único de la entidad  - `localServerPath[string]`: Cadena de texto obligatoria utilizada para declarar la ruta en la que se guarda la capa de datos de salida en el servidor.  . Model: [https://schema.org/Text](https://schema.org/Text)- `location[*]`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon.  - `name[string]`: El nombre de este artículo  - `operationalMode[string]`: Una cadena de texto utilizada para declarar los modos de sensor soportados si están disponibles  . Model: [https://schema.org/Text](https://schema.org/Text)- `orbitNumber[number]`: Número de órbita del pase del satélite. Todas las unidades se aceptan en código [CEFACT](https://www.unece.org/cefact.html)  . Model: [ https://schema.org/Number]( https://schema.org/Number)- `owner[array]`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios.  - `platformName[string]`: Cadena de texto obligatoria utilizada para declarar el nombre de la plataforma.  . Model: [https://schema.org/Text](https://schema.org/Text)- `processedBbox[*]`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon.  - `productBbox[*]`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon.  - `productFormat[string]`: Cadena de texto obligatoria utilizada para declarar el formato del producto.  . Model: [https://schema.org/Text](https://schema.org/Text)- `productID[string]`: Cadena de texto obligatoria utilizada para declarar el ID único del producto.  . Model: [https://schema.org/Text](https://schema.org/Text)- `productType[string]`: Cadena de texto obligatoria utilizada para declarar el tipo de producto  . Model: [https://schema.org/Text](https://schema.org/Text)- `productURL[string]`: Una url obligatoria utilizada para declarar el enlace de descarga del producto  . Model: [https://schema.org/url](https://schema.org/url)- `provider[string]`: El proveedor del algoritmo  . Model: [ https://schema.org/Text]( https://schema.org/Text)- `resultDescription[string]`: La descripción del resultado del análisis  - `seeAlso[*]`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `sensingDate[string]`: Hora a la que el sensor tomó la imagen  . Model: [https://schema.org/Time](https://schema.org/Time)- `source[string]`: Secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen o la URL del objeto de origen.  - `storageFormat[string]`: Formato de satorage de la entidad  - `type[string]`: Tipo de entidad NGSI. Debe ser igual a EOSatelliteImagery  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propiedades requeridas  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## Descripción de las propiedades del modelo de datos  
Ordenados alfabéticamente (pulse para más detalles)  
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
## Ejemplo de carga útil  
#### EOSatelliteImagery NGSI-v2 key-values Ejemplo  
Aquí hay un ejemplo de un EOSatelliteImagery en formato JSON-LD como key-values. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
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
#### EOSatelliteImagery NGSI-v2 normalizado Ejemplo  
He aquí un ejemplo de un EOSatelliteImagery en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
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
#### EOSatelliteImagery NGSI-LD key-values Ejemplo  
Aquí hay un ejemplo de un EOSatelliteImagery en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
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
#### EOSatelliteImagery NGSI-LD normalizado Ejemplo  
He aquí un ejemplo de una EOSatelliteImagery en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
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
Consulte [FAQ 10](https://smartdatamodels.org/index.php/faqs/) para obtener una respuesta sobre cómo tratar las unidades de magnitud.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
