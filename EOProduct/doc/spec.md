Entity: EOProduct  
=================  
[Open License](https://github.com/smart-data-models//dataModel.SatelliteImagery/blob/master/EOProduct/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Global description: **This entity contains a harmonised description of a generic EOProduct made for the Satellite Imagerry domain. This entity is primarily associated with the satellite products related to Earth Observation Analysis applications.**  

## List of properties  

- `address`: The mailing address  - `alternateName`: An alternative name for this item  - `areaServed`: The geographic area where a service or offered item is provided  - `cloudCoverage`: The cloud coverage percentage. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.  - `dataProvider`: A sequence of characters identifying the provider of the harmonised data entity.  - `dateCreated`: Entity creation timestamp. This will usually be allocated by the storage platform.  - `dateModified`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  - `description`: A description of this item  - `hostedOn`: The ID of the data hub that the product is hosted on  - `id`: Unique identifier of the entity  - `ingestionDate`: The time at which the data was made available in the online archive  - `location`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  - `name`: The name of this item.  - `observedBy`: The ID of the instrument that the product was observed by  - `orbitDirection`: The orbit pass orientation  - `orbitNumber`: The orbit number of tha satellite pass. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.  - `owner`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `processingLevel`: A mandatory text string used to declare the processing level of the product  - `productFormat`: A mandatory text string used to declare the format of the product  - `productID`: A mandatory text string used to declare the unique ID of the product  - `productType`: A mandatory text string used to declare the type of the product  - `productURL`: A mandatory url used to declare the downlaod link of the product  - `seeAlso`: list of uri pointing to additional resources about the item  - `sensingDate`: The time at which the image was taken by the sensor  - `sensingStartedAt`: The time of the satellite on-board acquisition of the first line of the image in the product  - `sensingStoppedAt`: The time of the satellite on-board acquisition of the last line of the image in the product  - `source`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  - `timeliness`: The timeliness of the product  - `type`: NGSI-LD Entity Type. It must be equal to EOProduct.    
Required properties  
- `id`  - `location`  - `productFormat`  - `productID`  - `productURL`  - `sensingDate`  - `type`  ## Data Model description of properties  
Sorted alphabetically (click for details)  
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
      type: Property    
      x-ngsi:    
        model: https://schema.org/address    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    cloudCoverage:    
      description: 'The cloud coverage percentage. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.'    
      type: Property    
      x-ngsi:    
        model: ' https://schema.org/Number'    
        units: percent    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    description:    
      description: 'A description of this item'    
      type: Property    
    hostedOn:    
      description: 'The ID of the data hub that the product is hosted on'    
      format: uri    
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
      type: Property    
    ingestionDate:    
      description: 'The time at which the data was made available in the online archive'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Time    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: 'Geoproperty. Geojson reference to the item. Point'    
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
        - description: 'Geoproperty. Geojson reference to the item. LineString'    
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
        - description: 'Geoproperty. Geojson reference to the item. Polygon'    
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
        - description: 'Geoproperty. Geojson reference to the item. MultiPoint'    
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
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
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
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
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
      type: Geoproperty    
    name:    
      description: 'The name of this item.'    
      type: Property    
    observedBy:    
      description: 'The ID of the instrument that the product was observed by'    
      format: uri    
      type: Relationship    
    orbitDirection:    
      description: 'The orbit pass orientation'    
      enum:    
        - Ascending    
        - Descending    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    orbitNumber:    
      description: 'The orbit number of tha satellite pass. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code.'    
      type: Property    
      x-ngsi:    
        model: ' https://schema.org/Number'    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *eoproduct_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    processingLevel:    
      description: 'A mandatory text string used to declare the processing level of the product'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    productFormat:    
      description: 'A mandatory text string used to declare the format of the product'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    productID:    
      description: 'A mandatory text string used to declare the unique ID of the product'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    productType:    
      description: 'A mandatory text string used to declare the type of the product'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    productURL:    
      description: 'A mandatory url used to declare the downlaod link of the product'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/url    
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
      type: Property    
    sensingDate:    
      description: 'The time at which the image was taken by the sensor'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Time    
    sensingStartedAt:    
      description: 'The time of the satellite on-board acquisition of the first line of the image in the product'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Time    
    sensingStoppedAt:    
      description: 'The time of the satellite on-board acquisition of the last line of the image in the product'    
      format: date-time    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Time    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    timeliness:    
      description: 'The timeliness of the product'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    type:    
      description: 'NGSI-LD Entity Type. It must be equal to EOProduct.'    
      enum:    
        - EOProduct    
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
```  
</details>    
## Example payloads    
#### EOProduct NGSI-v2 key-values Example    
Here is an example of a EOProduct in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  
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
#### EOProduct NGSI-v2 normalized Example    
Here is an example of a EOProduct in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  
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
#### EOProduct NGSI-LD key-values Example    
Here is an example of a EOProduct in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
```json  
{  
  "id": "urn:ngsi-ld:EOProduct:123",  
  "type": "EOProduct",  
  "productID": "S2A_MSIL2A_20210118T092321_N0214_R093_T34TGN_20210118T120704",  
  "productURL": "https://scihub.copernicus.eu/dhus/odata/v1/Products('698c2089-704f-4d4f-aa2f-977902e2d35e')/$value",  
  "productType": "S2MSI2A",  
  "processingLevel": "Level-2A",  
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
  "productFormat": "SAFE",  
  "cloudCoverage": 19.125499,  
  "orbitDirection": "Descending",  
  "orbitNumber": 93,  
  "ingestionDate": "2021-01-18T18:29:16.884Z",  
  "sensingDate": "2021-01-18T09:23:21.024Z",  
  "sensingStartedAt": "2021-01-18T09:23:21.024Z",  
  "sensingStoppedAt": "2021-01-18T09:23:21.024Z",  
  "hostedOn": "urn:ngsi-ld:EODataHub:123",  
  "observedBy": "urn:ngsi-ld:EOInstrument:154",  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
#### EOProduct NGSI-LD normalized Example    
Here is an example of a EOProduct in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
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
    "type": "Property",  
    "value": "SAFE"  
  },  
  "cloudCoverage": {  
    "type": "Property",  
    "value": 19.125499,  
    "unitCode": "P1"  
  },  
  "orbitDirection": {  
    "type": "Property",  
    "value": "Descending"  
  },  
  "orbitNumber": {  
    "type": "Property",  
    "value": 93  
  },  
  "ingestionDate": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2021-01-18T18:29:16.884Z"  
    }  
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
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
