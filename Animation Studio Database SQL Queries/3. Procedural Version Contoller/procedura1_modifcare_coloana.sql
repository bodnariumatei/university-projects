CREATE PROCEDURE procedure1
AS
BEGIN
	ALTER TABLE Scena
	ALTER COLUMN cost FLOAT
	PRINT('Coloana cost din tabela Scena este acum de tipul FLOAT')
END;