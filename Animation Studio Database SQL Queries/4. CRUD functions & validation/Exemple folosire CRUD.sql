exec CRUD_Proiect @titlu_p='Finding Nemo', @descriere_p='Un peste care isi cauta fiul pierdut',
					@deadline='2026-03-22', @cid = 1001, @did = 3;
exec CRUD_Scena @durata_s = 120, @deadline_s='2023-05-12', @cost=450.45, @pid=3
exec CRUD_Task @scene_id = 51, @artist_id = 3

-- instructiuni care dau eroare din cauza id-urilor gresite
exec CRUD_Proiect @titlu_p='Finding Nemo', @descriere_p='Un peste care isi cauta fiul pierdut',
					@deadline='2026-03-22', @cid = 9999, @did = 3;
exec CRUD_Proiect @titlu_p='Finding Nemo', @descriere_p='Un peste care isi cauta fiul pierdut',
					@deadline='2026-03-22', @cid = 1001, @did = 99;
exec CRUD_Scena @durata_s = 120, @deadline_s='2023-05-12', @cost=450.45, @pid=99
exec CRUD_Task @scene_id = 51, @artist_id = 99
exec CRUD_Task @scene_id = 1000, @artist_id = 3
