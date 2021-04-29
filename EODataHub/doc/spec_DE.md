Entität: EODataHub  
==================  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.SatelliteImagery/blob/master/EODataHub/LICENSE.md)  
Globale Beschreibung: **Diese Entität enthält eine harmonisierte Beschreibung eines generischen EO-Instruments, das für die Domäne "Satellitenbilder" erstellt wurde. Diese Entität ist in erster Linie mit der Datendrehscheibe im Zusammenhang mit Erdbeobachtungsanalyseanwendungen verbunden.**  

## Liste der Eigenschaften  

- `dataHubName`: Ein obligatorischer Textstring, der verwendet wird, um den Namen des verwendeten Daten-Hubs zu deklarieren  - `dataHubURL`: Ein obligatorischer Textstring, der verwendet wird, um die URL des verwendeten Daten-Hubs zu deklarieren  - `type`: NGSI-LD Entity Type. Er muss gleich EODataHub sein.    
Erforderliche Eigenschaften  
- `dataHubName`  - `dataHubURL`  - `id`  - `type`  ## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
EODataHub:    
  description: 'This entity contains a harmonised description of a generic EOInstrument made for the Satellite Imagerry domain. This entity is primarily associated with the data hub related to Earth Observation Analysis applications.'    
  properties:    
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
    type:    
      description: 'NGSI-LD Entity Type. It must be equal to EODataHub.'    
      enum:    
        - EODataHub    
      type: Property    
  required:    
    - id    
    - type    
    - dataHubName    
    - dataHubURL    
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
