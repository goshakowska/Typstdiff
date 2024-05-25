import airquality
# jeżeli chcemy wywołać ten skrypt z argumentami
import sys
from random import choice
from matplotlib import pyplot as plt  # pip install matplotlib; aby za każdym razem nie pisać pyplot to zapisuję jako co chcę go importować

# biblioteka, która służy do tworzenia wykresów

# wykres może różnie wyglądać na różnych komputerach - wynika to z tego, że są używane różne backendy
# import matplotlib
# plt.use('Qt5Agg')

# przekazywanie danych do pythona - korzystamy z biblioteki
import argparse  # możemy stworzyć parsera linii poleceń


def find_station(id):
    for station in airquality.get_stations():
        if station.id() == id:
            return station


def list_stations(args):
    pattern = args.list_stations
    all_stations = airquality.get_stations()
    for station in all_stations:
        if pattern == ' ' or pattern in station.name():  # jeżeli wzorzec jest w nazwie tej stacji
            print(f'{station.id()}\t{station}')


def list_sensors(args):
    station_id = float(args.list_sensors)
    station = find_station(station_id)
    if station:
        for sensor in station.sensors():
            print(f'{sensor.id()}\t{sensor.name()}')
# action=store_true - zapisz prawdę w momencie, kiedy pojawi się ten argument
# argumenty wywołania programu otrzymujemy poprzez sys.argv
def main(arguments):  # funkcja main będzie zawierała mój właściwy skrypt
    parser = argparse.ArgumentParser()
    # temu parserowi podajemy wzorce, jakie on ma obsługiwać i na końcu będziemy musieli przeparsować to, co użytkownik podał - zostanie to umieszczone w obiekcie, z którego będziemy czytać dane
    parser.add_argument('--save')                   # ustawiamy tutaj dobrze znaną wartość const = " "
    parser.add_argument('--list-stations', nargs='?', const=' ')  # argument pozycyjny, główny argument; nargs=? czyli 0 albo 1
    parser.add_argument('--list-sensors')  # zakładam, że ta wartość zawsze będzie

    args = parser.parse_args(arguments[1:])  # pierwszym element naszej listy będzie nazwa naszego programu - chcemy to pominąć; podajemy od pierwszego w górę

    # przygotowuję uruchomienie tej funkcji
    # jeżeli wartość list_stations istnieje w args to:
    if args.list_stations:
        list_stations(args)  # jeżeli ta opcja była aktywna, to ja mówię, że nic więcej nie chcę robić i kończę funkcję main
        return
    # gdybym tutaj podała identyfikator 0 (dla sensora), to wtedy ten if by nie zadziałał, dlatego piszę is not None
    if args.list_sensors is not None:  # nie jest Nonem
        list_sensors(args)

    all_stations = [station for station in airquality.get_stations() if station.city_name() =='Warszawa']
    station = choice(all_stations)
    all_sensors = station.sensors()
    for sensor in all_sensors:
        if sensor.code() == 'CO':  # dwutlenek węgla "spłaszczał" nam wykresy - możemy go pominąć w iteracji pętli
            continue  # 1.13 minuta
        readings = sensor.readings()
        # if readings:  # jeżeli są jakiekolwiek odczyty
        #     print(readings[0])
        # wybieram, jakie wartości chcę mieć na osi x, jakie na osi y
        keys = [reading.date for reading in readings]  # klucze (x)  # date.strftime - możemy uzyskać jakiś rządany przez nas format daty 18.12.2020
        values = [reading.value for reading in readings]  # wartości (y)  # markersize - domyślnie jest 6
        plt.plot(keys, values, 'o-', label=sensor.name(), markersize=3)  # mówię, że chce mieć wykres zależności kluczy od tych wartości, jeżeli chcemy punkty pomiaru
    plt.legend()
    plt.title(label=station.name())  # tytuł wykresu, label - tytuł wykresu, który chcemy nadać
    plt.xticks(rotation=30, fontsize='xx-small', horizontalalignment='right')  # zmienia opis osi x - legenda nie jest podana poziomo, tylko pionowo; fontsize - albo podajemy wartości, albo hasła, które są wcześniej ustalone; wyrównanie do prawej
    plt.yticks(verticalalignment="left")
    # pobranie wykresu do zmiennej figure, gcf - get current figure:
    figure = plt.gcf()
    plt.show()  # po pokazaniu wykresu python czyści mi wykres, gdybyśmy zapisali po pokazaniu to byłby ro pusty plik
    # teraz jak mamy figure to niezależnie czy mamy pierwsze show czy save to to i tak zadziała
    if args.save:
        figure.savefig(args.save, format='pdf')  # podaję ścieżkę do pliku


