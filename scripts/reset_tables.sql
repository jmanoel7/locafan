BEGIN;
DROP TABLE `home_fantasias`;
DROP TABLE `home_locacoes`;
DROP TABLE `home_clientes`;
CREATE TABLE `home_clientes` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `nome` varchar(100) NOT NULL UNIQUE,
    `dt_nascimento` date NOT NULL,
    `rg` varchar(50) NOT NULL UNIQUE,
    `cpf` varchar(11) NOT NULL UNIQUE,
    `cep` varchar(8) NOT NULL,
    `end` varchar(100) NOT NULL,
    `end_comp` varchar(100),
    `bairro` varchar(100) NOT NULL,
    `cidade` varchar(100) NOT NULL,
    `uf` varchar(2) NOT NULL,
    `tel_fixo` varchar(10),
    `tel_cel` varchar(10) NOT NULL,
    `tel_trab` varchar(10),
    `email` varchar(100),
    `multa` numeric(6, 2) NOT NULL
)
;
CREATE TABLE `home_locacoes` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `dt_locacao` date NOT NULL,
    `dt_devolucao` date NOT NULL,
    `pg_realizado` double precision NOT NULL,
    `status` bool NOT NULL,
    `cliente_id_id` integer NOT NULL UNIQUE
)
;
ALTER TABLE `home_locacoes` ADD CONSTRAINT `cliente_id_id_refs_id_b2e7855` FOREIGN KEY (`cliente_id_id`) REFERENCES `home_clientes` (`id`);
CREATE TABLE `home_fantasias` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `nome` varchar(50) NOT NULL,
    `tipo` varchar(50) NOT NULL,
    `tema` varchar(50) NOT NULL,
    `valor_fantasia` double precision NOT NULL,
    `valor_locacao` double precision NOT NULL,
    `qtde_total` integer NOT NULL,
    `qtde_disponivel` integer NOT NULL,
    `locacao_id_id` integer NOT NULL UNIQUE,
    `locacao_cliente_id_id` integer NOT NULL UNIQUE
)
;
ALTER TABLE `home_fantasias` ADD CONSTRAINT `locacao_id_id_refs_id_60d02d39` FOREIGN KEY (`locacao_id_id`) REFERENCES `home_locacoes` (`id`);
ALTER TABLE `home_fantasias` ADD CONSTRAINT `locacao_cliente_id_id_refs_cliente_id_id_60d02d39` FOREIGN KEY (`locacao_cliente_id_id`) REFERENCES `home_locacoes` (`cliente_id_id`);
COMMIT;