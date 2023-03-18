#include "service.h"

int Service::count_artist(string artist) {
	int nr = 0;
	vector<Song> songs = repo.get_all();
	for (auto& s : songs) {
		if (s.get_artist() == artist) {
			nr++;
		}
	}
	return nr;
}

void Service::remove(int id) {
	repo.remove(id);
}

void Service::update_song(int id, string nTitle, int nRank) {
	repo.update(id, nTitle, nRank);
}