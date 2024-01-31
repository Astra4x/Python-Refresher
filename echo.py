#echo.py

def echo(text: str, repetitions: int = 3) -> str:
    """imitate a real-world echo"""
    if repetitions <= 0:
        return "."
    if repetitions > len(text):
        repetitions = len(text)
    return text[-repetitions:] + "\n" + echo(text, repetitions-1)

if __name__ == "__main__":
    text = input("yell something at a mountain. ")
    print(echo(text))