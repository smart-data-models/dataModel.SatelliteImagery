Entité : EOSatellitePlatform  
============================  
[Licence ouverte](https://github.com/smart-data-models//dataModel.SatelliteImagery/blob/master/EOSatellitePlatform/LICENSE.md)  
Description globale : **Cette entité contient une description harmonisée d'une EOSatellitePlatform générique faite pour le domaine de l'imagerie satellitaire. Cette entité est principalement associée aux plates-formes satellitaires liées aux applications d'analyse de l'observation de la Terre.**  

## Liste des biens  

- `platformID`: Une chaîne de texte obligatoire utilisée pour déclarer l'identifiant unique de la plate-forme  - `platformNSSDCA`: Une chaîne de texte obligatoire utilisée pour déclarer l'identifiant unique de la mission dans les archives du National Space Science Data Center  - `platformName`: Une chaîne de texte obligatoire utilisée pour déclarer le nom de la plate-forme  - `type`: Type d'entité NGSI-LD. Il doit être égal à EOSatellitePlatform.    
Propriétés requises  
- `id`  - `platformID`  - `platformNSSDCA`  - `platformName`  - `type`  ## Modèle de données description des biens  
Classement par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
EOSatellitePlatform:    
  description: 'This entity contains a harmonised description of a generic EOSatellitePlatform made for the Satellite Imagerry domain. This entity is primarily associated with the Satellite platforms related to Earth Observation Analysis applications.'    
  properties:    
    platformID:    
      description: 'A mandatory text string used to declare the unique ID of the platform'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    platformNSSDCA:    
      description: 'A mandatory text string used to declare the unique mission id in the National Space Science Data Center Archive'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    platformName:    
      description: 'A mandatory text string used to declare the name of the platform'    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    type:    
      description: 'NGSI-LD Entity Type. It must be equal to EOSatellitePlatform.'    
      enum:    
        - EOSatellitePlatform    
      type: Property    
  required:    
    - id    
    - type    
    - platformID    
    - platformName    
    - platformNSSDCA    
  type: object    
```  
</details>    
## Exemples de charges utiles  
#### EOSatellitePlatform NGSI V2 Exemple de valeurs clés  
Voici un exemple d'une EOSatellitePlatform au format JSON comme valeurs clés. Elle est compatible avec NGSI V2 lorsqu'elle utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:EOSatellitePlatform:154",  
  "type": "EOSatellitePlatform",  
  "platformID": "B",  
  "platformName": "Sentinel-1",  
  "platformNSSDCA": "2016-025A"  
}  
```  
Non disponible l'exemple d'une EOSatellitePlatform en format JSON comme normalisé. Il est compatible avec NGSI V2 lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
Non disponible l'exemple d'une EOSatellitePlatform en format JSON-LD comme valeurs clés. Il est compatible avec le format NGSI-LD lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
#### EOSatellitePlatform NGSI-LD normalisée Exemple  
Voici un exemple d'une EOSatellitePlatform au format JSON-LD tel que normalisé. Ce format est compatible avec JSON-LD lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
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
  "platformName": {  
    "type": "Property",  
    "value": "Sentinel-1"  
  },  
  "platformNSSDCA": {  
    "type": "Property",  
    "value": "2016-025A"  
  },  
  "@context": [  
    "https://schema.lab.fiware.org/ld/context"  
  ]  
}  
```  
