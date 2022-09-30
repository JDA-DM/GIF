デジタル社会推進実践ガイドブック DS-467

データ環境整備のためのアーキテクチャ管理

導入実践ガイドブック

2022年（令和4年）3月31日

デジタル庁

**〔キーワード〕**

アーキテクチャ

**〔概要〕**

デジタル社会は技術と制度が相互に関係するとともに分野横断の取組が多い複雑な構造をしています。これらの構造を明確にし、関係者の共通理解を深め、相互運用性の高い全体像を作っていくために、アーキテクチャは重要な役割を果たしていきます。

本ペーパーでは、アーキテクチャ作成や活用の考え方を示すとともに、その導入方法を説明します。

改定履歴

| 改定年月日    | 改定箇所 | 改定内容 |
|---------------|----------|----------|
| 2022年3月31日 | \-       | 初版決定 |

## 目次

[１ 背景と目的 [1][]][1]

[１.１ 背景 [1][2]][2]

[１.２ 目的 [2][]][2]

[１.３ 概要 [2][3]][3]

[１.４ 用語の定義 [4][]][4]

[２ アーキテクチャ全体俯瞰図による記述 [5][]][5]

[２.１ 基本とするレイヤー構造 [5][6]][6]

[２.２ 各エレメント、リレーションの定義及び使用例の整理 [6][]][6]

[３ アーキテクチャ全体俯瞰図の設計 [14][]][14]

[３.１ アーキテクチャ全体俯瞰図の設計準備 [14][7]][7]

[３.２ アーキテクチャ全体俯瞰図の設計の流れ [14][8]][8]

[1) 戦略レイヤー [14][9]][9]

[2) 組織レイヤー [15][]][15]

[3) ルールレイヤー [16][]][16]

[4) 業務（サービス）レイヤー、利活用環境レイヤー、連携基盤（ツール）レイヤー [17][]][17]

[5) データレイヤー、データ標準レイヤー [21][]][21]

[6) インフラレイヤー [21][10]][10]

[４ アーキテクチャ全体俯瞰図の活用例 [23][]][23]

[４.１ 戦略策定での活用 [23][11]][11]

[４.２ 全体の関係性の整理 [24][]][24]

[４.３ 戦略の整合性確保 [26][]][26]

[４.４ プラットフォーム間の共通化や連携の検討 [28][]][28]

[４.５ 分野横断の分析での活用 [28][12]][12]

[４.６ 価値連鎖の検討 [32][]][32]

[５ アーキテクチャ全体俯瞰図から詳細化の実施 [35][]][35]

## 

## 　背景と目的

### 　背景

政府のデジタル政策の推進でアーキテクチャが注目されています。政府では2000年代前半にエンタープライズ・アーキテクチャ[^1]を導入しましたが、方法論の検討が不十分だった上、使いこなせないまま廃止に至りました。その時の課題は、モデリング手法の軽視と、行政側のリテラシーと取組意識の低さにありました。

一方、世界ではアーキテクチャ記述のモデリング言語が開発されるなど、アーキテクチャの推進が体系的に行われています。

国内でアーキテクチャを再導入するにあたっては、これまでの反省を活かし、効率的、効果的に導入を進めていく必要があります。

最近は、社会全体が複雑化しており、分野横断でのプロジェクトというものが増えてきています。また、技術的な検討と並行して制度的な変更が行われるといったケースも増えています。このように複雑なサービス等の構築や運用では、全体像を可視化して関係者全体で共通の理解を図っていくことが重要となります。しかし、これまではアーキテクチャ的に設計が行われてこなかったために、プロジェクト開始までに時間がかかったり、運用間近になって検討項目の抜け漏れが発覚したりするなどの問題が発生していました。

アーキテクチャを使ったプロジェクトでも、独自のアーキテクチャ表現手法を使っているために、関係者の理解に時間がかかったり、誤解が生じてしまったりすることが散見されます。

このような課題を解決するために、グローバルな推進団体のオープン・グループが、アーキテクチャ標準のTOGAF(R)[^2]の開発を推進するとともに、アーキテクチャモデリング言語のArchiMate(R)[^3]を策定しています。他にグローバルなモデリング言語がないこともあり、国際的に利用が広がり始めています。

政府において、アーキテクチャの活用が目指されSociety5.0参照アーキテクチャ[^4]が整備され、スマートシティやデータ戦略の検討に展開されていますが、詳細な記述方法の定義がないため、アーキテクチャの導入が概念レベルで立ち止まっています。

### 　目的

本ガイドは、国際的にも活用されているアーキテクチャモデリング言語であるArchiMate(R)を活用して当該分野のアーキテクチャ全体俯瞰図を作成することで、複雑な全体像を可視化し、関係者が連携して取組みを進めることができるようにすることを目的とします。

アーキテクチャを正しく導入・活用することにより、システムやサービス間の相互運用性を高めると同時に、効率的なシステムの構築や管理を実現します。

また、本ガイドに沿ってサービスを設計することで、アーキテクチャの各層での分野横断の比較検証や記述の統一ができるようになります。

### 　概要

アーキテクチャの設計には、アーキテクチャ記述の統一が必要となります。アーキテクチャ記述の標準としては、ISO/IEC/IEEE 42010 Systems and software engineering - Architecture description[^5]があります。

<img src="md/467/media/image1.png" style="width:5.90556in;height:5.16389in" />

図 1　ISO42010のアーキテクチャ全体像[^6]

本全体像を参考にしつつ、アーキテクチャの構造は、Society5.0の参照アーキテクチャと、具体的にアーキテクチャを元にした取組が進んでいる包括的データ戦略のアーキテクチャを軸に整理していきます。

<img src="md/467/media/image2.png" style="width:5.90278in;height:3.29167in" />

図 2　Society5.0と包括的データ戦略のアーキテクチャ[^7]

アーキテクチャモデリング言語は、ArchiMate(R)とし、記述方法はそのルールに従います。そのモデリングツールとしてオープンソースのArchi[^8]を使用します。

### 用語の定義

・アーキテクチャ全体俯瞰図

> 　　　ある目的を実現するための全体像を表す考え方であり、レイヤー構造を持ち、機能など目的に応じて分割したエレメント（部品）の組合せで表現します。

・レイヤー

> 　　　アーキテクチャを構成する階層（視点）です。ルールやデータなど、検討が行いやすい単位で整理します。

・エレメント

> 　　　アーキテクチャの個々の機能やデータなどのオブジェクトを定義する部品です。

・ArchiMate(R)

> 　　　グローバルな推進団体のオープン・グループが開発したアーキテクチャモデリング言語です。

