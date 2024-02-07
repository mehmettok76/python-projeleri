def newton_raphson_method(func, deriv_func, ilk_deger, tol=0.05, max_iter=100):
    """
    Newton-Raphson yöntemi kullanarak bir fonksiyonun kökünü bulma.

    Parametreler:
    - func: Kökü bulunmaya çalışılan fonksiyon.
    - deriv_func: Fonksiyonun türevidir.
    - ilk_deger: Başlangıç tahmini.
    - tol: Kabul edilebilir hata.
    - max_iter: Maksimum iterasyon sayısı.
    Döndürülenler:
    - root: Kökün yaklaşık değeri.
    - iterations: Yapılan iterasyon sayısı.
    """
    x0 = ilk_deger
    iterations = 0

    while abs(func(x0)) > tol and iterations < max_iter:
        x1 = x0 - func(x0) / deriv_func(x0)
        x0 = x1
        iterations += 1

    return x1, iterations

# Örnek bir fonksiyon
def ornek_fonksiyon(x):
    return x**4 - 3*x**3 + 6*x**2 - 16

# Fonksiyonun türevi
def turev_fonksiyonu(x):
    return 4*x**3 - 9*x**2 + 12*x

# Newton-Raphson yöntemini uygula
kok, iterasyonlar = newton_raphson_method(ornek_fonksiyon, turev_fonksiyonu, ilk_deger=4)

print("Yaklaşık kök:", kok)
print("Yapılan iterasyon sayısı:", iterasyonlar)
