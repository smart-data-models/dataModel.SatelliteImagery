<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体：EOProduct  
============<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.SatelliteImagery/blob/master/EOProduct/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全球描述：**该实体包含对卫星图像领域通用 EOProduct 的统一描述。该实体主要与地球观测分析应用相关的卫星产品有关。  
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
- `alternateName[string]`: 该项目的替代名称  - `areaServed[string]`: 提供服务或提供物品的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `cloudCoverage[number]`: 云覆盖百分比。所有单位都接受 [CEFACT](https://www.unece.org/cefact.html) 代码  . Model: [ https://schema.org/Number]( https://schema.org/Number)- `dataProvider[string]`: 标识统一数据实体提供者的字符序列  - `dateCreated[date-time]`: 实体创建时间戳。通常由存储平台分配  - `dateModified[date-time]`: 实体最后一次修改的时间戳。通常由存储平台分配  - `description[string]`: 项目描述  - `hostedOn[uri]`: 产品所在数据中心的 ID  - `id[*]`: 实体的唯一标识符  - `ingestionDate[date-time]`: 在线档案中提供数据的时间  . Model: [https://schema.org/Time](https://schema.org/Time)- `location[*]`: 项目的 Geojson 引用。它可以是点、线条字符串、多边形、多点、多线条字符串或多多边形  - `name[string]`: 该项目的名称  - `observedBy[uri]`: 产品观测仪器的 ID  - `orbitDirection[string]`: 轨道通过方向  . Model: [https://schema.org/Text](https://schema.org/Text)- `orbitNumber[number]`: 卫星传回的轨道编号。所有单位均接受 [CEFACT](https://www.unece.org/cefact.html) 代码  . Model: [ https://schema.org/Number]( https://schema.org/Number)- `owner[array]`: 包含一个 JSON 编码字符序列的列表，其中引用了所有者的唯一 Ids  - `processingLevel[string]`: 强制性文本字符串，用于声明产品的处理级别  . Model: [https://schema.org/Text](https://schema.org/Text)- `productFormat[string]`: 必须填写的文本字符串，用于声明产品的格式  . Model: [https://schema.org/Text](https://schema.org/Text)- `productID[string]`: 必须填写的文本字符串，用于声明产品的唯一 ID  . Model: [https://schema.org/Text](https://schema.org/Text)- `productType[string]`: 必须填写的文本字符串，用于声明产品类型  . Model: [https://schema.org/Text](https://schema.org/Text)- `productURL[string]`: 必须填写的 URL，用于声明产品的下载链接  . Model: [https://schema.org/url](https://schema.org/url)- `seeAlso[*]`: 指向有关该项目的其他资源的 uri 列表  - `sensingDate[date-time]`: 传感器拍摄图像的时间  . Model: [https://schema.org/Time](https://schema.org/Time)- `sensingStartedAt[date-time]`: 卫星机载采集产品中第一行图像的时间  . Model: [https://schema.org/Time](https://schema.org/Time)- `sensingStoppedAt[date-time]`: 卫星机载采集产品中最后一行图像的时间  . Model: [https://schema.org/Time](https://schema.org/Time)- `source[string]`: 以 URL 形式给出实体数据原始来源的字符串。建议使用源提供者的完全合格域名或源对象的 URL  - `timeliness[string]`: 产品的及时性  . Model: [https://schema.org/Text](https://schema.org/Text)- `type[string]`: NGSI-LD 实体类型。它必须等于 EOProduct  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
所需属性  
- `id`  - `location`  - `productFormat`  - `productID`  - `productURL`  - `sensingDate`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 属性的数据模型描述  
按字母顺序排列（点击查看详情）  
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
## 有效载荷示例  
#### EOProduct NGSI-v2 key-values 示例  
下面是一个以 JSON-LD 格式作为键值的 EOProduct 示例。当使用 `options=keyValues` 时，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
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
#### EOProduct NGSI-v2 标准化示例  
下面是一个规范化 JSON-LD 格式的 EOProduct 示例。在不使用选项的情况下，它与 NGSI-v2 兼容，并返回单个实体的上下文数据。  
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
#### EOProduct NGSI-LD key-values 示例  
下面是一个以 JSON-LD 格式作为键值的 EOProduct 示例。当使用 `options=keyValues` 时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
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
#### EOProduct NGSI-LD normalized 示例  
下面是一个规范化 JSON-LD 格式的 EOProduct 示例。在不使用选项时，它与 NGSI-LD 兼容，并返回单个实体的上下文数据。  
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
请参阅 [FAQ 10](https://smartdatamodels.org/index.php/faqs/)，获取如何处理幅度单位的答案。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
