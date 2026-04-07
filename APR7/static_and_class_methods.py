class Example:
    name="Tarak"
    @staticmethod
    def add(a,b):
        return a+b
    @classmethod
    def sample(cls):
        return cls.name
    def addition(self,a,b):
        self.a=a
        self.b=b
        return self.a+self.b
    
example=Example()
print(example.add(2,3))
print(Example.sample())
print(example.addition(10,20))

    