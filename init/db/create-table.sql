create table tkrprices(tkr varchar, csvd text, csvh text, csvs text);

create table features(tkr varchar, csv text);

create table unsplit_prices(tkr varchar, csvd text, csvh text, csvs text);

create table  IF NOT EXISTS
    predictions(
    tkr          VARCHAR
    ,yrs         INTEGER
    ,mnth        VARCHAR
    ,features    VARCHAR
    ,algo        VARCHAR
    ,algo_params VARCHAR
    ,csv         TEXT
    ,kmodel_h5   BYTEA
);