if __name__ == "__main__":  # jeżeli nazwa tego skryptu jest "__main__", tak python nas uruchomi to ma się uruchomić funkcja main
    main(sys.argv)

# argv - tablica argumentów


#1h40 minuta


# import sys
# import argparse

# from FileConverter import FileConverter
# from iterating import Comparison

# # Define the possible customizations
# style_types = {
#     'h': 'highlight',
#     'f': 'font'
# }

# colors = {
#     'r': 'red',
#     'g': 'green',
#     'b': 'blue',
#     'y': 'yellow',
#     't': 'teal'
# }

# def parse_style_param(param):
#     """Parse style parameters to handle both highlight and font colors."""
#     if not param:
#         return None
    
#     style = {'highlight': None, 'font': None}
#     i = 0
#     while i < len(param):
#         if param[i] in style_types:
#             style_type = style_types[param[i]]
#             if i + 1 < len(param) and param[i + 1] in colors:
#                 color = colors[param[i + 1]]
#                 style[style_type] = color
#                 i += 2
#             else:
#                 raise ValueError(f"Invalid color after '{param[i]}': {param}")
#         else:
#             raise ValueError(f"Invalid style parameter: {param[i]}")
    
#     style_string = ', '.join([f"{key}({value})" for key, value in style.items() if value])
#     return style_string if style_string else None

# def main(arguments):
#     parser = argparse.ArgumentParser(
#         prog='TypstDiff',
#         description="Mark differences between two Typst files.",
#         epilog="Copyright (c) 2024, Dominika Ferfecka, Sara Fojt, Małgorzata Kozłowska"
#     )

#     parser.add_argument('old_version', type=str, help="Path to old version of Typst file")
#     parser.add_argument('new_version', type=str, help="Path to new version of Typst file")
#     parser.add_argument('diff_output_file', type=str, help="Path to output diff file")
    
#     group = parser.add_mutually_exclusive_group()
#     group.add_argument('-add', '--only-inserted', help="Only show added changes to new Typst file", action='store_true')
#     group.add_argument('-del', '--only-deleted', help="Only show deleted changes to new Typst file", action='store_true')
    
#     parser.add_argument('-si', '--style-inserted', help="Set custom style to added changes", type=str, default='')
#     parser.add_argument('-sd', '--style-deleted', help="Set custom style to deleted changes", type=str, default='')

#     args = parser.parse_args(arguments)
    
#     style_inserted = parse_style_param(args.style_inserted)
#     style_deleted = parse_style_param(args.style_deleted)

#     # Placeholder for the actual file conversion and comparison logic
#     file_converter = FileConverter()
#     file_converter.convert_with_pandoc('typst', 'json', args.new_version, 'new.json')
#     file_converter.convert_with_pandoc('typst', 'json', args.old_version, 'old.json')
    
#     comparison = Comparison("new.json", "old.json")
#     comparison.apply_diffs_recursive(comparison.diffs, comparison.parsed_new_file, None, comparison.parsed_old_file)

#     # Apply styles if any
#     if style_inserted:
#         comparison.set_style_inserted(style_inserted)
#     if style_deleted:
#         comparison.set_style_deleted(style_deleted)

#     # Handle the optional parameters
#     if args.only_inserted:
#         comparison.show_only_inserted()
#     if args.only_deleted:
#         comparison.show_only_deleted()

#     # Output the final diff file
#     comparison.write_diff_output(args.diff_output_file)

# if __name__ == "__main__":
#     main(sys.argv[1:])

