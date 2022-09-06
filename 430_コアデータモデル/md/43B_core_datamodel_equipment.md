デジタル社会推進実践ガイドブック DS-43B

> コアデータモデル解説書  
> 設備

2022年（令和4年）5月9日

デジタル庁

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>[キーワード]</p>
<p>設備、データモデル</p>
<p>[概要]</p>
<p>設備の情報をシステム実装する際に参照すべきデータモデルについて解説するガイドブックです。このガイドに従いデータ設計を行うことで、同じ設計規則に従うシステム間、分野間でのデータ連携を容易かつ正確に行えるようになります。また、データ設計を実施するコストも削減することができます。</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## 設備のデータモデル

設備の情報を記述するためのデータモデルです。

必須項目以外は任意項目なので、用途に応じて項目を選択、あるいは独自項目を追加するなどのカスタマイズを行って利用してください。

### 設備データモデルの項目

設備データモデルの項目は表1の通りです。英語名や記入例などを含む詳細については、別添の「438_コアデータモデル_DMD.xlsx」を参照してください。

表1 設備データモデルの項目一覧

| 必須項目 | 項目名       | 説明                                                         |
|----------|--------------|--------------------------------------------------------------|
|          | ID           | 機械的に採番された設備を一意に識別するID。設備単位に付番する |
|          | 区分         | 設備の区分                                                   |
|          | 種類         | 設備の種類                                                   |
| 必       | 名称         | 設備の名称                                                   |
| 必       | 名称（カナ） | 設備のカナ表記                                               |
| 必       | 名称（英字） | 設備の英語名またはローマ字表記                               |
|          | 説明         | 設備情報として公開可能な詳細情報                             |
|          | 状態         | 「稼働中」などのステータス                                   |
| 必       | 設備住所     | 住所情報（住所型　※緯度経度を使用）                          |
|          | サービス曜日 | 設備を利用できる曜日                                         |
|          | 開始時刻     | 設備を利用開始できる時間                                     |
|          | 終了時刻     | 設備の利用終了時間                                           |
|          | 日時備考     | 定型で表せない設備の利用日時情報                             |
|          | URL          | AEDの設置場所写真のURLなど                                   |
|          | 備考         | 設備の備考                                                   |
|          | 連絡先情報   | 連絡先の情報（連絡先型）                                     |

## 関連データ定義

### データモデルの関係性

設備は、IMIコア語彙や3D都市モデル標準性仕様書（CityGML）furniturにも定義があります。その関係性を以下に示します。

表3 設備データモデルと関連モデルとの関係性

| GIFデータ項目 | 対応するIMI     | 対応するCityGML |
|---------------|-----------------|-----------------|
| ID            | ic:ID           |                 |
| 区分          |                 | frn:class       |
| 種類          |                 | frn:function    |
| 名称          | ic:名称         | gml:name        |
| 名称（カナ）  | ic:名称         | gml:name        |
| 名称（英字）  | ic:名称         | gml:name        |
| 説明          | ic:記述         | gml:description |
| 状態          |                 |                 |
| 設備住所      | ic:住所         |                 |
| サービス曜日  | ic:利用可能時間 |                 |
| 開始時刻      | ic:利用可能時間 |                 |
| 終了時刻      | ic:利用可能時間 |                 |
| 日時備考      | ic:利用可能時間 |                 |
| URL           | ic:Webサイト    |                 |
| 備考          | ic:記述         |                 |
| 連絡先情報    | ic:連絡先       |                 |

### コントロールド・ボキャブラリ（統制語彙）

####### 区分

> CityGML 2.0　Annex C.4のコードを使用する。

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 76%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>コード</p>
</blockquote></th>
<th><blockquote>
<p>説明</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>1000</p>
</blockquote></td>
<td><blockquote>
<p>交通施設</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>1010</p>
</blockquote></td>
<td><blockquote>
<p>通信施設</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>1020</p>
</blockquote></td>
<td><blockquote>
<p>保安施設</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>1030</p>
</blockquote></td>
<td><blockquote>
<p>その他</p>
</blockquote></td>
</tr>
</tbody>
</table>

####### 種類