## 　アーキテクチャ全体俯瞰図による記述

### 　基本とするレイヤー構造

アーキテクチャの全体像は図 1に示しましたが、アーキテクチャ記述は多様なドキュメントがあります。そこで、データ検討のためのアーキテクチャ整理では、全体の関係性を俯瞰することを目的とした図 3の例に示すレイヤーとエレメントで構成されたアーキテクチャ全体俯瞰図を活用することとします。

<img src="md/467/media/image3.jpeg" style="width:5.20397in;height:6.56728in" />

図 3アーキテクチャ全体俯瞰図の例（スマートシティ）

アーキテクチャ全体俯瞰図を用いることで、当該分野に関する構成要素を洗い出し、抜け漏れや重複を防止するとともに、関係者間の調整を容易にします。さらに各分野でアーキテクチャ全体俯瞰図を用いることで、分野間連携を容易にします。

アーキテクチャ全体俯瞰図では、Society5.0参照アーキテクチャにおける「利活用機能」レイヤーは、データ取引市場のようなサービスと検索などの機能を明確に区別して、データ環境整備をするために「利活用環境」と「連携基盤」の2つのレイヤーに分離しています。また、Society5.0参照アーキテクチャの「データ連携」レイヤーは、エッジコンピューティングを意識したデバイスレベルでの連携用ツールや機能を記述するレイヤーとなりますが、包括的データ戦略のように社会システムを記述する際にはエッジコンピューティングまで詳細化することが少ないため、このレイヤーは省略しています。

さらに、データ標準は「ルール」レイヤーの一部となりますが、「データ」レイヤーと関係性が深いため、「データ」レイヤーの下に「データ標準」レイヤーを設定しました。

よって、アーキテクチャ全体俯瞰図は、以下のレイヤー構成で記述します。

-   戦略

-   組織

-   業務（サービス）

-   ルール

-   利活用環境

-   連携基盤（ツール）

-   データ

-   データ標準

-   インフラ

### 　各エレメント、リレーションの定義及び使用例の整理

ArchiMate(R)には多くのエレメントが定義されていますが、StakeholderとBusiness Actor等、意味の近いものが多く、同一レイヤーにすべてのエレメントを使用すると記述におけるバラツキが出て記述者にも読者にもわかりにくくなります。一方、ArchiMate(R)を導入している欧州のEIRA（European Interoperability Reference Architecture）[^9]は、エレメントを絞りすぎておりアーキテクチャ記述として不便な面もあります。

そこで、本ガイドは、主要なエレメント、リレーションの定義及び使用例を以下のように定めます。定義には使用可能なレイヤーを明示しました。

