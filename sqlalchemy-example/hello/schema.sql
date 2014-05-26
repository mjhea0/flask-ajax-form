BEGIN;


DROP TABLE IF EXISTS departments;
CREATE TABLE departments (
    id              INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name            VARCHAR(50)
);


DROP TABLE IF EXISTS employees;
CREATE TABLE employees (
    id              INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name            VARCHAR(100),
    department_id   INTEGER,
    FOREIGN KEY(department_id) REFERENCES departments(id)
);


COMMIT;

INSERT INTO departments (id, name) VALUES (1, "Accounting");
INSERT INTO departments (id, name) VALUES (2, "Sales");
INSERT INTO departments (id, name) VALUES (3, "Management");

INSERT INTO employees (id, name, department_id) VALUES (1, "Kyra Davis", 1);
INSERT INTO employees (id, name, department_id) VALUES (2, "Abigail Whitfield", 1);
INSERT INTO employees (id, name, department_id) VALUES (3, "Maya Chase", 1);
INSERT INTO employees (id, name, department_id) VALUES (4, "Lydia Hyde", 1);
INSERT INTO employees (id, name, department_id) VALUES (5, "Wynne Erickson", 2);
INSERT INTO employees (id, name, department_id) VALUES (6, "Candice Davidson", 2);
INSERT INTO employees (id, name, department_id) VALUES (7, "Lawrence Roman", 2);
INSERT INTO employees (id, name, department_id) VALUES (8, "Kameko Parker", 2);
INSERT INTO employees (id, name, department_id) VALUES (9, "Jamal Everett", 3);
INSERT INTO employees (id, name, department_id) VALUES (10, "Avram Burks", 3);
INSERT INTO employees (id, name, department_id) VALUES (11, "Mia Mendez", 3);
INSERT INTO employees (id, name, department_id) VALUES (12, "Ila Cantrell", 3);