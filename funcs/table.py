from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5.QtWidgets import QMessageBox, QFileDialog, QInputDialog, QMenu
from PyQt5.QtCore import QTime, QTimer, QDate, Qt, QDateTime

# Обновление таблицы
def update_table(self):
    cur = self.con.cursor()

    # Получаем данные о связях
    result = cur.execute("SELECT * FROM qsos").fetchall()

    self.table.setRowCount(len(result))

    # Вставляем в таблицу
    for i, elem in enumerate(result):
        for j, val in enumerate(elem):
            # Если это позывной, то вместо id подставляем позывной
            if j in (6, 7):
                val = cur.execute(f"""
                    SELECT callsign FROM callsigns
                    WHERE id = {val}""").fetchone()[0]
            # Если это режим, то вместо id подставляем режим
            elif j == 5:
                val = cur.execute(f"""
                    SELECT mode FROM modes
                    WHERE id = {val}""").fetchone()[0]
            self.table.setItem(i, j, QTableWidgetItem(str(val)))
    
    callsigns = len(cur.execute("SELECT id FROM callsigns").fetchall())
    
    # Подтяшиваем под значения, опускаемся в самый низ и обновляем информацию
    # о связях в статусбаре
    self.table.resizeColumnsToContents()
    self.table.scrollToBottom()
    self.statusbar.showMessage(f"QSOs: {len(result)}, Callsigns: {callsigns}")


# Контекстное меню
def contextMenuEvent(self, event):
    # Объявляем, добавляем пункты
    contextMenu = QMenu(self)
    editAct = contextMenu.addAction("Редактировать")
    deleteAct = contextMenu.addAction("Удалить")
    quitAct = contextMenu.addAction("Закрыть меню")
    action = contextMenu.exec_(self.mapToGlobal(event.pos()))
    # Если хотим удалить
    if action == quitAct:
        pass
    elif action == deleteAct:
        # Высчитываем какие записи были выделены
        rows = list(set([i.row() for i in self.table.selectedItems()]))
        ids = [self.table.item(i, 0).text() for i in rows]

        # Спрашиваем юзера
        valid = QMessageBox.question(
            self, '', "Действительно удалить связи с id " + ",".join(ids),
            QMessageBox.Yes, QMessageBox.No)

        # Если да, то удаляем
        if valid == QMessageBox.Yes:
            cur = self.con.cursor()
            cur.execute("DELETE FROM qsos WHERE id IN (" + ", ".join(
                '?' * len(ids)) + ")", ids)
            self.con.commit()
            self.update_table()
    # Если хотим отредачить
    elif action == editAct:
        # Высчитываем айдишник первой выделенной строки
        row = list(set([i.row() for i in self.table.selectedItems()]))[0]
        id_ = self.table.item(row, 0).text()

        callsign_1 = self.callsignEdit_1.text().upper()
        callsign_2 = self.callsignEdit_2.text().upper()
        RST_1 = self.RSTEdit_1.text()
        RST_2 = self.RSTEdit_2.text()
        comment_1 = self.commentEdit_1.text()
        comment_2 = self.commentEdit_2.text()
        mode = self.modeBox.currentText()
        freq = int(self.freqBox.value())

        if not self.edit_flag:
            self.qso_buffer = (callsign_1, callsign_2, RST_1, RST_2,
                               comment_1, comment_2, mode, freq)

        # Подставляем данные в поля
        cur = self.con.cursor()
        qso = cur.execute(f"""
            SELECT *
            FROM qsos
            WHERE id = {id_}""").fetchone()

        self.realTimeCheckBox.setChecked(False)
        call_1 = cur.execute(f"""
            SELECT callsign
            FROM callsigns
            WHERE id = {qso[6]}""").fetchone()[0]
        call_2 = cur.execute(f"""
            SELECT callsign
            FROM callsigns
            WHERE id = {qso[7]}""").fetchone()[0]
        self.callsignEdit_1.setText(call_1)
        self.callsignEdit_2.setText(call_2)

        self.freqBox.setValue(int(qso[4]))

        mode_text = cur.execute(f"""
            SELECT mode
            FROM modes
            WHERE id = {qso[5]}""").fetchone()[0]
        self.modeBox.setCurrentText(mode_text)

        self.dateEdit.setDate(QDate.fromString(qso[1], "dd.MM.yyyy"))
        self.startTimeEdit.setTime(QTime.fromString(qso[2], "HH:mm:ss"))
        self.endTimeEdit.setTime(QTime.fromString(qso[3], "HH:mm:ss"))

        # Запоминаем айдишник, включаем режим редактирования
        self.edit_id = id_
        self.edit_flag = True
