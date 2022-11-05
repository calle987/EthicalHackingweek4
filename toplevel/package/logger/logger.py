import csv
class Logger:
    def __init__(self, file_name, header):
        self.file_name = file_name
        self.header = header

    def log(self, data):
        with open(self.file_name, 'a', newline='\n') as file:
            writer = csv.writer(file)
            writer.writerow(data)

    def log_header(self):
        with open(self.file_name, 'w', newline='\n') as file:
            writer = csv.writer(file)
            writer.writerow(self.header)

if __name__ == '__main__':
    logger = Logger('/package/logger/log.csv', ["method","data"])
    logger.log_header()



