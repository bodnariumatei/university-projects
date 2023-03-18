-- Selecteaza numele artistilor si scenele la care lucreaza si deadline-ul lor
SELECT a.nume_a, s.scene_id, s.deadline_s
FROM Artist a, Scena s, Task t
WHERE t.aid=a.aid AND t.scene_id=s.scene_id
ORDER BY s.deadline_s

-- Selecteaza clientul si directorul pentru fiecare proiect 
SELECT c.nume_c as Client, p.titlu_p as Titlu, d.nume_d as Director
FROM Client c, Proiect p, Director d
WHERE p.cid=c.cid AND p.did=d.did

-- Selecteaza proiectele cu costul total al scenelor > 2000
SELECT p.titlu_p, SUM(s.cost) as cost_total
FROM Proiect p, Scena s
WHERE s.pid=p.pid
GROUP BY p.titlu_p
HAVING SUM(s.cost)>2000

-- Selecteaza pentru fiecare scena toate elementele atribuite acesteia si descrierea lor
SELECT s.scene_id, e.denumire_e, e.descriere_e
FROM Element e, Scena s, Atribuire a
WHERE s.scene_id=a.scene_id AND e.eid=a.eid

-- Selecteaza fiecare tip de artist care lucreaza la o anumita scena
SELECT DISTINCT s.scene_id, t.denumire_t
FROM Scena s INNER JOIN Task tsk ON tsk.scene_id=s.scene_id 
    INNER JOIN Artist a ON tsk.aid=a.aid
	INNER JOIN TipArtist t ON t.tid=a.tid

-- Selecteaza proiectele, deadline-ul lor si artistii care lucreaza la ele
-- pentru proiectele cu deadline in 2023
SELECT p.titlu_p, a.nume_a, p.deadline_p
FROM Proiect p INNER JOIN Scena s ON p.pid=s.pid
	 INNER JOIN Task t ON s.scene_id=t.scene_id
	 INNER JOIN Artist a ON t.aid=a.aid
WHERE p.deadline_p LIKE '2023%'

-- Selecteaza Clientul, Proiectul si Durata totala a scenelor
-- pentru proiectele care au o durata mai mare de 120
SELECT c.nume_c, p.titlu_p, SUM(s.durata_s) as durata_totala
FROM Proiect p, Scena s, Client c
WHERE s.pid=p.pid AND c.cid=p.cid
GROUP BY c.nume_c, p.titlu_p
HAVING SUM(s.durata_s)>120

-- Selecteaza titlul proiectelor si numarul de artisti care lucreaza la el
-- pentru proiectele la care lucreaza mai mult de trei
SELECT p.titlu_p, COUNT(a.aid) as Numar_artisti
FROM Proiect p INNER JOIN Scena s ON p.pid=s.pid
	INNER JOIN Task t ON s.scene_id=t.scene_id
	INNER JOIN Artist a ON t.aid=a.aid
GROUP BY p.titlu_p
HAVING COUNT(a.aid) > 3

-- Selecteaza titlul proiectelor si numele artistilor care lucreaza la ele
SELECT DISTINCT p.titlu_p, a.nume_a
FROM Proiect p INNER JOIN Scena s ON p.pid=s.pid
	INNER JOIN Task t ON s.scene_id=t.scene_id
	INNER JOIN Artist a ON t.aid=a.aid

-- Calculeaza costul total pentru fiecare client
SELECT c.nume_c, SUM(s.cost) as cost_total
FROM Client c, Proiect p, Scena s
WHERE c.cid=p.cid AND p.pid=s.pid
GROUP BY c.nume_c