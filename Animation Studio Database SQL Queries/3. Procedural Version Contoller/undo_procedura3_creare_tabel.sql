CREATE PROCEDURE undo_procedure3
AS
BEGIN
	DROP TABLE Creator
	PRINT('Tabela Creator a fost eliminata')
END;
