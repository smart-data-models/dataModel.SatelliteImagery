<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
엔티티: EOSatelliteImage  
=====================<!-- /10-Header -->  
<!-- 15-License -->  
[오픈 라이선스](https://github.com/smart-data-models//dataModel.SatelliteImagery/blob/master/EOSatelliteImagery/LICENSE.md)  
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
글로벌 설명: **이 스키마는 위성 이미지와 관련된 모든 기존 엔티티의 속성을 통합하여 위성 이미지 도메인 내의 통합 엔티티를 정의하며, EO 프로세스에서 전체적인 관점을 제공하도록 설계되었습니다**.  
버전: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## 속성 목록  

<sup><sub>[*] 속성에 유형이 없는 것은 여러 유형 또는 다른 형식/패턴을 가질 수 있기 때문입니다</sub></sup>.  
- `address[object]`: 우편 주소  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 국가. 예를 들어, 스페인  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: 도로명 주소가 있는 지역 및 해당 지역 내 지역  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: 해당 지역이 위치한 지역과 해당 국가의 지역  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: 지구는 일부 국가에서는 지방 정부에서 관리하는 행정 구역의 일종입니다.    
	- `postOfficeBoxNumber[string]`: 사서함 주소의 우체국 사서함 번호입니다. 예: 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: 우편 번호입니다. 예: 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: 거리 주소  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
	- `streetNr[string]`: 공공 도로의 특정 건물을 식별하는 번호    
- `alternateName[string]`: 이 항목의 대체 이름  - `analysisType[string]`: 적용된 엔티티의 분석 유형  - `areaServed[string]`: 서비스 또는 제공 품목이 제공되는 지리적 영역  . Model: [https://schema.org/Text](https://schema.org/Text)- `contentInformation[array]`: 각 레이어(예: band1) 또는 엔티티 이름, 정보 유형(예: 범주형, 숫자형) 및 표시된 값에 대한 설명이 포함된 배열(예: [1:기름, 0:기름 없음])  - `dataProvider[string]`: 조화된 데이터 엔티티의 공급자를 식별하는 일련의 문자  - `dateCreated[date-time]`: 엔티티 생성 타임스탬프. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `dateModified[date-time]`: 엔티티의 마지막 수정 타임스탬프입니다. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `description[string]`: 이 항목에 대한 설명  - `id[*]`: 엔티티의 고유 식별자  - `localServerPath[string]`: 출력 데이터 레이어가 서버에 저장되는 경로를 선언하는 데 사용되는 필수 텍스트 문자열입니다.  . Model: [https://schema.org/Text](https://schema.org/Text)- `location[*]`: 항목에 대한 지오숀 참조입니다. 포인트, 라인스트링, 다각형, 멀티포인트, 멀티라인스트링 또는 멀티폴리곤일 수 있습니다.  - `name[string]`: 이 항목의 이름  - `operationalMode[string]`: 지원되는 센서 모드(사용 가능한 경우)를 선언하는 데 사용되는 텍스트 문자열입니다.  . Model: [https://schema.org/Text](https://schema.org/Text)- `orbitNumber[number]`: 위성 패스의 궤도 번호입니다. 모든 단위는 [CEFACT](https://www.unece.org/cefact.html) 코드로 허용됩니다.  . Model: [ https://schema.org/Number]( https://schema.org/Number)- `owner[array]`: 소유자의 고유 ID를 참조하는 JSON 인코딩된 문자 시퀀스가 포함된 목록입니다.  - `platformName[string]`: 플랫폼의 이름을 선언하는 데 사용되는 필수 텍스트 문자열입니다.  . Model: [https://schema.org/Text](https://schema.org/Text)- `processedBbox[*]`: 항목에 대한 지오숀 참조입니다. 포인트, 라인스트링, 다각형, 멀티포인트, 멀티라인스트링 또는 멀티폴리곤일 수 있습니다.  - `productBbox[*]`: 항목에 대한 지오숀 참조입니다. 포인트, 라인스트링, 다각형, 멀티포인트, 멀티라인스트링 또는 멀티폴리곤일 수 있습니다.  - `productFormat[string]`: 제품 형식을 선언하는 데 사용되는 필수 텍스트 문자열입니다.  . Model: [https://schema.org/Text](https://schema.org/Text)- `productID[string]`: 제품의 고유 ID를 선언하는 데 사용되는 필수 텍스트 문자열입니다.  . Model: [https://schema.org/Text](https://schema.org/Text)- `productType[string]`: 제품 유형을 선언하는 데 사용되는 필수 텍스트 문자열입니다.  . Model: [https://schema.org/Text](https://schema.org/Text)- `productURL[string]`: 제품의 다운로드 링크를 선언하는 데 사용되는 필수 URL입니다.  . Model: [https://schema.org/url](https://schema.org/url)- `provider[string]`: 알고리즘 제공자  . Model: [ https://schema.org/Text]( https://schema.org/Text)- `resultDescription[string]`: 분석 결과에 대한 설명  - `seeAlso[*]`: 항목에 대한 추가 리소스를 가리키는 URL 목록  - `sensingDate[string]`: 센서가 이미지를 촬영한 시간입니다.  . Model: [https://schema.org/Time](https://schema.org/Time)- `source[string]`: 엔티티 데이터의 원본 소스를 URL로 제공하는 문자 시퀀스입니다. 소스 공급자의 정규화된 도메인 이름 또는 소스 개체에 대한 URL을 사용하는 것이 좋습니다.  - `storageFormat[string]`: 엔티티의 사토라지 형식  - `type[string]`: NGSI 엔티티 유형. EOSatelliteImage와 같아야 합니다.  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
필수 속성  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-NotesYaml -->  
<!-- /40-NotesYaml -->  
<!-- 50-DataModelHeader -->  
## 속성에 대한 데이터 모델 설명  
알파벳순으로 정렬(자세한 내용을 보려면 클릭)  
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
## 페이로드 예시  
#### EOSatelliteImagery NGSI-v2 키 값 예시  
다음은 키-값으로 JSON-LD 형식의 EOSatelliteImagery의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
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
#### EOSatelliteImagery NGSI-v2 정규화 예시  
다음은 정규화된 JSON-LD 형식의 EOSatelliteImage의 예시입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
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
#### EOSatelliteImagery NGSI-LD 키 값 예시  
다음은 키-값으로 JSON-LD 형식의 EOSatelliteImagery의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
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
#### EOSatelliteImagery NGSI-LD 정규화 예시  
다음은 정규화된 JSON-LD 형식의 EOSatelliteImage의 예시입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
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
규모 단위를 다루는 방법에 대한 답변은 [FAQ 10](https://smartdatamodels.org/index.php/faqs/)을 참조하세요.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
