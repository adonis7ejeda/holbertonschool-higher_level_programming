-- Lists all cities contained in the database hbtn_0d_usa
-- SQL is fun
SELECT c.id AS id, c.name AS name, s.name AS name FROM states s INNER JOIN cities c ON s.id = c.state_id;
