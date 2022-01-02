CREATE TABLE landmarks
(
  id SERIAL,
  city character varying(50),
  country character varying(50),
  description character varying(2000),
  location character varying(50),
  state character varying(70),
  state_abbrev character varying(2),
  latitude double precision,
  longitude double precision,
  city_latitude double precision,
  city_longitude double precision
);
