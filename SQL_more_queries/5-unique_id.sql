-- creates the table unique_id on your MySQL server.
CREATE TABLE IF NOT EXISTS unique_id(
    id INT UNIQUE DEFAULT 1, -- with the default value 1 and must be unique
    name VARCHAR(256)
);
