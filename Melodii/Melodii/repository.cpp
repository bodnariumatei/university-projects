#include "repository.h"
#include <fstream>
#include <sstream>

void Repository::load_from_file() {
	std::ifstream sFile(this->filename);
	if (!sFile.is_open())
		return;
	string line;
	while (std::getline(sFile, line)) {
		string title, artist;
		int id = 0, rank = 0;

		std::stringstream linestream(line);
		string current_item;
		int item_no = 0;

		while (getline(linestream, current_item, ',')) {
			if (item_no == 0) id = stoi(current_item);
			if (item_no == 1) title = current_item;
			if (item_no == 2) artist = current_item;
			if (item_no == 3) rank = stoi(current_item);
			item_no++;
		}
		Song s{ id, title, artist, rank };
		songs.push_back(s);
	}
	sFile.close();
}

void Repository::save_to_file() {
	std::ofstream sOutput(this->filename);
	if (!sOutput.is_open())
		return;
	for (auto& s : songs) {
		sOutput << s.get_id() << "," << s.get_title() << ",";
		sOutput << s.get_artist() << "," << s.get_rank() << std::endl;
	}
	sOutput.close();
}

void Repository::remove(int id) {
	songs.erase(std::remove_if(songs.begin(), songs.end(), [id](Song& s1) { return s1.get_id() == id; }));
	save_to_file();
}

void Repository::update(int id, string nTitle, int nRank) {
	int i = -1;
	for (auto& s : songs) {
		i++;
		if (s.get_id() == id) {
			break;
		}
	}
	songs.at(i).set_title(nTitle);
	songs.at(i).set_rank(nRank);
	save_to_file();
}