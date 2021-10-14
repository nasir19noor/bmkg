from bmkg import extract, show

if __name__ == '__main__':
    print("Last Earthquake Based on BMKG")
    result = extract()
    show(result)