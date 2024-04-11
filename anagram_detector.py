def is_anagrams(str1, str2):
    # Tworzenie zbiorów z liter w obu stringach
    set1 = set(str1.lower())
    set2 = set(str2.lower())
    
    # Porównanie zbiorów i zwrócenie wartości logicznej
    return set1 == set2

# Przykłady użycia
print(is_anagrams("foefet", "toffee"))  # True
print(is_anagrams("Buckethead", "DeathCubeK"))  # True
print(is_anagrams("AbC", "acB"))  # True
print(is_anagrams("hello", "world"))  # False