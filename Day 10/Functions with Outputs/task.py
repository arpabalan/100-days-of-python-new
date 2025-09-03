def format_name(f_name, l_name):
    if f_name == "" and l_name == "":
        return "You didnt provide a input"
    """
    :return function
    """
    full_name = str(f_name.title()) + ' ' + str(l_name.title())
    return full_name

your_name = format_name("", "")
print(your_name)

