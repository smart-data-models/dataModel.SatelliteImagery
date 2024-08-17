from __future__ import annotations

from enum import Enum
from typing import List, Optional, Union

from pydantic import AnyUrl, AwareDatetime, BaseModel, Field, RootModel, constr


class Address(BaseModel):
    addressCountry: Optional[str] = Field(
        None, description='The country. For example, Spain'
    )
    addressLocality: Optional[str] = Field(
        None,
        description='The locality in which the street address is, and which is in the region',
    )
    addressRegion: Optional[str] = Field(
        None,
        description='The region in which the locality is, and which is in the country',
    )
    district: Optional[str] = Field(
        None,
        description='A district is a type of administrative division that, in some countries, is managed by the local government',
    )
    postOfficeBoxNumber: Optional[str] = Field(
        None,
        description='The post office box number for PO box addresses. For example, 03578',
    )
    postalCode: Optional[str] = Field(
        None, description='The postal code. For example, 24004'
    )
    streetAddress: Optional[str] = Field(None, description='The street address')
    streetNr: Optional[str] = Field(
        None, description='Number identifying a specific property on a public street'
    )


class Type(Enum):
    Point = 'Point'


class Location(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[float] = Field(..., min_length=2)
    type: Type


class Coordinate(RootModel[List[float]]):
    root: List[float]


class Type1(Enum):
    LineString = 'LineString'


class Location1(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[Coordinate] = Field(..., min_length=2)
    type: Type1


class Type2(Enum):
    Polygon = 'Polygon'


class Location2(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type2


class Type3(Enum):
    MultiPoint = 'MultiPoint'


class Location3(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[float]]
    type: Type3


class Type4(Enum):
    MultiLineString = 'MultiLineString'


class Location4(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type4


class Type5(Enum):
    MultiPolygon = 'MultiPolygon'


class Location5(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[List[Coordinate]]]
    type: Type5


class OrbitDirection(Enum):
    Ascending = 'Ascending'
    Descending = 'Descending'


class Type6(Enum):
    EOProduct = 'EOProduct'


class EOProduct(BaseModel):
    address: Optional[Address] = Field(None, description='The mailing address')
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    areaServed: Optional[str] = Field(
        None,
        description='The geographic area where a service or offered item is provided',
    )
    cloudCoverage: Optional[float] = Field(
        None,
        description='The cloud coverage percentage. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code',
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
    hostedOn: Optional[AnyUrl] = Field(
        None, description='The ID of the data hub that the product is hosted on'
    )
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
    ingestionDate: Optional[AwareDatetime] = Field(
        None,
        description='The time at which the data was made available in the online archive',
    )
    location: Optional[
        Union[Location, Location1, Location2, Location3, Location4, Location5]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
    )
    name: Optional[str] = Field(None, description='The name of this item')
    observedBy: Optional[AnyUrl] = Field(
        None, description='The ID of the instrument that the product was observed by'
    )
    orbitDirection: Optional[OrbitDirection] = Field(
        None, description='The orbit pass orientation'
    )
    orbitNumber: Optional[float] = Field(
        None,
        description='The orbit number of tha satellite pass. All units are accepted in [CEFACT](https://www.unece.org/cefact.html) code',
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
    processingLevel: Optional[str] = Field(
        None,
        description='A mandatory text string used to declare the processing level of the product',
    )
    productFormat: Optional[str] = Field(
        None,
        description='A mandatory text string used to declare the format of the product',
    )
    productID: Optional[str] = Field(
        None,
        description='A mandatory text string used to declare the unique ID of the product',
    )
    productType: Optional[str] = Field(
        None,
        description='A mandatory text string used to declare the type of the product',
    )
    productURL: Optional[str] = Field(
        None,
        description='A mandatory url used to declare the downlaod link of the product',
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    sensingDate: Optional[AwareDatetime] = Field(
        None, description='The time at which the image was taken by the sensor'
    )
    sensingStartedAt: Optional[AwareDatetime] = Field(
        None,
        description='The time of the satellite on-board acquisition of the first line of the image in the product',
    )
    sensingStoppedAt: Optional[AwareDatetime] = Field(
        None,
        description='The time of the satellite on-board acquisition of the last line of the image in the product',
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    timeliness: Optional[str] = Field(None, description='The timeliness of the product')
    type: Optional[Type6] = Field(
        None, description='NGSI-LD Entity Type. It must be equal to EOProduct'
    )
