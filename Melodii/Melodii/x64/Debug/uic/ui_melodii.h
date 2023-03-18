/********************************************************************************
** Form generated from reading UI file 'melodii.ui'
**
** Created by: Qt User Interface Compiler version 6.3.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MELODII_H
#define UI_MELODII_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QToolBar>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MelodiiClass
{
public:
    QMenuBar *menuBar;
    QToolBar *mainToolBar;
    QWidget *centralWidget;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *MelodiiClass)
    {
        if (MelodiiClass->objectName().isEmpty())
            MelodiiClass->setObjectName(QString::fromUtf8("MelodiiClass"));
        MelodiiClass->resize(600, 400);
        menuBar = new QMenuBar(MelodiiClass);
        menuBar->setObjectName(QString::fromUtf8("menuBar"));
        MelodiiClass->setMenuBar(menuBar);
        mainToolBar = new QToolBar(MelodiiClass);
        mainToolBar->setObjectName(QString::fromUtf8("mainToolBar"));
        MelodiiClass->addToolBar(mainToolBar);
        centralWidget = new QWidget(MelodiiClass);
        centralWidget->setObjectName(QString::fromUtf8("centralWidget"));
        MelodiiClass->setCentralWidget(centralWidget);
        statusBar = new QStatusBar(MelodiiClass);
        statusBar->setObjectName(QString::fromUtf8("statusBar"));
        MelodiiClass->setStatusBar(statusBar);

        retranslateUi(MelodiiClass);

        QMetaObject::connectSlotsByName(MelodiiClass);
    } // setupUi

    void retranslateUi(QMainWindow *MelodiiClass)
    {
        MelodiiClass->setWindowTitle(QCoreApplication::translate("MelodiiClass", "Melodii", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MelodiiClass: public Ui_MelodiiClass {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MELODII_H