また、灰色のエレメントは、使用を推奨しないエレメントとなりますが、記述を明確にするうえで必要な場合には使用可能とします。

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 26%" />
<col style="width: 0%" />
<col style="width: 43%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th>No.</th>
<th>エレメント</th>
<th colspan="2">定義</th>
<th>使用例</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><img src="md/467/media/image4.png" style="width:1.37292in;height:0.66389in" /></td>
<td colspan="2"><p>関係者</p>
<p>戦略・ルールレイヤーで使用。</p></td>
<td></td>
</tr>
<tr class="even">
<td>2</td>
<td><img src="md/467/media/image5.png" style="width:1.38819in;height:0.67844in" /></td>
<td colspan="2"><p>ゴールやアウトカム等を実現するためのドライバー</p>
<p>戦略・ルールレイヤーで使用。</p></td>
<td></td>
</tr>
<tr class="odd">
<td>3</td>
<td><img src="md/467/media/image6.png" style="width:1.41806in;height:0.70139in" /></td>
<td colspan="2"><p>戦略を推進するために必要なアセスメント</p>
<p>戦略・ルールレイヤーで使用。</p></td>
<td></td>
</tr>
<tr class="even">
<td>4</td>
<td><img src="md/467/media/image7.png" style="width:1.38819in;height:0.66389in" /></td>
<td colspan="2"><p>ゴール</p>
<p>戦略・ルールレイヤーで使用。</p></td>
<td>戦略等に明記されている目標</td>
</tr>
<tr class="odd">
<td>5</td>
<td><img src="md/467/media/image8.png" style="width:1.40278in;height:0.66389in" /></td>
<td colspan="2"><p>ゴールを実現するための具体的な成果</p>
<p>戦略・ルールレイヤーで使用。</p></td>
<td></td>
</tr>
<tr class="even">
<td>6</td>
<td><img src="md/467/media/image9.png" style="width:1.36597in;height:0.70903in" /></td>
<td colspan="2"><p>原理・原則</p>
<p>戦略・ルールレイヤーで使用。</p></td>
<td></td>
</tr>
<tr class="odd">
<td>7</td>
<td><img src="md/467/media/image10.png" style="width:1.3125in;height:0.60417in" /></td>
<td colspan="2"><p>要求</p>
<p>戦略・ルールレイヤーで使用。</p></td>
<td><p>法律や制度、</p>
<p>提言等</p></td>
</tr>
<tr class="even">
<td>8</td>
<td><img src="md/467/media/image11.png" style="width:1.35069in;height:0.71667in" /></td>
<td colspan="2"><p>制約</p>
<p>戦略・ルールレイヤーで使用。</p></td>
<td>法律や制度</td>
</tr>
<tr class="odd">
<td>9</td>
<td><img src="md/467/media/image12.png" style="width:1.33611in;height:0.66389in" /></td>
<td colspan="2"><p>意味</p>
<p>戦略・ルールレイヤーで使用。</p></td>
<td></td>
</tr>
<tr class="even">
<td>10</td>
<td><img src="md/467/media/image13.png" /></td>
<td colspan="2"><p>価値</p>
<p>戦略・ルールレイヤーで使用。</p></td>
<td></td>
</tr>
<tr class="odd">
<td>11</td>
<td><img src="md/467/media/image14.png" style="width:1.33611in;height:0.66389in" /></td>
<td colspan="2"><p>動作する人</p>
<p>業務（サービス）レイヤーで使用。</p></td>
<td></td>
</tr>
<tr class="even">
<td>12</td>
<td><img src="md/467/media/image15.png" style="width:1.34306in;height:0.67917in" /></td>
<td colspan="2"><p>業務ロール</p>
<p>業務（サービス）レイヤーで使用。</p></td>
<td></td>
</tr>
<tr class="odd">
<td>13</td>
<td><img src="md/467/media/image16.png" style="width:1.32083in;height:0.66389in" /></td>
<td colspan="2">※使用を推奨しないコンポーネント</td>
<td></td>
</tr>
<tr class="even">
<td>14</td>
<td><img src="md/467/media/image17.png" style="width:1.34306in;height:0.65694in" /></td>
<td colspan="2"><p>業務インターフェース</p>
<p>業務（サービス）レイヤーで使用。</p></td>
<td>端末、スマートフォン等</td>
</tr>
<tr class="odd">
<td>15</td>
<td><img src="md/467/media/image18.png" style="width:1.36597in;height:0.65694in" /></td>
<td colspan="2"><p>業務プロセス</p>
<p>業務（サービス）レイヤーで使用。</p></td>
<td></td>
</tr>
<tr class="even">
<td>16</td>
<td><img src="md/467/media/image19.png" style="width:1.33611in;height:0.65694in" /></td>
<td colspan="2"><p>業務機能</p>
<p>業務（サービス）レイヤーで使用。</p></td>
<td></td>
</tr>
<tr class="odd">
<td>17</td>
<td><img src="md/467/media/image20.png" style="width:1.32083in;height:0.64931in" /></td>
<td colspan="2">※使用を推奨しないコンポーネント</td>
<td></td>
</tr>
<tr class="even">
<td>18</td>
<td><img src="md/467/media/image21.png" style="width:1.34306in;height:0.66389in" /></td>
<td colspan="2">※使用を推奨しないコンポーネント</td>
<td></td>
</tr>
<tr class="odd">
<td>19</td>
<td><img src="md/467/media/image22.png" style="width:1.35069in;height:0.64931in" /></td>
<td colspan="2"><p>業務サービス</p>
<p>業務（サービス）レイヤーで使用。</p></td>
<td></td>
</tr>
<tr class="even">
<td>20</td>
<td><img src="md/467/media/image23.png" style="width:1.32083in;height:0.65694in" /></td>
<td colspan="2"><p>業務オブジェクト</p>
<p>ルール・データ標準レイヤーで使用。</p></td>
<td>法律、制度で定められた標準、データモデル</td>
</tr>
<tr class="odd">
<td>21</td>
<td><img src="md/467/media/image24.png" style="width:1.35069in;height:0.66389in" /></td>
<td colspan="2"><p>契約</p>
<p>業務（サービス）レイヤーで使用。</p></td>
<td></td>
</tr>
<tr class="even">
<td>22</td>
<td><img src="md/467/media/image25.png" style="width:1.33611in;height:0.65694in" /></td>
<td colspan="2"><p>表現</p>
<p>業務（サービス）レイヤーで使用。</p></td>
<td>申請、証明データ</td>
</tr>
<tr class="odd">
<td>23</td>
<td><img src="md/467/media/image26.png" style="width:1.32083in;height:0.67917in" /></td>
<td colspan="2">※使用を推奨しないコンポーネント</td>
<td></td>
</tr>
<tr class="even">
<td>24</td>
<td><img src="md/467/media/image27.png" style="width:1.34375in;height:0.68819in" /></td>
<td colspan="2"><p>内部サービス</p>
<p>連携基盤（ツール）レイヤーで使用。</p></td>
<td></td>
</tr>
<tr class="odd">
<td>25</td>
<td><img src="md/467/media/image28.png" style="width:1.34375in;height:0.65625in" /></td>
<td colspan="2">※使用を推奨しないコンポーネント</td>
<td></td>
</tr>
<tr class="even">
<td>26</td>
<td><img src="md/467/media/image29.png" style="width:1.30417in;height:0.65625in" /></td>
<td colspan="2"><p>インターフェース</p>
<p>連携基盤（ツール）レイヤーで使用。</p></td>
<td>API</td>
</tr>
<tr class="odd">
<td>27</td>
<td><img src="md/467/media/image30.png" style="width:1.33611in;height:0.66389in" /></td>
<td colspan="2">※使用を推奨しないコンポーネント</td>
<td></td>
</tr>
<tr class="even">
<td>28</td>
<td><img src="md/467/media/image31.png" style="width:1.33611in;height:0.64792in" /></td>
<td colspan="2">※使用を推奨しないコンポーネント</td>
<td></td>
</tr>
<tr class="odd">
<td>29</td>
<td><img src="md/467/media/image32.png" style="width:1.32014in;height:0.64792in" /></td>
<td colspan="2">※使用を推奨しないコンポーネント</td>
<td></td>
</tr>
<tr class="even">
<td>30</td>
<td><img src="md/467/media/image33.png" style="width:1.35208in;height:0.65625in" /></td>
<td colspan="2">※使用を推奨しないコンポーネント</td>
<td></td>
</tr>
<tr class="odd">
<td>31</td>
<td><img src="md/467/media/image34.png" style="width:1.31181in;height:0.66389in" /></td>
<td colspan="2"><p>外部サービス、サービス単独で動作するもの</p>
<p>利活用環境レイヤーで使用。</p></td>
<td>認証、決済</td>
</tr>
<tr class="even">
<td>32</td>
<td><img src="md/467/media/image35.png" style="width:1.34375in;height:0.67986in" /></td>
<td colspan="2"><p>データオブジェクト</p>
<p>データレイヤーで使用。</p></td>
<td>交通データ、登記データ</td>
</tr>
<tr class="odd">
<td>33</td>
<td colspan="2"><img src="md/467/media/image36.png" style="width:1.37708in;height:0.67917in" /></td>
<td><p>ノード</p>
<p>インフラレイヤーで使用。</p></td>
<td>端末やセンサー</td>
</tr>
<tr class="even">
<td>34</td>
<td colspan="2"><img src="md/467/media/image37.png" style="width:1.36806in;height:0.67014in" /></td>
<td>※使用を推奨しないコンポーネント</td>
<td></td>
</tr>
<tr class="odd">
<td>35</td>
<td colspan="2"><img src="md/467/media/image38.png" style="width:1.32986in;height:0.67014in" /></td>
<td>※使用を推奨しないコンポーネント</td>
<td></td>
</tr>
<tr class="even">
<td>36</td>
<td colspan="2"><img src="md/467/media/image39.png" style="width:1.32986in;height:0.67014in" /></td>
<td>※使用を推奨しないコンポーネント</td>
<td></td>
</tr>
<tr class="odd">
<td>37</td>
<td colspan="2"><img src="md/467/media/image40.png" style="width:1.32986in;height:0.64167in" /></td>
<td>※使用を推奨しないコンポーネント</td>
<td></td>
</tr>
<tr class="even">
<td>38</td>
<td colspan="2"><img src="md/467/media/image41.png" style="width:1.32986in;height:0.64167in" /></td>
<td>※使用を推奨しないコンポーネント</td>
<td></td>
</tr>
<tr class="odd">
<td>39</td>
<td colspan="2"><img src="md/467/media/image42.png" style="width:1.32083in;height:0.64167in" /></td>
<td><p>ネットワーク</p>
<p>インフラレイヤーで使用。</p></td>
<td>5G</td>
</tr>
<tr class="even">
<td>40</td>
<td colspan="2"><img src="md/467/media/image43.png" style="width:1.32986in;height:0.64167in" /></td>
<td>※使用を推奨しないコンポーネント</td>
<td></td>
</tr>
<tr class="odd">
<td>41</td>
<td colspan="2"><img src="md/467/media/image44.png" style="width:1.32083in;height:0.66042in" /></td>
<td>※使用を推奨しないコンポーネント</td>
<td></td>
</tr>
<tr class="even">
<td>42</td>
<td colspan="2"><img src="md/467/media/image45.png" style="width:1.32083in;height:0.63194in" /></td>
<td>※使用を推奨しないコンポーネント</td>
<td></td>
</tr>
<tr class="odd">
<td>43</td>
<td colspan="2"><img src="md/467/media/image46.png" style="width:1.31111in;height:0.63194in" /></td>
<td>※使用を推奨しないコンポーネント</td>
<td></td>
</tr>
<tr class="even">
<td>44</td>
<td colspan="2"><img src="md/467/media/image47.png" style="width:1.32986in;height:0.63194in" /></td>
<td>※使用を推奨しないコンポーネント</td>
<td></td>
</tr>
<tr class="odd">
<td>45</td>
<td colspan="2"><img src="md/467/media/image48.png" style="width:1.32083in;height:0.64167in" /></td>
<td>※使用を推奨しないコンポーネント</td>
<td></td>
</tr>
<tr class="even">
<td>46</td>
<td colspan="2"><img src="md/467/media/image49.png" style="width:1.31111in;height:0.67917in" /></td>
<td>※使用を推奨しないコンポーネント</td>
<td></td>
</tr>
<tr class="odd">
<td>47</td>
<td colspan="2"><img src="md/467/media/image50.png" style="width:1.32083in;height:0.66042in" /></td>
<td><p>設備</p>
<p>インフラレイヤーで使用。</p></td>
<td></td>
</tr>
<tr class="even">
<td>48</td>
<td colspan="2"><img src="md/467/media/image51.png" style="width:1.32083in;height:0.66042in" /></td>
<td>※使用を推奨しないコンポーネント</td>
<td></td>
</tr>
<tr class="odd">
<td>49</td>
<td colspan="2"><img src="md/467/media/image52.png" style="width:1.29236in;height:0.64167in" /></td>
<td>※使用を推奨しないコンポーネント</td>
<td></td>
</tr>
<tr class="even">
<td>50</td>
<td><img src="md/467/media/image53.png" style="width:1.34722in;height:0.6875in" /></td>
<td colspan="2"><p>パック化されたコンセプチュアルなまとまり</p>
<p>全レイヤーで使用。</p></td>
<td></td>
</tr>
<tr class="odd">
<td>51</td>
<td><img src="md/467/media/image54.png" style="width:1.33333in;height:0.68056in" /></td>
<td colspan="2"><p>場所</p>
<p>ルールレイヤーで使用。</p></td>
<td>地域</td>
</tr>
<tr class="even">
<td>52</td>
<td><img src="md/467/media/image55.png" style="width:1.33333in;height:0.68056in" /></td>
<td colspan="2"><p>メモ</p>
<p>全レイヤーで使用。</p></td>
<td></td>
</tr>
<tr class="odd">
<td>53</td>
<td><img src="md/467/media/image56.png" style="width:1.3125in;height:0.63889in" /></td>
<td colspan="2"><p>レイヤーの枠、類似の分類</p>
<p>全レイヤーで使用。</p></td>
<td></td>
</tr>
<tr class="even">
<td>54</td>
<td><img src="md/467/media/image57.png" style="width:1.30556in;height:0.66667in" /></td>
<td colspan="2">※使用を推奨しないコンポーネント</td>
<td></td>
</tr>
<tr class="odd">
<td>55</td>
<td><img src="md/467/media/image58.png" style="width:1.32639in;height:0.68056in" /></td>
<td colspan="2">※使用を推奨しないコンポーネント</td>
<td></td>
</tr>
<tr class="even">
<td>56</td>
<td><img src="md/467/media/image59.png" style="width:1.34722in;height:0.68056in" /></td>
<td colspan="2">※使用を推奨しないコンポーネント</td>
<td></td>
</tr>
<tr class="odd">
<td>57</td>
<td><img src="md/467/media/image60.png" style="width:1.33333in;height:0.66667in" /></td>
<td colspan="2">※使用を推奨しないコンポーネント</td>
<td></td>
</tr>
<tr class="even">
<td>58</td>
<td><img src="md/467/media/image61.png" style="width:1.34722in;height:0.66667in" /></td>
<td colspan="2"><p>ギャップ（現状とのずれを記入）</p>
<p>全レイヤーで使用</p></td>
<td></td>
</tr>
<tr class="odd">
<td>59</td>
<td><img src="md/467/media/image62.png" style="width:1.33333in;height:0.66667in" /></td>
<td colspan="2"><p>リソース</p>
<p>組織レイヤーで使用</p></td>
<td><p>府省</p>
<p>人</p></td>
</tr>
<tr class="even">
<td>60</td>
<td><img src="md/467/media/image63.png" style="width:1.34722in;height:0.66667in" /></td>
<td colspan="2">※使用を推奨しないコンポーネント</td>
<td></td>
</tr>
<tr class="odd">
<td>61</td>
<td><img src="md/467/media/image64.png" style="width:1.3125in;height:0.63889in" /></td>
<td colspan="2">※使用を推奨しないコンポーネント</td>
<td></td>
</tr>
<tr class="even">
<td>62</td>
<td><img src="md/467/media/image65.png" style="width:1.3125in;height:0.64583in" /></td>
<td colspan="2"><p>行動指針</p>
<p>組織レイヤーで使用</p></td>
<td>ロードマップ、方針</td>
</tr>
</tbody>
</table>

