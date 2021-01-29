/* Oferta */
CREATE TABLE public.oferta
(
    id_oferta serial,
    id_webscraping integer,
    titulo character varying(200) COLLATE pg_catalog."default",
    empresa character varying(200) COLLATE pg_catalog."default",
    lugar character varying(100) COLLATE pg_catalog."default",
    tiempo_publicado character varying(100) COLLATE pg_catalog."default",
    salario character varying(100) COLLATE pg_catalog."default",
    modalidad_trabajo character varying(100) COLLATE pg_catalog."default",
    subarea character varying(100) COLLATE pg_catalog."default",
    url_oferta character varying(500) COLLATE pg_catalog."default",
    url_pagina character varying(500) COLLATE pg_catalog."default",
    area character varying(100) COLLATE pg_catalog."default",
    fecha_creacion date,
    fecha_modificacion date,
    oferta_detalle character varying(8000) COLLATE pg_catalog."default",
    fecha_publicacion date,
    time_publicacion character varying(60) COLLATE pg_catalog."default",
    id_anuncioempleo character varying(100) COLLATE pg_catalog."default",
    id_estado character(1) COLLATE pg_catalog."default",
    CONSTRAINT oferta_pkey PRIMARY KEY (id_oferta)
);


/* OfertaDetalle create */
CREATE TABLE public.oferta_detalle
(
    id_ofertadetalle serial,
    id_oferta integer NOT NULL,
    descripcion character varying(2000) COLLATE pg_catalog."default",
    descripcion_normalizada character varying(2000) COLLATE pg_catalog."default",
    ind_activo smallint,
    motivo_inactivo smallint,
    fecha_creacion date,
    fecha_modificacion date,
    ofertaperfil_id integer,
    CONSTRAINT oferta_detalle_pkey PRIMARY KEY (id_ofertadetalle)
);

/* Keywords */
CREATE TABLE public.keyword_search
(
    id_keyword serial,
    descripcion character varying(50) COLLATE pg_catalog."default",
    id_tipokeyword integer,
    CONSTRAINT keyword_search_pkey PRIMARY KEY (id_keyword)
);

/* insertamos */
INSERT INTO public.keyword_search( descripcion, id_tipokeyword)
VALUES 
    ('ANALISTA PROGRAMADOR', 1),
    ('ANALISTA DESARROLLO', 1),
    ('ANALISTA DE SISTEMAS', 1),
    ('ANALISTA FUNCIONAL', 1),
    ('ANALISTA BPM', 1),
    ('ANALISTA BI', 1),
    ('ANALISTA CALIDAD TI', 1),
    ('ANALISTA DE PROCESOS', 1),
    ('ANALISTA TI', 1);

/* webscraping */
CREATE TABLE public.webscraping
(
    id_webscraping serial,
    busqueda character varying(100) COLLATE pg_catalog."default",
    busqueda_area character varying(100) COLLATE pg_catalog."default",
    pagina_web character varying(50) COLLATE pg_catalog."default",
    url_pagina character varying(500) COLLATE pg_catalog."default",
    url_busqueda character varying(500) COLLATE pg_catalog."default",
    fecha_creacion date,
    fecha_modificacion date,
    id_keyword integer NOT NULL,
    delati_team character varying(60) COLLATE pg_catalog."default",
    CONSTRAINT webscraping_pkey PRIMARY KEY (id_webscraping)
);