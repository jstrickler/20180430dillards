#!/usr/bin/env python


nums = [24.3, 13.9, 'abc', 85.1, 27, 4.5, 0, 9.2804]

value = 100


for num in nums:
    try:
        result = value / num

    except ZeroDivisionError as err:
        print(err)

    except TypeError as err:
        print(err)

    except Exception as err:
        print(err)

    else:
        print(result)

    finally:
        print("Hoo-Rawwww")
