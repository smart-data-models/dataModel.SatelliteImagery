<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entità: Piattaforma EOSatellite  
===============================<!-- /10-Header -->  
<!-- 15-License -->  
[Licenza aperta](https://github.com/smart-data-models//dataModel.SatelliteImagery/blob/master/EOSatellitePlatform/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descrizione globale: **Questa entità contiene una descrizione armonizzata di una generica EOSatellitePlatform realizzata per il dominio Satellite Imagerry. Questa entità è associata principalmente alle piattaforme satellitari relative alle applicazioni di analisi dell'osservazione della Terra **.  
versione: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Elenco delle proprietà  

<sup><sub>[*] Se non c'è un tipo in un attributo è perché potrebbe avere diversi tipi o diversi formati/modelli</sub></sup>.  
- `alternateName[string]`: Un nome alternativo per questa voce  - `dataProvider[string]`: Una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata.  - `dateCreated[string]`: Timestamp di creazione dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione.  - `dateModified[string]`: Timestamp dell'ultima modifica dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione.  - `description[string]`: Descrizione dell'articolo  - `id[*]`: Identificatore univoco dell'entità  - `name[string]`: Il nome di questo elemento.  - `owner[array]`: Un elenco contenente una sequenza di caratteri codificata JSON che fa riferimento agli ID univoci dei proprietari.  - `platformID[string]`: Una stringa di testo obbligatoria utilizzata per dichiarare l'ID univoco della piattaforma.  . Model: [https://schema.org/Text](https://schema.org/Text)- `platformNSSDCA[string]`: Una stringa di testo obbligatoria utilizzata per dichiarare l'id univoco della missione nell'archivio del National Space Science Data Center.  . Model: [https://schema.org/Text](https://schema.org/Text)- `platformName[string]`: Una stringa di testo obbligatoria utilizzata per dichiarare il nome della piattaforma.  . Model: [https://schema.org/Text](https://schema.org/Text)- `seeAlso[*]`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source[string]`: Una sequenza di caratteri che indica la fonte originale dei dati dell'entità come URL. Si consiglia di utilizzare il nome di dominio completamente qualificato del provider di origine o l'URL dell'oggetto di origine.  - `type[string]`: Tipo di entità NGSI-LD. Deve essere uguale a EOSatellitePlatform.  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Proprietà richieste  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Modello di dati descrizione delle proprietà  
Ordinati in ordine alfabetico (clicca per i dettagli)  
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
## Esempi di payload  
#### EOSatellitePlatform NGSI-v2 valori-chiave Esempio  
Ecco un esempio di EOSatellitePlatform in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
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
#### EOSatellitePlatform NGSI-v2 normalizzato Esempio  
Ecco un esempio di EOSatellitePlatform in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.  
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
#### EOSatellitePlatform Valori chiave NGSI-LD Esempio  
Ecco un esempio di EOSatellitePlatform in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
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
#### EOSatellitePlatform NGSI-LD normalizzato Esempio  
Ecco un esempio di EOSatellitePlatform in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.  
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
Vedere [FAQ 10](https://smartdatamodels.org/index.php/faqs/) per ottenere una risposta su come gestire le unità di grandezza.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
