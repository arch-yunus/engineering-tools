import collections
import math

class Task:
    def __init__(self, name, o, m, p, predecessors=None):
        self.name = name
        self.o = o
        self.m = m
        self.p = p
        # PERT Expected Time: te = (o + 4m + p) / 6
        self.duration = (o + 4.0 * m + p) / 6.0
        # PERT Variance: var = ((p - o) / 6)^2
        self.variance = ((p - o) / 6.0) ** 2
        self.predecessors = predecessors if predecessors else []
        self.successors = []
        self.es = 0.0
        self.ef = 0.0
        self.ls = 0.0
        self.lf = 0.0
        self.slack = 0.0

def solve_cpm(tasks_dict):
    # Reset successors to prevent accumulative bugs
    for task in tasks_dict.values():
        task.successors = []
        
    # Establish successors
    for t_name, task in tasks_dict.items():
        for pred in task.predecessors:
            if pred in tasks_dict:
                tasks_dict[pred].successors.append(t_name)

    # Topological Sort to evaluate forward pass correctly
    in_degree = {name: len(task.predecessors) for name, task in tasks_dict.items()}
    queue = collections.deque([name for name, deg in in_degree.items() if deg == 0])
    topo_order = []
    
    while queue:
        u = queue.popleft()
        topo_order.append(u)
        for v in tasks_dict[u].successors:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
                
    if len(topo_order) != len(tasks_dict):
        return None, "Projede döngüsel bağımlılık (circular dependency) tespit edildi!"

    # Forward Pass: Calculate ES & EF
    for u in topo_order:
        task = tasks_dict[u]
        if not task.predecessors:
            task.es = 0.0
        else:
            task.es = max(tasks_dict[pred].ef for pred in task.predecessors)
        task.ef = task.es + task.duration

    # Project duration is max EF of all tasks
    project_duration = max(task.ef for task in tasks_dict.values())

    # Backward Pass: Calculate LS & LF
    for u in reversed(topo_order):
        task = tasks_dict[u]
        if not task.successors:
            task.lf = project_duration
        else:
            task.lf = min(tasks_dict[succ].ls for succ in task.successors)
        task.ls = task.lf - task.duration
        task.slack = task.lf - task.ef

    return topo_order, project_duration

def print_pert_results(tasks_dict, topo_order, duration):
    print("\n" + "=" * 95)
    print(f"               PERT & KRİTİK YOL METODU (CPM) ANALİZ SONUÇLARI")
    print("=" * 95)
    print(f"Beklenen Toplam Proje Süresi (Te): {duration:.2f} gün/birim")
    
    # Calculate critical path and sum variance
    critical_path = [u for u in topo_order if abs(tasks_dict[u].slack) < 0.0001]
    cp_variance = sum(tasks_dict[u].variance for u in critical_path)
    cp_std_dev = math.sqrt(cp_variance)
    
    print(f"Kritik Yol Varyansı           (Var): {cp_variance:.4f}")
    print(f"Kritik Yol Standart Sapması   (Sd) : {cp_std_dev:.4f}")
    
    # Simple probability examples (90% and 95% confidence intervals)
    print(f"Projenin Bitme İhtimali Aralığı:")
    print(f"  - %68 İhtimalle Bitiş Süresi : {duration - cp_std_dev:.2f} ile {duration + cp_std_dev:.2f} gün arası")
    print(f"  - %95 İhtimalle Bitiş Süresi : {duration - 1.96 * cp_std_dev:.2f} ile {duration + 1.96 * cp_std_dev:.2f} gün arası")
    print("-" * 95)
    print(f"{'Görev':<8} | {'(o)':<4} | {'(m)':<4} | {'(p)':<4} | {'Bekl(te)':<8} | {'ES':<6} | {'EF':<6} | {'LS':<6} | {'LF':<6} | {'Slack':<6} | {'Kritik?'}")
    print("-" * 95)
    for name in topo_order:
        t = tasks_dict[name]
        is_crit = "EVET" if abs(t.slack) < 0.0001 else "HAYIR"
        print(f"{t.name:<8} | {t.o:<4} | {t.m:<4} | {t.p:<4} | {t.duration:8.2f} | {t.es:6.1f} | {t.ef:6.1f} | {t.ls:6.1f} | {t.lf:6.1f} | {t.slack:6.1f} | {is_crit}")
    print("-" * 95)
    crit_path_str = " -> ".join(critical_path)
    print(f"Kritik Yol: {crit_path_str}")
    print("=" * 95)

