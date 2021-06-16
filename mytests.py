from window import *
import unittest
from datetime import timedelta



#1. Ustaw niepoprawną godzinę. Oczekiwany komunikat o błędzie. Ustawić godzinę na 12:34.

#2. Wrzucić 2zł, oczekiwany termin wyjazdu godzinę po aktualnym czasie. Dorzucić 4zł, oczekiwany termin wyjazdu dwie godziny po aktualnym czasie. Dorzuć 5zł, oczekiwany termin wyjazdu trzy godziny po aktualnym czasie. Dorzuć kolejne 5zł, oczekiwany termin wyjazdu wtedy godziny po aktualnym czasie.

#3. Wrzuć tyle pieniędzy , aby termin wyjazdu przeszedł na kolejny dzień, zgodnie z zasadami – wrzuć tyle monet aby termin wyjazdu był po godzinie 19:00, dorzuć monetę 5zł.

#4. Wrzuć tyle pieniędzy, aby termin wyjazdu przeszedł na kolejny tydzień, zgodnie z zasadami – wrzuć  tyle monet aby termin wyjazdu był w piątek o godzinie 19:00, a potem dorzucić monetę 5zł,

#5. Wrzucić 1zł, oczekiwany termin wyjazdu poł godziny po aktualnym czasie.

#6. Wrzucić 200 monet 1gr, oczekiwany termin wyjazdu godzinę po aktualnym czasie

#7. Wrzucić 201 monet 1gr, oczekiwana informacja o przepełnieniu parkomatu.

#8. Wciśnięcie „Zatwierdź” bez wrzucania monet – oczekiwana informacja o błędzie.

#9. Wciśnięcie „Zatwierdź” bez wpisania numeru rejestracyjnego – oczekiwana informacja o błędzie. Wciśniecie „Zatwierdź” po wpisaniu niepoprawnego numeru rejestracyjnego – oczekiwana informacja o błędzie



class Tests(unittest.TestCase):


    def test_number_one(self):

        Park = Parkomat()

        with self.assertRaises(ValueError) as exception:
            Park.actual_time_change('2000', '12', '14', 24, 34, 00)
            print(str(exception.value))


    def test_number_two(self):

        Park = Parkomat()

        Park.actual_time_change('2000', '12', '14', 10, 0, 0)
        Park.add_coins(2, 1)

        self.assertEqual(Park.get_actual_time() + timedelta(hours=1), Park.get_leaving_time())

        Park.add_coins(1, 4)

        self.assertEqual(Park.get_actual_time() + timedelta(hours=2), Park.get_leaving_time())

        Park.add_coins(1, 5)

        self.assertEqual(Park.get_actual_time() + timedelta(hours=3), Park.get_leaving_time())

        Park.add_coins(2, 2)
        Park.add_coins(1, 1)

        self.assertEqual(Park.get_actual_time() + timedelta(hours=4), Park.get_leaving_time())


    def test_number_three(self):

        Park = Parkomat()

        Park.actual_time_change('2000', '12', '14', 17, 10, 00)

        Park.add_coins(1, 2)
        Park.add_coins(1, 4)
        Park.add_coins(5, 1)
        self.assertEqual(Park.get_actual_time() + timedelta(hours=15), Park.get_leaving_time())


    def test_number_four(self):

        Park = Parkomat()

        Park.actual_time_change('2000', '12', '1', 17, 10, 00)  #(2000.12.1 - friday)

        Park.add_coins(1, 2)
        Park.add_coins(1, 4)
        Park.add_coins(5, 1)

        self.assertEqual(Park.get_actual_time() + timedelta(hours=63), Park.get_leaving_time())


    def test_number_five(self):

        Park = Parkomat()

        Park.actual_time_change('2000', '12', '14', 10, 00, 00)

        Park.add_coins(1, 1)

        self.assertEqual(Park.get_actual_time() + timedelta(minutes=30), Park.get_leaving_time())


    def test_number_six(self):

        Park = Parkomat()

        Park.actual_time_change('2000', '12', '14', 10, 00, 00)

        Park.add_coins(0.01,200)

        self.assertEqual(Park.get_actual_time() + timedelta(hours=1), Park.get_leaving_time())


    def test_number_seven(self):

        Park = Parkomat()

        Park.actual_time_change('2000', '12', '14', 10, 00, 00)

        with self.assertRaises(ParkomatOverflow) as exception:
            Park.add_coins(0.01, 201)
            print(str(exception.value))


    def test_number_eight(self):

        Park = Parkomat()

        with self.assertRaises(NoMoneyGiven) as exception:
            Park.confirm('kos 1234')
            print(str(exception.value))


    def test_number_nine(self):

        Park = Parkomat()

        Park.add_coins(1, 2)

        with self.assertRaises(WrongLicensePlate) as exception:
            Park.get_license_plate('')
            print(str(exception.value))



if __name__ == '__main__':
    unittest.main()