Entität: EODataHub  
==================  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.SatelliteImagery/blob/master/EODataHub/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Globale Beschreibung: **Diese Entität enthält eine harmonisierte Beschreibung eines generischen EO-Instruments, das für die Domäne "Satellitenbilder" erstellt wurde. Diese Entität ist in erster Linie mit der Datendrehscheibe im Zusammenhang mit Erdbeobachtungsanalyseanwendungen verbunden.**  

## Liste der Eigenschaften  

- `alternateName`: Ein alternativer Name für diesen Artikel  - `dataHubName`: Ein obligatorischer Textstring, der verwendet wird, um den Namen des verwendeten Daten-Hubs zu deklarieren  - `dataHubURL`: Ein obligatorischer Textstring, der verwendet wird, um die Url des verwendeten Daten-Hubs zu deklarieren  - `dataProvider`: Eine Folge von Zeichen, die den Anbieter der harmonisierten Dateneinheit identifiziert.  - `dateCreated`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen.  - `dateModified`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `description`: Eine Beschreibung dieses Artikels  - `id`: Eindeutiger Bezeichner der Entität  - `name`: Der Name dieses Elements.  - `owner`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Ids der Eigentümer verweist  - `seeAlso`: Liste von uri, die auf zusätzliche Ressourcen über das Element verweist  - `source`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL zum Quellobjekt.  - `type`: NGSI-LD Entity Type. Er muss gleich EODataHub sein.    
Erforderliche Eigenschaften  
- `id`  - `type`  ## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
EODataHub:    
  description: 'This entity contains a harmonised description of a generic EOInstrument made for the Satellite Imagerry domain. This entity is primarily associated with the data hub related to Earth Observation Analysis applications.'    
  properties:    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    dataHubName:    
      description: 'A mandatory text string used to declare the name of the used data hub'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    dataHubURL:    
      description: 'A mandatory text string used to declare the url of the used data hub'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/url    
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
    id:    
      anyOf: &eodatahub_-_properties_-_owner_-_items_-_anyof    
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
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *eodatahub_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
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
      type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    type:    
      description: 'NGSI-LD Entity Type. It must be equal to EODataHub.'    
      enum:    
        - EODataHub    
      type: Property    
  required:    
    - id    
    - type    
  type: object    
```  
</details>    
## Beispiel-Nutzlasten  
#### EODataHub NGSI-v2 key-values Beispiel  
Hier ist ein Beispiel für einen EODataHub im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-v2 bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "EODataHub:123",  
  "type": "EODataHub",  
  "dataHubName": "ESA Copernicus Open Access Hub",  
  "dataHubURL": "http://scihub.copernicus.eu"  
}  
```  
#### EODataHub NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für einen EODataHub im JSON-LD-Format wie normalisiert. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
    "id": "urn:ngsi-ld:EODataHub:123",  
    "type": "EODataHub",  
    "createdAt": "2020-03-13T15:42:00Z",  
    "modifiedAt": "2020-03-13T15:45:00Z",  
    "dataHubName": {  
        "type": "Property",  
        "value": "ESA Copernicus Open Access Hub"  
    },  
    "dataHubURL": {  
        "type": "url",  
        "value": "http://scihub.copernicus.eu"  
    }  
}  
```  
#### EODataHub NGSI-LD key-values Beispiel  
Hier ist ein Beispiel für einen EODataHub im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-LD bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "EODataHub:123",  
  "type": "EODataHub",  
  "dataHubName": "ESA Copernicus Open Access Hub",  
  "dataHubURL": "http://scihub.copernicus.eu",  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
#### EODataHub NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für einen EODataHub im JSON-LD-Format wie normalisiert. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "urn:ngsi-ld:EODataHub:123",  
  "type": "EODataHub",  
  "createdAt": "2020-03-13T15:42:00Z",  
  "modifiedAt": "2020-03-13T15:45:00Z",  
  "dataHubName": {  
    "type": "Property",  
    "value": "ESA Copernicus Open Access Hub"  
  },  
  "dataHubURL": {  
    "type": "url",  
    "value": "http://scihub.copernicus.eu"  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
