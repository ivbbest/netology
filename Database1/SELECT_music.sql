-- Извлечение информации из таблиц по требованиям домашнего задания

--название и год выхода альбомов, вышедших в 2018 году;

select name_album, year 
from album 
where year = 2018;

-- название и продолжительность самого длительного трека;

select name_song, duration
from song
order by duration desc
limit 1;

-- название треков, продолжительность которых не менее 3,5 минуты;

select name_song, duration
from song
where duration > 3.5;

-- названия сборников, вышедших в период с 2018 по 2020 год включительно;

select name
from digest
where year between 2018 and 2020;

-- исполнители, чье имя состоит из 1 слова;

select * 
from musician
where name not like '% %';

-- название треков, которые содержат слово "мой"/"my".

select name_song 
from song
where name_song like '%my%';