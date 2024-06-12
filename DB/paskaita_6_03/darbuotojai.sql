-- Create PROJEKTAS table
CREATE TABLE PROJEKTAS (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    PAVADINIMAS VARCHAR(255) NOT NULL
);

-- Insert data into PROJEKTAS
INSERT INTO PROJEKTAS (PAVADINIMAS) VALUES
('Izola'),
('Registrų Centras'),
('Kaunas');

-- Create SKYRIUS table with PRIMARY KEY
CREATE TABLE SKYRIUS (
    PAVADINIMAS VARCHAR(255) PRIMARY KEY,
    VADOVAS_ASMENSKODAS VARCHAR(255)
);

-- Insert data into SKYRIUS
INSERT INTO SKYRIUS VALUES
('Java', '48509141175'),
('Testavimo', '38804172782'),
('C#', '38904172782');

-- Create DARBUOTOJAS table with PRIMARY KEY and FOREIGN KEYS
CREATE TABLE DARBUOTOJAS (
    ASMENSKODAS CHAR(11) PRIMARY KEY,
    VARDAS VARCHAR(255),
    PAVARDE VARCHAR(255),
    DIRBANUO DATE,
    GIMIMOMETAI DATE,
    PAREIGOS VARCHAR(255),
    SKYRIUS_PAVADINIMAS VARCHAR(255),
    PROJEKTAS_ID INTEGER,
    FOREIGN KEY (SKYRIUS_PAVADINIMAS) REFERENCES SKYRIUS(PAVADINIMAS),
    FOREIGN KEY (PROJEKTAS_ID) REFERENCES PROJEKTAS(ID)
);

-- Insert data into DARBUOTOJAS
INSERT INTO DARBUOTOJAS (ASMENSKODAS, VARDAS, PAVARDE, DIRBANUO, GIMIMOMETAI, PAREIGOS, SKYRIUS_PAVADINIMAS, PROJEKTAS_ID) VALUES
('38101122335', 'Petras', 'Petraitis', '2009-10-30', '1981-01-11', 'Testuotojas', 'Testavimo', 1),
('38010101234', 'Jonas', 'Jonaitis', '2007-05-30', '1980-10-10', 'Programuotojas', 'Java', 2),
('38103201435', 'Rimas', 'Plekaitis', '2009-10-30', '1981-03-20', 'Programuotojas', 'Java', 3),
('48509141175', 'Zita', 'Lietuvaitė', '2012-06-15', '1985-09-14', 'Projektų vadovė', 'Java', 2),
('48410121275', 'Jurga', 'Jurgaityte', '2011-02-12', '1984-10-12', 'Programuotoja', 'C#', 1),
('38807201234', 'Giedrius', 'Sabutis', '2009-01-21', '1988-07-20', 'Testuotojas', 'Testavimo', 2),
('38807291234', 'Regimantas', 'Sabonis', '2013-01-21', '1988-07-29', 'Testuotojas', 'Testavimo', 3),
('38609191234', 'Saulius', 'Sabonis', '2013-01-21', '1986-09-19', 'Testuotojas', 'Testavimo', 3),
('38109197598', 'Justas', 'Sabonis', '2011-12-17', '1986-09-19', 'Testuotojas', 'Testavimo', 1),
('38503142412', 'Jonas', 'Kalnas', '2009-05-11', '1985-03-24', 'Programuotojas', 'Java', 1),
('39003142412', 'Stasys', 'Sakalas', '2009-05-11', '1990-03-24', 'Programuotojas', 'Java', 3),
('37803142412', 'Povilas', 'Vakalas', '2012-11-11', '1978-03-14', 'Programuotojas', 'C#', 2),
('38804172782', 'Deivydas', 'Piliukas', '2011-12-11', '1988-04-17', 'Projektu vadovas', 'Testavimo', 2),
('38904172782', 'Kestas', 'Liutas', '2012-12-11', '1989-04-17', 'Projektu vadovas', 'C#', 1),
('38901228523', 'laikinas', 'veikejas', '2009-01-22', '1989-01-22', NULL, NULL, NULL);

-- Create DEPARTAMENTAS table with PRIMARY KEY and FOREIGN KEY
CREATE TABLE DEPARTAMENTAS (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    PAVADINIMAS VARCHAR(255) NOT NULL,
    SKYRIUS_PAVADINIMAS VARCHAR(255),
    FOREIGN KEY (SKYRIUS_PAVADINIMAS) REFERENCES SKYRIUS(PAVADINIMAS)
);

-- Insert data into DEPARTAMENTAS
INSERT INTO DEPARTAMENTAS (PAVADINIMAS, SKYRIUS_PAVADINIMAS) VALUES
('IT', 'Java'),
('QA', 'Testavimo'),
('Development', 'C#');
