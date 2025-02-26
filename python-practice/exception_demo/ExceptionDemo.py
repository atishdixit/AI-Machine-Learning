class FileReader:
    def __init__(self):
        self.csvfile = None

    def readFile(self):
        try:
            print("opening file....")
            self.csvfile = open("sample.csv")
        except FileNotFoundError:
            print("File not  found...")

    def getFileName(self):
        return self.csvfile.name

    def showFileHeader(self):
        print(self.csvfile.readline())

    def closeOpenFile(self):
        print("closing file.....")
        self.csvfile.close()

    def showFileData(self):
        for line in self.csvfile:
            print(line)

    def readAndShowFileData(self):
        try:
            self.csvfile = open('sample.csv')
        except FileNotFoundError:
            print("File not found...")
        except Exception:
            print("Some Error happened...")
        else:
            for line in self.csvfile:
                print(line)
        finally:
            print("closing file....")
            self.csvfile.close()


reader = FileReader()
# reader.readFile()
# print(reader.getFileName())
# reader.showFileHeader()
# reader.showFileData()
# reader.closeOpenFile()
reader.readAndShowFileData()
