create database recipe_db;
create user dbuser with password 'recipe';
grant all privileges on database recipe_db to dbuser;