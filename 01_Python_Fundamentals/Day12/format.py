def show_formatting(name, text):
    """
    Show f-string formatting examples.
    """
    print("\n--- String Formatting Demo ---")
    print(f"User name: {name}")
    print(f"Original text: {text!r}")
    print(f"Characters: {len(text)}")
    print(f"Words: {len(text.split())}")
    print(f"First 10 chars (padded): {text[:10]:>15}")


if __name__ == "__main__":
    user = "Lokesh"
    sample = "Text processing with f-strings"
    show_formatting(user, sample)