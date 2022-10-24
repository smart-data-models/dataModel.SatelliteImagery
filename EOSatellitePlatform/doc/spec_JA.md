<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティEOSatellitePlatform  
=========================<!-- /10-Header -->  
<!-- 15-License -->  
[オープンライセンス](https://github.com/smart-data-models//dataModel.SatelliteImagery/blob/master/EOSatellitePlatform/LICENSE.md)  
[ドキュメント自動生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバルな記述。**このエンティティは、Satellite Imagerry ドメインのために作られた汎用 EOSatellitePlatform の調和された記述 を含む。このエンティティは、主に地球観測解析アプリケーションに関連する衛星プラットフォームと関連している。  
バージョン: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## プロパティ一覧  

<sup><sub>[*] 属性にタイプがない場合、複数のタイプまたは異なるフォーマット/パターンを持つ可能性があるためです</sub></sup>。  
- `alternateName[string]`: この項目の別称  - `dataProvider[string]`: 調和されたデータエンティティの提供者を識別する一連の文字。  - `dateCreated[string]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `dateModified[string]`: エンティティの最終更新のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `description[string]`: このアイテムの説明  - `id[*]`: エンティティの一意な識別子  - `name[string]`: このアイテムの名称です。  - `owner[array]`: 所有者の一意のIDを参照するJSONエンコードされた文字列を含むリスト  - `platformID[string]`: プラットフォームの固有 ID を宣言するために使用される必須のテキスト文字列  . Model: [https://schema.org/Text](https://schema.org/Text)- `platformNSSDCA[string]`: 国立宇宙科学データセンターアーカイブで一意のミッションIDを宣言するために使用される必須のテキスト文字列です。  . Model: [https://schema.org/Text](https://schema.org/Text)- `platformName[string]`: プラットフォームの名前を宣言するために使用される必須のテキスト文字列  . Model: [https://schema.org/Text](https://schema.org/Text)- `seeAlso[*]`: 項目に関する追加リソースを指すURIのリスト。  - `source[string]`: エンティティデータの元のソースをURLで示す一連の文字。ソースプロバイダの完全修飾ドメイン名、またはソースオブジェクトのURLであることが推奨されます。  - `type[string]`: NGSI-LD エンティティタイプ。EOSatellitePlatform と等しくなければならない。  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
必要なプロパティ  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## プロパティのデータモデル記述  
アルファベット順に並びます（クリックで詳細へ）  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
EOSatellitePlatform:    
  description: 'This entity contains a harmonised description of a generic EOSatellitePlatform made for the Satellite Imagerry domain. This entity is primarily associated with the Satellite platforms related to Earth Observation Analysis applications.'    
  properties:    
    alternateName:    
      description: 'An alternative name for this item'    
      type: string    
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
    id:    
      anyOf: &eosatelliteplatform_-_properties_-_owner_-_items_-_anyof    
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
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *eosatelliteplatform_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    platformID:    
      description: 'A mandatory text string used to declare the unique ID of the platform'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    platformNSSDCA:    
      description: 'A mandatory text string used to declare the unique mission id in the National Space Science Data Center Archive'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    platformName:    
      description: 'A mandatory text string used to declare the name of the platform'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
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
    type:    
      description: 'NGSI-LD Entity Type. It must be equal to EOSatellitePlatform.'    
      enum:    
        - EOSatellitePlatform    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.SatelliteImagery/blob/master/EOSatellitePlatform/LICENSE.md    
  x-model-schema: https://raw.githubusercontent.com/smart-data-models/dataModel.SatelliteImagery/master/EOSatellitePlatform/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ペイロードの例  
#### EOSatellitePlatform NGSI-v2 key-value の例。  
ここでは、EOSatellitePlatformをJSON-LD形式でkey-valuesとした例を示します。これは、`options=keyValues`を使用した場合、NGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返す。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:EOSatellitePlatform:154",  
  "type": "EOSatellitePlatform",  
  "platformID": "B",  
  "platformName": "Sentinel-1",  
  "platformNSSDCA": "2016-025A"  
}  
```  
</details>  
#### EOSatellitePlatform NGSI-v2 正規化例  
EOSatellitePlatformをJSON-LD形式で正規化した例です。これは、オプションを使用しない場合、NGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:EOSatellitePlatform:154",  
  "type": "EOSatellitePlatform",  
  "createdAt": "2020-03-13T15:42:00Z",  
  "modifiedAt": "2020-03-13T15:45:00Z",  
  "platformID": {  
    "type": "Property",  
    "value": "A"  
  },  
  "platformName": {  
    "type": "Property",  
    "value": "Sentinel-2"  
  },  
  "platformNSSDCA": {  
    "type": "Property",  
    "value": "2015-028A"  
  }  
}  
```  
</details>  
#### EOSatellitePlatform NGSI-LD key-value Example  
ここでは、EOSatellitePlatformをJSON-LD形式でkey-valueにした例を示します。これは、`options=keyValues`を使用した場合にNGSI-LDと互換性があり、個々のエンティティのコンテキストデータが返される。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:EOSatellitePlatform:154",  
    "type": "EOSatellitePlatform",  
    "platformID": "A",  
    "platformNSSDCA": "2015-028A",  
    "platformName": "Sentinel-2",  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.SatelliteImagery/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### EOSatellitePlatform NGSI-LD 正規化例  
EOSatellitePlatformをJSON-LD形式で正規化した例です。これはオプションを使用しない場合、NGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:EOSatellitePlatform:154",  
    "type": "EOSatellitePlatform",  
    "createdAt": "2020-03-13T15:42:00Z",  
    "modifiedAt": "2020-03-13T15:45:00Z",  
    "platformID": {  
        "type": "Property",  
        "value": "B"  
    },  
    "platformNSSDCA": {  
        "type": "Property",  
        "value": "2016-025A"  
    },  
    "platformName": {  
        "type": "Property",  
        "value": "Sentinel-1"  
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
マグニチュード単位の扱いについては、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照してください。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
