def exchange_rate(USD):
    USD = input('Enter a value in USD to be converted to EUR: ')
    EUR=1.1 
    error_message = 'Error: your input should be a positive number'
    
    try:
        USD = float(USD)
        if USD < 0:
            return error_message
        converted_value = USD / EUR 
        print("Your input is equal to {:.2f} EUR". format(converted_value))
        return converted_value
    except ValueError:
        return error_message     
    
    