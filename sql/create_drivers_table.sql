CREATE TABLE public.drivers (
    driver_id           uuid PRIMARY KEY,
    name                text,
    email               text,
    phone_number        text,
    vehicle_type        text,
    license_plate       text,
    registration_date   text, -- ShadowTraffic envia string
    total_deliveries    bigint,
    total_earnings      double precision,
    average_rating      double precision,
    last_login          text, -- ShadowTraffic envia string
    status              text
);