import os

def generate_rectangular_gcode(width, length, depth, safe_z, feed_rate, spindle_speed, tool_dia, filename):
    # Calculate tool path offset if doing pocket or simple profile
    # Let's write standard outer contour profile G-code (climb milling)
    half_w = width / 2.0
    half_l = length / 2.0
    
    gcode = []
    gcode.append("; CNC DIKDORTGEN PROFIL FREZELEME G-KODU")
    gcode.append(f"; Parametreler: W={width}mm, L={length}mm, Depth={depth}mm, Tool Dia={tool_dia}mm")
    gcode.append("G21 ; Metrik birim sistemi (mm)")
    gcode.append("G90 ; Mutlak koordinat sistemi")
    gcode.append("G94 ; Dakika basina ilerleme (feed rate)")
    gcode.append(f"M03 S{spindle_speed} ; Spindle calistir (Saat yonu, RPM={spindle_speed})")
    
    # Rapid to safe Z
    gcode.append(f"G00 Z{safe_z:.3f} ; Guvenli yukseklige hizli ilerleme")
    # Move to starting point (bottom left corner, with tool radius offset if requested, but let's do exact center-based coordinate path)
    # Start at bottom-left corner (-half_w, -half_l)
    gcode.append(f"G00 X{-half_w:.3f} Y{-half_l:.3f} ; Baslangic koordinatina hizli git")
    
    # Plunge to depth
    gcode.append(f"G01 Z{depth:.3f} F{feed_rate / 2:.0f} ; Kesim derinligine yavas dal")
    
    # Mill rectangle contour
    # Go to top-left corner
    gcode.append(f"G01 Y{half_l:.3f} F{feed_rate:.0f} ; Sol kenar kesim")
    # Go to top-right corner
    gcode.append(f"G01 X{half_w:.3f} ; Ust kenar kesim")
    # Go to bottom-right corner
    gcode.append(f"G01 Y{-half_l:.3f} ; Sag kenar kesim")
    # Go to bottom-left corner (complete loop)
    gcode.append(f"G01 X{-half_w:.3f} ; Alt kenar kesim")
    
    # Retract tool
    gcode.append(f"G01 Z{safe_z:.3f} F{feed_rate * 2:.0f} ; Takimi yukari cek")
    gcode.append("G00 X0 Y0 ; Baslangic merkezine don")
    gcode.append("M05 ; Spindle durdur")
    gcode.append("M30 ; Program sonu")
    
    return "\n".join(gcode)

def generate_circular_gcode(diameter, depth, safe_z, feed_rate, spindle_speed, tool_dia, filename):
    radius = diameter / 2.0
    
    gcode = []
    gcode.append("; CNC DAIRESEL PROFIL FREZELEME G-KODU")
    gcode.append(f"; Parametreler: Dia={diameter}mm, Depth={depth}mm, Tool Dia={tool_dia}mm")
    gcode.append("G21 ; Metrik birim (mm)")
    gcode.append("G90 ; Mutlak koordinat")
    gcode.append("G94 ; Dakika basina ilerleme")
    gcode.append(f"M03 S{spindle_speed} ; Spindle calistir (RPM={spindle_speed})")
    
    # Rapid to safe Z
    gcode.append(f"G00 Z{safe_z:.3f}")
    # Move to starting point on circle edge (X=radius, Y=0)
    gcode.append(f"G00 X{radius:.3f} Y0.000")
    
    # Plunge to depth
    gcode.append(f"G01 Z{depth:.3f} F{feed_rate / 2:.0f}")
    
    # Interpolate circle using G02 (CW circular interpolation)
    # I, J specify center offset relative to start point (Start: radius, 0. Center is 0,0. Offset is -radius, 0)
    gcode.append(f"G02 X{radius:.3f} Y0.000 I{-radius:.3f} J0.000 F{feed_rate:.0f} ; Tam daire kesim")
    
    # Retract tool
    gcode.append(f"G01 Z{safe_z:.3f} F{feed_rate * 2:.0f}")
    gcode.append("G00 X0 Y0")
    gcode.append("M05")
    gcode.append("M30")
    
    return "\n".join(gcode)

def main():
    print("\n==============================================")
    print("      CNC G-KODU JENERATÖRÜ (CAD/CAM UTILITY)   ")
    print("==============================================")
    print("Bu arac, belirlediginiz olculere gore CNC freze tezgahlarinda")
    print("kullanilabilecek standart ISO G-Kodlari (.nc) uretir.")
    print("Merkez nokta (0,0) olarak kabul edilir.")
    
    print("\nSekil Secimi:")
    print("1. Dikdortgen Profil Kesimi")
    print("2. Dairesel Profil Kesimi")
    shape_choice = input("Seciminiz (1/2): ").strip()
    
    if shape_choice not in ['1', '2']:
        print("[HATA] Gecersiz secim.")
        return
        
    try:
        # User parameters
        safe_z = float(input("Guvenli Z Yuksekligi (mm) [Varsayilan: 5.0]: ") or 5.0)
        depth = float(input("Kesim Derinligi (Z, eksi deger girin) [Varsayilan: -2.0]: ") or -2.0)
        feed_rate = float(input("Ilerleme Hizi (F, mm/dakika) [Varsayilan: 800]: ") or 800)
        spindle_speed = int(input("Spindle Hizi (S, RPM) [Varsayilan: 12000]: ") or 12000)
        tool_dia = float(input("Takim Capi (mm) [Varsayilan: 6.0]: ") or 6.0)
        
        output_name = input("Cikti Dosya Adi [Varsayilan: output_gcode.nc]: ").strip() or "output_gcode.nc"
        if not output_name.endswith(('.nc', '.gcode', '.txt')):
            output_name += ".nc"
            
        gcode_content = ""
        if shape_choice == '1':
            width = float(input("Genislik (X ekseni, mm): "))
            length = float(input("Uzunluk (Y ekseni, mm): "))
            gcode_content = generate_rectangular_gcode(width, length, depth, safe_z, feed_rate, spindle_speed, tool_dia, output_name)
        elif shape_choice == '2':
            diameter = float(input("Daire Capi (mm): "))
            gcode_content = generate_circular_gcode(diameter, depth, safe_z, feed_rate, spindle_speed, tool_dia, output_name)
            
        # Write to file
        output_path = os.path.join(os.path.dirname(__file__), output_name)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(gcode_content)
            
        print("\n--- Uretilen G-Kodu ---")
        print(gcode_content)
        print("-----------------------")
        print(f"\n[BAŞARILI] G-Kodu dosyasi '{output_path}' konumuna kaydedildi.")
        
    except ValueError:
        print("[HATA] Lutfen sayisal degerleri dogru girin.")
    except Exception as e:
        print(f"[HATA] Beklenmeyen hata: {e}")
        
    input("\nDevam etmek için Enter'a basın...")

if __name__ == "__main__":
    main()
