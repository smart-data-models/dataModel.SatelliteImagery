/* (Beta) Export of data model EOProduct of the subject dataModel.SatelliteImagery for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE orbitDirection_type AS ENUM ('Ascending','Descending');CREATE TYPE EOProduct_type AS ENUM ('EOProduct');
CREATE TABLE EOProduct (address JSON, alternateName TEXT, areaServed TEXT, cloudCoverage NUMERIC, dataProvider TEXT, dateCreated TIMESTAMP, dateModified TIMESTAMP, description TEXT, hostedOn TEXT, ingestionDate TIMESTAMP, name TEXT, observedBy TEXT, orbitDirection orbitDirection_type, orbitNumber NUMERIC, owner JSON, processingLevel TEXT, productFormat TEXT, productID TEXT, productType TEXT, productURL TEXT, sensingDate TIMESTAMP, sensingStartedAt TIMESTAMP, sensingStoppedAt TIMESTAMP, source TEXT, timeliness TEXT, type EOProduct_type);