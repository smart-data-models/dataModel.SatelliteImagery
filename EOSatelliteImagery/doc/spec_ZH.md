<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体：EOSatelliteImagery  
=====================<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.SatelliteImagery/blob/master/EOSatelliteImagery/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全局描述：**本模式定义了 SatelliteImagery 域内的一个统一实体，整合了与卫星图像相关的所有现有实体的属性，旨在为 EO 流程提供一个整体视图**。  
版本： 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## 属性列表  

<sup><sub>[*] 如果属性中没有类型，是因为它可能有多个类型或不同的格式/模式</sub></sup>。  
- `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 国家。例如，西班牙  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: 街道地址所在的地点，以及该地点所在的区域  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: 地点所在的地区，以及该地区位于哪个国家  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 地区是一种行政区划，在一些国家由地方政府管理    
	- `postOfficeBoxNumber[string]`: 用于邮政信箱地址的邮政信箱号码。例如：03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 邮政编码。例如：24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 街道地址  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: 标识公共街道上特定房产的编号    
- `alternateName[string]`: 该项目的替代名称  - `analysisType[string]`: 实体采用的分析类型  - `areaServed[string]`: 提供服务或提供物品的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `contentInformation[array]`: 一个数组，用于描述每个层（如 band1）或实体名称、信息类型（如分类、数值）以及描述值解释的数组（如 [1:油，0:无油]）。  - `dataProvider[string]`: 标识统一数据实体提供者的字符序列  - `dateCreated[date-time]`: 实体创建时间戳。通常由存储平台分配  - `dateModified[date-time]`: 实体最后一次修改的时间戳。通常由存储平台分配  - `description[string]`: 项目描述  - `id[*]`: 实体的唯一标识符  - `localServerPath[string]`: 必填文本字符串，用于声明输出数据层在服务器上的保存路径  . Model: [https://schema.org/Text](https://schema.org/Text)- `location[*]`: 项目的 Geojson 引用。它可以是点、线条字符串、多边形、多点、多线条字符串或多多边形  - `name[string]`: 该项目的名称  - `operationalMode[string]`: 文本字符串，用于声明所支持的传感器模式（如果有的话  . Model: [https://schema.org/Text](https://schema.org/Text)- `orbitNumber[number]`: 卫星传回的轨道编号。所有单位均接受 [CEFACT](https://www.unece.org/cefact.html) 代码  . Model: [ https://schema.org/Number]( https://schema.org/Number)- `owner[array]`: 包含一个 JSON 编码字符序列的列表，其中引用了所有者的唯一 Ids  - `platformName[string]`: 必须填写的文本字符串，用于声明平台名称  . Model: [https://schema.org/Text](https://schema.org/Text)- `processedBbox[*]`: 项目的 Geojson 引用。它可以是点、线条字符串、多边形、多点、多线条字符串或多多边形  - `productBbox[*]`: 项目的 Geojson 引用。它可以是点、线条字符串、多边形、多点、多线条字符串或多多边形  - `productFormat[string]`: 必须填写的文本字符串，用于声明产品的格式  . Model: [https://schema.org/Text](https://schema.org/Text)- `productID[string]`: 必须填写的文本字符串，用于声明产品的唯一 ID  . Model: [https://schema.org/Text](https://schema.org/Text)- `productType[string]`: 必须填写的文本字符串，用于声明产品类型  . Model: [https://schema.org/Text](https://schema.org/Text)- `productURL[string]`: 用于声明产品下载链接的必填网址  . Model: [https://schema.org/url](https://schema.org/url)- `provider[string]`: 算法提供者  . Model: [ https://schema.org/Text]( https://schema.org/Text)- `resultDescription[string]`: 分析结果说明  - `seeAlso[*]`: 指向有关该项目的其他资源的 uri 列表  - `sensingDate[string]`: 传感器拍摄图像的时间  . Model: [https://schema.org/Time](https://schema.org/Time)- `source[string]`: 以 URL 形式给出实体数据原始来源的字符串。建议使用源提供者的完全合格域名或源对象的 URL  - `storageFormat[string]`: 实体的萨特奇格式  - `type[string]`: NGSI 实体类型。它必须等于 EOSatelliteImagery  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
所需属性  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## 属性的数据模型描述  
按字母顺序排列（点击查看详情）  
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
## 有效载荷示例  
#### EOSatelliteImagery NGSI-v2 关键值示例  
下面是一个以 JSON-LD 格式作为键值的 EOSatelliteImagery 示例。当使用 "options=keyValues "时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
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
#### EOSatelliteImagery NGSI-v2 标准化示例  
下面是一个规范化 JSON-LD 格式的 EOSatelliteImagery 示例。当不使用选项时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
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
#### EOSatelliteImagery NGSI-LD 关键值 示例  
下面是一个以 JSON-LD 格式作为键值的 EOSatelliteImagery 示例。当使用 "options=keyValues "时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
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
#### EOSatelliteImagery NGSI-LD 归一化示例  
下面是一个规范化 JSON-LD 格式的 EOSatelliteImagery 示例。当不使用选项时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
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
请参阅 [FAQ 10](https://smartdatamodels.org/index.php/faqs/)，获取如何处理幅度单位的答案。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