また、リレーションは、以下を使用し、わからない場合にはAssociationで関連付けます。

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 33%" />
<col style="width: 57%" />
</colgroup>
<thead>
<tr class="header">
<th>No.</th>
<th>リレーション</th>
<th>定義</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><img src="md/467/media/image66.png" style="width:1.82153in;height:0.25278in" /></td>
<td><p>コンポジット（UMLと同義）</p>
<p>「全体」と「その全体の部分」の関係</p>
<p>全体エレメントの中に部分エレメントを入れて表現することを推奨。</p></td>
</tr>
<tr class="even">
<td>2</td>
<td><img src="md/467/media/image67.png" style="width:1.84167in;height:0.2625in" /></td>
<td>データ等を収集するときに使用する。</td>
</tr>
<tr class="odd">
<td>3</td>
<td><img src="md/467/media/image68.png" style="width:1.79236in;height:0.25278in" /></td>
<td>機能から、リソースやアセットをアサインするときに使用する。</td>
</tr>
<tr class="even">
<td>4</td>
<td><img src="md/467/media/image69.png" style="width:1.79236in;height:0.25278in" /></td>
<td><p>実現</p>
<p>ルール・データ標準レイヤーのエレメントの実現を表現。（例えば、「データ標準」の実現は「ベースレジストリ」）</p></td>
</tr>
<tr class="odd">
<td>5</td>
<td><img src="md/467/media/image70.png" style="width:1.79236in;height:0.27222in" /></td>
<td>別途整理（Associationを利用）</td>
</tr>
<tr class="even">
<td>6</td>
<td><img src="md/467/media/image71.png" style="width:1.81181in;height:0.2625in" /></td>
<td>データ等にアクセスするときに使用する。</td>
</tr>
<tr class="odd">
<td>7</td>
<td><img src="md/467/media/image72.png" style="width:1.81181in;height:0.27222in" /></td>
<td>別途整理（Associationを利用）</td>
</tr>
<tr class="even">
<td>8</td>
<td><img src="md/467/media/image73.png" style="width:1.79236in;height:0.25278in" /></td>
<td>別途整理（Associationを利用）</td>
</tr>
<tr class="odd">
<td>9</td>
<td><img src="md/467/media/image74.png" style="width:1.80208in;height:0.27222in" /></td>
<td>データの流れを示す。</td>
</tr>
<tr class="even">
<td>10</td>
<td><img src="md/467/media/image75.png" style="width:1.81181in;height:0.2625in" /></td>
<td>汎用的な要素を目的などに特化することを示す。（施設→学校　等）</td>
</tr>
<tr class="odd">
<td>11</td>
<td><img src="md/467/media/image76.png" style="width:1.81181in;height:0.2625in" /></td>
<td>エレメント同士の関連を示す。</td>
</tr>
</tbody>
</table>

　

