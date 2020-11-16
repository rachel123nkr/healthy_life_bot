-- create database healthy_app;

 USE healthy_app; 

CREATE TABLE user(
    id int not null  PRIMARY KEY,
    name varchar(50),
    birth_date date,
    max_calories float,
    max_fat float,
    max_sugar float,
    max_protein float,
    current_state varchar(50)
    );


CREATE TABLE user_day(
    user_id int,
    date_of_day date,
    max_calories float,
    max_fat float,
    max_sugar float,
    max_protein float,

    PRIMARY KEY (user_id, date_of_day),

    FOREIGN KEY(user_id) REFERENCES user(id)
)

