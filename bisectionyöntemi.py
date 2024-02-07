# encoding:utf-8
def bisection_method(func, a, b, tol=1e-6, max_iter=100):
    """
    [a, b] aralığında bir fonksiyonun kökünü bulmak için Bisection yöntemi.

    Parametreler:
    - func: Kökü bulunmaya çalışılan fonksiyon.
    - a, b: [a, b] aralığındaki kökü arama başlangıç noktaları.
    - tol: Kabul edilebilir hata.
    - max_iter: Maksimum iterasyon sayısı.

    Döndürülenler:
    - kok: Kökün yaklaşık değeri.
    - iterations: Yapılan iterasyon sayısı.
    """
 
    if func(a) * func(b) > 0:
        raise ValueError("Fonksiyon, aralık uç noktalarında farklı işaretlere sahip olmalıdır.")

    # Başlangıç değerleri
    x0 = a
    x1 = b
    iterations = 0

    while (b - a) / 2 > tol and iterations < max_iter:
        orta_nokta = (a + b) / 2

        if func(orta_nokta) == 0:
            return orta_nokta, iterations
        elif func(orta_nokta) * func(a) < 0:
            b = orta_nokta
        else:
            a = orta_nokta

        iterations += 1

    kok = (a + b) / 2
    return kok, iterations

# Örnek bir fonksiyon
def ornek_fonksiyon(x):
    return x**3 - 6*x**2 + 11*x - 6

# Bisection yöntemini uygula
kok, iterasyonlar = bisection_method(ornek_fonksiyon, 0, 3)

print("Yaklaşık kök:", kok)
print("Yapılan iterasyon sayısı:", iterasyonlar)
