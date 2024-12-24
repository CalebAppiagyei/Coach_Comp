DROP SCHEMA if exists coach_schema cascade;

CREATE SCHEMA coach_schema;

CREATE TABLE coach_schema.seasons (
    year INT PRIMARY KEY,
    games_played INT NOT NULL
);

CREATE TABLE coach_schema.coach_data (
    coach_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    games INT DEFAULT 0,
    wl_pct FLOAT DEFAULT 0
);

CREATE TABLE coach_schema.teams (
    team_id SERIAL PRIMARY KEY,
    team_name VARCHAR(255) NOT NULL,
    year INT NOT NULL REFERENCES coach_schema.seasons(year),
    coach_id INT NOT NULL REFERENCES coach_schema.coach_data(coach_id),
    games INT NOT NULL,
    extra_info JSONB DEFAULT '{}', -- Will use to handle coaches who didn't last a full season --
    UNIQUE (team_name, year)
);

CREATE TABLE coach_schema.tot_off_data (
    team_id INT NOT NULL PRIMARY KEY REFERENCES coach_schema.teams(team_id),
    pts_for INT DEFAULT 0,
    yds INT DEFAULT 0,
    plays INT DEFAULT 0,
    ypp FLOAT DEFAULT 0, -- yards per play --
    turnovers INT DEFAULT 0,
    penalties INT DEFAULT 0,
    pen_yds INT DEFAULT 0,
    firstD int DEFAULT 0
);

CREATE TABLE coach_schema.pass_off_data (
    team_id INT NOT NULL PRIMARY KEY REFERENCES coach_schema.teams(team_id),
    completions INT DEFAULT 0, 
    attempts INT DEFAULT 0,
    yards INT DEFAULT 0, 
    touchdowns INT DEFAULT 0, 
    interceptions INT DEFAULT 0, 
    nya FLOAT DEFAULT 0, -- Net yards per passing attempt
    first_downs INT DEFAULT 0 
);

CREATE TABLE coach_schema.rush_off_data (
    team_id INT NOT NULL PRIMARY KEY REFERENCES coach_schema.teams(team_id),
    attempts INT DEFAULT 0, 
    yards INT DEFAULT 0,     
    touchdowns INT DEFAULT 0, 
    ypa FLOAT DEFAULT 0,
    first_downs INT DEFAULT 0 
);

CREATE TABLE coach_schema.tot_def_data (
    team_id INT NOT NULL PRIMARY KEY REFERENCES coach_schema.teams(team_id),
    pa INT DEFAULT 0, -- Points Allowed --
    yds INT DEFAULT 0,
    plays INT DEFAULT 0,
    ypp FLOAT DEFAULT 0, -- yards per play --
    turnovers INT DEFAULT 0,
    penalties INT DEFAULT 0,
    pen_yds INT DEFAULT 0,
    firstD int DEFAULT 0
);

CREATE TABLE coach_schema.pass_def_data (
    team_id INT NOT NULL PRIMARY KEY REFERENCES coach_schema.teams(team_id),
    completions INT DEFAULT 0, 
    attempts INT DEFAULT 0,
    yards INT DEFAULT 0, 
    touchdowns INT DEFAULT 0, 
    interceptions INT DEFAULT 0, 
    nya FLOAT DEFAULT 0, -- Net yards per passing attempt
    first_downs INT DEFAULT 0 
);

CREATE TABLE coach_schema.rush_def_data (
    team_id INT NOT NULL PRIMARY KEY REFERENCES coach_schema.teams(team_id),
    attempts INT DEFAULT 0, 
    yards INT DEFAULT 0,     
    touchdowns INT DEFAULT 0, 
    ypa FLOAT DEFAULT 0,
    first_downs INT DEFAULT 0 
);