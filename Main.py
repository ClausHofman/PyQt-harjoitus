import sys
from datetime import datetime

import mysql.connector
import pandas as pd
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QMessageBox, QFileDialog
from PyQt5.QtCore import pyqtSlot

from Show_Data import Ui_MainWindow

class ConnectToMySQL():
    def __init__(self):
        self.host = '127.0.0.1'
        self.user = 'test_user'
        self.password = 'TEST@123456'
        self.port = '3306'
        self.database = 'sql_store'
        self.con = None
    
    def connect(self):
        """create connection with database
        :return:
        """
        self.con = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            port=self.port,
            database=self.database
        )
    
    def get_all_data_from_db(self):
        try:
            self.connect()
            cursor = self.con.cursor(dictionary=True)
            sql = "SELECT * FROM customers;"
            cursor.execute(sql)
            result = cursor.fetchall()

            return result
        except Exception as e:
            print("get data failed")
            print(e)
        
        finally:
            if self.con:
                self.con.close()
        

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ## =============================================================================================
        ## init all the widgets
        self.get_data_btn = self.ui.get_data_btn
        self.select_save_path_btn = self.ui.get_path_btn
        self.save_btn = self.ui.save_btn
        self.file_path = self.ui.lineEdit
        self.result_table = self.ui.tableWidget
    
    ## =============================================================================================
    ## create functions
    @pyqtSlot(bool)
    def on_get_data_btn_clicked(self):
        ## =========================================================================================
        ## get data from database
        result = ConnectToMySQL().get_all_data_from_db()

        if result:
            self.result_table.setRowCount(len(result))

            for row, item in enumerate(result):
                column_1_item = QTableWidgetItem(str(item['column1']))
                column_2_item = QTableWidgetItem(str(item['column2']))
                column_3_item = QTableWidgetItem(str(item['column3']))
                column_4_item = QTableWidgetItem(str(item['column4']))
                column_5_item = QTableWidgetItem(str(item['column5']))
                column_6_item = QTableWidgetItem(str(item['column6']))
                column_7_item = QTableWidgetItem(str(item['column7']))
                column_8_item = QTableWidgetItem(str(item['column8']))
                column_9_item = QTableWidgetItem(str(item['column9']))

                self.result_table.setItem(row, 0, column_1_item)
                self.result_table.setItem(row, 1, column_2_item)
                self.result_table.setItem(row, 2, column_3_item)
                self.result_table.setItem(row, 3, column_4_item)
                self.result_table.setItem(row, 4, column_5_item)
                self.result_table.setItem(row, 5, column_6_item)
                self.result_table.setItem(row, 6, column_7_item)
                self.result_table.setItem(row, 7, column_8_item)
                self.result_table.setItem(row, 8, column_9_item)

        else:
            ## =============================================================================================
            ## show message if no data retrieved from database
            QMessageBox.information(self, "Warning", "No data retrieved from database, please try again")
            return

    @pyqtSlot(bool)
    def on_get_path_btn_clicked(self):
        """get save file path
        :return:
        """
        folder_path = QFileDialog.getExistingDirectory(self, "Select Directory")
        if folder_path:
            self.file_path.setText(folder_path)
    
    @pyqtSlot(bool)
    def on_save_btn_clicked(self):
        """save data to excel
        """
        ## =============================================================================================
        ## get the save path from window
        file_path = self.file_path.text().strip()
        if not file_path:
            QMessageBox.information(self, "Warning", "Please select a save path...")
            return
        
        ## =============================================================================================
        ## create save file name
        now = datetime.now().strftime("%Y-%m-%d")
        file_name = f"Save Data {now}.xlsx"

        ## =============================================================================================
        ## get data from window table
        data_table = self.result_table

        try:
            writer = pd.ExcelWriter(f"{file_path}/{file_name}")

            ## =============================================================================================
            info_headers = [data_table.horizontalHeaderItem(x).text() for x in range(data_table.columnCount())]
            info_df = pd.DataFrame(columns=info_headers)

            for row in range(data_table.rowCount()):
                for col in range(data_table.columnCount()):
                    info_df.loc[row, info_headers[col]] = data_table.item(row, col).text()
            
            ## =============================================================================================
            ## save data to excel
            info_df.to_excel(writer, index=False)
            writer.save()

            ## =============================================================================================
            ## show some note after saved successfully
            QMessageBox.information(self, "Success", "Data saved successfully")
        except Exception as e:
            ## =============================================================================================
            ## show some note if save failed
            QMessageBox.information(self, "note", f'Failed to save data: {e}')


    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())