car = [1, 1, 1, 1, 0, 1, 0]
truck = [1, 1, 0, 1, 1, 1, 0]
specmachine = [1, 1, 0, 1, 0, 1, 1]


def test(line):
    try:
        list = line.split(';')
        if list[0] == 'car':
            for param in range(0, len(list)):
                if car[param] == 1 and list[param] == '':
                    return False
                elif car[param] == 0 and list[param] != '' and list[param] != '\n':
                    return False
            try:
                x = list[3].split('.')
            except:
                return False
            return 'car'

        elif list[0] == 'truck':
            for param in range(0, len(list)):
                if param != 4:
                    if truck[param] == 1 and list[param] == '':
                        return False
                    elif truck[param] == 0 and list[param] != '' and list[param] != '\n':
                        return False
            try:
                x = list[3].split('.')
            except:
                return False
            return 'truck'

        elif list[0] == 'spec_machine':
            for param in range(0, len(list)):
                if specmachine[param] == 1 and list[param] == '':
                    return False
                elif specmachine[param] == 0 and list[param] != '' and list[param] != '\n':
                    return False
            try:
                x = list[3].split('.')[1]
            except:
                return False
            return 'spec_machine'
    except:
        return False


class Carbase:
    def __init__(self, car_type, brand, photo_le_name, carrying):
        self.car_type = car_type
        self.brand = brand
        self.photo_le_name = photo_le_name
        self.carrying = float(carrying)

    def get_photo_le_ext(self):
        ph = self.photo_le_name.split('.')[1]
        return ph


class Car(Carbase):
    def __init__(self, car_type, brand, passenger_seats_count, photo_le_name, carrying):
        Carbase.__init__(self, car_type, brand, photo_le_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)


class Truck(Carbase):
    def __init__(self, car_type, brand, photo_le_name, whl, carrying):
        Carbase.__init__(self, car_type, brand, photo_le_name, carrying)
        if whl == '':
            self.body_width = float('0')
            self.body_height = float('0')
            self.body_length = float('0')
        else:
            whl_list = whl.split('x')
            self.body_width = float(whl_list[0])
            self.body_height = float(whl_list[1])
            self.body_length = float(whl_list[2])

    def get_body_volume(self):
        return self.body_width * self.body_height * self.body_length


class Specmachine(Carbase):
    def __init__(self, car_type, brand, photo_le_name, carrying, extra):
        Carbase.__init__(self, car_type, brand, photo_le_name, carrying)
        listextra = list(extra)
        listextra.pop()
        self.extra = ''.join(listextra)


def get_car_list(filename):
    car_list = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            try:
                result = test(line)
                if result == 'car':
                    list = line.split(';')
                    car_type = list[0]
                    brand = list[1]
                    passenger_seats_count = list[2]
                    photo_le_name = list[3]
                    carrying = list[5]
                    car_list.append(Car(car_type, brand, passenger_seats_count, photo_le_name, carrying))

                elif result == 'truck':
                    list = line.split(';')
                    car_type = list[0]
                    brand = list[1]
                    photo_le_name = list[3]
                    whl = list[4]
                    carrying = list[5]
                    car_list.append(Truck(car_type, brand, photo_le_name, whl, carrying))

                elif result == 'spec_machine':
                    list = line.split(';')
                    car_type = list[0]
                    brand = list[1]
                    photo_le_name = list[3]
                    carrying = list[5]
                    extra = list[6]
                    car_list.append(Specmachine(car_type, brand, photo_le_name, carrying, extra))
            except:
                continue
    return car_list


def main():
    print(get_car_list('solution.txt'))


if __name__ == '__main__':
    main()