## 　アーキテクチャ全体俯瞰図の設計

### 　アーキテクチャ全体俯瞰図の設計準備

アーキテクチャ全体俯瞰図を作成するために、必要となる対象分野の戦略やビジョン、システムやサービスなどの情報を収集します。

また、何を参照して資料を作成したかを明確にするために、アーキテクチャ全体俯瞰図のモデルの左上部分に主要な参照ドキュメントを明記します。

### 　アーキテクチャ全体俯瞰図の設計の流れ

アークテクチャ全体俯瞰図の設計は、戦略目標からトップダウンで、以下の流れで実施します。

1.  戦略や目的、生み出す価値や、それを目指すうえでの原則を明確にします。

2.  組織、データ等、わかっているものからエレメントを各レイヤーに記述していきます。リレーションは同時に記述していくのではなく、各エレメントを列挙した後に記述した方が効率的です。一方、関連性が明確なものはエレメントと同時に記述しても構いません。また、必要に応じてグルーピング機能を使ってエレメントをまとめていきます。

3.  概要が記述できたら、各エレメント間の関係を整理しながらモデル上の配置を調整していきます。この際、必要に応じて業務改革の可能性も検討していきます。

4.  概要のアーキテクチャができたところで各エレメントの細分化を図り、ルールなどの不足した部分を追記していきます。また、現状とギャップがある場合には、そのギャップなどを注記していきます。

#### 　戦略レイヤー

> アーキテクチャが何を目指しているかを明確にします。

###### 　利用エレメント

<img src="md/467/media/image4.png" style="width:5.57431in;height:1.73333in" /><img src="md/467/media/image5.png" style="width:5.57431in;height:1.73333in" /><img src="md/467/media/image6.png" style="width:5.57431in;height:1.73333in" /><img src="md/467/media/image7.png" style="width:5.57431in;height:1.73333in" /><img src="md/467/media/image10.png" style="width:5.57431in;height:1.73333in" /><img src="md/467/media/image11.png" style="width:5.57431in;height:1.73333in" /><img src="md/467/media/image12.png" style="width:5.57431in;height:1.73333in" /><img src="md/467/media/image8.png" style="width:5.57431in;height:1.73333in" /><img src="md/467/media/image77.png" style="width:0.99097in;height:0.53056in" /><img src="md/467/media/image61.png" style="width:5.57431in;height:1.73333in" /><img src="md/467/media/image9.png" style="width:5.57431in;height:1.73333in" /><img src="md/467/media/image53.png" style="width:5.57431in;height:1.73333in" /><img src="md/467/media/image55.png" style="width:5.57431in;height:1.73333in" />

　　　　

###### 　記述の流れ

1.  戦略目標であるGoalを確定します。その際、サブGoalがある場合には、その内容も記述します。

2.  Goalが生み出す価値であるValueを明確にします。

3.  Stakeholderを明確にします。

4.  原則であるPrincipleがある場合にはそれを明確にします。

5.  制約条件があるときにはConstraintを明確にします。

6.  その他必要項目を明確にします。

###### 　記述例

> ・大きな政策（ゴール）の中に複数のゴールがある場合
>
> <img src="md/467/media/image90.png" style="width:5.25309in;height:2in" />
>
> ・大きな政策（ゴール）の中に複数のプリンシプルがある場合
>
> <img src="md/467/media/image91.png" style="width:5.08999in;height:1.83717in" />

#### 　組織レイヤー

> アーキテクチャに関係する主要な組織を明確にします。組織レイヤーでは、関連性を詳細に列挙するよりも、全体としての特徴を意識して主要な関係者を列挙します。（エレメントの名称重複可）この組織レイヤーで組織名が出ていない場合でも、機能などを説明するためにBusiness Actor（業務（サービス）レイヤー）やStakeholder（戦略・ルールレイヤー）として関連付けして図中に記述されることはあります。

###### 　利用エレメント

<img src="md/467/media/image62.png" style="width:5.58611in;height:0.53472in" /><img src="md/467/media/image65.png" style="width:5.58611in;height:0.53472in" /><img src="md/467/media/image61.png" style="width:5.58611in;height:0.53472in" /><img src="md/467/media/image53.png" style="width:5.58611in;height:0.53472in" /><img src="md/467/media/image55.png" style="width:5.58611in;height:0.53472in" />

