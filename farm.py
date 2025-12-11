def print_that_its_cool():
	print("WOW! SUPER!")

def print_that_its_weird():
	print("Uhm. OK. Weird.")

ANIMAL = {
	"kota": print_that_its_cool,
	"psa": print_that_its_cool,
	"wija": print_that_its_weird
}

animal = input("Jakie masz zwierzę?")

# if animal in ANIMAL:
# 	ANIMAL[animal]()
# else:
# 	print("Nie ma czegoś takiego.")


try:
	ANIMAL[animal]()
except KeyError:
	print("Nie ma czegoś takiego")
