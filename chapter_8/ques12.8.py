phone_num = input("Enter the phone number: ")
length = len(phone_num)
if length == 12 \
    and phone_num[3] == "-" \
    and phone_num[7] == "-" \
    and phone_num[:3].isdigit() \
    and phone_num[4:7].isdigit() \
    and phone_num[8:].isdigit() :
    print("Valid Phone Number")
else :
    print("Invalid Phone Number")