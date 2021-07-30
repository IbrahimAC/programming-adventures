#Implementing simple functions to test my knowledge

def m_converter(m):

    """ Returns the given miles into kilometers
        input: int
        output: int"""

    kmConvert = m * 1.6
    km = []
    km.append(kmConvert)

    return kmConvert

print(m_converter(12))


def km_converter():
    
    storeOld = m_converter(10)
    distance_increase = storeOld * 5

    return  distance_increase
print(km_converter())

def adding(num):

    x = km_converter() + num
    print(x)
    print(km_converter())
    
    return x

print(adding(10))