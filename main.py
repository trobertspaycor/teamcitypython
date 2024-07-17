def main(num):
    result = num ** 2

    with open("output.txt", "w") as file:
            file.write(str(result))


if __name__ == "__main__":
    main(3)
