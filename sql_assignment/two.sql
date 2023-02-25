-- These statements use PostgreSQL syntax, but you may assume any other database or storage with an
-- SQL querying capabilities (any relational database, Hive, etc.). You may need to adjust these statements
-- if you chose to use another database.

-- If you chose to use PostgreSQL, this code can be sourced directly to SQL REPL, provided that it is
-- executed in a new clean temporary database.

create table room (
  id serial primary key,
  name varchar unique
);

create table sensor (
  id serial primary key,
  serial_number varchar unique,
  room_id int references room(id) -- zero, one or multiple sensors may be installed in any room (many to one)
);

-- Entries in this table represent a number of people
-- detected by a sensor **since the previous detection**,
-- and their direction. In other words, a set of records in
-- this table represents a people flow.
create table people_count (
  sensor_id int references sensor(id),
  ts timestamp,
  in_count int,
  out_count int
);

insert into room (name) values
  ('Office room'),
  ('Meeting room');

insert into sensor (serial_number, room_id) values
  ('a1', (select id from room where name = 'Office room')),
  ('b1', (select id from room where name = 'Meeting room')),
  ('b2', (select id from room where name = 'Meeting room'));

insert into people_count (sensor_id, ts, in_count, out_count) values
  ((select id from sensor where serial_number = 'a1'), '2021-05-01T10:00:00', 10, 2),
  ((select id from sensor where serial_number = 'b1'), '2021-04-30T16:00:00', 5, 35),
  ((select id from sensor where serial_number = 'b1'), '2021-05-01T10:00:00', 10, 5),
  ((select id from sensor where serial_number = 'b2'), '2021-05-01T12:00:00', 20, 10),
  ((select id from sensor where serial_number = 'b1'), '2021-05-01T16:00:00', 5, 20);

-- first question

-- select the count of people present in the "Meeting room" by 14:00 (UTC) on May 1, 2021:
-- expected result: 15

-- SECOND  question

-- Write a query to extract the number of people in a  room with the name "Meeting room", by 14:00 (UTC) on May 1st, 2021. Assume that the room is guaranteed to be empty by midnight (UTC) of every day.
