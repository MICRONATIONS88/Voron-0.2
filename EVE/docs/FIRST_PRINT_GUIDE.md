# EVE - 初回印刷までの手順ガイド

このガイドは EVE (Voron 0.2) を組み立て後、最初の印刷を行うまでの初期設定手順です。
Klipper コンソール（Mainsail / Fluidd）から各コマンドを実行してください。

---

## Step 1: 接続確認

### 1-1. Klipper UI にアクセス
- ブラウザで `http://<BTT Pi の IP アドレス>` を開く
- Mainsail または Fluidd の画面が表示されることを確認

### 1-2. MCU 接続確認
- Klipper が MCU に接続できていることを確認（エラーが出ていないこと）
- エラーが出る場合、BTT Pi で以下を実行して正しいシリアルIDを確認:
```bash
ls /dev/serial/by-id/
```
- 表示された ID を `printer.cfg` の `[mcu]` セクションに設定

---

## Step 2: ステッパーモーター方向確認

### 2-1. 各モーターを個別にテスト
コンソールで以下を実行（カスタムマクロも利用可能）:
```
CHECK_STEPPERS
```

または個別に:
```
STEPPER_BUZZ STEPPER=stepper_x
STEPPER_BUZZ STEPPER=stepper_y
STEPPER_BUZZ STEPPER=stepper_z
STEPPER_BUZZ STEPPER=extruder
```

### 2-2. 方向が逆の場合
`printer.cfg` の該当ステッパーの `dir_pin` を修正:
- 現在 `gpio10` → `!gpio10` に変更（反転）
- 現在 `!gpio28` → `gpio28` に変更（反転解除）

### 2-3. CoreXY の注意点
- X を動かすと **両方の AB モーター** が動く（正常）
- ツールヘッドが正しい方向に動くことを目視確認
- 間違っている場合はモーターコネクタの入れ替えも検討

---

## Step 3: エンドストップ確認

### 3-1. エンドストップ状態を確認
```
QUERY_ENDSTOPS
```
または:
```
CHECK_ENDSTOPS
```

### 3-2. 動作テスト
1. エンドストップを **押していない** 状態で `QUERY_ENDSTOPS` → `open` と表示
2. エンドストップを **手で押した** 状態で `QUERY_ENDSTOPS` → `TRIGGERED` と表示
3. 全軸（X, Y, Z）で確認

### 3-3. 反転している場合
`printer.cfg` のエンドストップピンの `^` を `^!` に変更（または逆）

---

## Step 4: ホーミングテスト

### 4-1. 緊急停止の準備
- **電源スイッチに手を添えた状態** で実行
- 異常な動きがあったらすぐに電源を切る

### 4-2. ホーミング実行
```
G28
```
- X → Y → Z の順でホーミングされる
- 各軸がエンドストップに向かって動き、触れたら停止することを確認

---

## Step 5: ヒーター & サーミスタ確認

### 5-1. テストマクロで確認
```
TEST_HEATERS
```
これはホットエンドを 150°C、ベッドを 60°C まで加熱し、正常に到達したら自動で冷却します。

### 5-2. 確認ポイント
- 温度が上昇していくことを画面で確認
- 温度が暴走しないこと（異常に速い上昇 = サーミスタ不良）
- 目標温度付近で安定すること

---

## Step 6: PID チューニング

### 6-1. ホットエンド PID
```
PID_CALIBRATE HEATER=extruder TARGET=245
```
完了まで数分かかります。

### 6-2. ベッド PID
```
PID_CALIBRATE HEATER=heater_bed TARGET=100
```

### 6-3. 設定保存
```
SAVE_CONFIG
```
これで PID 値が `printer.cfg` の末尾に自動保存され、Klipper が再起動します。

---

## Step 7: ベッドレベリング

### 7-1. ベッドスクリュー調整
```
G28
BED_SCREWS_ADJUST
```

### 7-2. 紙テスト
1. コピー用紙を置き、ノズルとベッドの間に挟む
2. 紙が軽い抵抗で動く程度に調整
3. `ACCEPT` → 次のスクリューへ → 全スクリュー調整後 `ABORT`

### 7-3. Z オフセット微調整
テストプリント中にベビーステッピングで微調整:
- ノズルが近すぎる → Z を上げる
- ノズルが遠すぎる → Z を下げる
- 最終値を `printer.cfg` の `position_endstop` に反映して `SAVE_CONFIG`

---

## Step 8: エクストルーダーキャリブレーション

### 8-1. rotation_distance の校正
1. ホットエンドを 200°C に加熱
2. フィラメントをエクストルーダー入口から **120mm** の位置にマーキング
3. 100mm 押出:
```
G91
G1 E100 F100
G90
```
4. 残りの長さを測定（例: 18mm 残り → 実際に 102mm 押出）
5. 新しい rotation_distance を計算:
```
新値 = 現在値 × (実測押出量 / 100)
例: 22.23 × (102 / 100) = 22.67
```
6. `printer.cfg` の `rotation_distance` を更新

---

## Step 9: テストプリント

### 9-1. スライサー設定
- **フィラメント**: PLA（最初は扱いやすい PLA を推奨）
- **ノズル温度**: 200-210°C
- **ベッド温度**: 60°C
- **速度**: 控えめに 80mm/s 以下
- **Start G-code**: `PRINT_START BED_TEMP=60 EXTRUDER_TEMP=200`
- **End G-code**: `PRINT_END`

### 9-2. 最初のプリント
- **XYZ キャリブレーションキューブ** (20x20x20mm) を印刷
- 最初のレイヤーがきちんとベッドに定着することを確認
- 寸法精度を測定

### 9-3. Pressure Advance チューニング（任意）
```
SET_VELOCITY_LIMIT SQUARE_CORNER_VELOCITY=1 ACCEL=500
TUNING_TOWER COMMAND=SET_PRESSURE_ADVANCE PARAMETER=ADVANCE START=0 FACTOR=.005
```
テストパターンを印刷し、最適な PA 値を `printer.cfg` に設定。

---

## チェックリスト

- [ ] Klipper UI に接続できる
- [ ] MCU がエラーなく認識されている
- [ ] 全ステッパーの方向が正しい
- [ ] 全エンドストップが正常動作
- [ ] ホーミング (G28) が正常
- [ ] ヒーターが正常に加熱・安定
- [ ] PID チューニング完了・保存済み
- [ ] ベッドレベリング完了
- [ ] エクストルーダー校正完了
- [ ] テストプリント成功
