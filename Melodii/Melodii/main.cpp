#include "gui.h"
#include <QtWidgets/QApplication>
#include "tests.h"

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    
    test_all();

    Repository repo("cantece.txt");

    Service srv(repo);
    SongsGui sgui(srv);

    sgui.show();
    return a.exec();
}
