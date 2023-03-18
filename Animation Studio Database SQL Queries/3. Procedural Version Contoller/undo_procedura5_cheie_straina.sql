CREATE PROCEDURE undo_procedure5
AS
BEGIN
	ALTER TABLE Element
	DROP CONSTRAINT FK_CreatorElement;
	PRINT('Constrangere cheie straina intre Element si Creator eliminata')
END;