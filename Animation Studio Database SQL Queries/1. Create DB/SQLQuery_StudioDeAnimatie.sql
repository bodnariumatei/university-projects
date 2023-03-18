--CREATE DATABASE StudioDeAnimatie
--GO
--USE StudioDeAnimatie
--GO

CREATE TABLE Client(
	cid INT PRIMARY KEY,
	nume_c VARCHAR(50),
	mail_c VARCHAR(50),
	adresa_c VARCHAR(100)
);

CREATE TABLE Director(
	did INT PRIMARY KEY IDENTITY,
	nume_d VARCHAR(50) NOT NULL,
	varsta_d INT,
	adresa_d VARCHAR(100)
);

CREATE TABLE Proiect(
	pid INT PRIMARY KEY,
	titlu_p VARCHAR(60) UNIQUE,
	descriere_p VARCHAR(150),
	deadline_p DATE,
	cid INT FOREIGN KEY REFERENCES Client(cid),
	did INT FOREIGN KEY REFERENCES Director(did)
);

CREATE TABLE Scena(
	scene_id INT PRIMARY KEY,
	durata_s INT,
	deadline_s DATE,
	cost INT,
	pid INT FOREIGN KEY REFERENCES Proiect(pid)
);

CREATE TABLE Element(
	eid INT PRIMARY KEY,
	sursa_e VARCHAR(50),
	denumire_e VARCHAR(30),
	descriere_e VARCHAR(65)
);

CREATE TABLE Atribuire(
	scene_id INT FOREIGN KEY REFERENCES Scena(scene_id),
	eid INT FOREIGN KEY REFERENCES Element(eid),
	CONSTRAINT pk_Atribuire PRIMARY KEY (scene_id,eid)
);

CREATE TABLE Supervizor(
	svid INT PRIMARY KEY,
	nume_sv VARCHAR(50)
);

CREATE TABLE TipArtist(
	tid INT PRIMARY KEY,
	denumire_t VARCHAR(60)
);

CREATE TABLE Artist(
	aid INT PRIMARY KEY IDENTITY,
	nume_a VARCHAR(60),
	tid INT FOREIGN KEY REFERENCES TipArtist(tid),
	svid INT FOREIGN KEY REFERENCES Supervizor(svid),
);

CREATE TABLE Task(
	aid INT FOREIGN KEY REFERENCES Artist(aid),
	scene_id INT FOREIGN KEY REFERENCES Scena(scene_id),
	CONSTRAINT pk_Task PRIMARY KEY (aid,scene_id)
);