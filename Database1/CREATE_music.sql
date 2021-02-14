create table if not exists Musician(
	id serial primary key,
	name varchar(80) not null unique
);

create table if not exists Album(
	id serial primary key,
	name_album varchar(80) not null unique,
	year integer not null,
	id_musician integer not null
);

create table if not exists Song(
	id serial primary key,
	name_song varchar(80) not null unique,
	duration numeric(3,2) not null,
	id_album integer not null REFERENCES album(id)
);

create table if not exists MusicianAlbum(
	musician_id integer REFERENCES Musician(id),
	album_id integer REFERENCES Album (id),
	constraint pk1 primary key (musician_id, album_id)
);

create table if not exists Digest(
	id serial primary key,
	name varchar(80) not null unique,
	year integer not null
);

create table if not exists DigestSong(
	song_id integer REFERENCES Song(id),
	digest_id integer REFERENCES Digest(id),
	constraint pk2 primary key (song_id, digest_id)
);

-- новые две базы

create table if not exists Genres(
	id serial primary key,
	name varchar(80) not null unique
);

create table if not exists genres_musicians(
	genre_id integer REFERENCES Genres(id),
	musician_id integer REFERENCES Musician(id),
	constraint pk3 primary key (genre_id, musician_id)
);