#pragma once
#include "repository.h"

class Service {
private:
	Repository& repo;
public:
	Service() = delete;
	Service(Repository& repo) : repo{repo}{}
	Service(const Service& srv) = delete;

	int count_artist(string artist);

	void remove(int id);

	void update_song(int id, string nTitle, int nRank);

	const vector<Song>& get_all() {
		return repo.get_all();
	}
};