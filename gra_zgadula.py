import random

print("Witaj w grze polegającej na odgadnięciu liczby z wybranego zakresu liczb. \nPowodzenia!")
random_maxi = int(input("Podaj z ilu liczb chcesz losować: "))
answer = random.randint(0, random_maxi)

print("Zgaduj liczbę z zakresu 0-{}: ".format(random_maxi), end='')
zgaduj = -99
ktory_raz = 0

while zgaduj != answer:
	zgaduj = int(input())
	if zgaduj < answer:
		print("Pudło, celuj wyżej: ", end='')
	elif zgaduj > answer:
		print("Pudło, celuj niżej: ", end='')
	ktory_raz += 1
	if zgaduj == answer:
		if ktory_raz == 1:
			print("- " * 20 + "\nZa pierwszym podejściem! Farciarz!")
		else:
			print("- " * 20 + "\nZgadłeś za {0} razem, szukana liczba to {1}.".format(ktory_raz, answer))
