--- Pt. tabela Scene
CREATE FUNCTION checkProjectId(@pid int)
RETURNS INT
AS
	BEGIN
		DECLARE @nr AS INT
		SELECT @nr=COUNT(*) FROM Proiect Where Proiect.pid=@pid
		IF @nr = 0
			RETURN 0
		RETURN 1
	END

--- Pt. tabela Tasks
CREATE FUNCTION checkSceneId(@scene_id int)
RETURNS INT
AS
	BEGIN
		DECLARE @nr AS INT
		SELECT @nr=COUNT(*) FROM Scena Where Scena.scene_id=@scene_id
		IF @nr = 0
			RETURN 0
		RETURN 1
	END


CREATE FUNCTION checkArtistId(@aid int)
RETURNS INT
AS
	BEGIN
		DECLARE @nr AS INT
		SELECT @nr=COUNT(*) FROM Artist Where Artist.aid=@aid
		IF @nr = 0
			RETURN 0
		RETURN 1
	END


--- Pt. tabela Proiect
CREATE FUNCTION checkClientId(@cid int)
RETURNS INT
AS
	BEGIN
		DECLARE @nr AS INT
		SELECT @nr=COUNT(*) FROM Client Where Client.cid=@cid
		IF @nr = 0
			RETURN 0
		RETURN 1
	END

CREATE FUNCTION checkDirectorId(@did int)
RETURNS INT
AS
	BEGIN
		DECLARE @nr AS INT
		SELECT @nr=COUNT(*) FROM Director Where Director.did=@did
		IF @nr = 0
			RETURN 0
		RETURN 1
	END