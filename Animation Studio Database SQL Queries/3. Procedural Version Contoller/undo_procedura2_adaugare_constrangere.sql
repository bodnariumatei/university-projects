CREATE PROCEDURE undo_procedure2
AS
BEGIN
	ALTER TABLE Client
	DROP CONSTRAINT cc_Email
	PRINT('Campul mail_c NU are constrangere de valoare implicita')
END;