-- creates the table unique_id on your MySQL server.
CRATE TABLE IF EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE
    name VARCHAR(256)
);
