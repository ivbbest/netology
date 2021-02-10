-- количество исполнителей в каждом жанре;

select g.name, count(m.name)
from musician m
join genres_musicians gm
on m.id = gm.musician_id
join genres g
on gm.genre_id = g.id
group by g.name;

-- количество треков, вошедших в альбомы 2019-2020 годов;

select count(name_song)
from song s
join album a
on s.id_album = a.id
where year between 2019 and 2020;

-- средняя продолжительность треков по каждому альбому;

select name_album, avg(duration) 
from song s
join album a
on s.id_album = a.id
group by a.name_album;

-- все исполнители, которые не выпустили альбомы в 2020 году;

select name from musician m
join album a
on m.id = a.id_musician
where a.year != 2020;

-- названия сборников, в которых присутствует конкретный исполнитель (выберите сами);

select distinct d.name 
from digest d
join digestsong ds
on d.id = ds.digest_id
join song s
on s.id = ds.song_id
join album a
on a.id = s.id_album
join musicianalbum ma
on ma.album_id = a.id
join musician m
on m.id = ma.musician_id
where m.name like '%Ledi%';

-- название альбомов, в которых присутствуют исполнители более 1 жанра;

select a.name_album
from album a
join musicianalbum ma
on ma.album_id = a.id
join musician m
on m.id = ma.musician_id
join genres_musicians gm
on m.id = gm.musician_id
join genres g
on gm.genre_id = g.id
group by a.name_album
having count(distinct g.name) > 1;

-- наименование треков, которые не входят в сборники;
-- !!!у меня здесь не получилось вывести данных, так как заполнял автоматически промежуточную таблицу через cross join

select s.name_song
from song s
join digestsong ds
on s.id = ds.song_id
where song_id is null;

-- исполнителя(-ей), написавшего самый короткий по продолжительности трек (теоретически таких треков может быть несколько);

select name, duration from song s
join album a
on s.id_album = a.id
join musician m
on m.id = a.id_musician
group by m.name, s.duration 
having duration = 
(
	select min(duration)
	from song
);

-- название альбомов, содержащих наименьшее количество треков.

select distinct a.name_album
from album as a
left join song as t on t.id_album = a.id
where t.id_album in (
    select id_album
    from song
    group by id_album
    having count(id) = (
        select count(id)
        from song
        group by id_album
        order by count
        limit 1
    )
)
order by name_album