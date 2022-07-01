CREATE TABLE fileinfo (
    id INT NOT NULL AUTO_INCREMENT,
    file_name VARCHAR(50) NOT NULL,
    file_path VARCHAR(100) NOT NULL,
    file_size VARCHAR(10) NOT NULL,
    file_type VARCHAR(50) NOT NULL,
    PRIMARY KEY (id)
);

