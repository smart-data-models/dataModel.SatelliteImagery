<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entidad: EOInstrument    
=====================<!-- /10-Header -->    
<!-- 15-License -->    
[Licencia abierta](https://github.com/smart-data-models//dataModel.SatelliteImagery/blob/master/EOInstrument/LICENSE.md)    
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Descripción global: **Esta entidad contiene una descripción armonizada de un EOInstrument genérico realizado para el dominio Satellite Imagerry. Esta entidad se asocia principalmente con los instrumentos de satélite relacionados con las aplicaciones de análisis de observación de la Tierra.**.    
versión: 0.0.1    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## Lista de propiedades    
<sup><sub>[*] Si no hay un tipo en un atributo es porque puede tener varios tipos o diferentes formatos/patrones</sub></sup>.    
- `alternateName[string]`: Un nombre alternativo para este artículo  - `carriedOn[uri]`: ID de la plataforma por satélite en la que se transporta el instrumento  - `dataProvider[string]`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada  - `dateCreated[date-time]`: Fecha de creación de la entidad. Normalmente será asignada por la plataforma de almacenamiento  - `dateModified[date-time]`: Marca de tiempo de la última modificación de la entidad. Suele ser asignada por la plataforma de almacenamiento  - `description[string]`: Descripción de este artículo  - `id[*]`: Identificador único de la entidad  - `instrumentID[string]`: Cadena de texto obligatoria utilizada para declarar el ID de la carga útil del instrumento.  . Model: [https://schema.org/Text](https://schema.org/Text)- `instrumentName[string]`: Cadena de texto obligatoria utilizada para declarar el nombre de la carga útil del instrumento.  . Model: [https://schema.org/Text](https://schema.org/Text)- `name[string]`: El nombre de este artículo  - `operationalMode[string]`: Una cadena de texto utilizada para declarar los modos de sensor soportados si están disponibles  . Model: [https://schema.org/Text](https://schema.org/Text)- `owner[array]`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios.  - `polarizationMode[string]`: Una cadena de texto utilizada para declarar los modos de polarización si están disponibles  . Model: [https://schema.org/Text](https://schema.org/Text)- `seeAlso[*]`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source[string]`: Secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen o la URL del objeto de origen.  - `swathID[string]`: Una cadena de texto utilizada para declarar el ID de la hilera si está disponible  . Model: [https://schema.org/Text](https://schema.org/Text)- `type[string]`: Tipo de entidad NGSI-LD. Debe ser igual a EOInstrument  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Propiedades requeridas    
- `id`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## Descripción de las propiedades del modelo de datos    
Ordenados alfabéticamente (pulse para más detalles)    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
EOInstrument:      
  description: This entity contains a harmonised description of a generic EOInstrument made for the Satellite Imagerry domain. This entity is primarily associated with the satellite instruments related to Earth Observation Analysis applications.      
  properties:      
    alternateName:      
      description: An alternative name for this item      
      type: string      
      x-ngsi:      
        type: Property      
    carriedOn:      
      description: The ID of the satellite platform that the instrument is carried on      
      format: uri      
      type: string      
      x-ngsi:      
        type: Relationship      
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
    instrumentID:      
      description: A mandatory text string used to declare the ID of the instrument payload      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    instrumentName:      
      description: A mandatory text string used to declare the name of the instrument payload      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
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
    polarizationMode:      
      description: A text string used to declare the polarization modes if available      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
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
    source:      
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'      
      type: string      
      x-ngsi:      
        type: Property      
    swathID:      
      description: A text string used to declare the swath ID if available      
      type: string      
      x-ngsi:      
        model: https://schema.org/Text      
        type: Property      
    type:      
      description: NGSI-LD Entity Type. It must be equal to EOInstrument      
      enum:      
        - EOInstrument      
      type: string      
      x-ngsi:      
        type: Property      
  required:      
    - id      
    - type      
  type: object      
  x-derived-from: ""      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.SatelliteImagery/blob/master/EOInstrument/LICENSE.md      
  x-model-schema: https://raw.githubusercontent.com/smart-data-models/dataModel.SatelliteImagery/master/EOInstrument/schema.json      
  x-model-tags: ""      
  x-version: 0.0.1      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## Ejemplo de carga útil    
#### EOInstrument NGSI-v2 key-values Ejemplo    
He aquí un ejemplo de un EOInstrument en formato JSON-LD como key-values. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:EOInstrument:154",  
  "type": "EOInstrument",  
  "instrumentID": "OLCI",  
  "instrumentName": "Ocean Land Colour Instrument",  
  "operationalMode": "INS-NOBS",  
  "polarizationMode": "HH+HV",  
  "swathID": "S1",  
  "carriedOn": "urn:ngsi-ld:EOSatellitePlatform:154"  
}  
```  
</details>    
#### EOInstrument NGSI-v2 normalizado Ejemplo    
He aquí un ejemplo de un EOInstrument en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:EOInstrument:154",  
  "type": "EOInstrument",  
  "createdAt": {  
    "type": "DateTime",  
    "value": "2020-03-13T15:42:00Z"  
  },  
  "modifiedAt": {  
    "type": "DateTime",  
    "value": "2020-03-13T15:45:00Z"  
  },  
  "carriedOn": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:EOSatellitePlatform:154"  
  },  
  "instrumentID": {  
    "type": "Text",  
    "value": "MSI"  
  },  
  "instrumentName": {  
    "type": "Text",  
    "value": "Multi-Spectral Instrument"  
  },  
  "swathID": {  
    "type": "Text",  
    "value": "S2"  
  }  
}  
```  
</details>    
#### EOInstrument NGSI-LD key-values Ejemplo    
He aquí un ejemplo de un EOInstrument en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:EOInstrument:154",  
  "type": "EOInstrument",  
  "carriedOn": "urn:ngsi-ld:EOSatellitePlatform:154",  
  "instrumentID": "MSI",  
  "instrumentName": "Multi-Spectral Instrument",  
  "swathID": "S2",  
  "@context": [  
    "https://raw.githubusercontent.com/smart-data-models/dataModel.SatelliteImagery/master/context.jsonld"  
  ]  
}  
```  
</details>    
#### EOInstrument NGSI-LD normalizado Ejemplo    
He aquí un ejemplo de un EOInstrument en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
    "id": "urn:ngsi-ld:EOInstrument:154",  
    "type": "EOInstrument",  
    "carriedOn": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:EOSatellitePlatform:154"  
    },  
    "createdAt": "2020-03-13T15:42:00Z",  
    "instrumentID": {  
        "type": "Property",  
        "value": "SAR-C"  
    },  
    "instrumentName": {  
        "type": "Property",  
        "value": "Synthetic Aperture Radar (C-band)"  
    },  
    "modifiedAt": "2020-03-13T15:45:00Z",  
    "operationalMode": {  
        "type": "Property",  
        "value": "IW"  
    },  
    "polarizaionMode": {  
        "type": "Property",  
        "value": "VV + VH"  
    },  
    "swathID": {  
        "type": "Property",  
        "value": "S1"  
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
