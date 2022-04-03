import pandas

data = pandas.read_csv('nato_phonetic_alphabet.csv')

nato_data = {row.letter : row.code for (index,row) in data.iterrows()}


def generate_word():
    user_ip = input("Enter code : ").upper()
    try:
        op_list = [nato_data[code] for code in user_ip]
    except KeyError:
        print(f"Sorry only alphabats allowed")
        generate_word()
    else:
        print(op_list)

generate_word()