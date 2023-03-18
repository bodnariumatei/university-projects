CREATE PROCEDURE procedure2
AS
BEGIN
	ALTER TABLE Client
	ADD CONSTRAINT cc_Email
	DEFAULT 'client@mail.domain' FOR mail_c;
	PRINT('Campul mail_c are constrangere de valoare implicita setata la: client@mail.domain')
END;

