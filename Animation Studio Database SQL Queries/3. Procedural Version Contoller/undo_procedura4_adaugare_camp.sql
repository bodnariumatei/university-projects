CREATE PROCEDURE undo_procedure4
AS
BEGIN
	ALTER TABLE Element
	Drop column creator_id
	PRINT('Campul creator_id a fost eliminat din tabela Element')
END;