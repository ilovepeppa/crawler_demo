create table maoyan (
  `id` bigint(20) not null auto_increment,
  `rank` varchar(255) not null,
  `image` varchar(255) not null,
  `title` varchar(255) not null,
  `author` varchar(255) not null,
  `time` varchar(255) not null ,
  `score` varchar(255) not null,
  primary key (id)
) ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

create table taobao (
  `id` bigint(20) not null auto_increment,
  `title` varchar(255) not null,
  `image` varchar(255) not null,
  `price` varchar(255) not null ,
  `shop` varchar(255) not null,
  `deal` varchar(255) not null,
  `location` varchar(255) not null,
  primary key (id)
) ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;