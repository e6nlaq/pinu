from deep_translator import GoogleTranslator

if __name__ == "__main__":
    print(GoogleTranslator().translate_file("./test/ja.txt"))
