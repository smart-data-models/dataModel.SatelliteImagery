Entität: EOInstrument  
=====================  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.SatelliteImagery/blob/master/EOInstrument/LICENSE.md)  
Globale Beschreibung: **Diese Entität enthält eine harmonisierte Beschreibung eines generischen EO-Instruments, das für die Domäne "Satellitenbilder" erstellt wurde. Diese Entität ist in erster Linie mit den Satelliteninstrumenten verbunden, die mit Erdbeobachtungsanalyseanwendungen in Verbindung stehen.**  

## Liste der Eigenschaften  

- `carriedOn`: Die ID der Satellitenplattform, auf der sich das Gerät befindet  - `instrumentID`: Ein obligatorischer Textstring, der zur Angabe der ID der Nutzlast des Geräts verwendet wird  - `instrumentName`: Ein obligatorischer Textstring, der zur Angabe des Namens der Nutzlast des Geräts verwendet wird  - `operationalMode`: Ein Textstring, der verwendet wird, um die unterstützten Sensormodi zu deklarieren, falls vorhanden  - `polarizationMode`: Ein Textstring, der zur Deklaration der Polarisationsmodi verwendet wird, falls vorhanden  - `swathID`: Ein Textstring, der zur Angabe der Schwad-ID verwendet wird, falls vorhanden  - `type`: NGSI-LD Entity Type. Er muss gleich EOInstrument sein.    
Erforderliche Eigenschaften  
- `id`  - `instrumentID`  - `instrumentName`  - `operationalMode`  - `type`  ## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
EOInstrument:    
  description: 'This entity contains a harmonised description of a generic EOInstrument made for the Satellite Imagerry domain. This entity is primarily associated with the satellite instruments related to Earth Observation Analysis applications.'    
  properties:    
    carriedOn:    
      description: 'The ID of the satellite platform that the instrument is carried on'    
      format: uri    
      type: Relationship    
    instrumentID:    
      description: 'A mandatory text string used to declare the ID of the instrument payload'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    instrumentName:    
      description: 'A mandatory text string used to declare the name of the instrument payload'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    operationalMode:    
      description: 'A text string used to declare the supported sensor modes if available'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    polarizationMode:    
      description: 'A text string used to declare the polarization modes if available'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    swathID:    
      description: 'A text string used to declare the swath ID if available'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    type:    
      description: 'NGSI-LD Entity Type. It must be equal to EOInstrument.'    
      enum:    
        - EOInstrument    
      type: Property    
  required:    
    - id    
    - type    
    - instrumentID    
    - instrumentName    
    - operationalMode    
  type: object    
```  
</details>    
## Beispiel-Nutzlasten  
#### EOInstrument NGSI-v2 key-values Beispiel  
Hier ist ein Beispiel für ein EOInstrument im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-v2 bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
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
#### EOInstrument NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für ein EOInstrument im JSON-LD-Format wie normalisiert. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden und liefert die Kontextdaten einer einzelnen Entität.  
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
#### EOInstrument NGSI-LD key-values Beispiel  
Hier ist ein Beispiel für ein EOInstrument im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-LD bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "urn:ngsi-ld:EOInstrument:154",  
  "type": "EOInstrument",  
  "instrumentID": "MSI",  
  "instrumentName": "Multi-Spectral Instrument",  
  "swathID": "S2",  
  "carriedOn": "urn:ngsi-ld:EOSatellitePlatform:154",  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
#### EOInstrument NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für ein EOInstrument im JSON-LD-Format wie normalisiert. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden und liefert die Kontextdaten einer einzelnen Entität.  
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
    "value": "SAR-C"  
  },  
  "instrumentName": {  
    "type": "Property",  
    "value": "Synthetic Aperture Radar (C-band)"  
  },  
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
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
