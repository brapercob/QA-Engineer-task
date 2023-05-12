import openpyxl
import os


class AlbumData:

    @staticmethod
    def get_titles():
        albums = []
        book = openpyxl.load_workbook(os.path.abspath('album_data/albums.xlsx'))
        sheet = book['Hoja1']
        for c in sheet['A'][0:5]:
            albums.append(c.value)
        return [albums]


