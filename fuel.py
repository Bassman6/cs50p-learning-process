def main():
    try:
        user_input = input("fraction")
        print(gauge(convert(user_input)))
    except ValueError:
        pass

def convert(fraction):
    x_str, y_str = fraction.split("/")
    x, y = int(x_str), int(y_str)
    if x > y :
        return ValueError
    if y == "0":
        return ZeroDivisionError
    else:
        return x/y


def gauge(percentage):
    
    percentage = round((percentage) * 100)
    if percentage > 1 and percentage < 99:
        return(f"{percentage}%")
    elif percentage <= 1:
        return("E")
    else:
        return("F")


if __name__ == "__main__":
    main()