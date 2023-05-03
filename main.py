def month_has_31_days(month:int) -> bool:
    return (month % 2 != 0 and month <= 7) or (month >= 8 and month % 2 == 0)

def date_calculator(date:str, days:int) -> str:
    # Splitting values and converting to int
    d, m, y = map(int, date.split("/"))
    for day in range(days):
        if (d >= 30):
            # Months with 31 days
            if month_has_31_days(m):
                if d == 30:
                    d+=1
                    continue
                if m == 12:
                    m = 0
                    y += 1
            m += 1
            d = 0
        # February workaround
        elif (d >= 28) and (m == 2):
            if(y % 4 != 0) or (d == 29):
                m += 1
                d = 0
        d+=1
    return f"{d}/{m}/{y}"

if __name__ == "__main__":
    date = "01/01/2023"
    d = date_calculator(date, 597)
    print(d)
