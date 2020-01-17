def arabic_to_roman(num):
   arabic_numbers = (1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1)
   roman_numerals = ('M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')
    
   romanDigit = ""
   k= 0
   while num > 0:
        for _ in range(num//arabic_numbers[k]): #_ = no iterable variable/ range of num dividing by arabic numbers at position k
            romanDigit += roman_numerals[k]     #adding roman numeral character at position k corresponding with arabic num at position k
            num -= arabic_numbers[k]            #subtract arabic numbers at k from num
           # print(num, romanDigit, arabic_numbers[k])
        k+= 1                                   #increment position k by 1
   return romanDigit

num_input = int(input("Enter a number~"))
print(arabic_to_roman(num_input))