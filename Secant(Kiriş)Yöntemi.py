def secant_method(func, x0, x1, tol=0.008, max_iter=100):
    """
    Secant (kiriş) yöntemi kullanarak bir fonksiyonun kökünü bulma.

    Parametreler:
    - func: Kökü bulunmaya çalışılan fonksiyon.
    - x0, x1: Başlangıç noktaları.
    - tol: Kabul edilebilir hata.
    - max_iter: Maksimum iterasyon sayısı.

    Döndürülenler:
    - root: Kökün yaklaşık değeri.
    - iterations: Yapılan iterasyon sayısı.
    """

    iterations = 0

    while abs(func(x1)) > tol and iterations < max_iter:
        x2 = x1 - (func(x1) * (x1 - x0)) / (func(x1) - func(x0))
        x0 = x1
        x1 = x2
        iterations += 1

    return x1, iterations

# Örnek bir fonksiyon
def ornek_fonksiyon(x):
    return x**7 -1000

# Secant yöntemini uygula
kok, iterasyonlar = secant_method(ornek_fonksiyon, x0=2, x1=3)

print("Yaklaşık kök:", kok)
print("Yapılan iterasyon sayısı:", iterasyonlar)
