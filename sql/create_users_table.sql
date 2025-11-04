CREATE TABLE public.users (
    user_id           uuid PRIMARY KEY,
    first_name        text,
    last_name         text,
    name              text,
    username          text,
    email             text,
    email_verified    boolean,
    phone_number      text,
    phone_verified    boolean,
    address_line1     text,
    address_line2     text,
    city              text,
    state             text,
    postal_code       text,
    country           text,
    date_of_birth     text, -- Data como TEXTO
    gender            text,
    preferred_language text,
    timezone          text,
    bio               text,
    signup_date       text, -- Data/Hora como TEXTO
    last_login        text, -- Data/Hora como TEXTO
    status            text,
    roles             text,
    two_factor_enabled boolean,
    subscription_tier text,
    subscription_renewal_date text, -- Data como TEXTO
    total_orders      bigint,
    total_spend       double precision,
    last_order_date   text, -- Data/Hora como TEXTO
    average_rating    double precision,
    marketing_opt_in  boolean,
    referral_source   text,
    referral_code     text,
    device_type       text,
    app_version       text,
    ip_address        text,
    lat               double precision,
    lon               double precision,
    payment_methods_count bigint,
    has_active_payment_method boolean,
    created_at        text, -- Data/Hora como TEXTO
    updated_at        text  -- Data/Hora como TEXTO
);