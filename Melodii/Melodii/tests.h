#pragma once
#include "domain.h"
#include <assert.h>

void test_domain() {
	Song s(141, "I took a pill in Ibiza", "Mike Poser", 9);

	assert(s.get_id() == 141);
	assert(s.get_title() == "I took a pill in Ibiza");
	assert(s.get_artist() == "Mike Poser");
	assert(s.get_rank() == 9);

	s.set_title("I took a pill");
	assert(s.get_title() == "I took a pill");

	s.set_rank(8);
	assert(s.get_rank() == 8);
}

void test_repo() {
	Repository testRepo("testFile.txt");

}

void test_all() {
	test_domain();
	test_repo();
}