CREATE TABLE public.skin_dataset (
    id integer,
    embeddings public.vector(384),
    image_id text,
    dx text,
    dx_type text,
    age double precision,
    sex text,
    localization text,
    image bytea
) DISTRIBUTED RANDOMLY;

COPY skin_dataset FROM '/home/gpadmin/skin_dataset.csv' CSV header delimiter '|' quote '"' NULL '';
