CREATE PROCEDURE undo_procedure1
AS
BEGIN
	ALTER TABLE Scena
	ALTER COLUMN cost INT
	PRINT('Coloana cost din tabela Scena este acum de tipul INT')
END;