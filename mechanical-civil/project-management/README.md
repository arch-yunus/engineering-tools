# Proje Yönetimi ve Planlama Standartları

Büyük mühendislik projelerinde (inşaat, makine imalatı, altyapı projeleri) zaman planı, kaynak ataması ve maliyet kontrolü hayati önem taşır. Bu süreçleri yönetmek için endüstride yaygın olarak **MS Project** ve **Oracle Primavera P6** yazılımları kullanılır.

## Kritik Yol Metodu (Critical Path Method - CPM) nedir?

CPM, bir projedeki iş adımlarının (aktivitelerin) süreleri ve aralarındaki bağımlılıkları analiz ederek projenin **en kısa sürede nasıl tamamlanacağını** belirleyen matematiksel bir yöntemdir.

### Temel Kavramlar:
*   **ES (Early Start - Erken Başlangıç):** Bir görevin öncül görevleri bittiğinde başlayabileceği en erken zaman.
*   **EF (Early Finish - Erken Bitiş):** Bir görevin bitebileceği en erken zaman ($EF = ES + \text{Süre}$).
*   **LS (Late Start - Geç Başlangıç):** Proje bitiş tarihini geciktirmeden bir görevin başlayabileceği en geç zaman.
*   **LF (Late Finish - Geç Bitiş):** Bir görevin tamamlanabileceği en geç zaman ($LF = LS + \text{Süre}$).
*   **Slack / Float (Bolluk Süresi):** Bir görevin projeyi geciktirmeden ne kadar ertelenebileceğini gösterir ($Slack = LF - EF$ veya $LS - ES$).
*   **Kritik Yol (Critical Path):** Bolluğu (slack) sıfır olan görevler zinciridir. Bu yol üzerindeki herhangi bir gecikme, projenin toplam bitiş tarihini doğrudan geciktirir.

---

## Örnek Proje Ağı (Aktivite Şeması)

Aşağıdaki şemada aktivitelerin birbirlerine olan bağımlılıkları gösterilmiştir:

```mermaid
graph LR
    A[A: Temel Kazısı<br>5 Gün] --> B[B: Beton Dökümü<br>3 Gün]
    B --> C[C: Duvar Örme<br>4 Gün]
    B --> D[D: Elk Tesisatı<br>2 Gün]
    C --> E[E: Sıva & Boya<br>5 Gün]
    D --> E
    E --> F[F: Temizlik & Teslim<br>2 Gün]
```

Bu ağda kritik yol **A -> B -> C -> E -> F** şeklindedir ve toplam süre **19 gündür**. D görevi (Elektrik tesisatı) 2 günlük bir bolluğa (slack) sahiptir, bu yüzden projeyi aksatmadan 2 gün gecikebilir.

---

## Klasördeki Araç

*   **[cpm_calculator.py](file:///g:/Diğer bilgisayarlar/Dizüstü Bilgisayarım/github repolarım/engineering-tools/mechanical-civil/project-management/cpm_calculator.py):** Kullanıcının tanımladığı veya hazır yüklü şablondaki aktiviteleri alan, İleri Geçiş (Forward Pass) ve Geri Geçiş (Backward Pass) hesaplamalarıyla erken/geç başlangıç sürelerini, bollukları (slack) ve projenin kritik yolunu bulan gelişmiş bir proje planlama aracıdır.
