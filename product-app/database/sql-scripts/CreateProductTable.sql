CREATE TABLE IF NOT EXISTS product (id INT NOT NULL AUTO_INCREMENT,
       name VARCHAR(100) NOT NULL,
       price FLOAT(5, 2) NOT NULL,
       category VARCHAR(50) NOT NULL,
       stocked BOOLEAN,
       PRIMARY KEY(id)) ENGINE=InnoDB;
