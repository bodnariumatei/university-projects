#include "gui.h"
#include <algorithm>
#include <QVBoxLayout>
#include <QHBoxLayout>
#include <qmessagebox.h>

void SongsGui::init_gui() {
	QHBoxLayout* lyMain = new QHBoxLayout;
	this->setLayout(lyMain);

	QWidget* left = new QWidget;
	QVBoxLayout* lyLeft = new QVBoxLayout;
	left->setLayout(lyLeft);
	tableSongs = new QTableWidget; tableSongs->setColumnCount(4);
	QStringList tblHeaderList;
	tblHeaderList << "ID" << "Titlu" << "Artist" << "Rank";
	tableSongs->setHorizontalHeaderLabels(tblHeaderList);
	lyLeft->addWidget(tableSongs);
	

	QWidget* right = new QWidget;
	QVBoxLayout* lyRight = new QVBoxLayout;
	right->setLayout(lyRight);
	QWidget* updateBox = new QWidget;
	QHBoxLayout* lyUpdateBox = new QHBoxLayout;
	updateBox->setLayout(lyUpdateBox);
	editTitle = new QLineEdit;
	btnUpdate = new QPushButton("Update");
	lyUpdateBox->addWidget(editTitle);
	lyUpdateBox->addWidget(btnUpdate);
	sliderRank = new QSlider(Qt::Horizontal);
	sliderRank->setMaximum(10);
	lyRight->addWidget(updateBox);
	lyRight->addWidget(sliderRank);
	btnRemove = new QPushButton("Remove");
	lyRight->addWidget(btnRemove);

	lyMain->addWidget(left);
	lyMain->addWidget(right);
}

void SongsGui::connect_ss() {
	QObject::connect(btnUpdate, &QPushButton::clicked, this, &SongsGui::gui_update);
	QObject::connect(btnRemove, &QPushButton::clicked, this, &SongsGui::gui_remove);
	QObject::connect(tableSongs, &QTableWidget::itemSelectionChanged, this, &SongsGui::item_selected);
}

void SongsGui::reload_table(const vector<Song>& songs) {
	tableSongs->clearContents();
	tableSongs->setRowCount(songs.size());
	vector<Song> sorted = songs;
	std::sort(sorted.begin(), sorted.end(), [](Song& s1, Song& s2) {return s1.get_rank() < s2.get_rank(); });

	int nl = 0;
	for (auto& s : sorted) {
		tableSongs->setItem(nl, 0, new QTableWidgetItem(QString::number(s.get_id())));
		tableSongs->setItem(nl, 1, new QTableWidgetItem(QString::fromStdString(s.get_title())));
		tableSongs->setItem(nl, 2, new QTableWidgetItem(QString::fromStdString(s.get_artist())));
		tableSongs->setItem(nl, 3, new QTableWidgetItem(QString::number(s.get_rank())));
		nl++;
	}
}

void SongsGui::item_selected() {
	int row = tableSongs->selectedItems().first()->row();
	QString title = tableSongs->item(row, 1)->text();
	int rank = tableSongs->item(row, 3)->text().toInt();

	editTitle->setText(title);
	sliderRank->setSliderPosition(rank);
}

void SongsGui::gui_update() {
	int row = tableSongs->selectedItems().first()->row();
	int id = tableSongs->item(row, 0)->text().toInt();

	string nTitle = editTitle->text().toStdString();
	int nRank = sliderRank->value();
	srv.update_song(id, nTitle, nRank);

	reload_table(srv.get_all());

	editTitle->clear();
	sliderRank->setSliderPosition(0);
}

void SongsGui::gui_remove() {
	int row = tableSongs->selectedItems().first()->row();
	string artist = tableSongs->item(row, 2)->text().toStdString();

	if (srv.count_artist(artist) == 1) {
		QMessageBox::warning(this, "Warning", QString::fromStdString(
			"Aceasta e ultima melodie a artistului!\nNu se poate sterge!"));
	}
	else {
		int id = tableSongs->item(row, 0)->text().toInt();
		srv.remove(id);
		reload_table(srv.get_all());
	}
}