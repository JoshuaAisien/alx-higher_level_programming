import dis
try:
    import hidden_4
except Exception as e:
    print(f"unable to import hidden_4 because of {e}")
    exit()

if __name__ == "__main__":
    names = []
    for name in dir(hidden_4):
        if not name.startswith('__'):
            names.append(name)

    for i in names:
        print(i)
