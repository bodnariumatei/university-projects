CREATE PROCEDURE procedure5
AS
BEGIN
	ALTER TABLE Element
	ADD CONSTRAINT FK_CreatorElement
	FOREIGN KEY (creator_id) REFERENCES Creator(creator_id);
	PRINT('Constrangere cheie straina adaugata pe tabela Element la tabela Creator')
END;