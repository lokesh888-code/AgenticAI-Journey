def show_methods(text):
    print("Lower:", text.lower())
    print("Upper:", text.upper())
    print("Title:", text.title())
    print("Strip:", text.strip())
    print("Replace spaces with hyphen:", text.replace(" ", "-"))
    print("Split words:", text.split())
    print("Find 'a':", text.find("a"))

# text = "  Hello, World!  "
# show_methods(text)