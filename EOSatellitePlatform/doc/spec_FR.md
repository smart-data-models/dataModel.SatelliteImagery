Entité : EOSatellitePlatform  
============================  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.SatelliteImagery/blob/master/EOSatellitePlatform/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Description globale : **Cette entité contient une description harmonisée d'une plateforme générique EOSatellitePlatform faite pour le domaine de l'imagerie satellitaire. Cette entité est principalement associée aux plateformes satellitaires liées aux applications d'analyse de l'observation de la Terre**.  

## Liste des propriétés  

- `alternateName`: Un nom alternatif pour cet élément  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `description`: Une description de cet article  - `id`: Identifiant unique de l'entité  - `name`: Le nom de cet élément.  - `owner`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  - `platformID`: Une chaîne de texte obligatoire utilisée pour déclarer l'ID unique de la plate-forme.  - `platformNSSDCA`: Une chaîne de texte obligatoire utilisée pour déclarer l'identifiant unique de la mission dans les archives du National Space Science Data Center.  - `platformName`: Une chaîne de texte obligatoire utilisée pour déclarer le nom de la plate-forme.  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur l'élément  - `source`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.  - `type`: Type d'entité NGSI-LD. Il doit être égal à EOSatellitePlatform.    
Propriétés requises  
- `id`  - `type`  ## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
EOSatellitePlatform:    
  description: 'This entity contains a harmonised description of a generic EOSatellitePlatform made for the Satellite Imagerry domain. This entity is primarily associated with the Satellite platforms related to Earth Observation Analysis applications.'    
  properties:    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
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
      type: Property    
    name:    
      description: 'The name of this item.'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *eosatelliteplatform_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
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
      description: 'NGSI-LD Entity Type. It must be equal to EOSatellitePlatform.'    
      enum:    
        - EOSatellitePlatform    
      type: Property    
  required:    
    - id    
    - type    
  type: object    
```  
</details>    
## Exemples de charges utiles  
#### EOSatellitePlatform Valeurs-clés NGSI-v2 Exemple  
Voici un exemple d'une EOSatellitePlatform au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:EOSatellitePlatform:154",  
  "type": "EOSatellitePlatform",  
  "platformID": "B",  
  "platformName": "Sentinel-1",  
  "platformNSSDCA": "2016-025A"  
}  
```  
#### EOSatellitePlatform NGSI-v2 normalisée Exemple  
Voici un exemple d'une EOSatellitePlatform au format JSON-LD tel que normalisé. Ce format est compatible avec la NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
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
#### EOSatellitePlatform Valeurs-clés NGSI-LD Exemple  
Voici un exemple d'une EOSatellitePlatform au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-LD lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:EOSatellitePlatform:154",  
  "type": "EOSatellitePlatform",  
  "platformID": "A",  
  "platformName": "Sentinel-2",  
  "platformNSSDCA": "2015-028A",  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
#### EOSatellitePlatform NGSI-LD normalisé Exemple  
Voici un exemple d'une EOSatellitePlatform au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
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
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
