CREATE PROCEDURE procedure3
AS
BEGIN
	CREATE TABLE Creator(
		creator_id INT PRIMARY KEY,
		nume_creator VARCHAR(60),
		mail_creator VARCHAR(60),
		);
	PRINT('Tabela Creator a fost creata')
END;

