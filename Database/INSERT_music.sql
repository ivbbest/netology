-- Это ввод данных в таблицы

INSERT INTO musician (name) VALUES ('Elvis Presli');
INSERT INTO musician (name) VALUES ('Jay-Z');
INSERT INTO musician (name) VALUES ('Eminem');
INSERT INTO musician (name) VALUES ('Pol Makkartni');
INSERT INTO musician (name) VALUES ('Ledi Gaga');
INSERT INTO musician (name) VALUES ('Madonna');
INSERT INTO musician (name) VALUES ('Keti Perri');
INSERT INTO musician (name) VALUES ('Alsu');
INSERT INTO musician (name) VALUES ('Drake');
INSERT INTO musician (name) VALUES ('Tatu');
INSERT INTO musician (name) VALUES ('Bruno Mars');

INSERT INTO album (name_album, year, id_musician) VALUES ('Hop', 2019, 1);
INSERT INTO album (name_album, year, id_musician) VALUES ('Hop-hop', 2019, 2);
INSERT INTO album (name_album, year, id_musician) VALUES ('Hop-lei', 2018, 3);
INSERT INTO album (name_album, year, id_musician) VALUES ('Ha-ha', 2017, 2);
INSERT INTO album (name_album, year, id_musician) VALUES ('Anna', 2016, 5);
INSERT INTO album (name_album, year, id_musician) VALUES ('Babah', 2018, 6);
INSERT INTO album (name_album, year, id_musician) VALUES ('Lalala', 2011, 7);
INSERT INTO album (name_album, year, id_musician) VALUES ('Mamamia', 2020, 4);
INSERT INTO album (name_album, year, id_musician) VALUES ('Sansari', 2017, 1);
INSERT INTO album (name_album, year, id_musician) VALUES ('Hangrena', 2018, 6);
INSERT INTO album (name_album, year, id_musician) VALUES ('Samara', 2017, 8);
INSERT INTO album (name_album, year, id_musician) VALUES ('Moskow', 2019, 1);
INSERT INTO album (name_album, year, id_musician) VALUES ('Vorona', 2018, 9);
INSERT INTO album (name_album, year, id_musician) VALUES ('Voronezh', 2018, 10);
INSERT INTO album (name_album, year, id_musician) VALUES ('Piter-Piter', 2017, 11);
INSERT INTO album (name_album, year, id_musician) VALUES ('Piter FM', 2016, 2);
INSERT INTO album (name_album, year, id_musician) VALUES ('Kakanata', 2017, 3);


INSERT INTO song (duration, name_song, id_album) VALUES (3.21, 'BBC', 1);
INSERT INTO song (duration, name_song, id_album) VALUES (4.21, 'USA', 2);
INSERT INTO song (duration, name_song, id_album) VALUES (2.23, 'Money-money', 3);
INSERT INTO song (duration, name_song, id_album) VALUES (1.25, 'Valera', 2);
INSERT INTO song (duration, name_song, id_album) VALUES (3.33, 'Lets go', 5);
INSERT INTO song (duration, name_song, id_album) VALUES (2.22, 'I want to', 6);
INSERT INTO song (duration, name_song, id_album) VALUES (1.11, 'I love', 7);
INSERT INTO song (duration, name_song, id_album) VALUES (1.13, 'I not love you', 4);
INSERT INTO song (duration, name_song, id_album) VALUES (5.55, 'Baby', 1);
INSERT INTO song (duration, name_song, id_album) VALUES (4.44, 'Boy', 6);
INSERT INTO song (duration, name_song, id_album) VALUES (6.56, 'Man', 8);
INSERT INTO song (duration, name_song, id_album) VALUES (1.44, 'Women', 1);
INSERT INTO song (duration, name_song, id_album) VALUES (2.33, 'Know', 9);
INSERT INTO song (duration, name_song, id_album) VALUES (2.55, 'Now', 10);
INSERT INTO song (duration, name_song, id_album) VALUES (3.31, 'I love you', 11);
INSERT INTO song (duration, name_song, id_album) VALUES (2.32, 'Father', 15);
INSERT INTO song (duration, name_song, id_album) VALUES (1.54, 'Mother', 15);
INSERT INTO song (duration, name_song, id_album) VALUES (1.34, 'Women you', 13);
INSERT INTO song (duration, name_song, id_album) VALUES (2.23, 'Know you', 16);
INSERT INTO song (duration, name_song, id_album) VALUES (2.55, 'Now 13', 17);
INSERT INTO song (duration, name_song, id_album) VALUES (3.11, 'I love baby', 12);
INSERT INTO song (duration, name_song, id_album) VALUES (2.02, 'Father you', 10);
INSERT INTO song (duration, name_song, id_album) VALUES (1.04, 'Mother 6', 11);
INSERT INTO song (duration, name_song, id_album) VALUES (0.24, 'My year', 12);
INSERT INTO song (duration, name_song, id_album) VALUES (3.04, 'I and my day', 15);

INSERT INTO digest (name, year) VALUES ('Any music dance', 2015);
INSERT INTO digest (name, year) VALUES ('Dance-dance', 2016);
INSERT INTO digest (name, year) VALUES ('Netology 2021', 2015);
INSERT INTO digest (name, year) VALUES ('Dance to dance', 2016);
INSERT INTO digest (name, year) VALUES ('My love', 2013);
INSERT INTO digest (name, year) VALUES ('One to one', 2018);
INSERT INTO digest (name, year) VALUES ('Its five', 2020);
INSERT INTO digest (name, year) VALUES ('My netology', 2020);
INSERT INTO digest (name, year) VALUES ('Allo', 2017);
INSERT INTO digest (name, year) VALUES ('My my my', 2019);
INSERT INTO digest (name, year) VALUES ('Any love', 2019);
INSERT INTO digest (name, year) VALUES ('Netology', 2019);
INSERT INTO digest (name, year) VALUES ('Music dance', 2016);
INSERT INTO digest (name, year) VALUES ('Dance', 2018);

-- заполнение информацией таблицы Genres

INSERT INTO Genres (name) VALUES ('pop');
INSERT INTO Genres (name) VALUES ('folk');
INSERT INTO Genres (name) VALUES ('dubstep');
INSERT INTO Genres (name) VALUES ('rock');
INSERT INTO Genres (name) VALUES ('metal');


-- заполнение информацией таблицы genres_musicians

insert into genres_musicians (genre_id, musician_id)
    select genres.id, musician.id
    from genres cross join
         musician
    order by genres.id, musician.id;
	
	
-- заполнение информацией таблицы DigestSong

insert into digestsong (song_id, digest_id)
    select song.id, digest.id
    from song cross join
         digest
    order by song.id, digest.id;
	
-- заполнение информацией таблицы MusicianAlbum

insert into musicianalbum (musician_id, album_id)
    select musician.id, album.id
    from musician cross join
         album
    order by musician.id, album.id;