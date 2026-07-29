import time
import random

class PLCSimulator:
    def __init__(self):
        # Modbus register tables
        # 0xxxx (Coils - Read/Write Bits)
        self.coils = {
            1: False, # Motor Start/Stop
            2: False, # Cooling Valve Open/Close
            3: False  # Alarm Buzzer On/Off
        }
        
        # 1xxxx (Discrete Inputs - Read-Only Bits)
        self.discrete_inputs = {
            101: False, # Emergency Stop Button pressed
            102: False  # Overheat Limit Switch tripped
        }
        
        # 3xxxx (Input Registers - Read-Only 16-bit integers)
        self.input_registers = {
            3001: 25,   # Temperature Sensor (°C)
            3002: 120,  # System Pressure (kPa)
            3003: 0     # Motor Speed (RPM)
        }
        
        # 4xxxx (Holding Registers - Read/Write 16-bit integers)
        self.holding_registers = {
            4001: 80,   # Temperature Setpoint (°C)
            4002: 1500  # Max Motor Speed Limit (RPM)
        }
        
        self.cycle_count = 0

    def print_registers(self):
        print("\n=== PLC MODBUS REGİSTER TABLOSU ===")
        print("\n[COILS (0xxxx) - Bobinler (Okunabilir/Yazılabilir Dijital)]")
        print(f"  0001 - Motor Start/Stop     : {'ON' if self.coils[1] else 'OFF'}")
        print(f"  0002 - Soğutma Valfi Açık   : {'ON' if self.coils[2] else 'OFF'}")
        print(f"  0003 - Alarm Buzzer         : {'ON' if self.coils[3] else 'OFF'}")
        
        print("\n[DISCRETE INPUTS (1xxxx) - Ayrık Girişler (Salt Okunur Dijital)]")
        print(f"  0101 - Acil Stop Butonu     : {'BASILI' if self.discrete_inputs[101] else 'NORMAL'}")
        print(f"  0102 - Aşırı Isı Sınırı     : {'TRİP' if self.discrete_inputs[102] else 'NORMAL'}")
        
        print("\n[INPUT REGISTERS (3xxxx) - Giriş Kaydedicileri (Salt Okunur Analog)]")
        print(f"  3001 - Sistem Sıcaklığı     : {self.input_registers[3001]} °C")
        print(f"  3002 - Hat Basıncı          : {self.input_registers[3002]} kPa")
        print(f"  3003 - Motor Hızı           : {self.input_registers[3003]} RPM")
        
        print("\n[HOLDING REGISTERS (4xxxx) - Tutma Kaydedicileri (Okunabilir/Yazılabilir Analog)]")
        print(f"  4001 - Sıcaklık Set Değeri  : {self.holding_registers[4001]} °C")
        print(f"  4002 - Maks. Hız Limiti     : {self.holding_registers[4002]} RPM")
        print("====================================")

    def scan_cycle(self):
        """Simulates one PLC scan cycle and physical system behaviors."""
        self.cycle_count += 1
        
        # Check Emergency Stop logic
        if self.discrete_inputs[101]:
            # If Emergency stop is pressed, instantly stop motor and trigger alarm
            self.coils[1] = False
            self.input_registers[3003] = 0
            self.coils[3] = True
            print("\n[ALARM] ACİL STOP BASILI! Motor durduruldu, alarm aktif.")
        
        # Physical system simulation
        # Motor speed logic
        if self.coils[1] and not self.discrete_inputs[101]:
            # Ramp speed up to Max Motor Speed Limit
            target_speed = self.holding_registers[4002]
            current_speed = self.input_registers[3003]
            if current_speed < target_speed:
                self.input_registers[3003] = min(current_speed + 300, target_speed)
        else:
            # Ramp speed down to 0
            current_speed = self.input_registers[3003]
            if current_speed > 0:
                self.input_registers[3003] = max(current_speed - 400, 0)
                
        # Temperature thermodynamics simulation
        temp = self.input_registers[3001]
        motor_speed = self.input_registers[3003]
        
        # If motor running, temp rises based on speed
        if motor_speed > 0:
            temp += int(motor_speed / 400) + random.randint(0, 1)
        else:
            temp -= random.randint(0, 1) if temp > 25 else 0 # cool down to ambient
            
        # Cooling valve logic
        if self.coils[2]:
            temp -= 4 # cooling drops temperature fast
            
        # Keep temperature realistic
        temp = max(temp, 20)
        self.input_registers[3001] = temp
        
        # Overheat safety limit check
        if temp >= self.holding_registers[4001]:
            self.discrete_inputs[102] = True
            self.coils[3] = True # Alarm ON
            self.coils[1] = False # Shut off motor
            print(f"\n[ALARM] AŞIRI ISI LİMİTİ AŞILDI! Sıcaklık: {temp}°C, Set: {self.holding_registers[4001]}°C")
        else:
            self.discrete_inputs[102] = False
            # Alarm automatically goes off if limit clear and e-stop clear
            if not self.discrete_inputs[101]:
                self.coils[3] = False
                
        # Pressure fluctuation simulation
        if motor_speed > 0:
            self.input_registers[3002] = 120 + int(motor_speed / 15) + random.randint(-5, 5)
        else:
            self.input_registers[3002] = 100 + random.randint(-2, 2)

