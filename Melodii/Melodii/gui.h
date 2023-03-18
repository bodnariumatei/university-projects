#pragma once
#include "service.h"
#include <qwidget.h>
#include <qtablewidget.h>
#include <qpushbutton.h>
#include <qlineedit.h>
#include  <qslider.h>
#include <qlabel.h>

class SongsGui : public QWidget {
private:
	Service& srv;

	QTableWidget* tableSongs;

	QLineEdit* editTitle;
	QPushButton* btnUpdate;
	QSlider* sliderRank;

	QPushButton* btnRemove;

	void init_gui();
	void connect_ss();
	void reload_table(const vector<Song>& songs);

	void gui_update();
	void gui_remove();
	void item_selected();
public:
	SongsGui(Service& srv) : srv{ srv } {
		init_gui();
		connect_ss();
		reload_table(srv.get_all());
	}
};