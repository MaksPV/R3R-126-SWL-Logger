import sys
import requests
import yaml
import sqlite3
import json

from ui import Ui_MainWindow
# from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5.QtWidgets import QMessageBox, QFileDialog, QInputDialog, QMenu
from PyQt5.QtCore import QTime, QTimer, QDate, Qt, QDateTime

from pyhamtools.locator import calculate_distance, latlong_to_locator

from funcs import export
from funcs import table

version = 0.4

# , Ui_MainWindow
class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.version = version
        settings = {"callsign": "", "locator": "", 
                    "eqsl_user": "", "eqsl_pswd": ""}
        
        # Загружаем файл конфигурации, если нет - создаём новый
        try:
            with open("settings.yml", "r") as f:
                s = yaml.safe_load(f)
                if set(s) != set(settings):
                    raise BaseException
                settings = s
                f.close()
        except:
            with open("settings.yml", "w") as f:
                callsign, ok = QInputDialog().getText(self, "Позывной", "Ваш позывной:")
                locator, ok = QInputDialog().getText(self, "Локатор", "Ваш локатор:")
                eqsl_user, ok = QInputDialog().getText(self, "Логин на eQSL", "Ваш логин на eQSL:")
                eqsl_pswd, ok = QInputDialog().getText(self, "Пароль на eQSL", "Ваш пароль на eQSL:")
                settings = {"callsign": callsign, "locator": locator, 
                            "eqsl_user": eqsl_user, "eqsl_pswd": eqsl_pswd}
                yaml.dump(settings, f, default_flow_style=False)
                f.close()

        # Загружаем настройки
        self.my_loc = settings["locator"]
        self.my_call = settings["callsign"]
        self.settings = settings
        self.edit_flag = False
        self.edit_id = 0
        self.qso_buffer = tuple()

        # uic.loadUi('untitled11.ui', self)

        # Таймер для даты и времени
        timer = QTimer(self)
        timer.timeout.connect(self.show_time)
        timer.start(1000)
        self.show_time()

        # Подключаем кнопки
        self.okButton.clicked.connect(self.add_row)
        self.clearButton.clicked.connect(self.clear_lines)

        # Подключаем поля изменения позывного
        for i in (self.callsignEdit_1, self.callsignEdit_2):
            i.textChanged.connect(self.make_upper)
            i.textChanged.connect(self.changes_call)

        # Подключаем поля с локаторами к функции, считающей расстояние
        self.locatorEdit_1.textChanged.connect(self.changes_beetwen)
        self.locatorEdit_2.textChanged.connect(self.changes_beetwen)

        # Подключаем пункты меню
        self.actionADIF.triggered.connect(self.to_adif)
        self.action_eQSL.triggered.connect(self.to_eqsl)
        self.actionClearBase.triggered.connect(self.clear_base)
        self.actionChangeBand.triggered.connect(self.change_band)
        self.actionChangeMode.triggered.connect(self.change_mode)
        self.actionAbout.triggered.connect(self.about)

        # Подключаем базы данных
        self.con = sqlite3.connect("radio_data.sqlite")
        self.con_cty = sqlite3.connect("cty_data.sqlite")
        self.update_table()

        # Мне крайне стыдно за это, но оно так работает быстрее
        cur_cty = self.con_cty.cursor()
        self.cty = dict()
        cty = self.cty
        for k, i in cur_cty.execute("SELECT prefix, loc FROM global_cty").fetchall():
            cty[k] = i

        self.euro_cty = dict()
        euro_cty = self.euro_cty
        for k, i in cur_cty.execute("SELECT prefix, loc FROM euro_cty").fetchall():
            euro_cty[k] = i

    def about(self):
        about_text = "Логгер сделал Попов Максим (R3R-126)\n"
        about_text += "Для себя и в роли проекта для Яндекс Лицея\n"
        about_text += f"\nВерсия {version}"
        QMessageBox.about(self, "R3R-126 SWL Logger", about_text)

    # Обновляем дату и время
    def show_time(self):
        if self.realTimeCheckBox.isChecked():
            date_time = QDateTime().currentDateTimeUtc()
            time = date_time.time()
            self.startTimeEdit.setTime(time.addSecs(-60))
            self.endTimeEdit.setTime(time)

            date = date_time.date()
            self.dateEdit.setDate(date)

    # Добавляем запись в базу данных
    def add_row(self):
        # Сбор из всех полей
        callsign_1 = self.callsignEdit_1.text().upper()
        callsign_2 = self.callsignEdit_2.text().upper()
        callsigns = (callsign_1, callsign_2)
        RST_1 = self.RSTEdit_1.text()
        RST_2 = self.RSTEdit_2.text()
        name_1 = self.nameEdit_1.text()
        name_2 = self.nameEdit_2.text()
        names = (name_1, name_2)
        QTH_1 = self.QTHEdit_1.text()
        QTH_2 = self.QTHEdit_2.text()
        QTHs = (QTH_1, QTH_2)
        locator_1 = self.locatorEdit_1.text()
        locator_2 = self.locatorEdit_2.text()
        locators = (locator_1, locator_2)
        comment_1 = self.commentEdit_1.text()
        comment_2 = self.commentEdit_2.text()
        mode = self.modeBox.currentText()
        freq = int(self.freqBox.value())

        # Если хотя бы один из позывных длинной не меньше трёх
        # то заносим запись
        if len(callsign_1) >= 3 or len(callsign_2) >= 3:
            cur = self.con.cursor()

            # Обновляем или добавляем информацию о позывных
            for i in range(2):
                if len(cur.execute(f"SELECT * FROM callsigns WHERE callsign = '{callsigns[i]}'").fetchall()):
                    cur.execute(f"""
                        UPDATE callsigns
                        SET callsign = '{callsigns[i]}', name = '{names[i]}',
                                qth = '{QTHs[i]}', locator = '{locators[i]}'
                        WHERE callsign = '{callsigns[i]}'""")
                else:
                    cur.execute(f"""
                        INSERT INTO callsigns(callsign, name, qth, locator)
                        VALUES('{callsigns[i]}', '{names[i]}', '{QTHs[i]}', '{locators[i]}')""")

            # Преобразуем данные для базы даннных
            date = self.dateEdit.date().toString("dd.MM.yyyy")
            time_start = self.startTimeEdit.time().toString("HH:mm:ss")
            time_end = self.endTimeEdit.time().toString("HH:mm:ss")

            # Ищем айдишники для позывных и режима из базы даннных
            id_mode = cur.execute(f"SELECT id FROM modes WHERE mode = '{mode}'").fetchone()[0]
            id_call_1 = cur.execute(f"SELECT id FROM callsigns WHERE callsign = '{callsign_1}'").fetchone()[0]
            id_call_2 = cur.execute(f"SELECT id FROM callsigns WHERE callsign = '{callsign_2}'").fetchone()[0]

            # Если включён режим изменения записи, то обновляем запись, если нет, то добавляем новую
            if not self.edit_flag:
                cur.execute(f"""
                    INSERT INTO qsos(date, time_start, time_end, freq, mode, call_1, call_2,
                    rst_1, rst_2, comment_1, comment_2) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                            (date, time_start, time_end, freq, id_mode, id_call_1, id_call_2, RST_1, RST_2, comment_1,
                             comment_2))
            else:
                cur.execute(f"""
                UPDATE qsos
                SET date = ?, time_start = ?, time_end = ?, freq = ?, mode = ?, call_1 = ?, call_2 = ?,
                    rst_1 = ?, rst_2 = ?, comment_1 = ?, comment_2 = ?
                WHERE id = {self.edit_id}""",
                            (date, time_start, time_end, freq, id_mode,
                             id_call_1, id_call_2, RST_1, RST_2, comment_1, comment_2))
                self.exit_from_edit()

            # сохраняем, обновляем, чистим поля
            self.con.commit()
            self.update_table()
            self.clear_lines()

    # Функция чистит поля
    def clear_lines(self):
        lines_1 = (self.callsignEdit_1, self.RSTEdit_1,
                   self.nameEdit_1, self.QTHEdit_1,
                   self.locatorEdit_1, self.commentEdit_1, self.textBrowser)

        lines_2 = (self.callsignEdit_2, self.RSTEdit_2,
                   self.nameEdit_2, self.QTHEdit_2,
                   self.locatorEdit_2, self.commentEdit_2, self.textBrowser_2)

        if not self.nonClearButton_1.isChecked() or self.edit_flag:
            for i in lines_1:
                i.setText("")
        if not self.nonClearButton_2.isChecked() or self.edit_flag:
            for i in lines_2:
                i.setText("")

        if self.edit_flag:
            self.exit_from_edit()

    # Делаем символы в полях позывных большими
    # и переводим кириллицу в латиницу
    def make_upper(self):
        ru = list("йцукенгшщзфывапролдячсмить.ёхъжэбю")
        latin = list("qwertyuiopasdfghjklzxcvbnm/`[];',.")

        new_line = ""
        for i in self.sender().text().lower():
            if i in ru:
                new_line += latin[ru.index(i)]
            else:
                new_line += i

        pos = self.sender().cursorPosition()
        self.sender().setText(new_line.upper())
        self.sender().setCursorPosition(pos)

    # функция триггерится на изменение в позывном
    def changes_call(self):
        callsignEdits = (self.callsignEdit_1, self.callsignEdit_2)
        locatorEdits = (self.locatorEdit_1, self.locatorEdit_2)
        textBrowsers = (self.textBrowser, self.textBrowser_2)
        RSTEdits = (self.RSTEdit_1, self.RSTEdit_2)
        QTHEdits = (self.QTHEdit_1, self.QTHEdit_2)
        nameEdits = (self.nameEdit_1, self.nameEdit_2)

        sender_ind = callsignEdits.index(self.sender())
        cur = self.con.cursor()

        # Загружаем данные из памяти, если они есть
        result = cur.execute(f"""
            SELECT qth, name FROM callsigns
            WHERE callsign = '{self.sender().text()}'""").fetchone()
        if result and self.sender().text() != "":
            QTHEdits[sender_ind].setText(result[0])
            nameEdits[sender_ind].setText(result[1])

        # Автоматическое подставление 59
        if len(self.sender().text()) >= 3 and RSTEdits[sender_ind].text() == "":
            RSTEdits[sender_ind].setText("59")
            RSTEdits[sender_ind].selectAll()
        # Загрузка дополнительной информации о позывном
        # Из интернета, если юзер выбрал такой способ получения инфы
        if len(self.sender().text()) == 4 and self.hamQTHBox.isChecked():
            try:
                r = requests.get("http://www.hamqth.com/dxcc_json.php", params={"callsign": self.sender().text()})
                call_info = json.loads(r.text)
            except requests.exceptions.RequestException:
                textBrowsers[sender_ind].setText("Не удалось подключиться к HamQTH")
                call_info = {'details': '', 'waz': 0, 'itu': 0, 'continent': 'EU',
                             'lat': 0, 'lng': 0, 'tz': 0, 'len': 0, 'primary_pfx': []}
        # Иначе берём инфу из собственной базы данных
        else:
            call_info = self.get_info(self.sender().text())

        loc_1 = latlong_to_locator(float(call_info["lat"]), float(call_info["lng"]))
        locatorEdits[sender_ind].setText(loc_1)

        text = f"Континент: {call_info['continent']}, ITU: {call_info['itu']}, CQ: {call_info['waz']}"
        text += f"\nCoords: {call_info['lat']}, {call_info['lng']}"
        text += f"\n{call_info['details']}"
        text += f"\nДо вас: {round(calculate_distance(loc_1, self.my_loc), 2)} км"

        # Отформатированный текст вставляем в текстовое поле под позывным
        textBrowsers[sender_ind].setText(text)

    # Подсчитываем расстояние между двумя станциями
    def changes_beetwen(self):
        if self.locatorEdit_1 != "" and self.locatorEdit_2 != "":
            try:
                # Пытаемся посчитать
                self.beeEdit.setText(
                    str(round(calculate_distance(self.locatorEdit_1.text(), self.locatorEdit_2.text()), 2)) + " км")
            except ValueError:
                # Иначе просто чистим поле
                self.beeEdit.setText("")

    # Получение дополнительных данных о позывном из базы даннных
    def get_info(self, call):
        a = {'details': '', 'waz': 0, 'itu': 0, 'continent': 'EU', 'lat': 0, 'lng': 0, 'tz': 0, 'len': 0,
             'primary_pfx': []}

        cur = self.con_cty.cursor()

        # Поочерёдно проходимся по обоем таблицам
        # Сначала по странам мира, а потом по регионам
        for j in (self.cty, self.euro_cty):
            for i in range(6, 0, -1):
                # r = cur.execute(f"SELECT * FROM {j} WHERE prefix = '{call[:i]}'").fetchone()
                # if r != None:
                #    id_ = r[2]
                # else:
                #    continue

                if call[:i] in j:
                    id_ = j[call[:i]]
                else:
                    continue

                res = cur.execute(f"SELECT * FROM locs WHERE id = {id_}").fetchone()
                a["details"] += res[1] + " "
                a["waz"] = res[2]
                a["itu"] = res[3]
                a["continent"] = res[4]
                a["lat"] = res[5]
                a["lng"] = -res[6]
                a["tz"] = res[7]
                a["len"] = res[8]
                a["primary_pfx"].append(res[9])
                break
        # Возвращаем информацию
        return a

    # Отработчик нажатий
    def keyPressEvent(self, event):
        quene = (self.callsignEdit_1, self.callsignEdit_2, self.RSTEdit_1, self.nameEdit_1,
                 self.QTHEdit_1, self.RSTEdit_2, self.nameEdit_2, self.QTHEdit_2)
        # Если нажата кнопка вверх, то смещаем фокус вперёд по quene
        if event.key() == Qt.Key_Up:
            for k, i in enumerate(quene):
                if i.hasFocus():
                    quene[(k + 1) % len(quene)].setFocus()
                    break
        # Если нажата кнопка вниз, то смещаем фокус назад по quene
        elif event.key() == Qt.Key_Down:
            for k, i in enumerate(quene):
                if i.hasFocus():
                    quene[(k - 1) % len(quene)].setFocus()
                    break
        # Если нажата кнопка Enter, то вносим запись
        elif event.key() in (Qt.Key_Return, Qt.Key_Enter):
            self.add_row()

    # Меняем диапозон по нажатию ALT + B
    def change_band(self):
        freq = self.freqBox.value()

        band_dict = {(135, 138): "2200M", (1800, 2000): "160M", (3500, 3800): "80M",
                     (7000, 7200): "40M", (10100, 10150): "30M", (14000, 14350): "20M",
                     (18050, 18200): "17M", (21000, 21450): "15M", (24890, 24990): "12M",
                     (28000, 29700): "10M", (144000, 146000): "2M", (430000, 440000): "432"}

        bands = list(band_dict)

        for k, i in enumerate(bands):
            if i[0] <= freq <= i[1]:
                self.freqBox.setValue(bands[(k + 1) % len(bands)][0])
                break

    # Меняем режим по нажатию ALT + M
    def change_mode(self):
        modes = ("SSB", "FM", "SSTV", "DIGI", "CW", "RTTY", "Other", "AM")

        current_text = self.modeBox.currentText()
        self.modeBox.setCurrentText(modes[(modes.index(current_text) + 1) % len(modes)])

    # Чистим базу даннных
    def clear_base(self):
        cur = self.con.cursor()
        cur.execute("DELETE FROM qsos")
        cur.execute("DELETE FROM SQLite_sequence WHERE name = 'qsos'")
        self.update_table()

    # Выход из режима редактирования
    def exit_from_edit(self):
        self.edit_flag = False
        self.realTimeCheckBox.setChecked(True)
        qso_buffer = self.qso_buffer

        self.clear_lines()

        lines = (self.callsignEdit_1, self.callsignEdit_2, self.RSTEdit_1,
                 self.RSTEdit_1, self.commentEdit_1, self.commentEdit_2)

        for k, i in enumerate(lines):
            i.setText(self.qso_buffer[k])

        self.modeBox.setCurrentText(qso_buffer[-2])
        self.freqBox.setValue(qso_buffer[-1])

MyWidget.to_adif = export.to_adif
MyWidget.update_table = table.update_table
MyWidget.contextMenuEvent = table.contextMenuEvent
MyWidget.get_adif = export.get_adif
MyWidget.to_eqsl = export.to_eqsl

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # Тема Фужн
    app.setStyle('Fusion')
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
