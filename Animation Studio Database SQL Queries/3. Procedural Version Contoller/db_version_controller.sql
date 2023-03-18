-- CREATE TABLE DatabaseVersions(
--	version_id INT PRIMARY KEY IDENTITY,
--	version_number INT
-- );

-- INSERT INTO DatabaseVersions(version_number) VALUES (0)

CREATE PROCEDURE db_version_controller @reqVersion INT
AS
BEGIN
	IF @reqVersion >5
	BEGIN
		RAISERROR('Versiunea ceruta trebuie sa fie un numar intreg intre 0 si 5!',16,1);
		RETURN;
	END

	IF @reqVersion <0
	BEGIN
		RAISERROR('Versiunea ceruta trebuie sa fie un numar intreg intre 0 si 5!',16,1);
		RETURN;
	END

	DECLARE @crntVersion INT
	SELECT TOP 1 @crntVersion=[version_number]
	FROM DatabaseVersions ORDER BY version_id DESC

	IF @reqVersion = @crntVersion
	BEGIN
		RAISERROR('Versiunea data este deja folosita!',16,1);
		RETURN;
	END

	IF @reqVersion > @crntVersion
	BEGIN
		WHILE @crntVersion < @reqVersion
		BEGIN
			IF @crntVersion = 4
			BEGIN
				EXEC procedure5;
				SET @crntVersion = @crntVersion + 1
			END

			IF @crntVersion = 3
			BEGIN
				EXEC procedure4;
				SET @crntVersion = @crntVersion + 1
			END

			IF @crntVersion = 2
			BEGIN
				EXEC procedure3;
				SET @crntVersion = @crntVersion + 1
			END

			IF @crntVersion = 1
			BEGIN
				EXEC procedure2;
				SET @crntVersion = @crntVersion + 1
			END

			IF @crntVersion = 0
			BEGIN
				EXEC procedure1;
				SET @crntVersion = @crntVersion + 1
			END
		END
	END

	IF @crntVersion > @reqVersion
	BEGIN
		WHILE @crntVersion > @reqVersion
		BEGIN
			IF @crntVersion = 1
			BEGIN
				EXEC undo_procedure1;
				SET @crntVersion = @crntVersion - 1
			END

			IF @crntVersion = 2
			BEGIN
				EXEC undo_procedure2;
				SET @crntVersion = @crntVersion - 1
			END

			IF @crntVersion = 3
			BEGIN
				EXEC undo_procedure3;
				SET @crntVersion = @crntVersion - 1
			END

			IF @crntVersion = 4
			BEGIN
				EXEC undo_procedure4;
				SET @crntVersion = @crntVersion - 1
			END
			IF @crntVersion = 5
			BEGIN
				EXEC undo_procedure5;
				SET @crntVersion = @crntVersion - 1
			END
		END
	END
	
	INSERT INTO	DatabaseVersions(version_number) VALUES (@reqVersion)
END;

