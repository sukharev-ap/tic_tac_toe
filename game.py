# game.py

from gameparts import Board
from gameparts.exceptions import CellOccupiedError, FieldIndexError


def save_results(result):
    with open('result.txt', 'a') as file:
        # Открываем файл в режиме добавления
        file.write(result + '\n')


def main():
    game = Board()
    # Первыми ходят крестики.
    current_player = 'X'
    # Эта флаговая переменная. По умолчанию игра запущена и продолжается.
    running = True
    game.display()
    
    # Тут запускается основной цикл игры
    while running:     
        print(f'Ход делают {current_player}')
        # Запускается бесконечный цикл
        while True:
        # в этом блоке содержаться операции, которые могут вызвать исключения
            try:
                # Тут пользователь вводит координаты ячейки
                row = int(input('Введите номер строки: '))
                if row < 0 or row >= game.field_size:
                    #выбросить искллючние FieldIndexError.
                    raise FieldIndexError
                column = int(input('Введите номер столбца: '))
                if column < 0 or column >= game.field_size:
                    #выбросить искллючние FieldIndexError.
                    raise 
                if game.board[row][column] != ' ':
                    # Выбрасываем исключение
                    raise CellOccupiedError
            # При вводе числа за диапозоном поля
            except FieldIndexError:
                # Вывод сообщения
                print(
                    'Значение должно быть не отрицательным и меньше'
                    f' {game.field_size}'
                )
                print('Пожалуйста, введите значение для строки и столбца заново')
                # И цикл начинает свою работу сначала,
                # предстовляя пользователю еще одну попытку ввести данные.
                continue
            # Обработка исключений.
            # При вводе строки
            except ValueError:
                print('Буквы вводить нельзя. Только числа.')
                print('Пожалуйста, введите значения для строки и столбца заново.')
                # И цикл начинает свою работу сначала,
                # предстовляя пользователю еще одну попытку ввести данные.
                continue
            
            except CellOccupiedError:
                print('Ячейка занята')
                print('Введите значение для строки и столбца заново.')
                
            # При прочих ошибках
            except Exception as e:
                print(f'Возникла ошибка: {e}')


            else:
                # ...значит, введённые значения прошли все проверки
                # и могут быть использованы в дальнейшем.
                # Цикл прерывается.
                break
        
        # Теперь для установки значения на поле само значение берётся
        # из переменной current_player.
        game.make_move(row, column, current_player)
        print('Ход сделан!')
        game.display()
        
        if game.check_win(current_player):
            result = (f'Победили {current_player}!')
            print(result)
            save_results(result)
            running = False
        elif game.is_board_full():
            result = ('Ничья!')
            print(result)
            save_results(result)
            running = False           
        # Тернарный оператор, через который реализована смена игроков.
        # Если current_player равен X, то новым значением бу
        # иначе — новым значением будет X.
        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == '__main__':
    main() 