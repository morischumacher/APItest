
CREATE TABLE IF NOT EXISTS connections (
    id SERIAL PRIMARY KEY,
    from_planet_id BIGINT,
	to_planet_id BIGINT,
	price BIGINT
);

CREATE TABLE IF NOT EXISTS planets (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

INSERT INTO planets (name) VALUES
    ('Earth'),
    ('Mars'),
    ('Venus'),
    ('Jupiter'),
    ('Saturn');

INSERT INTO connections (from_planet_id, to_planet_id, price) VALUES
    (1, 2, 100),
    (1, 3, 150),
    (2, 3, 200),
    (2, 4, 300),
    (3, 4, 250),
    (4, 5, 400);





