# APPLICATION FOR SHOWING SUMMARY DATA ABOUT MEAT GIVEN TO SHARE GROUP
# ====================================================================

# LIBRARIES AND MODULES
# ---------------------

import sys # Needed for starting the application
import psycopg2
from PyQt5.QtWidgets import * # All widgets
from PyQt5.uic import loadUi

# CLASS DEFINITIONS FOR THE APP
# -----------------------------

class groupMainWindow(QMainWindow):
    
    # Constructor, a method for creating objects from this class
    def __init__(self):
        QMainWindow.__init__(self)

        # Create an UI from the ui file
        loadUi('groupInfoMainWindow.ui', self)

        # Define properties for ui elements
        self.refreshBtn = self.refreshPushButton
        self.groupInfo = self.groupSummaryTableWidget
        self.sharedMeatInfo = self.meatSharedTableWidget

        # Database connection parameters
        self.database = "metsastys"
        self.user = "sovellus"
        self.userPassword = "Q2werty"
        self.server = "localhost"
        self.port = "5432"

        # SIGNALS

        # Emit a signal when refresh push button is pressed
        self.refreshBtn.clicked.connect(self.refreshData)

    # SLOTS

    #Load data to table widgets
    # Try to establish a connection to DB server
    def refreshData(self):
        
        # To avoid Fatal error crashing the app use try-except-finally structure
        try:
            # Create a connection object
            dbaseconnetion = psycopg2.connect(database=self.database, user=self.user, password=self.userPassword,
                                            host=self.server, port=self.port)
            
            # Create a cursor to execute commands and retrieve result set
            cursor = dbaseconnetion.cursor()
            
            # Execute a SQL command to get hunters (jasen)
            command = "SELECT * FROM public.jaetut_lihat;"
            cursor.execute(command)
            result_set = cursor.fetchall()
            print("Lihaa on jaettu seuraavasti:", result_set)

        # Throw an error if connection or cursor creation fails                                     
        except(Exception, psycopg2.Error) as e:
            print("Tietokantayhteydess?? tapahtui virhe", e)

        # If or if not successfull close the cursor and the connection   
        finally:
            if (dbaseconnetion):
                cursor.close()
                dbaseconnetion.close()
                print("Yhteys tietokantaan katkaistiin")

if __name__ == "__main__":

    # Create an application object
    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    # Create the Main Window object from GroupMainWindow Class
    appWindow = groupMainWindow()
    appWindow.show()
    sys.exit(app.exec_())