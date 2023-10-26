<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
엔티티: EOInstrument  
=================<!-- /10-Header -->  
<!-- 15-License -->  
[오픈 라이선스](https://github.com/smart-data-models//dataModel.SatelliteImagery/blob/master/EOInstrument/LICENSE.md)  
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
글로벌 설명: **이 엔티티에는 위성 영상 영역용으로 만들어진 일반 EOInstrument에 대한 조화로운 설명이 포함되어 있습니다. 이 엔티티는 주로 지구 관측 분석 애플리케이션과 관련된 위성 기기와 연관되어 있습니다.**  
버전: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## 속성 목록  

<sup><sub>[*] 속성에 유형이 없는 것은 여러 유형 또는 다른 형식/패턴을 가질 수 있기 때문입니다</sub></sup>.  
- `alternateName[string]`: 이 항목의 대체 이름  - `carriedOn[uri]`: 기기가 탑재된 위성 플랫폼의 ID입니다.  - `dataProvider[string]`: 조화된 데이터 엔티티의 공급자를 식별하는 일련의 문자  - `dateCreated[date-time]`: 엔티티 생성 타임스탬프. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `dateModified[date-time]`: 엔티티의 마지막 수정 타임스탬프입니다. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `description[string]`: 이 항목에 대한 설명  - `id[*]`: 엔티티의 고유 식별자  - `instrumentID[string]`: 상품 페이로드의 ID를 선언하는 데 사용되는 필수 텍스트 문자열입니다.  . Model: [https://schema.org/Text](https://schema.org/Text)- `instrumentName[string]`: 상품 페이로드의 이름을 선언하는 데 사용되는 필수 텍스트 문자열입니다.  . Model: [https://schema.org/Text](https://schema.org/Text)- `name[string]`: 이 항목의 이름  - `operationalMode[string]`: 지원되는 센서 모드(사용 가능한 경우)를 선언하는 데 사용되는 텍스트 문자열입니다.  . Model: [https://schema.org/Text](https://schema.org/Text)- `owner[array]`: 소유자의 고유 ID를 참조하는 JSON 인코딩된 문자 시퀀스가 포함된 목록입니다.  - `polarizationMode[string]`: 가능한 경우 편광 모드를 선언하는 데 사용되는 텍스트 문자열입니다.  . Model: [https://schema.org/Text](https://schema.org/Text)- `seeAlso[*]`: 항목에 대한 추가 리소스를 가리키는 URL 목록  - `source[string]`: 엔티티 데이터의 원본 소스를 URL로 제공하는 문자 시퀀스입니다. 소스 공급자의 정규화된 도메인 이름 또는 소스 개체에 대한 URL을 사용하는 것이 좋습니다.  - `swathID[string]`: 사용 가능한 경우 스와스 ID를 선언하는 데 사용되는 텍스트 문자열입니다.  . Model: [https://schema.org/Text](https://schema.org/Text)- `type[string]`: NGSI-LD 엔티티 유형. EOInstrument와 같아야 합니다.  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
필수 속성  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 속성에 대한 데이터 모델 설명  
알파벳순으로 정렬(자세한 내용을 보려면 클릭)  
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
## 페이로드 예시  
#### EO인스트루먼트 NGSI-v2 키-값 예제  
다음은 키-값으로 JSON-LD 형식의 EOInstrument의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
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
#### EO인스트루먼트 NGSI-v2 정규화 예제  
다음은 정규화된 JSON-LD 형식의 EOInstrument의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:EOInstrument:154",  
  "type": "EOInstrument",  
  "createdAt": "2020-03-13T15:42:00Z",  
  "modifiedAt": "2020-03-13T15:45:00Z",  
  "carriedOn": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:EOSatellitePlatform:154"  
  },  
  "instrumentID": {  
    "type": "Property",  
    "value": "MSI"  
  },  
  "instrumentName": {  
    "type": "Property",  
    "value": "Multi-Spectral Instrument"  
  },  
  "swathID": {  
    "type": "Property",  
    "value": "S2"  
  }  
}  
```  
</details>  
#### EO인스트루먼트 NGSI-LD 키-값 예제  
다음은 키-값으로 JSON-LD 형식의 EOInstrument의 예입니다. 이는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
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
#### EO인스트루먼트 NGSI-LD 정규화 예제  
다음은 정규화된 JSON-LD 형식의 EOInstrument의 예입니다. 이는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
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
[FAQ 10](https://smartdatamodels.org/index.php/faqs/)을 참조하여 규모 단위를 다루는 방법에 대한 답변을 확인하세요.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
