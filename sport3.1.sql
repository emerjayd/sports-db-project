CREATE TABLE IF NOT EXISTS COACH (
    coach_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    address TEXT,
    yrs_experience INTEGER
);

CREATE TABLE IF NOT EXISTS PLAYER (
    player_id INTEGER PRIMARY KEY AUTOINCREMENT,
    number INTEGER,
    first_name TEXT,
    last_name TEXT,
    score INTEGER,
    team TEXT
);

CREATE TABLE IF NOT EXISTS GAME (
    game_id INTEGER PRIMARY KEY AUTOINCREMENT,
    home TEXT,
    away TEXT,
    date TEXT,
    time TEXT,
    location TEXT
);

CREATE TABLE IF NOT EXISTS SEASON (
    season_id INTEGER PRIMARY KEY AUTOINCREMENT,
    begin TEXT,
    end TEXT
);
