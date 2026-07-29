import collections

class Task:
    def __init__(self, name, duration, predecessors=None):
        self.name = name
        self.duration = duration
        self.predecessors = predecessors if predecessors else []
        self.successors = []
        self.es = 0
        self.ef = 0
        self.ls = 0
        self.lf = 0
        self.slack = 0

def solve_cpm(tasks_dict):
    # Establish successors
    for t_name, task in tasks_dict.items():
        for pred in task.predecessors:
            if pred in tasks_dict:
                tasks_dict[pred].successors.append(t_name)

    # Topological Sort to evaluate forward pass correctly
    # Standard Kahn's algorithm
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
        # Cycle detected
        return None, "Projede döngüsel bağımlılık (circular dependency) tespit edildi!"

    # Forward Pass: Calculate ES & EF
    for u in topo_order:
        task = tasks_dict[u]
        if not task.predecessors:
            task.es = 0
        else:
            task.es = max(tasks_dict[pred].ef for pred in task.predecessors)
        task.ef = task.es + task.duration

    # Project duration is max EF of all tasks
    project_duration = max(task.ef for task in tasks_dict.values())

    # Backward Pass: Calculate LS & LF
    # We traverse in reverse topological order
    for u in reversed(topo_order):
        task = tasks_dict[u]
        if not task.successors:
            task.lf = project_duration
        else:
            task.lf = min(tasks_dict[succ].ls for succ in task.successors)
        task.ls = task.lf - task.duration
        task.slack = task.lf - task.ef

    # Identify critical path tasks
    critical_path = [u for u in topo_order if tasks_dict[u].slack == 0]
    
    return topo_order, project_duration

def print_cpm_results(tasks_dict, topo_order, duration):
    print("\n" + "=" * 80)
    print(f"               KRİTİK YOL METODU (CPM) ANALİZ SONUÇLARI")
    print("=" * 80)
    print(f"Toplam Proje Süresi: {duration} gün/birim")
    print("-" * 80)
    print(f"{'Görev':<10} | {'Süre':<6} | {'ES':<5} | {'EF':<5} | {'LS':<5} | {'LF':<5} | {'Slack':<6} | {'Kritik mi?'}")
    print("-" * 80)
    for name in topo_order:
        t = tasks_dict[name]
        is_crit = "EVET" if t.slack == 0 else "HAYIR"
        print(f"{t.name:<10} | {t.duration:<6} | {t.es:<5} | {t.ef:<5} | {t.ls:<5} | {t.lf:<5} | {t.slack:<6} | {is_crit}")
    print("-" * 80)
    crit_path_str = " -> ".join([t for t in topo_order if tasks_dict[t].slack == 0])
    print(f"Kritik Yol: {crit_path_str}")
    print("=" * 80)

def run_preset_demo():
    print("\n[BİLGİ] Bir inşaat projesi şablonu yükleniyor...")
    # Standard engineering / construction project example:
    # A: Temel kazısı (5 gün, bağımlılık yok)
    # B: Beton dökümü (3 gün, A'ya bağlı)
    # C: Duvar örme (4 gün, B'ye bağlı)
    # D: Elektrik tesisatı (2 gün, B'ye bağlı)
    # E: Sıva ve boya (5 gün, C ve D'ye bağlı)
    # F: Temizlik ve Teslim (2 gün, E'ye bağlı)
    tasks = {
        "A": Task("A", 5),
        "B": Task("B", 3, ["A"]),
        "C": Task("C", 4, ["B"]),
        "D": Task("D", 2, ["B"]),
        "E": Task("E", 5, ["C", "D"]),
        "F": Task("F", 2, ["E"])
    }
    
    order, duration = solve_cpm(tasks)
    if order:
        print_cpm_results(tasks, order, duration)
    else:
        print(f"\n[HATA] {duration}")

def run_custom_cpm():
    print("\n--- Özel Proje Tanımlama ---")
    try:
        num_tasks = int(input("Projedeki görev sayısını girin: "))
        tasks = {}
        for i in range(num_tasks):
            print(f"\n{i+1}. Görev Tanımı:")
            name = input("Görev Kodu/Adı (Örn: A, T1): ").strip()
            if not name:
                print("İsim boş geçilemez.")
                return
            duration = int(input(f"'{name}' Görevinin Süresi: "))
            pred_str = input(f"Öncül Görevler (Aralarında virgül koyun, örn: A,B - Öncül yoksa boş geçin): ").strip()
            
            predecessors = []
            if pred_str:
                predecessors = [p.strip() for p in pred_str.split(",")]
                
            tasks[name] = Task(name, duration, predecessors)
            
        order, duration = solve_cpm(tasks)
        if order:
            print_cpm_results(tasks, order, duration)
        else:
            print(f"\n[HATA] {duration}")
            
    except ValueError:
        print("[HATA] Lütfen geçerli sayısal değerler girin.")
    except Exception as e:
        print(f"[HATA] Hata oluştu: {e}")

def main():
    while True:
        print("\n==============================================")
        print("    KRİTİK YOL METODU (CPM) HESAPLAYICI       ")
        print("==============================================")
        print("Bu program proje planlama ve yönetiminde kritik")
        print("yolları belirler, görev bolluklarını (slack) bulur.")
        print("\nSeçenekler:")
        print("1. Örnek İnşaat Projesi Simülasyonunu Çalıştır")
        print("2. Kendi Projemi Oluştur ve Analiz Et")
        print("0. Geri Dön")
        print("==============================================")
        secim = input("Seçiminiz: ").strip()
        
        if secim == '1':
            run_preset_demo()
        elif secim == '2':
            run_custom_cpm()
        elif secim == '0':
            break
        else:
            print("Geçersiz seçim.")
        input("\nDevam etmek için Enter'a basın...")

if __name__ == "__main__":
    main()
