from PyQt5.QtWidgets import QFileDialog, QMessageBox
import requests

# Экспорт в формат ADIF
def to_adif(self):
    # Спрашиваем юзера куда сохранить
    adif_name, choosen = QFileDialog.getSaveFileName(self, "Save ADIF", "", "ADIF (*.adi)")

    # Если юзер согласился, то начинаем экспорт
    if choosen:
        header = self.get_adif()
        
        # Сохраняем
        with open(adif_name, "w") as f:
            f.write(header)
            f.close()


def to_eqsl(self):
    header = self.get_adif(eqsl=True)
    try:
        r = requests.post("http://www.eQSL.cc/qslcard/importADIF.cfm", data={"ADIFData": header})
        text = "Успешно"
    except:
        text = "Не удалось связаться с eQSL"
    QMessageBox.about(self, "Информация с eQSL", text)


def get_adif(self, ids=(), eqsl=False):
    operator = self.my_call
    # Словарь диапозонов
    band_dict = {(135, 138): "2200M", (1800, 2000): "160M", (3500, 3800): "80M",
                 (7000, 7200): "40M", (10100, 10150): "30M", (14000, 14350): "20M",
                 (18050, 18200): "17M", (21000, 21450): "15M", (24890, 24990): "12M",
                 (28000, 29700): "10M", (144000, 146000): "2M", (430000, 440000): "432"}

    # Заголовок для ADIF файла
    header = "<PROGRAMID:18>R3R-126 SWL Logger\n"
    header += f"<PROGRAMVERSION:{len(str(self.version))}>{self.version}\n"
    header += "<ADIF_VER:5>3.0.4\n"
    if eqsl:
        eqsl_user = self.settings["eqsl_user"]
        eqsl_pswd = self.settings["eqsl_pswd"]
        header += f"<EQSL_USER:{len(eqsl_user)}>{eqsl_user}\n"
        header += f"<EQSL_PSWD:{len(eqsl_pswd)}>{eqsl_pswd}\n"
    header += "<EOH>"

    # Загружаем все связи
    cur = self.con.cursor()
    if ids:
        result = cur.execute(f"SELECT * FROM qsos WHERE id IN {tuple(ids)}").fetchall()
    else:
        result = cur.execute("SELECT * FROM qsos").fetchall()
    
    wkd = (list(), list())
    for k, i in enumerate(result):
        # Разбираем i
        date = i[1]
        date = date[-4:] + date[3:5] + date[:2]
        time_start = i[2]
        time_start = time_start[:2] + time_start[3:5] + time_start[6:8]
        time_end = i[3]
        time_end = time_end[:2] + time_end[3:5] + time_end[6:8]
        freq = str(i[4])
        band = ""
        # Получаем диапозон из частоты
        for j in band_dict:
            if j[0] <= int(freq) <= j[1]:
                band = band_dict[j]
        if band == "":
            band = str(freq)[:-3]
        mode = cur.execute(f"""
            SELECT mode FROM modes
            WHERE id = {i[5]}""").fetchone()[0]
        call_1_info = cur.execute(f"""
            SELECT callsign, name, qth, locator
            FROM callsigns
            WHERE id = {i[6]}""").fetchone()
        call_2_info = cur.execute(f"""
            SELECT callsign, name, qth, locator
            FROM callsigns
            WHERE id = {i[7]}""").fetchone()
        callsign_1 = call_1_info[0]
        callsign_2 = call_2_info[0]
        RST_1 = str(i[8])
        RST_2 = str(i[9])
        name_1 = call_1_info[1]
        name_2 = call_2_info[1]
        QTH_1 = call_1_info[2]
        QTH_2 = call_2_info[2]
        loc_1 = call_1_info[3]
        loc_2 = call_2_info[3]
        comment_1 = i[10]
        comment_2 = i[11]
        
        flag_1 = True
        flag_2 = True
        if k + 1 < len(result) - 1:
            if i[6] == result[k + 1][6]:
                wkd[0].append(callsign_2)
                flag_1 = False
            if i[7] == result[k + 1][7]:
                wkd[1].append(callsign_1)
                flag_2 = False
        
        
        # Добавляем связи в формате ADIF
        if callsign_1 != "" and flag_1:
            header += f"\n<OPERATOR:{len(operator)}>{operator}<SWL:1>Y<CALL:{len(callsign_1)}>{callsign_1}"
            header += f"<QSO_DATE:8>{date}<TIME_ON:6>{time_start}<TIME_OFF:6>{time_end}<FREQ:{len(freq)}>{freq}"
            header += f"<BAND:{len(band)}>{band}<MODE:{len(mode)}>{mode}<RST_RCVD:{len(RST_2)}>{RST_2}"
            header += f"<RST_SENT:{len(RST_1)}>{RST_1}<NAME:{len(name_1)}>{name_1}<QTH:{len(QTH_1)}>{QTH_1}"
            header += f"<GRIDSQUARE:{len(loc_1)}>{loc_1}"
            wkd[0].append(callsign_2)
            if comment_1:
                header += f"<QSLMSG:{len(', '.join(wkd[0])) + len(comment_1) + 11}>You WKD {', '.join(wkd[0])} | {comment_1}<EOR>"
            else:
                header += f"<QSLMSG:{len(', '.join(wkd[0])) + 8}>You WKD {', '.join(wkd[0])}<EOR>"
            wkd[0].clear()

        if callsign_2 != "" and flag_2:
            header += f"\n<OPERATOR:{len(operator)}>{operator}<SWL:1>Y<CALL:{len(callsign_2)}>{callsign_2}"
            header += f"<QSO_DATE:8>{date}<TIME_ON:6>{time_start}<TIME_OFF:6>{time_end}<FREQ:{len(freq)}>{freq}"
            header += f"<BAND:{len(band)}>{band}<MODE:{len(mode)}>{mode}<RST_RCVD:{len(RST_1)}>{RST_1}"
            header += f"<RST_SENT:{len(RST_2)}>{RST_2}<NAME:{len(name_2)}>{name_2}<QTH:{len(QTH_2)}>{QTH_2}"
            header += f"<GRIDSQUARE:{len(loc_2)}>{loc_2}"
            wkd[1].append(callsign_1)
            if comment_1:
                header += f"<QSLMSG:{len(', '.join(wkd[1])) + len(comment_2) + 11}>You WKD {', '.join(wkd[1])} | {comment_1}<EOR>"
            else:
                header += f"<QSLMSG:{len(', '.join(wkd[1])) + 8}>You WKD {', '.join(wkd[1])}<EOR>"
            wkd[1].clear()
    
    return header