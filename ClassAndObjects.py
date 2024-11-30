class MyComplexNumber:
    # Constructor Methods
    def __init__(self, real = 0, img = 0):
        print ("MyComplexNumber constructor executing...")
        self.real_part = real
        self.img_part = img

        def displayComplex(self):
            print ("{0} + {1}j".format(self.real_part, self.img_part))