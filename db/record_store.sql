DROP TABLE IF EXISTS albums;
DROP TABLE IF EXISTS artists;

CREATE TABLE artists (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE albums (
    id SERIAL PRIMARY KEY,
    artist INT NOT NULL REFERENCES artists(id) ON DELETE CASCADE,
    title VARCHAR(255),
    year_released INT,
    genre VARCHAR(255),
    stock_qty INT,
    purchase_price FLOAT,
    sell_price FLOAT
);
