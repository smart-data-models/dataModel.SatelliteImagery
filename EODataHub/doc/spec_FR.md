Entité : EODataHub  
==================  
[Licence ouverte](https://github.com/smart-data-models//dataModel.SatelliteImagery/blob/master/EODataHub/LICENSE.md)  
Description globale : **Cette entité contient une description harmonisée d'un instrument d'observation de la Terre générique conçu pour le domaine de l'imagerie par satellite. Cette entité est principalement associée au centre de données lié aux applications d'analyse de l'observation de la Terre.**  

## Liste des biens  

- `dataHubName`: Une chaîne de texte obligatoire utilisée pour déclarer le nom du centre de données utilisé  - `dataHubURL`: Une chaîne de texte obligatoire utilisée pour déclarer l'url du hub de données utilisé  - `type`: Type d'entité NGSI-LD. Il doit être égal à EODataHub.    
Propriétés requises  
- `dataHubName`  - `dataHubURL`  - `id`  - `type`  ## Modèle de données description des biens  
Classement par ordre alphabétique (cliquez pour plus de détails)  
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
## Exemples de charges utiles  
#### Exemple de valeurs clés EODataHub NGSI V2  
Voici un exemple d'EODataHub au format JSON comme valeurs clés. Il est compatible avec NGSI V2 lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
```json  
{  
  "id": "EODataHub:123",  
  "type": "EODataHub",  
  "dataHubName": "ESA Copernicus Open Access Hub",  
  "dataHubURL": "http://scihub.copernicus.eu"  
}  
```  
Non disponible l'exemple d'un EODataHub en format JSON comme normalisé. Il est compatible avec NGSI V2 lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
Non disponible l'exemple d'un EODataHub en format JSON-LD comme valeurs clés. Il est compatible avec le format NGSI-LD lorsqu'il utilise "options=keyValues" et renvoie les données de contexte d'une entité individuelle.  
#### EODataHub NGSI-LD normalisé Exemple  
Voici un exemple d'EODataHub au format JSON-LD tel que normalisé. Il est compatible avec le format NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données de contexte d'une entité individuelle.  
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
        "https://schema.lab.fiware.org/ld/context"  
    ]  
}  
```  
