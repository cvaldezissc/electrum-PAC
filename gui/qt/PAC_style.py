"""PAC look and feel."""

PAC_stylesheet = """

/* Lite Mode -- cloned from "CleanLook" theme */
#main_window
{
    /*border-image: url(:/icons/bg.png) 0 0 0 0 stretch stretch;*/
}

MiniWindow QPushButton {
    color: #777;
    border: 1px solid #CCC;
    border-radius: 0;
    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
stop: 0 white, stop: 1 #E6E6E6);
    min-height: 30px;
    min-width: 30px;
}

#send_button{
    color: #FFF;
    border: 1px solid #3786E6;
    border-radius: 4px;
    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
stop: 0 #72B2F8, stop: 1 #3484E6);
    padding: 2px;
    width: 20px;
}

#send_button:disabled{
    color: #D3E8FE;
    border: 1px solid #6DAEF7;
    border-radius: 4px;
    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
stop: 0 #A5CFFA, stop: 1 #72B2F8);
}
#address_input, #amount_input, #label_input
{
    color: #000;
    padding: 5px;
    border-radius: 5px;
    min-height: 23px;
    border: 1px solid #AAA9A9;
    width: 200px;
}

#address_input[isValid=true]
{
    color: #4D9948;
}

#address_input[isValid=false]
{
    color: #CE4141;
}

#balance_label
{
    color: #000;
}

#history
{
    color: #888;
}


/**********************/
/* $PAC CSS */
/*
0. OSX Reset
1. Navigation Bar
2. Editable Fields, Labels
3. Containers
4. File Menu, Toolbar
5. Buttons, Spinners, Dropdown
6. Table Headers
7. Scroll Bar
8. Tree View
9. Dialog Boxes
*/
/**********************/


/**********************/
/* 0. OSX Reset */

QWidget { /* Set default style for QWidget, override in following statements */
    border: 0;
}

QGroupBox {
    margin-top: 1em;
}

QGroupBox::title {
    subcontrol-origin: margin;
}

/**********************/
/* 1. Navigation Bar */

#main_window_topbar{
    background-color: #000;
    position: absoulte;
}

#main_window_topbar #logo_image{
    background: url(:/icons/top_bar_logo.png) no-repeat left top;
}

#main_window_topbar QPushButton{
    background-color: #000;
    width: 10px;
}

#main_window_topbar QPushButton:hover{
    background-color:#333333;
}

#main_window_nav_bar {
    border:0;
    position: absolute;
}

#main_window_nav_bar QTabBar{
    color: #fff;
    border:0;
}

QTabWidget#main_window_nav_bar::tab-bar {
    alignment: center;
}

QTabWidget#main_window_nav_bar::pane {
    position: absolute;
}

#main_window_nav_bar QTabBar::tab {
    background-color:#000;
    color:#fff;
    min-height: 50px;
    min-width: 40px;
    padding-left:1em;
    padding-right:1em;
    padding-bottom:1em;
}

#main_window_nav_bar QTabBar::tab:first {
    border-left: 0 solid #fff;
}

#main_window_nav_bar QTabBar::tab:last {
    border-right: 0 solid #fff;
}

#main_window_nav_bar QTabBar::tab:selected, #main_window_nav_bar QTabBar::tab:hover {
    background-color:#333333;
}

/**********************/
/* 2. Editable Fields and Labels */

QCheckBox { /* Checkbox Labels */
    color:#333333;
    background-color:transparent;
}

QCheckBox:hover {
    background-color:transparent;
}

QValidatedLineEdit, QLineEdit, PayToEdit, QPlainTextEdit { /* Text Entry Fields */
    border: 0px;
    outline:0;
    background-color:#fff;
    color: #000;
    border-radius: 5px;
}

PayToEdit{
    padding-top: 5px;
}

ButtonsLineEdit {
    color: #000;
    background: #fff;
}

QLabel {
    color: #000;
    min-height:25px;
}

QLineEdit#search_box{
    max-width: 250px;
}

/**********************/
/* 3. Containers */


/* Dashboard Container */

QWidget#main_window_container {
    background: #f8f6f6;
    color: #000;
}

QWidget#central_widget {
    background-color:#000;
}

QWidget#section_title{
    font-weight:bold;
    font-size: 36px;
    text-transform: uppercase;
}

QWidget#section_content > QLabel{
    background-color:#fff;
    font-size: 18px !important;
    border-radius: 5px;
    height: 40px;
    padding-left: 10px;
}

QWidget#section_content > QValidatedLineEdit, 
QWidget#section_content > QLineEdit, 
QWidget#section_content > PayToEdit, 
QWidget#section_content > QPlainTextEdit { 
    height:40px;
    font-size: 18px;
    padding-left: 10px;
}

QWidget#section_content > QComboBox {
    font-size: 18px;
}

#sub_section_title{
    font-size: 22px;
}

QWidget#sub_section_content{
    background-color:#fff;
    min-height: 50px;
    border-radius: 5px;
    border-top: 1px solid #e6e6e6;
    border-left: 1px solid #e6e6e6;
    padding-top: 15px;
    padding-bottom: 15px;
    padding-left: 25px;
    padding-right: 25px;
}

QWidget#home_container,
QWidget#addresses_container,
QWidget#coins_container,
QWidget#contacts_container,
QWidget#history_container,
QWidget#send_container,
QWidget#receive_container,
QWidget#console_container {
    border-image: url(:/icons/background.png) 300 0 100 0 stretch stretch;
}

QWidget#home_container #sub_section_content QLabel#important_label{
    font-size: 18px;
    font-weight:bold;
}

QWidget#home_container #sub_section_content QLabel#normal_label{
    font-size: 18px !important;
}

QWidget#home_container QTreeWidget QHeaderView::section,
QWidget#addresses_container QTreeWidget QHeaderView::section,
QWidget#coins_container QTreeWidget QHeaderView::section,
QWidget#contacts_container QTreeWidget QHeaderView::section,
QWidget#history_container QTreeWidget QHeaderView::section,
QWidget#receive_container  QTreeWidget QHeaderView::section{
    font-size: 15px;
}

/* History Container */
#history_container {
}

/* Send Container */
#send_container {
}

#send_container  QLabel#section_column {
    min-width:142px;
}

/* Receive Container */
#receive_container {
}

#receive_container QLabel#section_column {
    min-width:142px;
}

/* Addressses Container */
#addresses_container {
}

/* Coins Container */
#coins_container {
}

/* Contacts Container */
#contacts_container {
}

/* Console Container */
#console_container > QPlainTextEdit{
    font-size: 14px;
}

/* Balance Label */
#main_window_balance {
    color:#fff;
    font-weight:bold;
}


/**********************/
/* 4. File Menu, Toolbar */

#main_window_container QMenuBar {
    color: #fff;
}

QMenuBar {
    background-color:#fff;
}

QMenuBar::item {
    background-color:#fff;
    color:#333;
}

QMenuBar::item:selected {
    background-color:#f8f6f6;
}

QMenu {
    background-color:#f8f6f6;
    border:1px solid #2B2727;
}

QMenu::item {
    color:#333;
}

QMenu::item:selected {
    background-color:#f2f0f0;
    color:#333;
}

QToolBar {
    background-color:#3398CC;
    border:0px solid #000;
    padding:0;
    margin:0;
}

QToolBar > QToolButton {
    background-color:#3398CC;
    border:0px solid #333;
    min-height:2.5em;
    padding: 0em 1em;
    font-weight:bold;
    color:#fff;
}

QToolBar > QToolButton:checked {
    background-color:#fff;
    color:#333;
    font-weight:bold;
}

QMessageBox {
    background-color:#F8F6F6;
}

QMessageBox > QLabel {
    min-height: 70px;
}


QLabel { /* Base Text Size & Color */
    color:#000;
}


/**********************/
/* 5. Buttons, Spinners, Dropdown */

QPushButton { /* Global Button Style */
    background-color: #000;
    border:0;
    border-radius:3px;
    color:#ffffff;
    font-size: 18px;
    font-weight:bold;
    padding-left:25px;
    padding-right:25px;
    padding-top:5px;
    padding-bottom:5px;
    min-height:25px;
}

QPushButton:hover {
    background-color: #fef000;
    color: #000;
}

QPushButton:focus {
    border:none;
    outline:none;
}

QPushButton:pressed {
    border:1px solid #333;
}

QPushButton:disabled
{
    color: #000;
    background-color: #e7e4e4;
}

QComboBox { /* Dropdown Menus */
    border:0px;
    padding: 3px 5px 3px 5px;
    background:#fff;
    min-height:40px;
    color:#000;

}

QComboBox:checked {
    background:#f2f2f2;
}

QComboBox:editable {
    background: #3398CC;
    color:#616161;
    border:0px solid transparent;
}

QComboBox::drop-down {
    width:25px;
    border:0px;
}

QComboBox::down-arrow {
    border-image: url(':/icons/PAC_downArrow.png') 0 0 0 0 stretch stretch;
}

QComboBox QListView {
    background:#fff;
    border:1px solid #333;
    padding-right:1px;
    padding-left:1px;
}

QComboBox QAbstractItemView::item { margin:4px; }

QComboBox::item {
    color:#818181;
}

QComboBox::item:alternate {
    background:#fff;
}

QComboBox::item:selected {
    border:0px solid transparent;
    background:#f2f2f2;
}

QComboBox::indicator {
    background-color:transparent;
    selection-background-color:transparent;
    color:transparent;
    selection-color:transparent;
}

QAbstractSpinBox {
    border:1px solid #82C3E6;
    padding: 3px 5px 3px 5px;
    background:#fcfcfc;
    min-height:25px;
    color:#818181;
}

QAbstractSpinBox::up-button {
    subcontrol-origin: border;
    subcontrol-position: top right;
    width:21px;
    background:#fcfcfc;
    border-left:0px;
    border-right:1px solid #82C3E6;
    border-top:1px solid #82C3E6;
    border-bottom:0px;
    padding-right:1px;
    padding-left:5px;
    padding-top:2px;
}


QAbstractSpinBox::down-button {
    subcontrol-origin: border;
    subcontrol-position: bottom right;
    width:21px;
    background:#fcfcfc;
    border-top:0px;
    border-left:0px;
    border-right:1px solid #82C3E6;
    border-bottom:1px solid #82C3E6;
    padding-right:1px;
    padding-left:5px;
    padding-bottom:2px;
}


/**********************/
/* 6. Table Headers */

QHeaderView { /* Table Header */
    background-color:transparent;
    border:0px;

}

QHeaderView::section { /* Table Header Sections */
    qproperty-alignment:center;
    background-color:qlineargradient(x1: 0, y1: 0, x2: 0, y2: 0.25, stop: 0 #CCC7C7, stop: 1 #CCC7C7);
    color:#000;
    min-width: 50px;
    min-height:25px;
    font-weight:bold;
    font-size:11px;
    outline:0;
    border:0;
    border-right:1px solid #F8F6F6;
    padding-left:2px;
    padding-right:10px;
    padding-top:1px;
    padding-bottom:1px;
}

#contacts_container QHeaderView::section {
}

#contacts_container QHeaderView::section:first {
    padding-left:50px;
    padding-right:40px;
}

QHeaderView::section:last {
    border-right: 0px solid #d7d7d7;
}


/**********************/
/* 7. Scroll Bar */

QScrollBar { /* Scroll Bar */

}

QScrollBar:vertical { /* Vertical Scroll Bar Attributes */
    border:0;
    background:#ffffff;
    width:18px;
    margin: 18px 0px 18px 0px;
}

QScrollBar:horizontal { /* Horizontal Scroll Bar Attributes */
    border:0;
    background:#ffffff;
    height:18px;
    margin: 0px 18px 0px 18px;
}


QScrollBar::handle:vertical { /* Scroll Bar Slider - vertical */
    background:#e0e0e0;
    min-height:10px;
}

QScrollBar::handle:horizontal { /* Scroll Bar Slider - horizontal */
    background:#e0e0e0;
    min-width:10px;
}

QScrollBar::add-page, QScrollBar::sub-page { /* Scroll Bar Background */
    background:#F8F6F6;
}

QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical, QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal { /* Define Arrow Button Dimensions */
    background-color:#F8F6F6;
    border: 1px solid #f2f0f0;
    width:16px;
    height:16px;
}

QScrollBar::add-line:vertical:pressed, QScrollBar::sub-line:vertical:pressed, QScrollBar::add-line:horizontal:pressed, QScrollBar::sub-line:horizontal:pressed {
    background-color:#e0e0e0;
}

QScrollBar::sub-line:vertical { /* Vertical - top button position */
    subcontrol-position:top;
    subcontrol-origin: margin;
}

QScrollBar::add-line:vertical { /* Vertical - bottom button position */
    subcontrol-position:bottom;
    subcontrol-origin: margin;
}

QScrollBar::sub-line:horizontal { /* Vertical - left button position */
    subcontrol-position:left;
    subcontrol-origin: margin;
}

QScrollBar::add-line:horizontal { /* Vertical - right button position */
    subcontrol-position:right;
    subcontrol-origin: margin;
}

QScrollBar:up-arrow, QScrollBar:down-arrow, QScrollBar:left-arrow, QScrollBar:right-arrow { /* Arrows Icon */
    width:10px;
    height:10px;
}

QScrollBar:up-arrow {
    background-image: url(':/icons/PAC_upArrow_small.png');
}

QScrollBar:down-arrow {
    background-image: url(':/icons/PAC_downArrow_small.png');
}

QScrollBar:left-arrow {
    background-image: url(':/icons/PAC_leftArrow_small.png');
}

QScrollBar:right-arrow {
    background-image: url(':/icons/PAC_rightArrow_small.png');
}


/**********************/
/* 8. Tree Widget & QTableView */

QTreeWidget{
    border: 0;
    background-color:rgba(255,255,255,128);
}

QTableView {
    border: 0;
    background-color:#fff;
}

QTreeWidget::item, 
QTableView::item {
    color:#333;
}

QTreeWidget QHeaderView::section, 
QTableView QHeaderView::section{
    background-color: #fff;
    color: #000;
    text-transform: uppercase;
}

QTreeWidget QHeaderView::section:horizontal, 
QTableView QHeaderView::section:horizontal{
    border-bottom: 3px solid #fef000;
}

/**********************/
/* 9. Dialog Boxes */

QDialog {
    background:qradialgradient(cx:0.5, cy:0.5, radius: 0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 255, 255), stop: 1 rgba(233, 233, 233, 255));
}

QDialog QTabWidget {
    border-bottom:1px solid #333;
}

QDialog QTabWidget::pane {
    border: 1px solid #d7d7d7;
}

QDialog QTabWidget QTabBar::tab {
    background-color:qradialgradient(cx:0.5, cy:0.5, radius: 0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 255, 255, 255), stop: 1 rgba(233, 233, 233, 255));;
    color:#333;
    padding-left:10px;
    padding-right:10px;
    padding-top:5px;
    padding-bottom:5px;
    border-top: 1px solid #d7d7d7;
}

QDialog QTabWidget QTabBar::tab:first {
    border-left: 1px solid #d7d7d7;
}

QDialog QTabWidget QTabBar::tab:last {
    border-right: 1px solid #d7d7d7;
}

QDialog QTabWidget QTabBar::tab:selected, QDialog QTabWidget QTabBar::tab:hover {
    background-color:#ffffff;
    color:#333;
}

QDialog QTabWidget QWidget {
    /*color:#333;*/
}

QDialog QTabWidget QWidget QAbstractSpinBox {
    min-height:15px;
}

QDialog QTabWidget QWidget QAbstractSpinBox::down-button {
    width:15px;
}

QDialog QTabWidget QWidget QAbstractSpinBox::up-button {
    width:15px;
}

QDialog QTabWidget QWidget QComboBox {
    min-height:15px;
}

QDialog QWidget { /* Remove Annoying Focus Rectangle */
    outline: 0;
}
"""