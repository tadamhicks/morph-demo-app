create database demo_app;

use demo_app;

GRANT ALL PRIVILEGES
ON demo_app.*
TO 'admin'@'%'
IDENTIFIED BY 'password';

create table word (
	wordage varchar(128),
	phone_spell varchar(128),
	primary key (wordage)
);

create index idx_word
	on word(wordage);

create table location (
	wordage varchar(128),
	ip_address varchar(128),
	latitude float(8,4),
	longitude float(8,4),
	primary key (wordage, ip_address)
	);

create index idx_word_loc
	on location(wordage);