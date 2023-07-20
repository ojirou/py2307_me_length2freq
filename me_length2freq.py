def calculate_frequencies(wavelength, dielectric_constant):
    # 比誘電率を考慮して周波数を計算
    frequencies = [
        300 / (wavelength * (dielectric_constant ** 0.5)),            # 1波長
        300 / (wavelength * 2 * (dielectric_constant ** 0.5)),      # 1/2波長
        300 / (wavelength * 4 * (dielectric_constant ** 0.5)),      # 1/4波長
        300 / (wavelength * 6 * (dielectric_constant ** 0.5)),      # 1/6波長
        300 / (wavelength * 10 * (dielectric_constant ** 0.5))      # 1/10波長
    ]
    return frequencies
while True:
    # 導体の長さ[mm]の入力を取得
    input_length = input("導体の長さ[m]を入力してください (qで終了): ")
    if input_length.lower() == "q":
        print("プログラムを終了します。")
        break
    try:
        length = float(input_length)
    except ValueError:
        print("無効な入力です。数値を入力してください。")
        continue
    # 比誘電率の入力を取得
    try:
        dielectric_constant = float(input("比誘電率を入力してください: "))
    except ValueError:
        print("無効な入力です。数値を入力してください。")
        continue
    # 周波数を計算
    frequencies = calculate_frequencies(length, dielectric_constant)
    # 結果を表示
    print(f"\n導体の長さ {length} [mm] の場合、比誘電率 {dielectric_constant} の時、以下の周波数[MHz]になります:")
    print(f"1波長: {frequencies[0]:.2f}")
    print(f"1/2波長: {frequencies[1]:.2f}")
    print(f"1/4波長: {frequencies[2]:.2f}")
    print(f"1/6波長: {frequencies[3]:.2f}")
    print(f"1/10波長: {frequencies[4]:.2f}")