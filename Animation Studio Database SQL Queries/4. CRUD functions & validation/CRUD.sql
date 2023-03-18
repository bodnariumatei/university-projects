ALTER PROCEDURE CRUD_Proiect
@titlu_p varchar(60),
@descriere_p varchar(150),
@deadline date,
@cid int,
@did int
AS
BEGIN
	IF(dbo.checkClientId(@cid) = 1 AND dbo.checkDirectorId(@did) = 1)
	BEGIN
		DECLARE @pid int
		SELECT TOP 1 @pid=Proiect.pid FROM Proiect ORDER BY pid DESC
		SET @pid = @pid + 1
		-- CREATE ( INSERT )
		INSERT INTO Proiect(pid, titlu_p, descriere_p, deadline_p, cid, did)
		VALUES (@pid, @titlu_p, @descriere_p, @deadline, @cid, @did)

		-- SELECT ( READ )
		SELECT * FROM Proiect

		-- UPDATE
		UPDATE Proiect SET descriere_p = 'Done' WHERE deadline_p < GETDATE()

		-- DELETE
		DELETE FROM Task WHERE scene_id in (SELECT scene_id FROM Scena WHERE pid=@pid)
		DELETE FROM Atribuire WHERE scene_id in (SELECT scene_id FROM Scena WHERE pid=@pid)
		DELETE FROM Scena WHERE pid = @pid
		DELETE FROM Proiect WHERE pid = @pid

		print 'CRUD Proiect terminat'
	END
	ELSE
	BEGIN
		PRINT 'Error'
		PRINT 'Id client sau Id director incorect'
		RETURN
	END
END


CREATE PROCEDURE CRUD_Scena
@durata_s int,
@deadline_s date,
@cost float,
@pid int
AS
BEGIN
	IF (dbo.checkProiectId(@pid) = 1)
	BEGIN
		DECLARE @scene_id INT
		SELECT TOP 1 @scene_id=Scena.scene_id FROM Scena ORDER BY scene_id DESC
		SET @scene_id = @scene_id + 1

		-- CREATE ( INSERT )
		INSERT INTO Scena(scene_id, durata_s, deadline_s, cost, pid)
		VALUES (@scene_id, @durata_s, @deadline_s, @cost, @pid)

		-- SELECT ( READ )
		SELECT * FROM Scena

		-- UPDATE
		UPDATE Scena SET cost = cost + 50 WHERE deadline_s > GETDATE()

		-- DELETE
		DELETE FROM Task WHERE scene_id = @scene_id
		DELETE FROM Atribuire WHERE scene_id = @scene_id
		DELETE FROM Scena WHERE scene_id = @scene_id

		print 'CRUD Scena terminat'
	END
	ELSE BEGIN
		PRINT ('EROARE!')
		PRINT ('ID Proiect incorect')
	END
END


CREATE PROCEDURE CRUD_Task
@scene_id INT,
@artist_id INT
AS
BEGIN
	IF (dbo.checkSceneID(@scene_id) = 1 AND dbo.checkArtistId(@artist_id) = 1)
	BEGIN
		-- CREATE ( INSERT )
		INSERT INTO Task(scene_id, aid)
		VALUES (@scene_id, @artist_id)

		-- SELECT ( READ )
		SELECT * FROM Task

		-- UPDATE
		-- C'est ne pas possible - Contine doar chei straine => cheie primara

		-- DELETE
		DELETE FROM Task WHERE scene_id = @scene_id AND aid = @artist_id

		print 'CRUD Task terminat'
	END
	ELSE BEGIN
		PRINT ('EROARE!')
		PRINT ('ID Scena sau ID Artist incorect')
	END
END