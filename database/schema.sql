CREATE DATABASE IF NOT EXISTS election_system;

USE election_system;

CREATE TABLE citizens(
    citizen_id INT AUTO_INCREMENT PRIMARY KEY,
    national_id VARCHAR(15) UNIQUE NOT NULL,
    full_name VARCHAR(100) NOT NULL,
    dob DATE NOT NULL,
    phone_number VARCHAR(15) UNIQUE NOT NULL,
    gender VARCHAR(10) NOT NULL,
    registered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE voters(
    voter_id INT AUTO_INCREMENT PRIMARY KEY,
    national_id VARCHAR(15) UNIQUE NOT NULL,
    username VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    voter_code VARCHAR(20) UNIQUE NOT NULL ,
    has_voted BOOLEAN DEFAULT FALSE,
    registered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (national_id)
    REFERENCES citizens(national_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

CREATE TABLE candidates(
    candidate_id INT AUTO_INCREMENT PRIMARY KEY,
    national_id VARCHAR(15) UNIQUE NOT NULL,
    party_name VARCHAR(50) NOT NULL,
    position VARCHAR(50) NOT NULL,
    status VARCHAR(20) DEFAULT 'Pending',
    vote_count INT DEFAULT 0,
    registered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (national_id)
    REFERENCES citizens(national_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

CREATE TABLE votes(
    vote_id INT AUTO_INCREMENT PRIMARY KEY,
    voter_id INT NOT NULL,
    candidate_id INT NOT NULL,
    vote_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(voter_id),
    FOREIGN KEY (voter_id)
    REFERENCES voters(voter_id)
    ON DELETE CASCADE,
    FOREIGN KEY (candidate_id)
    REFERENCES candidates(candidate_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

CREATE TABLE admins(
    admin_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    role VARCHAR(30) NOT NULL
);

INSERT INTO admins(
    username,
    password,
    role
)
VALUES(
    "admin_1",
    "admin123",
    "super_admin"
);

INSERT INTO admins(
    username,
    password,
    role
)
VALUES(
    "admin_2",
    "admin456",
    "candidate_admin"
);

INSERT INTO admins(
    username,
    password,
    role
)
VALUES(
    "admin_3",
    "admin789",
    "result_admin"
);