###### 　記述の流れ

1.  アーキテクチャに関係する組織をResourceとして明記します。

2.  組織内に手順や活動指針がある場合には、Course of Actionとして明記します。

3.  必要に応じて業務（サービス）のレイヤーに記述されるBusiness Actorと関連付けます。

###### 　記述例

> ・組織レイヤーのResourceと業務（サービス）レイヤーのBusiness Actorの場合
>
> <img src="md/467/media/image94.png" style="width:4.97917in;height:2.01122in" />

#### 　ルールレイヤー

> アーキテクチャに関連した法や制度に関する事項を記述します。主に要求事項のRequirementや制約条件のConstraintで記述されます。

###### 　利用エレメント

<img src="md/467/media/image23.png" style="width:5.58125in;height:1.675in" /><img src="md/467/media/image54.png" style="width:5.58125in;height:1.675in" /><img src="md/467/media/image4.png" style="width:5.58125in;height:1.675in" /><img src="md/467/media/image5.png" style="width:5.58125in;height:1.675in" /><img src="md/467/media/image6.png" style="width:5.58125in;height:1.675in" /><img src="md/467/media/image7.png" style="width:5.58125in;height:1.675in" /><img src="md/467/media/image10.png" style="width:5.58125in;height:1.675in" /><img src="md/467/media/image11.png" style="width:5.58125in;height:1.675in" /><img src="md/467/media/image12.png" style="width:5.58125in;height:1.675in" /><img src="md/467/media/image8.png" style="width:5.58125in;height:1.675in" /><img src="md/467/media/image77.png" style="width:0.99097in;height:0.53056in" /><img src="md/467/media/image9.png" style="width:5.58125in;height:1.675in" /><img src="md/467/media/image61.png" style="width:5.58125in;height:1.675in" /><img src="md/467/media/image53.png" style="width:5.58125in;height:1.675in" /><img src="md/467/media/image55.png" style="width:5.58125in;height:1.675in" />　　　　

###### 　記述の流れ

1.  ルールは包括的に多くのエレメントに関連することが多いことからリレーションを意識せずに備忘録的にエレメントを記述していきます。

2.  業務やサービスを行ううえでクリティカルに関係がある場合には、関係エレメントとのリレーションを明記します。

3.  制度的な課題がある場合には、課題をGapとして明記します。

#### 　業務（サービス）レイヤー、利活用環境レイヤー、連携基盤（ツール）レイヤー

> この３レイヤーは、業務やそれを実現するアプリケーション、ツールまでを記述します。そのため一体で検討されることが多くなります。

###### 　利用エレメント

> ・業務（サービス）レイヤー

<img src="md/467/media/image18.png" style="width:5.50278in;height:1.85347in" /><img src="md/467/media/image14.png" style="width:5.50278in;height:1.85347in" /><img src="md/467/media/image15.png" style="width:5.50278in;height:1.85347in" /><img src="md/467/media/image17.png" style="width:5.50278in;height:1.85347in" /><img src="md/467/media/image19.png" style="width:5.50278in;height:1.85347in" /><img src="md/467/media/image22.png" style="width:5.50278in;height:1.85347in" /><img src="md/467/media/image24.png" style="width:5.50278in;height:1.85347in" /><img src="md/467/media/image25.png" style="width:5.50278in;height:1.85347in" /><img src="md/467/media/image61.png" style="width:5.50278in;height:1.85347in" /><img src="md/467/media/image53.png" style="width:5.50278in;height:1.85347in" /><img src="md/467/media/image55.png" style="width:5.50278in;height:1.85347in" />

> ・利活用環境レイヤー

<img src="md/467/media/image34.png" style="width:4.36944in;height:0.57569in" /><img src="md/467/media/image61.png" style="width:4.36944in;height:0.57569in" /><img src="md/467/media/image53.png" style="width:4.36944in;height:0.57569in" /><img src="md/467/media/image55.png" style="width:4.36944in;height:0.57569in" />

> ・連携基盤（ツール）レイヤー

<img src="md/467/media/image27.png" style="width:5.54444in;height:0.59653in" /><img src="md/467/media/image29.png" style="width:5.54444in;height:0.59653in" /><img src="md/467/media/image61.png" style="width:5.54444in;height:0.59653in" /><img src="md/467/media/image53.png" style="width:5.54444in;height:0.59653in" /><img src="md/467/media/image55.png" style="width:5.54444in;height:0.59653in" />

###### 　記述の流れ

1.  業務やサービスといった観点から、そこに関係する人であるBusiness Actorや、何を介してアクセスするかというBusiness Interfaceと業務サービスであるBusiness Serviceを明確にします。業務サービスの中には、機能や役割や業務プロセスを含むことがあります。

2.  このサービスを実現するためのApplication Service（Webサービスを含む）を明確化します。

3.  そのアプリケーションを実現するための機能であるApplication Componentを明確にします。

> ※上記の1で社会のサービスという観点で整理を行い、2、3でシステム（ソフトウェア）の観点で整理を行います。

###### 　記述例

> ・一般的な記述を下記に示します。
>
> （設計対象により途中のエレメントを省略可）

　　<img src="md/467/media/image108.png" style="width:4.98664in;height:6.48837in" />

> ・Business Serviceの実現システムがApplication Componentの場合
>
> <img src="md/467/media/image109.png" style="width:3.88333in;height:4.25824in" />
>
> ・Business Serviceの実現システムがApplication Serviceの場合
>
> <img src="md/467/media/image110.png" style="width:3.88333in;height:3.88333in" />

#### 　データレイヤー、データ標準レイヤー

> データ間の関係性やデータ標準との関係性を明確にします。

###### 　利用エレメント

> ・データレイヤー
>
> <img src="md/467/media/image35.png" style="width:4.38611in;height:0.53125in" /><img src="md/467/media/image53.png" style="width:4.38611in;height:0.53125in" /><img src="md/467/media/image55.png" style="width:4.38611in;height:0.53125in" /><img src="md/467/media/image61.png" style="width:4.38611in;height:0.53125in" />
>
> ・データ標準レイヤー
>
> <img src="md/467/media/image23.png" style="width:4.38611in;height:0.53958in" /><img src="md/467/media/image53.png" style="width:4.38611in;height:0.53958in" /><img src="md/467/media/image55.png" style="width:4.38611in;height:0.53958in" /><img src="md/467/media/image61.png" style="width:4.38611in;height:0.53958in" />

