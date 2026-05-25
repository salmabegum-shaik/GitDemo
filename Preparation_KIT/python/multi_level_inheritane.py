class grandfather:
    def __init__(self):
        print("Grandfather Constructor")
class father(grandfather):
    def __init__(self):
        super().__init__()
        print("Father Constructor")


class child(father):
    def __init__(self):
        super().__init__()
        print("Child Constructor")
c1 = child()