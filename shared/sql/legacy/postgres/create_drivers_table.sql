CREATE TABLE public.drivers (
    driver_id           int PRIMARY KEY,
    name                text,
    email               text,
    phone_number        text,
    vehicle_type        text,
    vehicle_make        text,
    vehicle_model       text,
    vehicle_year        int,
    license_plate       text,
    license_number      text,
    city                text,
    registration_date   text, -- ShadowTraffic envia string
    total_deliveries    bigint,
    total_earnings      double precision,
    average_rating      double precision,
    last_login          text, -- ShadowTraffic envia string
    status              text
);