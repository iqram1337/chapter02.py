full_name = lambda fn, ln: fn.strip('321').title() + " " + ln.strip('312').title()
x = full_name("123iqram", "123HARIS")
print(x)