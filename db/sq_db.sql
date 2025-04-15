CREATE TABLE IF NOT EXISTS dkp1 (
id integer PRIMARY KEY AUTOINCREMENT,
number text,
contract_date text,
seller_id integer,
buyer_id integer,
created_at text,
updated_at text,
deleted_at text
);
INSERT OR IGNORE INTO dkp1 VALUES
(1, 'dkp1-1/1', '2025-01-01', 2, 1, null, null, null),
(2, 'dkp1-2/1', '2025-02-01', 2, 1, null, null, null);
CREATE TABLE IF NOT EXISTS companies (
id integer PRIMARY KEY AUTOINCREMENT,
short_name text NOT NULL,
inn text,
created_at text,
updated_at text,
deleted_at text
);
INSERT OR IGNORE INTO companies VALUES
(1, 'ABL Factoring', '123435235', null, null, null),
(2, 'Major', '2409234098', null, null, null),
(3, 'Chuang Huang', '02750973250', null, null, null);
CREATE TABLE IF NOT EXISTS cars (
id integer PRIMARY KEY AUTOINCREMENT,
vin text NOT NULL,
mark text,
model text,
color text,
country text,
body_number text,
engine text,
dkp1_id integer,
dkp2_id integer,
price integer,
epts text,
created_at text,
updated_at text,
deleted_at text
);
INSERT OR IGNORE INTO cars VALUES
(1, 'XTK21060050125601', 'VAZ', '2106', 'white', 'Russia', 'E21067483', 'petrol', 1, 1, 35000000, 'X09780' null, null, null),
(2, 'XEV20934723094709', 'Skoda', 'Octavia', 'blue', 'Russia', 'LJKSFN0982', 'petrol, BSF 1.6', 1, 1, 300000000, 'XLKJSF35i345', null, null, null),
(3, 'LVVDB21B5RC054886', 'Chery', 'TIGGO4 PRO', 'white', 'China', '', 'diesel, 1.5 CVT Action', 1, null, 295000000, null, null, null, null),
(3, 'LVVDB21B5RC054887', 'Chery', 'TIGGO4 PRO', 'white', 'China', '', 'diesel, 1.5 CVT Action', 1, null, 295000000, null, null, null, null);
CREATE TABLE IF NOT EXISTS dkp2 (
id integer PRIMARY KEY AUTOINCREMENT,
number text,
contract_date text,
seller_id integer,
buyer_id integer,
created_at text,
updated_at text,
deleted_at text
);
INSERT OR IGNORE INTO dkp2 VALUES
(1, 'dkp2-1/1', '2025-02-01', 2, 1, null, null, null),
(2, 'dkp2-2/1', '2025-02-01', 2, 1, null, null, null);
CREATE TABLE IF NOT EXISTS documents (
id integer PRIMARY KEY AUTOINCREMENT,
doc_type integer,
doc_name text,
filetype text,
path text,
created_at text,
updated_at text,
deleted_at text,
downloaded_at text
)
