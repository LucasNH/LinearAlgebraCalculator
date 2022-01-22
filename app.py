import determinant
import rref


def main():
    print("Welcome to the state of the art Linear Algebra Calculator")
    get_computation()


def get_computation():
    user_input = \
        str(input("Type 'D/d' to compute a determinant," +
                  " or 'R/r' to row reduce: ")).upper()
    while user_input != 'D' and user_input != 'R':
        user_input = str(input("Type 'D/d' or 'R/r: ")).upper()

    if user_input == 'D':
        determinant.main()
    else:
        rref.main()

    cont = \
        str(input("\nWould you like to do another computation?" +
                  " (Y/n): ")).upper()
    while cont != 'Y' and cont != 'N':
        cont = \
            str(input("Would you like to do another computation?" +
                      " (Y/n): ")).upper()
    if cont == 'Y':
        get_computation()


if __name__ == "__main__":
    main()
