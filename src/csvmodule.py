# IMPORTS
import csv
import os
from pathlib import Path

# Clasa para hacer la escritura del fichero csv
class Csvmodule():

    # Constructos de la clase
    # path: ruta del fichero
    # fileName: nombre del fichero
    # data: datos de la forma lista de listas
    # columnsName: nombre de las columna del fichero
    def __init__(self, path, fileName, data, columnsName = None):
        self.path = path
        self.fileName = fileName
        self.data = data
        self.columnsName = columnsName
    
    # Método que comprueba que existe la ruta, si no lo crea
    def __checkPath__(self):
        try:
            Path(self.path).mkdir(parents=True, exist_ok=True)
            return True

        except:
            return False
    
    # Método que se encarga de crear el fichero csv
    def __writeCsv__(self, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL):
        if (self.__checkPath__()):
            with open(os.path.join(self.path, self.fileName), mode='w+', newline="") as csv_file:
                employee_writer = csv.writer(csv_file, delimiter=delimiter, quotechar=quotechar, quoting=quoting)

                if (self.columnsName is not None):
                    employee_writer.writerow(self.columnsName)
                
                for row in self.data:
                    employee_writer.writerow(row)
        else:
            print("ERROR: compruebe la ruta")