> 道路基盤地図情報製品仕様書（案）、作業規程の準則（公共測量標準図式）を使用する。

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 76%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>コード</p>
</blockquote></th>
<th><blockquote>
<p>説明</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>1000</p>
</blockquote></td>
<td><blockquote>
<p>道路標示</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>1010</p>
</blockquote></td>
<td><blockquote>
<p>区画線</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>1020</p>
</blockquote></td>
<td><blockquote>
<p>車道中央線</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>1030</p>
</blockquote></td>
<td><blockquote>
<p>車線境界線</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>1040</p>
</blockquote></td>
<td><blockquote>
<p>車道外側線</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>1100</p>
</blockquote></td>
<td><blockquote>
<p>指示標示</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>1110</p>
</blockquote></td>
<td><blockquote>
<p>横断歩道</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>1120</p>
</blockquote></td>
<td><blockquote>
<p>停止線</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>1200</p>
</blockquote></td>
<td><blockquote>
<p>規制標示</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>2000</p>
</blockquote></td>
<td><blockquote>
<p>柵・壁</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>3000</p>
</blockquote></td>
<td><blockquote>
<p>道路標識</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>3110</p>
</blockquote></td>
<td><blockquote>
<p>案内標識</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>3120</p>
</blockquote></td>
<td><blockquote>
<p>警戒標識</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>3130</p>
</blockquote></td>
<td><blockquote>
<p>規制標識</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>3140</p>
</blockquote></td>
<td><blockquote>
<p>指示標識</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>3150</p>
</blockquote></td>
<td><blockquote>
<p>補助標識</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>4000</p>
</blockquote></td>
<td><blockquote>
<p>建造物</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>4010</p>
</blockquote></td>
<td><blockquote>
<p>上屋</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>4020</p>
</blockquote></td>
<td><blockquote>
<p>地下出入口</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>4100</p>
</blockquote></td>
<td><blockquote>
<p>視線誘導標</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>4120</p>
</blockquote></td>
<td><blockquote>
<p>道路反射鏡</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>4200</p>
</blockquote></td>
<td><blockquote>
<p>照明施設</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>4300</p>
</blockquote></td>
<td><blockquote>
<p>道路情報管理施設</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>4400</p>
</blockquote></td>
<td><blockquote>
<p>災害検知器</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>4500</p>
</blockquote></td>
<td><blockquote>
<p>気象観測装置</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>4600</p>
</blockquote></td>
<td><blockquote>
<p>道路情報板</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>4700</p>
</blockquote></td>
<td><blockquote>
<p>光ファイバー</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>4800</p>
</blockquote></td>
<td><blockquote>
<p>柱</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>4810</p>
</blockquote></td>
<td><blockquote>
<p>路側</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>4820</p>
</blockquote></td>
<td><blockquote>
<p>片持</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>4830</p>
</blockquote></td>
<td><blockquote>
<p>門型</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>4840</p>
</blockquote></td>
<td><blockquote>
<p>電柱</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>4900</p>
</blockquote></td>
<td><blockquote>
<p>交通信号機</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>5000</p>
</blockquote></td>
<td><blockquote>
<p>階段</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>5010</p>
</blockquote></td>
<td><blockquote>
<p>通路</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>5020</p>
</blockquote></td>
<td><blockquote>
<p>エレベータ</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>5030</p>
</blockquote></td>
<td><blockquote>
<p>エスカレータ</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>5100</p>
</blockquote></td>
<td><blockquote>
<p>管理用地上施設</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>5200</p>
</blockquote></td>
<td><blockquote>
<p>電線共同溝</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>5300</p>
</blockquote></td>
<td><blockquote>
<p>CAB</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>5400</p>
</blockquote></td>
<td><blockquote>
<p>情報BOX</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>5500</p>
</blockquote></td>
<td><blockquote>
<p>管路</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>5600</p>
</blockquote></td>
<td><blockquote>
<p>管理用開口部</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>5610</p>
</blockquote></td>
<td><blockquote>
<p>マンホール</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>5620</p>
</blockquote></td>
<td><blockquote>
<p>ハンドホール</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>5630</p>
</blockquote></td>
<td><blockquote>
<p>入孔</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>6000</p>
</blockquote></td>
<td><blockquote>
<p>距離標</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>6010</p>
</blockquote></td>
<td><blockquote>
<p>境界標識</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>6020</p>
</blockquote></td>
<td><blockquote>
<p>道路元標・里程標</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>6100</p>
</blockquote></td>
<td><blockquote>
<p>料金徴収施設</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>6200</p>
</blockquote></td>
<td><blockquote>
<p>融雪施設</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>7000</p>
</blockquote></td>
<td><blockquote>
<p>排水施設</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>7100</p>
</blockquote></td>
<td><blockquote>
<p>集水桝</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>7200</p>
</blockquote></td>
<td><blockquote>
<p>排水溝</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>7300</p>
</blockquote></td>
<td><blockquote>
<p>側溝</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>7400</p>
</blockquote></td>
<td><blockquote>
<p>排水管</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>7500</p>
</blockquote></td>
<td><blockquote>
<p>排水ポンプ</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>8010</p>
</blockquote></td>
<td><blockquote>
<p>停留所</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>8020</p>
</blockquote></td>
<td><blockquote>
<p>消火栓</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>8030</p>
</blockquote></td>
<td><blockquote>
<p>郵便ポスト</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>8040</p>
</blockquote></td>
<td><blockquote>
<p>電話ボックス</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>8050</p>
</blockquote></td>
<td><blockquote>
<p>輸送管</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>8060</p>
</blockquote></td>
<td><blockquote>
<p>軌道</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>8070</p>
</blockquote></td>
<td><blockquote>
<p>架空線</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>8080</p>
</blockquote></td>
<td><blockquote>
<p>自動販売機</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>8090</p>
</blockquote></td>
<td><blockquote>
<p>墓碑</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>8100</p>
</blockquote></td>
<td><blockquote>
<p>記念碑</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>8110</p>
</blockquote></td>
<td><blockquote>
<p>立像</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>8120</p>
</blockquote></td>
<td><blockquote>
<p>噴水</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>8130</p>
</blockquote></td>
<td><blockquote>
<p>井戸</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>8140</p>
</blockquote></td>
<td><blockquote>
<p>掲示板</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>8150</p>
</blockquote></td>
<td><blockquote>
<p>点字ブロック</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>8160</p>
</blockquote></td>
<td><blockquote>
<p>ベンチ</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>8170</p>
</blockquote></td>
<td><blockquote>
<p>テーブル</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>9000</p>
</blockquote></td>
<td><blockquote>
<p>その他</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>9001</p>
</blockquote></td>
<td><blockquote>
<p>看板（自立式）</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>9002</p>
</blockquote></td>
<td><blockquote>
<p>水飲み</p>
</blockquote></td>
</tr>
</tbody>
</table>

## 変更履歴

| 改定年月日   | 改定箇所 | 改定内容 |
|--------------|----------|----------|
| 2022年5月9日 | \-       | 初版決定 |
