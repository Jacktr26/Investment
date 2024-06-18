investment = int(input("How much would you like to invest?"))

average = [
    ["Apple", 173.72, 12.57],
    ["Microsoft", 417.32, 14.23],
    ["Amazon", 174.48, 81.32],
    ["Google", 148.48, 46.66],
    ["Meta", 496.98, 147.99]
]

expensive = [
    ["Berkshire Hathaway", 617880, 35.67],
    ["NVR", 6466, 47.1],
    ["Seaboard", 3768, -16.26],
    ["Booking Holdings", 3110, 44.6],
    ["Autozone", 2528, 36.16]
]

cheap = [
    ["Alok Industries Ltd", 2.22, 130.2],
    ["Inventure Growth Ltd", 0.20, 39.39],
    ["Ajooni Biotech ", 4.85, 61.33],
    ["Nyssa Corporation Ltd", 0.30, 84.62],
    ["Advik Capital Services Ltd", 0.51, -18.75]
]

def calculate_returns(stock_info, investment_amount):
    returns = {}
    for stock in stock_info:
        stock_name = stock[0]
        stock_price = stock[1]
        ytd_percentage = stock[2]
        num_stocks = investment_amount / stock_price
        money_returned = num_stocks * (stock_price * (1 + (ytd_percentage / 100)) - stock_price)
        returns[stock_name] = money_returned
    return returns

def suggest_investment():
    if investment > 100000:
        print("Try investing in any of these companies:", '\n', expensive[0][0], '\n', expensive[1][0], '\n', expensive[2][0])
    elif investment > 100:
        print("Try investing in any of these companies:", '\n', average, '\n', expensive[0][0], '\n', expensive[1][0])
    elif investment < 100:
        print("Try investing in any of these companies:", '\n', cheap, '\n', expensive[0][0], '\n', expensive[1][0])

def money_decider():
    returns = calculate_returns(expensive, investment)
    for stock, profit in returns.items():
        print("If you invested in", stock, "last year, you would have made a profit of $", round(profit, 2))

suggest_investment()
money_decider()
