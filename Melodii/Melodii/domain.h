#pragma once
#include <string>
using std::string;

class Song {
private:
	int id, rank;
	string title, artist;
public:
	Song() = delete;

	Song(int id, string title, string artist, int rank)
		: id{id},title{title}, artist{artist}, rank{rank}{}

	Song(const Song& ot) 
		: id{ot.id}, title{ot.title}, artist{ot.artist}, rank{ot.rank}{}

	bool operator==(const Song& ot) {
		return this->id == ot.id;
	}

	int get_id() noexcept {
		return this->id;
	}

	int get_rank() noexcept {
		return this->rank;
	}

	string get_title() {
		return this->title;
	}

	string get_artist() {
		return this->artist;
	}

	void set_title(string nTitle) {
		this->title = nTitle;
	}

	void set_rank(int nRank) {
		this->rank = nRank;
	}
};
