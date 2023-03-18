#pragma once
#include "domain.h"
#include <vector>
using std::vector;

class Repository {
private:
	string filename;
	vector<Song> songs;

	void load_from_file();
	void save_to_file();
public:
	Repository() = delete;
	Repository(const Repository& repo) = delete;
	Repository(string file) : filename{ file }{
		load_from_file();
	}

	// Sterge o melodie cu id-ul dat
	/// <param name="id"> id-ul melodiei care se sterge
	void remove(int id);

	/// Modifica atributele unei melodii identificata prin id
	/// <param name="id"> id-ul melodiei care se modifica
	/// <param name="title"> noul titlu
	/// <param name="rank"> noul rank
	void update(int id, string title, int rank);

	// Returneaza lista cu toate melodiile
	const vector<Song>& get_all() {
		return this->songs;
	}
};