def run_preset_demo():
    print("\n[BİLGİ] Bir inşaat projesi şablonu (PERT Parametreleriyle) yükleniyor...")
    # Standard engineering / construction project example:
    # Arguments: name, optimistic, most_likely, pessimistic, predecessors
    # A: Temel kazısı (o:3, m:5, p:7)
    # B: Beton dökümü (o:2, m:3, p:5, A'ya bağlı)
    # C: Duvar örme (o:3, m:4, p:6, B'ye bağlı)
    # D: Elektrik tesisatı (o:1, m:2, p:4, B'ye bağlı)
    # E: Sıva ve boya (o:3, m:5, p:8, C ve D'ye bağlı)
    # F: Temizlik ve Teslim (o:1, m:2, p:3, E'ye bağlı)
    tasks = {
        "A": Task("A", 3, 5, 7),
        "B": Task("B", 2, 3, 5, ["A"]),
        "C": Task("C", 3, 4, 6, ["B"]),
        "D": Task("D", 1, 2, 4, ["B"]),
        "E": Task("E", 3, 5, 8, ["C", "D"]),
        "F": Task("F", 1, 2, 3, ["E"])
    }
    
    order, duration = solve_cpm(tasks)
    if order:
        print_pert_results(tasks, order, duration)
    else:
        print(f"\n[HATA] {duration}")

def run_custom_pert():
    print("\n--- Özel PERT & CPM Projesi Tanımlama ---")
    try:
        num_tasks = int(input("Projedeki görev sayısını girin: "))
        tasks = {}
        for i in range(num_tasks):
            print(f"\n{i+1}. Görev Tanımı:")
            name = input("Görev Kodu/Adı (Örn: A, T1): ").strip()
            if not name:
                print("İsim boş geçilemez.")
                return
            
            calc_type = input("Süre Tipi - Tek bir sabit süre mi, yoksa PERT (o,m,p) mi? (S/P): ").strip().upper()
            if calc_type == 'P':
                o = float(input("  İyimser Süre (Optimistic - o): "))
                m = float(input("  En Muhtemel Süre (Most Likely - m): "))
                p = float(input("  Kötümser Süre (Pessimistic - p): "))
            else:
                dur = float(input("  Görevin Süresi (Gün/Birim): "))
                o = m = p = dur
                
            pred_str = input(f"Öncül Görevler (Aralarında virgül koyun, örn: A,B - Öncül yoksa boş geçin): ").strip()
            
            predecessors = []
            if pred_str:
                predecessors = [p.strip() for p in pred_str.split(",")]
                
            tasks[name] = Task(name, o, m, p, predecessors)
            
        order, duration = solve_cpm(tasks)
        if order:
            print_pert_results(tasks, order, duration)
        else:
            print(f"\n[HATA] {duration}")
            
    except ValueError:
        print("[HATA] Lütfen geçerli sayısal değerler girin.")
    except Exception as e:
        print(f"[HATA] Hata oluştu: {e}")

def main():
    while True:
        print("\n==============================================")
        print("    PERT & KRİTİK YOL METODU (CPM) PLANLAYICI ")
        print("==============================================")
        print("Bu program proje planlama ve yönetiminde olasılıksal")
        print("PERT modelleri çözer, kritik yolları ve riskleri bulur.")
        print("\nSeçenekler:")
        print("1. Örnek İnşaat Projesi Simülasyonunu Çalıştır (PERT)")
        print("2. Kendi Projemi Oluştur ve Analiz Et")
        print("0. Geri Dön")
        print("==============================================")
        secim = input("Seçiminiz: ").strip()
        
        if secim == '1':
            run_preset_demo()
        elif secim == '2':
            run_custom_pert()
        elif secim == '0':
            break
        else:
            print("Geçersiz seçim.")
        input("\nDevam etmek için Enter'a basın...")

if __name__ == "__main__":
    main()
