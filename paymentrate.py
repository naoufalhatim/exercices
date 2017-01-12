def computepay():
    try: 
        hours = raw_input("Enter Hours")
        h = float(hours)
        rate= raw_input("Enter Rate")
        r = float(rate)
    except:
        print "Error, please enter a numeric input"
        quit()
    if h >= 40:
        mypay = 40 * r + (h - 40) * r * 1.5

        return mypay
    else:
        theirpay = h * r
        return theirpay
print computepay()