###### 　記述の流れ

1.  業務で使っているデータを明確にします。

2.  関係しそうなデータ標準を明確にし、必要に応じてデータと関連付けます。

3.  ベースレジストリは、エレメントの文字を赤色（赤文字）で表現します。

#### 　インフラレイヤー

> インフラレイヤーは、多くの機能やサービスの基盤となります。そのためリレーションを記述しないで各要素のみ記述しても構いません。

###### 　利用エレメント

<img src="md/467/media/image50.png" style="width:5.54722in;height:1.09514in" /><img src="md/467/media/image36.png" style="width:5.54722in;height:1.09514in" /><img src="md/467/media/image42.png" style="width:5.54722in;height:1.09514in" /><img src="md/467/media/image53.png" style="width:5.54722in;height:1.09514in" /><img src="md/467/media/image55.png" style="width:5.54722in;height:1.09514in" /><img src="md/467/media/image61.png" style="width:5.54722in;height:1.09514in" />

###### 　記述の流れ

1.  アセットやインフラを列挙します。

2.  アセットやインフラに関するGapを明確にします。

> ※インフラは全般的に使用されることが多いため、無理にリレーションを張る必要はありません。

###### 　記述例

> ・インフラレイヤーのノードと業務インターフェースの場合
>
> <img src="md/467/media/image115.png" style="width:4.83333in;height:2.25442in" />
>
> エレメント同士の関係性をリレーションにより示さない場合でも、縦のラインを合わせることで全体の関係性が分かりやすくなります。

## 　アーキテクチャ全体俯瞰図の活用例

### 　戦略策定での活用

> 分野横断でのデータ連携を前提とすることや欧州のデータ戦略がアーキテクチャ思考で推進されていることから、包括的データ戦略は検討当初からアーキテクチャを意識した検討を行いました。
>
> 包括的データ戦略では、データ利活用面を重視したために、データ連携のツールのレイヤーを省略し、「利活用機能」を「利活用環境」と「連携基盤」の２つのレイヤーに分離しています。また、「組織」と「ビジネス」のレイヤーを一体としてサービス検討を行っています。
>
> このように、Society5.0の参照アーキテクチャをベースにして他分野との連携を容易にするとともに、検討しやすくするためレイヤー構造をカスタマイズしています
>
> こうしてレイヤーを整理した上で、国内の既存の関連政策や各国のデータ戦略等をアーキテクチャの各レイヤーで明確化し、各レイヤーを項目ベースで比較して、データ戦略の検討項目の抜け漏れの確認を行いました。さらに、この比較を通じて、日本の優位点であるネットワークインフラや、取組が不足している基盤データの整備等の強化すべきポイントをグローバルな視点から整理しました。
>
> <img src="md/467/media/image116.png" style="width:5.90556in;height:3.23333in" alt="画像5" />

図 4　アーキテクチャによる検討項目の検証

> <img src="md/467/media/image117.emf" style="width:5.90556in;height:3.17014in" />

図 5　各国戦略との比較結果の概要

> このようにアーキテクチャを使って戦略を検討することで、戦略事項の確認作業が効率的になる等、戦略策定場面でのアーキテクチャ活用の有効性が確認されました。

### 　全体の関係性の整理

アーキテクチャ全体俯瞰図の作成にモデリングツールを使うことで全体の整合性を確認することが容易にできます。本ガイド作成にはArchiをモデリングツールとして使用しているため、下図の画面下部のリレーションのように、各要素間の関係性を確認することが可能になります。

<img src="md/467/media/image118.png" style="width:5.90556in;height:3.23333in" alt="画像8" />

図 6　モデリングツール画面での全体の関係性の確認

### 　戦略の整合性確保

複数の戦略を同時並行で検討することがありますが、このような検討時にも相互の整合性をとるのにアーキテクチャは有効です。

内閣官房情報通信技術（IT）総合戦略室では、2020年９月から12月まで、以下の相互に密接に関係した３つの戦略・方針策定の作業を行いました。

-   アーキテクチャをベースに検討した「データ戦略タスクフォース第一次とりまとめ[^10]（76ページ）」

-   IT基本法の見直しやデジタル庁設置の考え方等の方針である「デジタル社会の実現に向けた改革の基本方針[^11]（本文18ページ、別紙51ページ）」

-   デジタル・ガバメントの今後の方向性を示した「デジタル・ガバメント実行計画[^12]（全体335ページ）」

これらの関係性を整理するために３つの文書を比較し、データ戦略のアーキテクチャを共通軸に他の２つの戦略を整理しました。

下図の左の縦のブロックが「デジタル社会の実現に向けた改革の基本方針」、中央の縦のブロックが「データ戦略タスクフォース第一次とりまとめ」、右の縦のブロックが「デジタル・ガバメント実行計画」です。

アーキテクチャ全体俯瞰図を使うことで、各戦略のフォーカスするポイントが少しずつ違っていながらも、相互に連携していることが分かります。

<img src="md/467/media/image119.png" style="width:5.90556in;height:5.28681in" alt="画像3" />

図 7　各種戦略の関係性の整理

単なる文書の比較ではなくアーキテクチャ全体俯瞰図を使った比較により、戦略の全体像や役割分担が明確になりました。

このような可視化の取組により、デジタル庁の創設を見据えたチーム間の協力関係が明確になったことは重要な成果です。

### 　プラットフォーム間の共通化や連携の検討

> 包括的データ戦略では、分野別や分野横断のプラットフォーム[^13]の構築を検討していますが、ここでもアーキテクチャ全体俯瞰図を活用しています。従来、各分野の担当部門が整理する資料では、ルールを重視する報告や技術を重視する報告、サービスを下から支える図や上からブレイクダウンする図等、それぞれが独自の形式で報告しており、全体を俯瞰して横断的に検討することが困難でした。

### 　分野横断の分析での活用

> 分野横断での分析を可能とするため、下図の通り、縦軸にアーキテクチャ全体俯瞰図の視点、横軸に各分野を並べて整理しました。横に見ていくことで、例えばPDS（Personal Data Store）[^14]が各分野で必要なことが明示的にわかります。
>
> このように横軸で分野横断的に見ることは、基本的要件や共通機能の検討が効率的にできるようになります。また、共通機能の検討が集約して行えるようになるため、各分野では分野特有の機能や課題を集中的に検討できるようになります。
>
> さらに、標準データを元にした、分野別データモデルの検討といったことも可能になります。

<img src="md/467/media/image120.png" style="width:5.20679in;height:3.19792in" alt="画像5" />

図 8　各分野から共通機能の抽出と標準の適用

