# HKMA 網絡防衛計劃（CFI）詳細分析

## 基本資料

| 項目 | 內容 |
|------|------|
| **名稱** | Cybersecurity Fortification Initiative (CFI) 網絡防衛計劃 |
| **發布機構** | 香港金融管理局（HKMA） |
| **首次發布** | 2016年5月（諮詢）、2016年12月（正式實施） |
| **最新版本** | CFI 2.0（2020年11月發布，2021年1月生效） |
| **適用對象** | 所有認可機構（Authorized Institutions, AIs）|

---

## CFI 三大支柱

| 支柱 | 名稱 | 作用 |
|------|------|------|
| **1** | 網絡防衛評估框架（C-RAF） | 評估銀行網絡風險同成熟度 |
| **2** | 專業培訓計劃（PDP） | 培訓合資格網絡安全專業人員 |
| **3** | 網絡風險資訊共享平台（CRISP/CISP） | 銀行間共享網絡威脅情報 |

---

## C-RAF 評估框架（核心）

### 三步驟評估

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│  Step 1        │    │  Step 2         │    │  Step 3         │
│  固有風險評估   │ →  │  成熟度評估     │ →  │  改進路線圖     │
│ Inherent Risk  │    │  Maturity       │    │  Roadmap for    │
│ Assessment      │    │  Assessment     │    │  Improvement    │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

### Step 1：固有風險評估（Inherent Risk Assessment）

**目的：** 評估機構的固有網絡風險水平

**考慮因素：**
- 採用的技術及交付渠道
- 活動、產品、服務
- 基礎設施
- 營運環境
- 網絡威脅歷史紀錄

**風險評級：**

| 固有風險水平 | 預期成熟度水平 |
|-------------|---------------|
| High（高） | Advanced（高級） |
| Medium（中） | Intermediate（中級） |
| Low（低） | Baseline（基準） |

### Step 2：成熟度評估（Maturity Assessment）

**目的：** 評估機構實際網絡韌性成熟度

**七大評估領域：**
1. Threat Intelligence（威脅情報）
2. Behavioral Controls（行為控制）
3. Security Controls（安全控制）
4. Process Management（流程管理）
5. Detection & Analysis（偵測及分析）
6. Response & Recovery（應變及恢復）
7. Testing & Exercises（測試及演練）

**成熟度級別：**
- Baseline（基準）
- Intermediate（中級）
- Advanced（高級）

### Step 3：改進路線圖（Roadmap for Improvement）

**目的：** 識別差距並制定改善計劃

- 將預期成熟度與實際成熟度進行比較
- 識別差距
- 制定達標的改進計劃

---

## iCAST 測試

### Intelligence-led Cyber Attack Simulation Testing

**對象：** 固有風險評級為「中」或「高」的機構

**特點：**
- 模擬真實網絡攻擊
- 利用網絡威脅情報
- 不只測試技術，還包括「人」和「流程」元素

**CFI 2.0 新增要求：**
- **Blue Team要求** — 測試機構的偵測、應變及恢復功能是否有效

---

## PDP 專業培訓計劃

### C-RAF 評估員資格

| 角色 | 認可資格 |
|------|---------|
| **C-RAF Assessor** | CISA, CISSP, CISM, CRISC, CSX-F, CSX-P, CISP-HK, CEH * |

### iCAST 人員資格

| 角色 | 認可資格 |
|------|---------|
| **iCAST Manager** | CCASM, GPEN+GXPN, OSCE+OSEE |
| **iCAST Threat Intelligence Specialist** | CCTIM, GPEN, GXPN, OSCE, OSEE, GCTI *, CCIP * |
| **iCAST Specialist** | CCSAS, GPEN+GXPN, OSCE+OSEE, eCPTX *, CRTE * |
| **iCAST Tester (IT infrastructure)** | CCT Inf, GPEN, OSCE, OSCP * |
| **iCAST Tester (web application)** | CCT Web App, GWAPT, OSWE, OSCP *, eCPPT *, CRTP * |

*標記為CFI 2.0新增資格*

---

## CFI 2.0 主要更新（相較2016年版本）

| 項目 | CFI 1.0 | CFI 2.0 |
|------|---------|---------|
| **控制原則** | 基本 | 新增反映最新國際實務的控制原則 |
| **技術趨勢** | 傳統 | 加入雲端技術及虛擬化安全 |
| **iCAST** | 基本要求 | 加入Blue Team要求 |
| **集團評估結果** | 不接受 | 允許利用母公司/銀行集团的評估結果 |
| **專業資格** | 基本清單 | 擴展至涵蓋主要海外司法管轄區的資格 |
| **情報共享** | 基本平台 | 建議開發目標運作模式 |

---

## 分階段實施時間表

### CFI 1.0（2016-2018）

| 階段 | 涵蓋範圍 | 截止日期 |
|------|---------|---------|
| 第一階段 | 約30間（包括所有大型零售銀行） | 固有風險+成熟度：2017年9月 / iCAST：2018年6月 |
| 第二階段 | 其餘所有AIs | 固有風險+成熟度：2018年12月 |
| 第三階段 | 所有其餘AIs | iCAST：2020年中 |

### CFI 2.0（2021-2023）

| 組別 | 固有風險+成熟度評估 | iCAST（中高風險） |
|------|-------------------|------------------|
| Group 1 | 2021年9月底 | 2022年6月底 |
| Group 2 | 2022年6月底 | 2023年3月底 |
| Group 3 | 2023年3月底 | 2023年12月底 |

---

## 與IA GL20的分別

| 項目 | HKMA CFI/C-RAF | IA GL20 |
|------|---------------|---------|
| **監管機構** | 香港金融管理局 | 保險業監管局 |
| **適用對象** | 認可機構（銀行） | 獲授權保險人 |
| **評估框架** | C-RAF（銀行版） | CRAF（保險版） |
| **iCAST測試** | 有 | GL20無明确iCAST要求 |
| **法律效力** | 不具法律效力 | 不具法律效力 |
| **專業資格認證** | PDP + 等同資格清單 | GL20無明確要求 |

**相同點：** 兩者框架概念相似，都係固有風險評估 → 成熟度評估 → 差距改善

---

## 資料檔案

| 檔案 | 描述 |
|------|------|
| [20161221_CFI_EN.pdf](./20161221_CFI_EN.pdf) | CFI 2016英文版（4頁） |
| [20160518_CRAF_Framework.pdf](./20160518_CRAF_Framework.pdf) | CRAF框架介紹簡報（13頁） |
| [20201103_CFI2-1_EN.pdf](./20201103_CFI2-1_EN.pdf) | CFI 2.0英文版（2頁） |
| [20201103_CFI2_TC.pdf](./20201103_CFI2_TC.pdf) | CFI 2.0中文附件（3頁） |

---

*最後更新：2026-04-21*
*資料來源：HKMA官方文件*
