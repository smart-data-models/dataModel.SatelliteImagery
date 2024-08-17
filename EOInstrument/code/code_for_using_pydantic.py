from __future__ import annotations

from enum import Enum
from typing import List, Optional, Union

from pydantic import AnyUrl, AwareDatetime, BaseModel, Field, constr


class Type(Enum):
    EOInstrument = 'EOInstrument'


class EOInstrument(BaseModel):
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    carriedOn: Optional[AnyUrl] = Field(
        None,
        description='The ID of the satellite platform that the instrument is carried on',
    )
    dataProvider: Optional[str] = Field(
        None,
        description='A sequence of characters identifying the provider of the harmonised data entity',
    )
    dateCreated: Optional[AwareDatetime] = Field(
        None,
        description='Entity creation timestamp. This will usually be allocated by the storage platform',
    )
    dateModified: Optional[AwareDatetime] = Field(
        None,
        description='Timestamp of the last modification of the entity. This will usually be allocated by the storage platform',
    )
    description: Optional[str] = Field(None, description='A description of this item')
    id: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(None, description='Unique identifier of the entity')
    instrumentID: Optional[str] = Field(
        None,
        description='A mandatory text string used to declare the ID of the instrument payload',
    )
    instrumentName: Optional[str] = Field(
        None,
        description='A mandatory text string used to declare the name of the instrument payload',
    )
    name: Optional[str] = Field(None, description='The name of this item')
    operationalMode: Optional[str] = Field(
        None,
        description='A text string used to declare the supported sensor modes if available',
    )
    owner: Optional[
        List[
            Union[
                constr(
                    pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!,:\\\\]+$',
                    min_length=1,
                    max_length=256,
                ),
                AnyUrl,
            ]
        ]
    ] = Field(
        None,
        description='A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)',
    )
    polarizationMode: Optional[str] = Field(
        None,
        description='A text string used to declare the polarization modes if available',
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    swathID: Optional[str] = Field(
        None, description='A text string used to declare the swath ID if available'
    )
    type: Optional[Type] = Field(
        None, description='NGSI-LD Entity Type. It must be equal to EOInstrument'
    )