アーキテクチャへの知見がない人にアーキテクチャモデル全体像を説明すると、難しい印象を持たれて敬遠されてしまうことがあります。そこで、最初に簡易的なモデルを示すことでアーキテクチャの重要性や有効性を理解してもらい、その上で、全体アーキテクチャの詳細なモデル図（アーキテクチャ全体俯瞰図）を示し議論を行うことで円滑に検討を進めることが可能となります。

<img src="md/467/media/image121.emf" style="width:5.90556in;height:2.87569in" />

図 9　アーキテクチャの詳細化（一覧からモデル化）

それでもモデル図は専門的知識のない人には難しい面もあります。よって今回のプラットフォームの検討では、専門的なモデル図は補足資料とし、第一段階では、誰もが分かりやすいイメージ図でアーキテクチャを示し検討を行いました。

<img src="md/467/media/image122.png" style="width:5.90556in;height:3.45486in" alt="画像6" />

図 10　プラットフォーム検討の初期イメージ

上の図では、各分野を「サービス」「機能」「データ」の３階層で明確化し共通化や連携の可能性を検討しており、アーキテクチャモデルを使わずにイメージ化することができました。

このようにイメージ化を図ることで関係府省との議論が深まり、さらには下図のように詳細化を行うことも可能となりました。

全体像

<img src="md/467/media/image123.png" style="width:5.90556in;height:2.31806in" alt="画像7" />

教育部分の拡大

<img src="md/467/media/image124.png" style="width:5.90556in;height:4.06389in" />

図 11　プラットフォーム検討の整理イメージ

> 現在は、下図のように分野毎に詳細アーキテクチャを比較して議論を進めていますが、そうすることで優先的に整備すべきサービスやデータモデルを明確にすることができます。
>
> <img src="md/467/media/image125.emf" style="width:5.90556in;height:2.24375in" />

図 12　各分野のアーキテクチャの詳細比較

> このように段階的にアーキテクチャを作り検討を深めていくことは有効な手法と考えられます。

### 　価値連鎖の検討

アーキテクチャの縦の連鎖も検討していく必要があります。サブゴールなどの特定のビジョンを達成するためにどのような進め方をすればよいのか各エレメント間の関係性を検討します。

<img src="md/467/media/image126.emf" style="width:4.67119in;height:6.71323in" />

図 13　価値連鎖のイメージ

さらに、各項目をKGI、KPIという視点で見ることで、体系的な効果測定を行うことができるようになります。

<img src="md/467/media/image127.emf" style="width:5.90556in;height:2.84861in" />

図 14　KPIの連鎖

## 　アーキテクチャ全体俯瞰図から詳細化の実施

アーキテクチャ全体俯瞰図の各レイヤーは、検討を深めたり実装を行うために詳細化が行われます。ArchiMate(R)で詳細化することも可能ですが、より専門的に記述するためには専門のモデリング手法を活用した方が正確かつ効率的にモデル化することができます。

機能モデリングはArchiMate(R)で行い、業務プロセスモデリングにBPMN[^15]、データモデルはUMLのクラス図[^16]で展開していくことが国際的な主流になっています。図 15のように各レイヤーの詳細化を図っていきます。

<img src="md/467/media/image128.emf" style="width:5.90556in;height:4.35in" />

図 15　アーキテクチャ全体俯瞰図の詳細化

[^1]: 組織全体の業務とシステムを共通言語と統一的手法でモデル化し、最適化を図る設計手法。

[^2]: <https://www.opengroup.org/togaf>

[^3]: <https://www.opengroup.org/archimate-home>

[^4]: <https://www8.cao.go.jp/cstp/tyousakai/juyoukadai/14kai/siryo2-1.pdf>

[^5]: <https://www.iso.org/standard/50508.html>

[^6]: <http://www.iso-architecture.org/ieee-1471/cm/>

[^7]: <https://www.kantei.go.jp/jp/singi/it2/dgov/dai10/siryou_a.pdf>

[^8]: <https://www.archimatetool.com/>

[^9]: <https://joinup.ec.europa.eu/collection/european-interoperability-reference-architecture-eira>

[^10]: <https://www.kantei.go.jp/jp/singi/it2/dgov/dai10/siryou_a.pdf>

[^11]: <https://www.kantei.go.jp/jp/singi/it2/dgov/201225/siryou1.pdf>

[^12]:  <https://www.kantei.go.jp/jp/singi/it2/dgov/201225/siryou4.pdf>

[^13]: 広く多様なデータを活用して新たな価値を創出するためには、「データ連携」とそれを「利活用したサービスを提供」する基盤（プラットフォーム）の構築が鍵となる。プラットフォームはデータ連携基盤（ツール）、利活用環境とデータ連携に必要なルールを提供するものである。［「包括的データ戦略」（デジタル社会の実現に向けた重点計画 別紙 令和３年6月18日）より抜粋］

[^14]: 他者保有データの集約を含め、個人が自らの意思で自らのデータを蓄積・管理するための仕組み（システム）であって、第三者への提供に係る制御機能（移管を含む）を有するもの 。

[^15]: Business Process Model and Notation（ビジネスプロセス・モデルと表記法）の略で、世界で最も普及している業務プロセス表記標準。

[^16]: 世界で最も普及しているデータモデルの表記標準であり、本アーキテクチャのデータモデルの記述にクラス図を用いる。

  [1]: #背景と目的
  [2]: #背景
  [2]: #目的
  [3]: #概要
  [4]: #用語の定義
  [5]: #アーキテクチャ全体俯瞰図による記述
  [6]: #基本とするレイヤー構造
  [6]: #各エレメントリレーションの定義及び使用例の整理
  [14]: #アーキテクチャ全体俯瞰図の設計
  [7]: #アーキテクチャ全体俯瞰図の設計準備
  [8]: #アーキテクチャ全体俯瞰図の設計の流れ
  [9]: #戦略レイヤー
  [15]: #組織レイヤー
  [16]: #ルールレイヤー
  [17]: #業務サービスレイヤー利活用環境レイヤー連携基盤ツールレイヤー
  [21]: #データレイヤーデータ標準レイヤー
  [10]: #インフラレイヤー
  [23]: #アーキテクチャ全体俯瞰図の活用例
  [11]: #戦略策定での活用
  [24]: #全体の関係性の整理
  [26]: #戦略の整合性確保
  [28]: #プラットフォーム間の共通化や連携の検討
  [12]: #分野横断の分析での活用
  [32]: #価値連鎖の検討
  [35]: #アーキテクチャ全体俯瞰図から詳細化の実施
