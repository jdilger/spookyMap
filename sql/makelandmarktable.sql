DROP TABLE landmarks;
CREATE TABLE landmarks
(
  city VARCHAR(200),
  country VARCHAR(200),
  description VARCHAR(10000),
  location VARCHAR(5000),
  state VARCHAR(70),
  state_abbrev VARCHAR(2),
  latitude double precision,
  longitude double precision,
  city_latitude double precision,
  city_longitude double precision
);

