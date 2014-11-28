BEGIN;
CREATE TABLE `home_cliente` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `nome` varchar(100) NOT NULL UNIQUE,
    `dt_nascimento` date NOT NULL,
    `rg` varchar(50) NOT NULL UNIQUE,
    `cpf` varchar(14) NOT NULL UNIQUE,
    `cep` varchar(9) NOT NULL,
    `end` varchar(100) NOT NULL,
    `end_comp` varchar(100),
    `bairro` varchar(100) NOT NULL,
    `cidade` varchar(100) NOT NULL,
    `uf` varchar(2) NOT NULL,
    `tel_fixo` varchar(14),
    `tel_cel` varchar(14) NOT NULL,
    `tel_trab` varchar(14),
    `email` varchar(100),
    `multa` numeric(8, 2) NOT NULL
)
;
CREATE TABLE `home_fantasia` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `nome` varchar(50) NOT NULL,
    `tipo` varchar(50) NOT NULL,
    `tema` varchar(50) NOT NULL,
    `valor_fantasia` double precision NOT NULL,
    `valor_locacao` double precision NOT NULL,
    `qtde_total` integer NOT NULL,
    `qtde_disponivel` integer NOT NULL
)
;
CREATE TABLE `home_locacao_fantasias` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `locacao_id` integer NOT NULL,
    `fantasia_id` integer NOT NULL,
    UNIQUE (`locacao_id`, `fantasia_id`)
)
;
ALTER TABLE `home_locacao_fantasias` ADD CONSTRAINT `fantasia_id_refs_id_ad0f67ae` FOREIGN KEY (`fantasia_id`) REFERENCES `home_fantasia` (`id`);
CREATE TABLE `home_locacao` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `dt_locacao` date NOT NULL,
    `dt_devolucao` date NOT NULL,
    `pg_realizado` numeric(8, 2) NOT NULL,
    `status` bool NOT NULL,
    `cliente_id` integer NOT NULL
)
;
ALTER TABLE `home_locacao` ADD CONSTRAINT `cliente_id_refs_id_bf3cecc5` FOREIGN KEY (`cliente_id`) REFERENCES `home_cliente` (`id`);
ALTER TABLE `home_locacao_fantasias` ADD CONSTRAINT `locacao_id_refs_id_3bc86a96` FOREIGN KEY (`locacao_id`) REFERENCES `home_locacao` (`id`);
CREATE INDEX `home_locacao_52f540a3` ON `home_locacao` (`cliente_id`);
COMMIT;
