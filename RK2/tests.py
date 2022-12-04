from main import *


class TestRK:
    # Каталоги файлов
    catalogs = [
        Catalog(1, 'C:\\'),
        Catalog(2, 'C:\\Users\\'),
        Catalog(3, 'C:\\Users\\User\\'),

        Catalog(11, 'D:\\'),
        Catalog(22, 'D:\\Users\\'),
        Catalog(33, 'D:\\Users\\User\\'),
    ]

    # Файлы
    files = [
        File(1, 'AllGuys.mp4', 14.9, 1),
        File(2, 'Valorant.mp4', 1699.84, 2),
        File(3, 'Atement.docx', 0.013, 3),
        File(4, 'Statement.pdf', 0.013, 3),
        File(5, 'Programm.zip', 100, 3),
    ]

    # Файлы в каталогах файлов
    files_catalogs = [
        FileCatalog(1, 1),
        FileCatalog(2, 2),
        FileCatalog(3, 3),
        FileCatalog(3, 4),
        FileCatalog(3, 5),

        FileCatalog(11, 1),
        FileCatalog(22, 2),
        FileCatalog(33, 3),
        FileCatalog(33, 4),
        FileCatalog(33, 5),
    ]

    def test_exercise1(self):
        assert exercise1(TestRK.catalogs, TestRK.files, TestRK.files_catalogs) == [
            ('AllGuys.mp4', 14.9, 'C:\\'), ('Atement.docx', 0.013, 'C:\\Users\\User\\')]

    def test_exercise2(self):
        assert exercise2(TestRK.catalogs, TestRK.files, TestRK.files_catalogs) == [
            ('C:\\Users\\', 1699.84), ('C:\\', 14.9), ('C:\\Users\\User\\', 0.013)]

    def test_exercise3(self):
        assert exercise3(TestRK.catalogs, TestRK.files, TestRK.files_catalogs) == [
            ('C:\\', ['AllGuys.mp4']), ('D:\\', ['AllGuys.mp4']), ('C:\\Users\\User\\', [
                'Atement.docx', 'Programm.zip', 'Statement.pdf']),
            ('D:\\Users\\User\\', ['Atement.docx',
             'Programm.zip', 'Statement.pdf']),
            ('C:\\Users\\', ['Valorant.mp4']), ('D:\\Users\\', ['Valorant.mp4'])]
