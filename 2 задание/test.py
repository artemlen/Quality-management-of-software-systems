import pytest
import shutil
import os
import sys
import file_manager2 as fm

#Тест функции №1 просмотр всех файлов папки
@pytest.fixture()
def ls_fixture():
    fm.ls()
    return True
def test_ls(ls_fixture):
    assert ls_fixture == True



#Тест функции №2 создание пустых файлов с указанием имени;
@pytest.fixture()
def create_fixture():
    fm.create('ind.txt')
    return True
def test_create(create_fixture):
    assert create_fixture == True



#Тест функции №3 Запись текста в файл;
@pytest.fixture()
def rewrite_fixture():
    fm.rewrite('new.txt', 'privet')
    return True
def test_rewrite(rewrite_fixture):
    assert rewrite_fixture == True


#Тест функции №4  Дозапись текста в файл;
@pytest.fixture()
def add_fixture():
    fm.add('new.txt', ', privet snova')
    return True
def test_add(add_fixture):
    assert add_fixture == True



#Тест функции №5 Удаление файлов по имени
#(Негативное тестирование (проверка на ошибку))
@pytest.fixture()
def remove_fixture():
    try:
        #должен выдать ошибку
        fm.rmv('')
        return True
    except:
        return False
def test_remove(remove_fixture):
    assert remove_fixture == False



#Тест функции №6 Переименование файлов
@pytest.fixture()
def rename_fixture():
    fm.rename('ind.txt', 'new_ind.txt')
    return True
def test_rename(rename_fixture):
    assert rename_fixture == True


#Тест функции №7 Копирование файлов из одной папки в другую;
@pytest.fixture()
def copy_fixture():
    fm.copy('new_ind.txt', 'new_ind2.txt')
    return True
def test_copy(copy_fixture):
    assert copy_fixture == True



#Тест функции №8 Перемещение файлов;
@pytest.fixture()
def move_fixture():
    fm.move('new_ind2.txt', 'new_ind3.txt')
    return True
def test_move(move_fixture):
    assert move_fixture == True


#Тест функции №9 Создание папки;
@pytest.fixture()
def mkfold_fixture():
    fm.mkfold('newfold')
    return True
def test_mkfold(mkfold_fixture):
    assert mkfold_fixture == True



#Тест функции №10 Перемещение между папками (в пределах рабочей папки) - заход в папку по имени, выход на уровень вверх;
@pytest.fixture()
def cf_fixture():
    fm.cf('./newfold')
    return True
def test_cf(cf_fixture):
    assert cf_fixture == True



#Тест функции №11 Удаление папки;
@pytest.fixture()
def rmfold_fixture():
    fm.rmfold('newfold')
    return True
def test_rmfold(rmfold_fixture):
    assert rmfold_fixture == True



#Тест функции №12 Просмотр содержимого файла;
@pytest.fixture()
def cet_fixture():
    fm.cet('new.txt')
    return True
def test_cet(cet_fixture):
    assert cet_fixture == True



#Тест функции №13 просмотр текущего пути;
@pytest.fixture()
def pwd_fixture():
    fm.pwd()
    return True
def test_pwd(pwd_fixture):
    assert pwd_fixture == True


#Тест функции №14 определение длины текущего пути;
@pytest.fixture()
def beginerLength_fixture():
    fm.beginerLength()
    return True
def test_beginerLength(beginerLength_fixture):
    assert beginerLength_fixture == True

#Тест функции №15 функция вызывающая помощь;
@pytest.fixture()
def  help_fixture():
    fm.help()
    return True
def test_help(help_fixture):
    assert help_fixture == True









