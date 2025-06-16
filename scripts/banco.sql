CREATE TABLE `animais` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `nome` varchar(255),
  `idade` integer,
  `peso` float,
  `exames` text,
  `proprietario_id` integer
);

CREATE TABLE `proprietarios` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `nome` varchar(255),
  `endereco` text,
  `telefone` varchar(255)
);

CREATE TABLE `agendamentos` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `animal_id` integer,
  `data_agendamento` timestamp,
  `status` varchar(255)
);

ALTER TABLE `animais` ADD FOREIGN KEY (`proprietario_id`) REFERENCES `proprietarios` (`id`);

ALTER TABLE `agendamentos` ADD FOREIGN KEY (`animal_id`) REFERENCES `animais` (`id`);
