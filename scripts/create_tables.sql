BEGIN;
CREATE TABLE "home_cliente" (
    "id" integer NOT NULL PRIMARY KEY,
    "nome" varchar(100) NOT NULL UNIQUE,
    "sexo" varchar(1) NOT NULL,
    "dt_nascimento" date NOT NULL,
    "rg" varchar(50) NOT NULL UNIQUE,
    "cpf" varchar(11) NOT NULL UNIQUE,
    "cep" varchar(8) NOT NULL,
    "end" varchar(100) NOT NULL,
    "end_comp" varchar(100),
    "bairro" varchar(100) NOT NULL,
    "cidade" varchar(100) NOT NULL,
    "uf" varchar(2) NOT NULL,
    "tel_fixo" varchar(10),
    "tel_cel" varchar(10) NOT NULL,
    "tel_trab" varchar(10),
    "email" varchar(100),
    "multa" decimal NOT NULL,
    "tem_locacao" bool NOT NULL
)
;
CREATE TABLE "home_fantasia" (
    "id" integer NOT NULL PRIMARY KEY,
    "nome" varchar(50) NOT NULL,
    "tipo" varchar(2) NOT NULL,
    "tema" varchar(50) NOT NULL,
    "valor_fantasia" decimal NOT NULL,
    "valor_locacao" decimal NOT NULL,
    "qtde_total" integer NOT NULL,
    "qtde_disponivel" integer NOT NULL
)
;
CREATE TABLE "home_locacao_fantasias" (
    "id" integer NOT NULL PRIMARY KEY,
    "locacao_id" integer NOT NULL,
    "fantasia_id" integer NOT NULL REFERENCES "home_fantasia" ("id"),
    UNIQUE ("locacao_id", "fantasia_id")
)
;
CREATE TABLE "home_locacao" (
    "id" integer NOT NULL PRIMARY KEY,
    "dt_locacao" date NOT NULL,
    "dt_devolucao" date NOT NULL,
    "pg_realizado" decimal NOT NULL,
    "status" bool NOT NULL,
    "cliente_id" integer NOT NULL REFERENCES "home_cliente" ("id")
)
;
CREATE INDEX "home_locacao_52f540a3" ON "home_locacao" ("cliente_id");
COMMIT;