def main():
    plc = PLCSimulator()
    print("PLC Simülatörüne Hoş Geldiniz.")
    while True:
        plc.print_registers()
        print("\nİşlemler:")
        print("1. Bobin Durumu Değiştir (Write Coil)")
        print("2. Set Değeri Değiştir (Write Holding Register)")
        print("3. Acil Stop Butonuna Bas/Bırak")
        print("4. Sistem Döngüsünü Çalıştır (1 Çevrim - Scan Cycle)")
        print("5. Sürekli Çalıştır (Gerçek Zamanlı Simülasyon)")
        print("0. Geri Dön")
        
        secim = input("\nSeçiminiz: ").strip()
        
        if secim == '1':
            try:
                addr = int(input("Yazmak istediğiniz Bobin Adresi (1: Motor, 2: Soğutma Valfi): "))
                if addr not in [1, 2]:
                    print("Hatalı adres!")
                    continue
                val = input("Değer (1/0 veya True/False): ").strip().upper()
                plc.coils[addr] = val in ['1', 'TRUE', 'T', 'ON']
                print("[BAŞARILI] Bobin yazıldı.")
            except ValueError:
                print("Lütfen sayısal bir adres girin.")
                
        elif secim == '2':
            try:
                addr = int(input("Yazmak istediğiniz Register Adresi (4001: Sıcaklık Set, 4002: Maks Hız): "))
                if addr not in [4001, 4002]:
                    print("Hatalı adres!")
                    continue
                val = int(input("Değer: "))
                plc.holding_registers[addr] = val
                print("[BAŞARILI] Holding register yazıldı.")
            except ValueError:
                print("Lütfen sayısal bir değer girin.")
                
        elif secim == '3':
            plc.discrete_inputs[101] = not plc.discrete_inputs[101]
            print(f"\n[BİLGİ] Acil Stop butonu durumu değiştirildi: {'BASILI' if plc.discrete_inputs[101] else 'SERBEST'}")
            plc.scan_cycle()
            
        elif secim == '4':
            print("\nScan Cycle tetiklendi...")
            plc.scan_cycle()
            
        elif secim == '5':
            print("\nReal-time Simülasyon başladı. Durdurmak için Ctrl+C'ye basın...")
            try:
                while True:
                    plc.scan_cycle()
                    plc.print_registers()
                    time.sleep(1.5)
            except KeyboardInterrupt:
                print("\nSimülasyon durduruldu.")
                
        elif secim == '0':
            break
        else:
            print("Geçersiz seçim.")
            
        input("\nDevam etmek için Enter'a basın...")

if __name__ == "__main__":
    main()
