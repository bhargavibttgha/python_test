def in_autotests_we_trust(a, b):
    if a == b:
        print('a and b are equal, Test passed')
    else:
        print('a and b are not equal, Test failed')

in_autotests_we_trust(10, '10')

in_autotests_we_trust(0, False)
