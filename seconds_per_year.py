# Use python to determine the seconds in a year

MINUTE = 60
HOUR = 60
DAY = 24
YEAR = 365

def main():
    s_py = YEAR*DAY*HOUR*MINUTE
    print("There are" , s_py, "in a year!")

if __name__ == "__main__":
    main()