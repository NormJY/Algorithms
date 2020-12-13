def second_index(text: str, symbol: str) -> [int, None]:
    if text.count(symbol) < 2:
        return None
    
    first = text.find(symbol)

    return text.find(symbol, first + 1)