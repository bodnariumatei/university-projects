CREATE PROCEDURE procedure4
AS
BEGIN
	ALTER TABLE Element
	ADD creator_id INT
	PRINT('Campul creator_id a fost adaugat in tabela Element')
END;